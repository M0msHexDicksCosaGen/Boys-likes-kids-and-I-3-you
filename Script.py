import discord
from discord.ext import commands
import asyncio
import random
import traceback
import logging
import os
bot = commands.Bot (command_prefix = "!")
client = discord.Client()
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Logycl is burning over here")

@bot.event
async def on_member_join(member):
    await member.guild.get_channel(347845197780221953).send(f"<@{member.id}> has joined the mafia!")
    await member.edit(roles=member.roles+[discord.utils.get(member.guild.roles,name='Italian')])

@bot.command()
async def mute(ctx, member:discord.Member):
    """Mute the client on the server."""
    if "Boss" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        for each in ctx.guild.channels:
                await each.set_permissions(member, overwrite=overwrite) 

@bot.command()
async def unmute(ctx, member:discord.Member):
    """Unmute the client on the server."""
    if "Boss" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = None
        for each in ctx.guild.channels:
            await each.set_permissions(member, overwrite=overwrite)
            
@bot.command()
async def ban (ctx, member:discord.Member):
    """Bans the client with mention."""
    await ctx.guild.ban(member)
    await ctx.send(f"Bitch,{member.mention} has been banned!")

@bot.command()
async def kick(ctx, *, member : discord.Member = None):
    """Kick the client at the server."""
    try:
        await member.kick()
        await ctx.send(ctx.message.author.mention + "Done, This motherfucker already wanted some smoke!")
    except discord.errors.Forbidden:
        await ctx.send('I don\'t have perms')
        
@bot.command()
async def warn(ctx, user: discord.Member, *, reason: str):
    await ctx.send(f'{ctx.author.mention} You have successfully warned **{user.mention}** for `{reason}`.')
    await ctx.send(f'{user} You have been warned for `{reason}` in `{ctx.guild.name}`.')
    warning = open("warned.txt", "a+")
    warning.write(f' {user} has been warned for `{reason}` `this was done by {ctx.author.mention}`') 
    warning.close()
    await ctx.send(f":warning: {user.mention} had been warned")  
    
@bot.command()
async def prune(ctx, number: int, user: discord.Member = None):
    """Deletes the specified amount of messages."""
    lim = 0
    if number is None:
        await ctx.send("Please specify a number of messages to be deleted.")
    else:
        async for x in ctx.history(limit=5000, before=ctx.message.created_at):
            if lim > number:
                break
            if user:
                if x.author == user:
                    await x.delete()
                else:
                    pass
            else:
                await x.delete()
            lim += 1
            
            
@bot.command()
@commands.is_owner()
async def play(ctx,*game :str):
    """Playing status for the bot {Bot-Owner Only}."""
    print(*game)
    await bot.change_presence(activity=discord.Game(name="!help | pl0t.gq"))
    
@bot.command()
@commands.is_owner()
async def stream(ctx,* , title : str):
    await bot.change_presence(activity=discord.Streaming(name=title, url="https://twitch.tv/discordapp"))
    
@bot.command()
@commands.is_owner()
async def listen(ctx,* ,title : str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))

@bot.command()
@commands.is_owner()
async def watch(ctx,* ,title : str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=title)) 
        
@bot.command()
async def Spotify(ctx):
    if "Italian" in [role.name for role in ctx.author.roles]:
        things = random.choice(["nothingguy000@yahoo.com:nobody00 | Premium for Family |  | US," , "floresana2011@yahoo.com:green12 | Premium for Family | 5/16/18 | US," , "carollewiwi@gmail.com:Olyn7711 | Premium for Family |  | ID," , "delta.onta@gmail.com:Ontagracia7474 | Spotify Premium |  | ID" , "sigal.teller@gmail.com:gargamel | Spotify Premium | 5/10/18 | IL," , "tomermx@gmail.com:603603 | Spotify Premium | 5/11/18 | IL, " , "riklommert@hotmail.com:boterletter | Spotify Premium | 5/4/18 | NL" , "h.lazo.aravena@gmail.com:1619901990 | Spotify Premium | 6/3/18 | CL" , "fedecardelino@gmail.com:cabecha1 | Premium for Family |  | UY"])
        embed = discord.Embed(colour=0x00FFFF)
        embed.add_field(name='Your Spotify Account', value='What to add?')
        await ctx.author.send(embed=embed)

bot.run(os.getenv('TOKEN'))
