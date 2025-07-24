import discord
from discord.ext import commands
import logging
import os   
from dotenv.main import load_dotenv

## Load environment variables from .env file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

## Intent handling for message content and members
handler = logging.FileHandler(filename='discord.log', encoding="utf8", mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

## Prefix
bot = commands.Bot(command_prefix='?', intents=intents)
bot.remove_command("help")  

## Logging 
@bot.event 
async def on_ready():
    print(f"Acy is Ready.")

## Test Command 

@bot.command(name='test')
async def test_command(ctx):                            
    await ctx.send("hi chud")

## Run the bot with the token and logging handler
bot.run (token, log_handler=handler, log_level=logging.DEBUG)