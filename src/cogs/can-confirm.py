# CanConfirm
# A new member confirmation cog for Discord bots
# Copyright 2022 StillChillDevs. See the LICENSE file to see full license

import discord
from discord.ext import commands
import storage

class CanConfirm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot