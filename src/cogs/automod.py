# Automoderation tools for ChillBot
# Copyright 2022 StillChillDevs. See the LICENSE file to see full license

import discord
from discord.ext import commands
import storage
from datetime import datetime, timezone

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
        # Does the server even have spam ping detection on? If no, return
        # Does the message have mentions? If no, return
        # Get guild.user.last_pinged
        # Does mentioned user_id exist in guild.user.last_pinged.keys()?
        #   Yes:
        #   Is guild.user.last_pinged[mentioned user_id]['last_pinged'] - current_unix_time < 60?
        #       Yes:
        #       Change guild.user.last_pinged[mentioned user_id]['ping_count'] by 1
        #       
        #       No:
        #       Set guild.user.last_pinged[mentioned user_id]['ping_count'] to 1 
        #
        #   No:
        #   Set guild.user.last_pinged[mentioned user_id] to {}
        #   Set guild.user.last_pinged[mentioned user_id]['last_pinged'] to current unix time
        #   Set guild.user.last_pinged[mentioned user_id]['ping_count'] to 1
        # 
        # Get guild.user.last_pinged[mentioned user_id]['ping_count']
        # Get guild.ping_per_second_max
        # Is guild.user.last_pinged[mentioned user_id]['ping_count']
        #   Yes:
        #   Get guild.spam_ping_punishment
        #   punish(guild_id, member, punishment_type)

    
        # Does the server even have spam ping detection on? If no, return
        # Does the message have mentions? If no, return
        if not storage.get_guild_data(message.guild.id, 'is_spam_ping_detect') or len(message.mentions) == 0:
            return
        
        # Get last_pinged
        last_pinged = storage.get_guild_user_data(message.guild.id, message.author.id, 'last_pinged')

        for mentioned_user in message.mentions:

            # Does mentioned user_id exist in guild.user.last_pinged.keys()?
            if last_pinged != None and mentioned_user in last_pinged.keys():

                # Is guild.user.last_pinged[mentioned user_id]['last_pinged'] - current_unix_time < 60?
                if last_pinged[mentioned_user.id]['last_pinged'] - datetime.now(timezone.utc).timestamp() < 60:
                    # Yes: Change guild.user.last_pinged[mentioned user_id]['ping_count'] by 1

                    last_pinged[mentioned_user.id]['ping_count'] += 1
                    storage.set_guild_user_data(message.guild.id, message.author.id, 'last_pinged', last_pinged)
                else:
                    # No: Set guild.user.last_pinged[mentioned user_id]['ping_count'] to 1     

                    last_pinged[mentioned_user.id]['ping_count'] = 1
                    storage.set_guild_user_data(message.guild.id, message.author.id, 'last_pinged', last_pinged)
                
            else:
                #37
                pass