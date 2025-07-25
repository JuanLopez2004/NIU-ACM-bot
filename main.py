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
    await ctx.send("hi")

## Welcome Message
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:

        # Create the embed with welcome text
        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}!",
            description=(
                f"{member.mention}, If you haven't already, join the HuskieHub to become an official NIU ACM member!\n\n"
                "[Click here to Join ACM](https://huskiehub.niu.edu/NIUACM/club_signup)"
            ),
        )

        # Attach an image to display inside the embed
        embed.set_image(url="attachment://psychcs.png")

        # Open the image and send it along with the embed
        with open(r"C:\Users\radis\OneDrive\Desktop\NIU-ACM-bot\images\psychcs.png", "rb") as f:
            file = discord.File(f, filename="psychcs.png")
            await channel.send(embed=embed, file=file)

## ICS Huskie Hub event posting







## Run the bot with the token and logging handler
bot.run (token, log_handler=handler, log_level=logging.DEBUG)