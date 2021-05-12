import discord
from discord.ext import commands

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
    print("online")



@client.command()
async def help(ctx):
    await ctx.channel.send("Pomoc")


client.run("token")
