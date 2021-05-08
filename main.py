import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time
import random

intends = discord.Intents.default()
intends.members = True
client = commands.Bot(intents=intends, command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready")
    await client.change_presence(activity=discord.Game(name="The Vidarn"))



@client.event
async def on_member_join(member):
    kanal=client.get_channel(838361960994308117)
    rola=discord.utils.get(member.guild.roles, id=840411251447693313)
    await kanal.send(f"Witaj <@{member.id}>")
    await member.add_roles(rola)

@client.event
async def on_member_remove(member):
    kanal=client.get_channel(838361960994308117)
    await kanal.send(f"Żegnaj <@{member.id}>")
    



@client.command()
@has_permissions(manage_messages = True)
async def mute(ctx, member : discord.Member, czas = 5):
    rola = discord.utils.get(ctx.guild.roles, name = "mute")
    await member.add_roles(rola)
    await ctx.send(f"zmutowano na {member} na {czas}m")
    time.sleep(czas * 60)
    await member.remove_roles(rola)
    await ctx.send(f"odmutowało {member}")




@client.command()
@has_permissions(manage_messages = True)
async def streamuj(ctx):
    await client.change_presence(activity=discord.Streaming(name="Stream", url="https://www.twitch.tv/mario1842"))

@client.command()
@has_permissions(manage_messages = True)
async def sluchaj(ctx):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Właściciela"))

    
@client.command()
@has_permissions(manage_messages = True)
async def ogladaj(ctx):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Serial"))


@client.command()
@has_permissions(manage_messages = True)
async def graj(ctx, wco="gre"):
    await client.change_presence(activity=discord.Game(name=wco))

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



client.run("twój roken")
