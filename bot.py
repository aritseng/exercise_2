import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="&",intents=discord.Intents.all())

@bot.command()
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

bot.run("MTEwNDcwMjk4NDExOTY1NjQ5OQ.GOjntO.p-RLlej8WhT1C2KCrKhjlKneVazZ8f68wb1T7w")