import discord
from discord.ext import commands

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
    print("online")



@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help ", url="https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A", description="Commands", color=0xeb1e1e)
    embed.add_field(name="help", value="pokazuje okienko", inline=False)
    embed.add_field(name="test", value="test", inline=False)
    embed.add_field(name="test1", value="test1", inline=False)
    await ctx.send(embed=embed, delete_after = 10)



client.run("token")
