import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(filename="base.log", level=logging.INFO)


class TemplateBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        # Cogs, which should be added manually to self._cogs
        self._cogs = ['cogs.example', ]
        super().__init__(command_prefix=os.getenv("PREFIX"), case_insensitive=True)

    async def on_connect(self):
        logging.info(
            f"Connected to Discord (latency: {self.latency*1000:,.0f} ms).")

    async def on_ready(self):
        logging.info("Running setup...")
        for cog in self._cogs:
            self.load_extension(cog)
            logging.info(f"Loaded `{cog}` cog.")
        logging.info("Setup complete.")
        logging.info("Logged in")


intents = discord.Intents.all()
bot = TemplateBot(intents=intents)
bot.run(os.getenv("TOKEN"))
