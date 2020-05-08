import discord
from discord import utils
from discord.ext import commands
import asyncio
import random
import os

token = os.environ.get('btoken')
serverid = 495444566460334089

#client = discord.Client()
client = commands.Bot( command_prefix = '.')
client.remove_command( 'help' )
PREFIX = "."

@client.command()
async def game(ctx):
	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'Minecraft с Равшаном'  ) )

@client.command()
async def info(ctx):
    print('Табличка с инфой работает')
    embed=discord.Embed(title="ПИ-БОТ", description="Бот был написан специально для ПИ-18(9)", color=0x0080ff)
    
    embed.add_field(name="Cоздатель:", value="L0veLy#0930", inline=True)
    embed.add_field(name="Версия:", value="1.4", inline=True)
    embed.set_thumbnail(url = 'https://sun9-20.userapi.com/c854428/v854428908/2254db/JbzkuFH0T74.jpg')
    embed.set_footer(text="Бот пока что без хоста потому что у создателя руки из жопы. Буду рад любой помощи.")
    
    await ctx.send(embed=embed)

#Сообщение о том, что Юзер зашёл на сервер + выдача роли
@client.event
async def on_member_join( member ):
    print('Приветственное сообщение работает')
    emb = discord.Embed( description = f"Крыса под именем **{member.mention}** зашла на сервер, добро пожаловать!", color = 0x0c0c0c )
    role = discord.utils.get( member.guild.roles, id = 671094284254183434 ) # Айди роли, которая будет выдаваться, когда человек зашёл на сервер

    await member.add_roles( role )
    channel = client.get_channel( 495444566896410635 ) # Айди канала, куда будет писаться сообщение
    await channel.send( embed = emb ) 

colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]
rainbowrolename = "АДМИНЫ"
delay = 5

@client.event
async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))  

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))
    print('Радужная роль работает')     
         
Bot.run(str(token))
#client.run(token)
