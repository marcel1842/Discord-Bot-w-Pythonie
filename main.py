import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready")


@client.command()
async def help(ctx):
    await ctx.send("Na razie jest tylko komenda help")



@client.command()
@has_permissions(manage_messages = True)
async def clear(ctx, value=5):
    await ctx.channel.purge(limit=value+1)


@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, *, reason="No Reason"):
    await member.kick(reason=reason)

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="No Reason"):
    await member.ban(reason=reason)



client.run("ODM4MjM5NDY2OTAzOTYxNjQx.YI4NVg.my4hTcUkYiUdY-8I7nCthH8HYmg")
