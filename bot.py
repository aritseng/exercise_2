import discord
from discord.ext import commands
import json
import random 

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile) 

bot = commands.Bot(command_prefix="*",intents=discord.Intents.all())                  #指令*

@bot.event
#當機器人完成啟動時
async def on_ready():
    print(">> bot is online <<")
    game = discord.Game('跟老大躲貓貓')                                                #設定機器人狀態
    await bot.change_presence(status=discord.Status.online, activity=game)            #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible

@bot.event                                                                            #歡迎成員加入
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F"{member} 黨歡迎你!")

@bot.event                                                                            #成員離開
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F"{member} 已離開! 這就是ㄘㄨㄚˋ執政的下場")

@bot.command()                                                                        #測試ping值
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)}(ms)")

@bot.command()                                                                        #你在什麼頻道
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

@bot.command()                                                                        #彩蛋-汪
async def dog(ctx):
    await ctx.send(F"汪")

@bot.command()                                                                        #彩蛋-喵
async def cat(ctx):
    await ctx.send(F"喵")                                          

@bot.command()                                                                        #本地圖片(波奇)
async def bocchi(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)

@bot.command()                                                                        #網路圖片(喜多)
async def kita(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

@bot.command()                                                                        #晚餐隨機功能
async def food(ctx):
    random_dinner = random.choice(jdata['dinner'])
    await ctx.send(random_dinner)

@bot.command()                                                                        #晚餐premium隨機功能                                                                    
async def food_premium(ctx):
    random_dinnerpremium = random.choice(jdata['dinner_premium'])
    await ctx.send(random_dinnerpremium)

@bot.event
async def on_message(message):                                                        #關鍵字觸發訊息(老大、走啊)
    if message.author == bot.user:
        return
    if '老大' in message.content:
        await message.channel.send('老大在躲你')

    if '走啊' in message.content:
        await message.channel.send('走你大頭')

    if '原神' in message.content:
        await message.channel.send('不要跟我說那破爛遊戲')

    if '週本' in message.content:
        await message.channel.send('不要跟我說那破爛遊戲')

    if '納西妲' in message.content:
        await message.channel.send('不要跟我說那破爛遊戲')        

    if '吃' in message.content:
        await message.channel.send('吃你大頭') 

    if '吃飯' in message.content:
        await message.channel.send('林宗憶你他媽給我滾出來吃飯')

    if 'Ok' in message.content:
        await message.channel.send('老大氣到不想說話了') 

    if 'lol' in message.content:
        await message.channel.send('鄭學志你他媽到底有沒有要來打') 

    if '躲' in message.content:
        await message.channel.send('玩躲貓貓囉')   

    if  message.content == '喜多':
        await message.channel.send('我老婆')

    if '三小' in message.content:
        await message.channel.send('問老大')

    if '啥' in message.content:
        await message.channel.send('問老大')

    if '九妹' in message.content:
        await message.channel.send('割韭菜')

    if '...' in message.content:
        await message.channel.send('林宗憶你看不起我是不是')

    if '蔡' in message.content:
        await message.channel.send('操機掰ㄘㄨㄚˋ英文   ㄘㄨㄚˋ英文操機掰')

    if '菜' in message.content:
        await message.channel.send('操機掰ㄘㄨㄚˋ英文   ㄘㄨㄚˋ英文操機掰')

    if '民進黨' in message.content:
        await message.channel.send('操機掰ㄘㄨㄚˋ英文   ㄘㄨㄚˋ英文操機掰')

    if 'ㄘㄨㄚˋ' in message.content:
        await message.channel.send('操機掰ㄘㄨㄚˋ英文   ㄘㄨㄚˋ英文操機掰')                

    await bot.process_commands(message)

@bot.command()                                                                        #覆誦+刪除訊息
async def sayd(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message) 

@bot.command()                                                                        #清理訊息
async def clean(ctx,num:int):
    await ctx.channel.purge(limit=num+1)  
     

bot.run(jdata['TOKEN'])