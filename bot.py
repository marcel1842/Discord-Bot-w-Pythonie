import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
    print("online")
    await client.change_presence(activity=discord.Game(name="?help"))


@client.command()
async def losuj(ctx, min : int, max : int):
    if(min < max):
        numer = random.randrange(min, max)
        await ctx.channel.send(numer)
    else:
        await ctx.channel.send("podałeś złe liczby")

@client.command()
async def witaj(ctx):
    tablica = ["cześć", "witaj", "siemanko"]
    await ctx.channel.send(random.choice(tablica))




@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help ", url="https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A", description="Commands", color=0xeb1e1e)
    embed.add_field(name="help", value="pokazuje okienko", inline=False)
    embed.add_field(name="test", value="test", inline=False)
    embed.add_field(name="test1", value="test1", inline=False)
    await ctx.send(embed=embed, delete_after = 10)



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.ban(reason=reason)
    await ctx.channel.send(f"Zbanowano {member.mention} za {reason}", delete_after=10)


@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.kick(reason=reason)
    await ctx.channel.send(f"Wyrzucono <@{member.id}> za {reason}", delete_after=10)



@client.command()
async def graj(ctx, game):
    await client.change_presence(activity=discord.Game(name=game))


@client.command()
async def streamuj(ctx, game):
    await client.change_presence(activity=discord.Streaming(name=game, url="https://www.twitch.tv/mario1842"))

@client.command()
async def sluchaj(ctx, music):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=music))
    
@client.command()
async def ogladaj(ctx, film):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=film))

client.run("token")
