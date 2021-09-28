import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot Ready")

@client.command()
async def yt(ctx):
    await ctx.send("ZestOo's YouTube Channel is: https://www.youtube.com/c/ZestOoMC")
    await ctx.send("The latest Video By ZestOo is: https://www.youtube.com/watch?v=_hLn6A8-D_4")

@client.command()
async def announce(ctx):
    channel = client.get_channel(841563717573279744)
    await channel.send("||@everyone|| NEW VIDEO POGGGG GO WATCH NOW E,\n https://www.youtube.com/watch?v=_hLn6A8-D_4")

client.run('ODkyMjcxNDUzNDIzMTUzMTgz.YVKejA.xYe9_ppuDh_d0zy-Za7wrEz0OWQ')