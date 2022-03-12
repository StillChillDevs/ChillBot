# Anti Ping stuff
# Anti ghost ping
# Copyright 2022 StillChillDevs

import discord
from discord.ext import commands
import storage

class AntiPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Detect deleted ghost ping messages
    @commands.Cog.listener()
    async def on_message_delete(message):
        if message.author.bot:
            return
        
        if message.mentions:
            for user in message.mentions:
                embed=discord.Embed(title='You were ghost pinged!', description='The original message has been deleted', color=0xff0000)
                embed.add_field(name='You were pinged by:', value=f'{message.author.mention}', inline=False)
                embed.add_field(name='Original message was:', value=f'{message.content}', inline=False)

                send_notif = storage.get_guild_user_data(message.guild.id, user.id, 'ghost_ping_notify')

                if send_notif:
                    try:
                        await user.send(embed=embed)
                    except:
                        pass

        if message.mention_everyone():
            send_ping_log = storage.get_guild_data(message.guild.id, 'guild_ghost_ping_notify')
            logging_channel_id = storage.get_guild_data(message.guild.id, 'logging_channel_id')

            if send_ping_log and logging_channel_id:
                logging_channel = message.guild.get_channel(logging_channel_id)

                embed=discord.Embed(title='@everyone Ghost Ping Detected', description='Original message was deleted', color=0xff0000)
                embed.add_field(name='Ghost ping sent by:', value=f'{message.author.mention}', inline=False)
                embed.add_field(name='Message contents:', value=f'{message.content}', inline=False)

                await logging_channel.send(embed=embed)