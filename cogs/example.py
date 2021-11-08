import logging
import discord
from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        logging.info("Used hello command")
        await ctx.send("Hello, world!")


def setup(bot):
    bot.add_cog(ExampleCog(bot))
