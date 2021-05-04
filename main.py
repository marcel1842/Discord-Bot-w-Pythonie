import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time
import random

client = commands.Bot(command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready")


@client.command()
async def help(ctx, value=None):

    if(value == "test"):
        await ctx.send("test")
    elif(value == "test2"):
        await ctx.send("test2")
    elif(value == None):
        embed=discord.Embed(title="Help Commands", description="Categories", color=0x52fa0f)
        embed.add_field(name="help test", value="pokazuje test", inline=False)
        embed.add_field(name="help test2", value="pokazuje test2", inline=False)
        await ctx.send(embed=embed)


@client.command()
async def witaj(ctx):
    odp =['czesc', 'witaj','miło cie poznać']
    await ctx.send(random.choice(odp))


@client.command()
async def pewny(ctx):
    procent = random.randrange(1, 101)
    await ctx.send(f'jestem pewny na {procent} %')
    
    



@client.command()
@has_permissions(manage_messages = True)
async def clear(ctx, value=5):
    await ctx.channel.purge(limit=value+1)
    time.sleep(1)
    embed=discord.Embed(title=f"usuniento {value}", color=0x52fa0f)
    message = await ctx.send(embed=embed, delete_after=5)

@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, *, reason="No Reason"):
    await member.kick(reason=reason)

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="No Reason"):
    await member.ban(reason=reason)



client.run("twój token")
