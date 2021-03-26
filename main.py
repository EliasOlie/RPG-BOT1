import discord
from discord.ext import commands
from random import randint
import json
import setting
import os

description = '''Bot para jogar RPG de mesa na quarentena.'''

intents = discord.Intents.default()

bot = commands.Bot('?',description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def hi(ctx):
    await ctx.send(f'Hi, {ctx.author.name}')

@bot.command()
async def roll(ctx, number):
    if number == 'd4':
        result = f'{ctx.author.mention}!\n--> {randint(1,4)}'
        await ctx.send(result)
    
    if number == 'd6':
        result = f'{ctx.author.mention}!\n--> {randint(1,6)}'
        await ctx.send(result)
    
    if number == 'd8':
        result = f'{ctx.author.mention}!\n--> {randint(1,8)}'
        await ctx.send(result)
    
    if number == 'd10':
        result = f'{ctx.author.mention}!\n--> {randint(1,10)}'
        await ctx.send(result)
    
    if number == 'd12':
        result = f'{ctx.author.mention}!\n--> {randint(1, 12)}'
        await ctx.send(result)
    
    if number == 'd20':
        result = f'{ctx.author.mention}!\n--> {randint(1,20)}'
        await ctx.send(result)
    
@bot.command()
async def criarFicha(ctx, cN, cR, cC, fo, de, co, inte, ws, ch):
    attributes = {
        "Strenght": fo,
        "Dextery": de,
        "Constitution": co,
        "Inteligence": inte,
        "Wisdom": ws,
        "Charisma": ch
    }
    
    equipments = {
        "MainWea":"18",
        "SecWea": "5",
        "Kit": "kitname",
        "Armor": "ArmorRate",
        "Currency": "value"
    }
    
    ficha = {
        str(ctx.author.name): {
            "CharName": cN,
            "CharRace": cR,
            "CharClass": cC,
            "CharAttributes": attributes,
            "CharEquipments": equipments
        } 
    }

    arquivo = json.dumps(ficha)


    ex = open('fichas.json', 'w')
    ex.write(arquivo)    
    print('Feito')
    ex.close()


    await ctx.send('Done!')


bot.run(os.getenv('TOKEN'))