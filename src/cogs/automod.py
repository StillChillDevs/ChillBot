# Automoderation tools for ChillBot
# Copyright 2022 StillChillDevs. See the LICENSE file to see full license

from datetime import datetime, timezone

import discord
import storage
from discord.ext import commands


class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    ###################
    # EVENT LISTENERS #
    ###################

    @commands.Cog.listener()
    async def on_message(message):
        pass

    #####################
    # PROCESS FUNCTIONS #
    #####################

    def check_spam_ping(message):  
        '''Takes in the message and checks if the user is spam pinging'''

        # Goals:
        # 1. Check how many members were mentioned by this message, set that to members_mentioned
        # 2. Increment the amount of times the sender mentioned others in the last 60 seconds
        # 3. Check if the the sender mentioned people above the limit, if so mute them

        # Does the server even have spam ping detection on? If no, return
        # Does the message have mentions? If no, return
        if not storage.get_guild_data(message.guild.id, 'is_spam_ping_detect') or len(message.mentions) == 0:
            return

        # Goal 1: Check how many members were mentioned by this message, set that to members_mentioned
        members_mentioned = len(message.mentions)

        # Goal 2: Increment the amount of times the sender mentioned others in the last 60 seconds
        
        # First we have to get the mention_times list
        # mention_times contains the times when the member mentioned someone
        # For example, if the member mentioned 3 people at time x, then there will be 3 entries of x in mention_times
        # The time is in unix time in seconds
        # A mention_times is made for each user for each guild

        mention_times = storage.get_guild_user_data(message.guild.id, message.author.id, 'mention_times')

        # If the mention_times doesn't exist, make one and set it to blank for now
        if mention_times == None:
            storage.set_guild_user_data(message.guild.id, message.author.id, 'mention_times', [])
            mention_times = storage.get_guild_user_data(message.guild.id, message.author.id, 'mention_times')
        
        # Get the UTC unix time when the message was sent in seconds, then add the time to mention times
        # ... based on how many members was mentioned (members_mentioned)

        message_create_time = message.created_at.timestamp()

        print('Line 63, this is unix time at which message was created' + str(message_create_time))
        for x in range(members_mentioned):
            mention_times.append(message_create_time)
        
        # Goal 3: Check if the the sender mentioned people above the limit, if so mute them
        # First we need to get the mention_limit
        mention_limit = storage.get_guild_data(message.guild.id, 'mention_limit')

        if mention_limit == None:
            # Something is clearly wrong, for now just print to output
            print('Line 74, mention_limit does not exist, even though spam ping detection is on')

        mentions_in_last_minute = 0

        # Loop through mentions_times, and see which times are less than 60 seconds
        for time in mention_times:
            current_time = datetime.utcnow().timestamp()
            
            if current_time - time <= 60:
                # Mentioned in the last minute, increment mentions_in_last_minute
                mentions_in_last_minute += 1
            else:
                # Otherwise we can actually just remove the time from mention_times
                mention_times.remove(time)
        
        # Now we check if the mentions_in_last_minute is more than mention_limit
        if mentions_in_last_minute > mention_limit:
            # Mentions more than minute, get mute duration and mute the user
            mute_duration = storage.get_guild_data(message.guild.id, 'spam_ping_mute_duration')

            if mute_duration == None:
                # Something is clearly wrong, for now just print to output
                print('Line 95, mute_duration does not exist, even though spam ping detection is on')
            
            mute(message.guild.id, message.member.id, f'Mention spam: Member reached mentions per minute limit of {mention_limit}')