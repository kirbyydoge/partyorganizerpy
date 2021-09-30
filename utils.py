import discord
from discord.ext import commands

class User():
    def __init__(self, ctx:commands.Context):
        self.server_id = ctx.message.guild.id
        self.user_id = ctx.message.author.id
        self.username = ctx.message.author.display_name
        self.picture = ctx.message.author.avatar_url

    def get_embed(self, title):
        embed = discord.Embed(
            title = title,
            color = discord.Colour.red()
        )
        embed.set_thumbnail(url=self.picture)
        return embed