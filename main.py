import discord
from discord.ext import commands
import requests
import random

bot = commands.Bot(command_prefix='+', intents=discord.Intents().all())

@bot.event
async def on_ready():
    print(f'logged {bot.user}')
    await ctx.send(f'ПРИВЕТ {bot.user}!')

@bot.command('plastic')
async def plastic(ctx):
    await ctx.send(f'25%')

@bot.command('metal')
async def metal(ctx):
    await ctx.send(f'25%')

@bot.command('dirt')
async def dirt(ctx):
    await ctx.send(f'100%')

@bot.command('wood')
async def wood(ctx):
    await ctx.send(f'100%')

@bot.command('clay')
async def clay(ctx):
    await ctx.send(f'100%')

@bot.command('stone')
async def stone(ctx):
    await ctx.send(f'100%')

@bot.command('glass')
async def glass(ctx):
    await ctx.send(f'90%')

@bot.command('concrete')
async def concrete(ctx):
    await ctx.send(f'50%')

@bot.command('help')
async def concrete(ctx):
    await ctx.send(f'Привет чел {bot.user}. это вот про екологию, здесь можеш писать толко мартерялы на ENG. например как (plastic) и т.п')
    
bot.run('')
