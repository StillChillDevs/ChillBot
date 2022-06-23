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
        # A mention_times is made for each user

        
        