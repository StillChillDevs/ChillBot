# Automoderation tools for ChillBot
# Copyright 2022 StillChillDevs. See the LICENSE file to see full license

import discord
from discord.ext import commands
import storage

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
        pass