import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# set discord token
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Privileged Gateway Intents
intents = discord.Intents.default()
intents.message_content = True

# command_prefix for user
client = commands.Bot(command_prefix="-", intents=intents)


@client.event
async def on_ready():
    print("Bot is Running")
    print("--------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello")


client.run(TOKEN)
