import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.idle, activity=discord.Game('ReTro'))
    print ("ReTro is ready")
    
client.run(os.environ['DISCORD_TOKEN'])
