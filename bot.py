import discord
from discord.ext import commands
import json
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile) 

bot = commands.Bot(command_prefix=";",intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print(">> bot is online <<")

@bot.command()
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F"{member} 歡迎加入!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F"{member} 已離開!")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)}(ms)")

@bot.command()
async def dog(ctx):
    await ctx.send(F"汪")            

bot.run(jdata['TOKEN'])