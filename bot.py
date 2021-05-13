import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
    print("online")
    await client.change_presence(activity=discord.Game(name="?help"))



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


@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.kick(reason=reason)




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
