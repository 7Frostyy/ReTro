import discord
import os

client = discord.Client()

@client.event
async def on-ready():
    print ("ReTro is ready")
    
client.run(os.environ['DISCORD_TOKEN'])