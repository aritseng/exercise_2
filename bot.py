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
    await channel.send(F"{member}")
    await channel.send(F"黨歡迎你加入")

@bot.event                                                                            #成員離開
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F"{member}")
    await channel.send(F"已離開! 這就是ㄘㄨㄚˋ執政的下場")


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

@bot.command()                                                                        #網路圖片(喜多)
async def kita(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

@bot.command()                                                                        #網路圖片(虹夏)
async def nijika(ctx):
    random_pic2 = random.choice(jdata['url_pic2'])
    await ctx.send(random_pic2)

@bot.command()                                                                        #網路圖片(虹夏)
async def bocchi(ctx):
    random_pic3 = random.choice(jdata['url_pic3'])
    await ctx.send(random_pic3)    

@bot.command()                                                                        #晚餐隨機功能
async def food(ctx):
    random_dinner = random.choice(jdata['dinner'])
    await ctx.send(random_dinner)

@bot.command()                                                                        #晚餐premium隨機功能                                                                    
async def food_premium(ctx):
    random_dinnerpremium = random.choice(jdata['dinner_premium'])
    await ctx.send(random_dinnerpremium)

@bot.command()                                                                        #擲骰子                                                                    
async def dice(ctx):
    random_dice = random.choice(jdata['dice_random'])
    await ctx.send(F"上帝真的會擲骰子") 
    await ctx.send(random_dice)

@bot.command()                                                                        #上帝不會擲骰子                                                                    
async def dice_god(ctx):
    await ctx.send(F"上帝不會擲骰子")
    await ctx.send(F"6")        

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

    if message.content == '你好':
        await message.channel.send('哈囉')

    if '烤肉' in message.content:
        await message.channel.send('豪生你他媽是有沒有要烤肉')

    if '星爆' in message.content:
        await message.channel.send('快...還要更快...')
        await message.channel.send('https://i.ytimg.com/vi/yAitBgZwkDQ/maxresdefault.jpg')

    if '幫我撐十秒' in message.content:
        await message.channel.send('那是什麼招式啊')                                 

    await bot.process_commands(message)

@bot.command()                                                                        #覆誦+刪除訊息
async def sayd(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message) 

@bot.command()                                                                        #清理訊息
async def clean(ctx,num:int):
    await ctx.channel.purge(limit=num+1)

@bot.command()                                                                        #關於機器人
async def about(ctx):
    embed=discord.Embed(title="about", url="https://youtu.be/dQw4w9WgXcQ", description="about the bot", color=0xf202a6)
    embed.set_author(name="波奇醬", url="https://youtu.be/dQw4w9WgXcQ", icon_url="https://memeprod.ap-south-1.linodeobjects.com/user-template/e07d50327828a93c4098ef5432d6d564.png")
    embed.set_thumbnail(url="https://memeprod.ap-south-1.linodeobjects.com/user-template/e07d50327828a93c4098ef5432d6d564.png")
    embed.add_field(name="晚餐功能(宜蘭限定)", value="*food", inline=True)
    embed.add_field(name="晚餐功能(豪華版)", value="*food_premium", inline=True)
    embed.add_field(name="測試ping值", value="*ping", inline=True)
    embed.add_field(name="你位於什麼頻道", value="*here", inline=True)
    embed.add_field(name="生成喜多圖片", value="*kita", inline=True)
    embed.add_field(name="生成虹夏圖片", value="*nijika", inline=True)
    embed.add_field(name="生成小孤獨圖片", value="*bocchi", inline=True)
    embed.add_field(name="擲骰子", value="*dice", inline=True)
    embed.add_field(name="上帝不會擲骰子", value="*dice_god", inline=True)
    embed.add_field(name="用機器人說話", value="*sayd [你要說的話]", inline=True)
    embed.add_field(name="清理訊息", value="*clean [數字]", inline=True)
    embed.add_field(name="天氣功能(開發中)", value="*weather", inline=True)
    embed.add_field(name="地震功能(開發中)", value="*earthquake", inline=True)
    embed.add_field(name="SAO冒險功能(開發中)", value="*link_start", inline=True)
    embed.add_field(name="關鍵字自動回覆", value="你好、老大、走啊、星爆、原神、吃、九妹、菜", inline=True)
    embed.set_footer(text="指令功能")
    await ctx.send(embed=embed)  
     

bot.run(jdata['TOKEN'])