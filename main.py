import discord
from discord import app_commands, Member
from discord.ext import commands, tasks
import random
import json
from typing import Optional

import pandas as pd
import numpy as np
import asyncio
from time import sleep
import os
import logging
from datetime import datetime
import pytz
import variables
from variables import GiftName

from enum import Enum

cached_messages = {}

gifts = {
    '5.5': "游戏机",
    '7.88': "气噗噗的老头",
    '6.61': "SB14K",
    '6.62': "印花集",
    '13.14': "要抱抱",
    '28.8': "枪响人亡",
    '33.44': "生日蛋糕",
    '52': "水栽竹",
    '88': "美杜莎",
    '128': "波塞冬",
    '66.1': "半日冠名 - 女神之泪",
    '131.4': "一日冠名",
    '365': "三日冠 - 骑士之誓",
    '521': "五日冠名 - 救赎",
    '888': "周冠名 - 炙热香炉",
    '1588': "半月冠 - 双生暗影",
    '3188': '月冠 - 潘多拉的秘密',
    '8888': "季冠名 - 自然之力",
    '32888': "年冠名 - 无限宝珠",
    '52.1': "歌手半日冠",
    '100': "歌手日冠名",
    '99': '儿童节全套玩具',
    '99.2': "虚拟恋人",
    '66': "兔几便当盒",
    '33': "喵子冰淇淋",
    '25': '艾草',
    '75': '甜咸小祖粽',
    '140': '端午节限定一日冠',
    '380': '端午节限定三日冠',
    '540': '端午节限定五日冠',
    '1160': '端午节全套礼物'
}

specialGifts = ['火焰之心 Flame heart', '坚韧之盾 Shield of Resilience', '幸运宝链 Lucky Charm',
                '活力之源  Essence of Vitality', '奔流之风 Zephyrs Flow', '璀璨之星 Radiant Star',
                '奇迹之锚 Anchor of Wonders', '𝓢𝓡 胜利之冠 Crown of Victory', '𝓢𝓡 神奇魔杖 Enchanted Wand',
                '𝓢𝓢𝓡 征服之剑 Sword of Conquest']
prob = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.3, 0.2, 0.15]


# Custom formatter
class MyFormatter(logging.Formatter):
    converter = datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            s = dt.astimezone(pytz.timezone('America/New_York')).strftime(datefmt)
        else:
            t = dt.astimezone(pytz.timezone('America/New_York')).timetuple()
            s = self.default_time_format % t[:6]
        return s


# create logger
logger = logging.getLogger(' ')
logger.setLevel(logging.INFO)

# create file handler which logs even debug messages
fh = logging.FileHandler('./inkbot/logs.txt')
fh.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = MyFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %Z%z')
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)

# log some messages
logger.info('bot started\n\n')

# token = 'MTA3NDc0NTEyMzA3OTk4NzIxMA.GmMtlj.DQ3TbcgkwVBvRgYd_Bob422HBBPGVT8SRVISo0'
guild = ''

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

oChanneln = 1112208806546509895
cChanneln = 1112208558763819008
tChanneln = variables.lwbb
dChanneln = 1111868751990763652
roleID = 966085269965119488

from xdz import *


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.scheduler = None
        self.tree = app_commands.CommandTree(self)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('版本信息：')
    print('Beta 1.0 \n ')

    try:
        check_cooldowns.start()
        auto_clear_warning.start()
        synced = await client.tree.sync()
        print(f'synced {len(synced)} commands')
    except Exception as e:
        print(e)


cooldown_time = 604800  # One week in seconds
cooldown_file = './inkbot/cd.txt'
check_interval = 60



def load_last_data():
    try:
        with open(cooldown_file, 'r') as f:
            data = json.load(f)
            return datetime.strptime(data["time"], '%Y-%m-%dT%H:%M:%S'), data["user_id"]
    except (FileNotFoundError, ValueError, KeyError):
        return None, None

# Save the last usage time to file
def save_last_data(time, user_id):
    with open(cooldown_file, 'w') as f:
        json.dump({"time": time.strftime('%Y-%m-%dT%H:%M:%S'), "user_id": user_id}, f)




last_usage, last_user_id = load_last_data()


entrylist = []
winnerlist = []
egg_flag = True

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    # if message.author == client.user:
    #    return
    a = '100$代金券'
    b = '150$代金券'
    c = '200$代金券'
    d = '女神之泪（半日冠名）'
    e = '$88美杜莎'
    f = '再来一次！'
    #g = '自定义tag 三个月（2人）'
    h = '$30各种游戏代金券（riot等）'
    i = '返场限时tag'
    j = '返场永久tag'
    k = '感谢惠顾'
    l = '指定陪玩三日自定义后缀（需征求同意）'
    m = '女神之泪（半日冠名）'
    n = '$52 水栽竹'
    o = '四陪一一小时娱乐代金券'
    p = '春节礼物 虎虎哈嘿'

    if message.channel.id in game_start_channels:
        # 加入游戏participants
        game_start_channels[message.channel.id]['participants'].append(message.author.id)


    if message.content == "开箱一时爽，一直开箱一直爽" and message.channel.name == "『🎰』﹒潘多拉的宝箱":


        targets = [a, b, c, d, e, f, h, i, j, k]
        accuracy = [0.06, 0.04, 0.03, 0.12, 0.08, 0.15, 0.20, 0.12, 0.05, 0.15]

        result = str(random.choices(targets, accuracy))
        result = result.replace('[', '')
        result = result.replace(']', '')
        result = result.replace("'", '')
        result = result.replace('"', '')
        aaa = result
        result = "恭喜您获得： " + result

        await message.channel.send(result)
        image_path = f'./inkbot/pdlimg/{aaa}.png'
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                picture = discord.File(f)
            await message.channel.send(file=picture)
        await client.process_commands(message)

    elif message.content == "拜托了，出个金的呗" and message.channel.name == "🐯－虎虎生威，嗷呜":
        targets = [l, m, n, o, p]
        accuracy = [0.20, 0.20, 0.20, 0.20, 0.20]

        result = str(random.choices(targets, accuracy))
        result = result.replace('[', '')
        result = result.replace(']', '')
        result = result.replace("'", '')
        result = result.replace('"', '')
        result = "恭喜您获得： " + result
        await message.channel.send(result)
        await client.process_commands(message)

    elif message.content == "Libra生日快樂" and message.channel.name == "抽奖咯✌":
        entry = message.author
        if entry not in entrylist:
            entrylist.append(entry)
        else:
            entrylist.remove(entry)
    elif message.content == "截止" and message.channel.name == "抽奖咯✌":
        print(entrylist)
        for number in range(21):
            try:
                randomnumber = random.randint(0, len(entrylist))
            except Exception as e:
                print("error?", e)
                randomnumber = random.randint(0, len(entrylist))
            if randomnumber >= len(entrylist):
                randomnumber = random.randint(0, len(entrylist))
            elif randomnumber <= len(entrylist):
                winner = entrylist[randomnumber]
                if winner not in winnerlist:
                    await message.channel.send("The winner is: " + winner.mention)
                winnerlist.append(winner)
        await message.channel.send(
            "恭喜以上中獎的各位，也請各位得獎的幸運兒記得報單，獎品是yhj，老闆是Libra! 感謝各位的大力支持")
    elif message.content == "开始抽奖啦，想参加的话请输入:Libra生日快樂" and message.channel.name == "抽奖咯✌":
        for i in range(len(entrylist)):
            entrylist.remove(entrylist[i])
        await message.channel.send("抽奖初始完成！！")

    elif message.channel.name == "『💬』﹒24hr热聊大厅":

        global last_usage, last_user_id
        now = datetime.utcnow()
        if last_usage:
            difference = (now - last_usage).total_seconds()
            if difference < cooldown_time:
                return


        random_num = random.randint(1, 200)
        print(f'{now} ,  rand: {random_num}')

        if random_num < 199:
            return


        try:
            print('triggered 彩蛋')
              # So you can modify the global variable


            await message.author.edit(nick=f'{message.author.name}🥚彩蛋幸运者')
            await message.channel.send(f'{message.author.mention} 触发彩蛋了！')

            last_usage = now
            last_user_id = message.author.id
            save_last_data(now, message.author.id)


            logger.info(f'修改昵称成功: {message.author.name}  彩蛋幸运者')
        except Exception as e:
            # 如果发生异常，那么把彩蛋视作失败

            logger.error(f'修改昵称失败: {e}')




    await client.process_commands(message)



@tasks.loop(seconds=check_interval)
async def check_cooldowns():
    now = datetime.utcnow()
    if not last_usage:
        return


    difference = (now - last_usage).total_seconds()

    if difference >= cooldown_time:

        for guild in client.guilds:
            member = guild.get_member(int(last_user_id))
            if member and member.nick and member.nick.endswith('🥚彩蛋幸运者'):
                try:
                    new_nick = member.nick[:-6]  # Removing the 'cd' from the end
                    await member.edit(nick=new_nick)
                except discord.Forbidden:
                    # If bot doesn't have permission to edit member's nickname
                    pass












@client.tree.command()
@app_commands.describe(
    成员='看指定成员的加入时间，不输入则默认为当前发出指令的成员'
)
async def joined(interaction: discord.Interaction, 成员: Optional[discord.Member] = None):
    """显示member的加入时间"""
    member = 成员 or interaction.user
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}',
                                            ephemeral=True)












def phase():
    with open('./inkbot/phase.txt', 'r') as file:
        total = file.read()
    return int(total)


def checkInteraction(interaction):
    role = discord.utils.get(interaction.guild.roles, id=roleID)

    if interaction.user.id == 717898166011297842:
        return True
    if not role in interaction.user.roles:

        return False
    else:
        return True


def check(ctx):
    role = discord.utils.get(ctx.guild.roles, id=roleID)

    if ctx.author.id == 717898166011297842:
        return True

    if not role in ctx.author.roles:

        return False
    else:
        return True


@client.command()
async def manual(ctx):
    if not check(ctx):
        await ctx.channel.send("没有权限")
        return

    t = "!list     礼物对应点数\n\n\n!songli 送礼人ID 接收人ID 礼物点数（ 如： !songli 717898166011297842 717898166011297842 6.61） 用户dcID可以通过右键用户头像查看（需要在设置中打开开发者模式（设置-> 高级设置-> 开发者模式) \n\n\n!total    查看当前全工会累计点数 \n\n\n!clear  清空所有数据（慎用!)\n\n\n!edit 送礼人ID 任意点数 （如： !edit 717898166011297842 -100） 此功能用于送错礼物时调整累计点数\n\n!chaxun ID  可以查询单人贡献，管理员可以查询所有人，其他的阿猫阿狗只能查询自己（如： !chaxun 717898166011297842）\n\n !drsl 送礼人 接受人s 礼物编号（送礼人的ID + 空格后 接所有接受人的id 注意⚠️  几个接受人中间没有空格！！！）"

    await ctx.channel.send(t)


@client.command()
async def chaxun(ctx, id):
    if check(ctx) or ctx.author.id == id:
        res = 0
        df = pd.read_csv('./inkbot/data1.csv')

        p = phase()
        names = df.iloc[:, 0].tolist()
        values = df.iloc[:, p].tolist()
        if id == 'all' or id == 'ALL':
            res = ''
            for i, j in zip(names, values):
                res = res + f"<@{i}> {i} :   {j}\n\n"
            l = []
            for i in range(0, len(res), 2000):
                l.append(res[i:i + 2000])
            for j in l:
                await ctx.channel.send(j)
            return

        for i in range(len(names)):
            if str(names[i]) == str(id):
                indvalues = df.loc[i].tolist()

                for j in range(1, len(indvalues)):
                    res += float(indvalues[j])
                await ctx.channel.send(f"<@{id}> 再当前阶段的贡献值为： {values[i]}，总贡献值为 {res} 。"
                                       )
                return

        await ctx.channel.send(f"<@{id}> 没有任何送礼记录。")
    else:
        await ctx.channel.send("没有权限。")


def update(sender, num):
    p = phase()
    filename = "./inkbot/data1.csv"

    num = np.float64(num)
    # Read the CSV file into a pandas DataFrame
    with open('./inkbot/total.txt', 'r') as file:

        total = file.read()
    new = float(total) + float(num)

    with open('./inkbot/total.txt', 'w') as file:
        file.write(str(new))

    df = pd.read_csv(filename)
    df['client1'] = df['client1'].astype(str)

    matching_rows = df[df.iloc[:, 0] == str(sender)]

    if not matching_rows.empty:
        # Modify the second column of the matching rows
        df.loc[matching_rows.index, df.columns[p]] += num



    else:
        new_row = [sender] + [0] * 5
        new_row[p] = num
        df.loc[len(df)] = new_row

    df.to_csv('./inkbot/data1.csv', index=False)

    # write to today's file

    desired_timezone = pytz.timezone('America/New_York')
    current_time = datetime.now(desired_timezone)
    filename = str(current_time)
    filename = filename[:10]
    filename = "./inkbot/" + filename

    if os.path.isfile(filename):

        df = pd.read_csv(filename)
        df['client1'] = df['client1'].astype(str)

        matching_rows = df[df.iloc[:, 0] == str(sender)]

        if not matching_rows.empty:
            # Modify the second column of the matching rows
            df.loc[matching_rows.index, df.columns[1]] += num
        else:
            new_row = [sender, num]

            df.loc[len(df)] = new_row
    else:

        data = {"client1": [str(sender)], "value1": [num]}
        df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def announcePhase():
    p = int(phase())
    tChannel = client.get_channel(tChanneln)

    res = '0'
    with open('./inkbot/total.txt', 'r') as file:

        total = float(file.read())

    with open('./inkbot/caps.txt', "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    phases = lines[0].split()
    caps = lines[1].split()
    mid = lines[2].split()
    midcaps = lines[3].split()

    for i in range(len(phases)):
        if p == int(phases[i]):

            if total >= int(mid[i]):
                if midcaps[i] == '0':
                    # announce
                    res = mid[i]

                    midcaps[i] = '1'

            if total >= int(caps[i]):
                # announce
                print('reached')
                print(caps[i])
                p = p + 1
                res = caps[i]

    with open('./inkbot/caps.txt', "w") as file:
        file.write(' '.join(map(str, phases)) +
                   '\n')  # Convert elements to strings and join with spaces
        file.write(' '.join(caps) + '\n')
        file.write(' '.join(mid) + '\n')
        file.write(' '.join(midcaps) + '\n')

    with open('./inkbot/phase.txt', 'w') as file:
        file.write(str(p))

    return res


def getTops(p):
    res = []
    df = pd.read_csv('./inkbot/data1.csv')

    names = df.iloc[:, 0].tolist()
    values = df.iloc[:, p].tolist()
    values = [int(i) for i in values]

    sorted_lists = sorted(zip(values, names), reverse=True)

    sorted_values, sorted_names = zip(*sorted_lists)

    res.append(sorted_names[:5])
    res.append(sorted_values[:5])

    return res


@client.command()
async def c(ctx):
    desired_timezone = pytz.timezone('America/New_York')
    current_time = datetime.now(desired_timezone)
    filename = str(current_time)
    filename = filename[:10]
    filename = "./inkbot/" + filename
    df = pd.read_csv(filename)

    names = df.iloc[:, 0].tolist()
    value = df.iloc[:, 1].tolist()

    sorted_lists = sorted(zip(value, names), reverse=True)
    value, names = zip(*sorted_lists)
    value = value[:5]
    names = names[:5]
    res = ""
    for i, j in zip(names, value):
        res = res + f"<@{i}> :  {j}\n\n"

    await ctx.channel.send(res)


@client.command()
async def cc(ctx):
    desired_timezone = pytz.timezone('America/New_York')
    current_time = datetime.now(desired_timezone)
    filename = str(current_time)
    x = filename[9]
    x = int(x) - 1
    filename = filename[:9] + str(x)
    filename = "./inkbot/" + filename
    df = pd.read_csv(filename)

    names = df.iloc[:, 0].tolist()
    value = df.iloc[:, 1].tolist()

    sorted_lists = sorted(zip(value, names), reverse=True)
    value, names = zip(*sorted_lists)

    value = value[:5]
    names = names[:5]
    res = ""
    for i, j in zip(names, value):
        res = res + f"<@{i}> :  {j}\n\n"
    await ctx.channel.send(res)






def bobao(sender, receiver, points):
    res = ""
    receiver = receiver[2:-1]
    if points == '7.88':
        res = "<:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770><:tworabbits:1113127724647710770>" \
              "\n\n" \
              f"感谢 <a:804201856988348436:928185595648409630> 可爱迷人 <a:804201962614292482:928185622303240253> 的 <@{sender}> 送 <@{receiver}> 的 <:827326957716373514:957450665267978250> 气噗噗的老头 <:827326957716373514:957450665267978250> ！" \
              "\n\n" \
              " <a:1_17:928211220945846362> 感谢老板  <a:712524119983259681:922646454642819103> \n" \
              " <:FROG15:1039249529792381090> 心动值+7.88点"

    elif points == '6.62':
        res = "<a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644><a:1025149108077465610:1039977030965530644>" \
              "\n\n" \
              f"<a:962887121998315631:1039977513478262794><a:962887121998315631:1039977513478262794>  感谢 <a:804201856988348436:928185595648409630> 可爱迷人 <a:804201962614292482:928185622303240253> 的 <@{sender}> 送 <@{receiver}> 的 印花集！\n\n<a:1_17:928211220945846362> 感谢老板  <a:712524119983259681:922646454642819103> \n<a:heart:837437667276750868>心动值+6.6点<:p_02kiss01:1042991665314537585>"

    elif points == '131.4':
        res = "<a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452><a:little_twin_stars_star:1042991982206779452> \n\n" \
              f"<a:zzcafe_coffeecupcute2:1042992288957210764><a:zzcafe_coffeecupcute2:1042992288957210764> 感谢 <a:804201856988348436:928185595648409630> 可爱迷人 <a:804201962614292482:928185622303240253> 的 <@{sender}> 送 <@{receiver}> 的一日冠名！\n\n<a:1_17:928211220945846362> 感谢老板  <a:712524119983259681:922646454642819103> \n<a:heart:837437667276750868>心动值 +131.4 点<:p_02kiss01:1042991665314537585>"

    elif points == '66.1':
        res = "<a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278><a:851001082356170792:1039977746543157278>" \
              f"\n\n<a:C2_RainbowHeart:1042991399634735115><a:C2_RainbowHeart:1042991399634735115> 感谢 <a:804201856988348436:928185595648409630> 可爱迷人 <a:804201962614292482:928185622303240253> 的 <@{sender}> 送 <@{receiver}> 的半日冠名！\n\n<a:1_17:928211220945846362> 感谢老板  <a:712524119983259681:922646454642819103> \n<a:heart:837437667276750868>心动值 +66 点<:p_02kiss01:1042991665314537585>"

    elif points == '365':
        res = "<a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159>\n\n" \
              f"<a:4328heartpinkpuff:1042993563249676320><a:4328heartpinkpuff:1042993563249676320> 感谢  <a:804201856988348436:928185595648409630> <:hfk:1042620659139887165> 可爱迷人 <:hfk:1042620659139887165>  <a:804201962614292482:928185622303240253>  的 <@{sender}> \n\t\t送给 <@{receiver}> 的\n\n\t\t\t\t <a:hyheart:1042993724952686602>  骑士之誓  三日冠！<a:hyheart:1042993724952686602> \n\n\t\t\t\t\t\t\t\t <a:712524119983259681:922646454642819103>  感谢老板！<a:1_17:928211220945846362>老板大气~\n <:853947868553543700:1042621451922051142>: 心动值+365点  <:star:1042621508629057586>   <a:4328heartpinkpuff:1042993563249676320> <a:4328heartpinkpuff:1042993563249676320>"

    elif points == '6.61':
        res = "<a:S_:1113127463111889007><a:B_:1113127520938766386><a:1_:1113127540027039816><a:4_:1113127555231395890><a:k_:1113127572415459368><a:S_:1113127463111889007><a:B_:1113127520938766386><a:1_:1113127540027039816><a:4_:1113127555231395890><a:k_:1113127572415459368><a:S_:1113127463111889007><a:B_:1113127520938766386><a:1_:1113127540027039816><a:4_:1113127555231395890><a:k_:1113127572415459368><a:S_:1113127463111889007><a:B_:1113127520938766386><a:1_:1113127540027039816><a:4_:1113127555231395890><a:k_:1113127572415459368>" \
              f"\n\n <:rainbow:928122825997422602><:rainbow:928122825997422602>感谢<a:bluewing_left:1113127591285633164> 可爱迷人 <a:bluewing_right:1113127657773731881>  的  <@{sender}>  送给<@{receiver}>  的sb14k！\n\n <a:1_17:928211220945846362>感谢老板<a:1_21:928211202918731807>\n<a:874456786646757396:1069514552405934150>心动值+6.6点 <:frog:1113127710760370327> "

    elif points == '33':
        res = "<a:pink3Dheart:1113127883104329788><a:pinkcake:1113127935570878548><a:heart:981480427602722836><a:heart:981480427602722836><a:pink3Dheart:1113127883104329788><a:pinkcake:1113127935570878548><a:heart:981480427602722836><a:heart:981480427602722836><a:pink3Dheart:1113127883104329788><a:pinkcake:1113127935570878548><a:heart:981480427602722836><a:heart:981480427602722836><a:pink3Dheart:1113127883104329788><a:pinkcake:1113127935570878548><a:heart:981480427602722836><a:heart:981480427602722836><a:pink3Dheart:1113127883104329788><a:pinkcake:1113127935570878548>\n\n" \
              f"\t\t\t  <a:hy_petals:1042993303450288159> 感谢 <a:rabbit:836770901101379694> 可爱迷人 <a:rabbit:836770901101379694> <@{sender}> 送给 <@{receiver}> 的\n\n" \
              "\t\t\t\t\t   <:pinkcat:1113128027635847168> <a:pink:1113128045709111326>  喵子冰淇淋  <a:pink:1113128045709111326> <:pinkcat:1113128027635847168>\n\n\t\t♡ ｡..:･\n\t\t\t“呐！最甜的冰淇淋才配得上最甜的你 ♡”\n\t\t\t\t\t\t\t\t\t\t\t♡ ｡..:･ " \
              "<a:pinkrainbow:1113128090453954570>  感谢老板<a:pinkheart_flying:1113128123119194112> \n <a:pinkmovingheart:1113128162314944533>  心动值+33点"

    elif points == '66':
        res = "<a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282><a:pinkheart_loading:1113128211577065493><a:pinkheart_loading:1113128211577065493><a:rabbit:1113127999601119282>\n\n" \
              f"\t\t\t <a:pinkrabbitjump:1113128249615196241>  感谢 <:bluewing_left:1113128290631290991>  可爱迷人 <:bluewing_right:1113128321950175353>  <@{sender}> 送给 <@{receiver}> 的\n\n\t\t\t\t\t<a:rabbiteating:1113128331857109133>  <a:pinkheart_popping:1113128364769824809>  兔兔饭盒 <a:pinkheart_popping:1113128364769824809> <a:rabbiteating:1113128331857109133> \n\t\t ⊹ . ⊹  “ ˚  ‧  ‧ \n\t\t\t\t “阿~ 张嘴 <:DGF_Heart1:922627674629877760> 好吃的都给你哇 ！ ”\n\t\t\t\t\t\t\t\t\t\t\t\t ‧  ‧ ˚ “ ⊹ . ⊹" \
              "<a:pinkrainbow:1113128090453954570>  感谢老板<a:pinkheart_flying:1113128123119194112>\n<a:pinkmovingheart:1113128162314944533>  心动值 +66 点 "

    elif points == '99':
        res = '<a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496><a:BongoCat:957801846892789760><a:BongoCat:957801846892789760><a:956325724669771816:977342830085308496>\n\n' \
              f" \t\t\t\t<a:CWheartCinnamoroll1:1113397125154353202> 感谢 <a:ag_heartpulse1:1113396353847005214> 可爱迷人 <a:ag_heartpulse1:1113396353847005214>  <@{sender}>\n\n\t\t\t\t送给 <a:ag_heartpulse1:1113396353847005214> 迷人可爱的 <a:ag_heartpulse1:1113396353847005214> <@{receiver}>\n\n" \
              "\t\t\t\t  <a:angelWBblobkiss:1113396120614354944> 儿童节全套玩具 <a:angelWBblobkiss:1113396120614354944>\n\n                   ⋆︒⠄ ⦁ ◌⠁ ∙\n\t\t\t\t\t        说好啦~你永远都会是我的小朋友<a:1_21:928211202918731807>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t                          ⋆︒⠄ ⦁ ◌⠁ ∙\n<a:4302_angelhearts:1113397370646962197> 感谢老板 \n<a:C2_RainbowHeart:1042991399634735115> 心动值+99点\n<a:Cat:957801846922149908> 解锁 【儿童节半日冠+小礼物+自定义后缀xx的几百月小朋友】"

    elif points == '25':
        res = "<:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580>" \
              f"\n\n             <a:angelWBblobkiss:1113396120614354944> 感谢 <a:844186727371374632:976498406254067732> 可爱迷人 <a:844186727371374632:976498406254067732> 的 <@{sender}> 送给 <@{receiver}> 的 <a:food_greentea:1113398255661879346> 艾草 <a:food_greentea:1113398255661879346>\n\n" \
              "                                             ┉ ∞ <:cuteflower:1113396155305447454> ￣ <:cuteflower:1113396155305447454> ∞ ┉\n" \
              "                                      悠悠艾草香，绵绵情意长。\n" \
              "                                             ┉ ∞ <:cuteflower:1113396155305447454> ￣ <:cuteflower:1113396155305447454> ∞ ┉ \n\n" \
              "<:Sunflower_bun:1113396240420442163> 感谢老板 <a:Lumi_rainbow_heart_melt:1113396280438300763>\n<a:rainbowheart:1113396307856461845> 心动值+25点 "

    elif points == '75':
        res = "<:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580><a:WingsWhite:1113396081301131287><a:WingsWhite:1113396081301131287><:Plant:1113396059075522580>" \
              f"\n\n             <a:angelWBblobkiss:1113396120614354944> 感谢 <a:844186727371374632:976498406254067732> 可爱迷人 <a:844186727371374632:976498406254067732> 的 <@{sender}> 送给 <@{receiver}> 的 <a:Agoat_eat:1113398046647124038> 甜咸小祖粽 <a:Agoat_eat:1113398046647124038>\n\n" \
              "                                             ┉ ∞ <:cuteflower:1113396155305447454> ￣ <:cuteflower:1113396155305447454> ∞ ┉ \n" \
              "                                粽子口味再多，思念也只有一种，\n" \
              "                                            无论甜咸，不如相见。 \n" \
              "                                             ┉ ∞ <:cuteflower:1113396155305447454> ￣ <:cuteflower:1113396155305447454> ∞ ┉ \n\n" \
              "<:Sunflower_bun:1113396240420442163> 感谢老板 <a:Lumi_rainbow_heart_melt:1113396280438300763>\n<a:rainbowheart:1113396307856461845> 心动值+75点 \n<a:a_diamondrock1:1113396671544573963> 解锁【端午节限定半日冠】"


    elif points == '140':
        res = "<a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476><a:ag_heartpulse1:1113396353847005214><:__dango21:1113396394988945419><a:s_pinksparkles1:1113396454455783476>" \
              f"\n\n             <:peeking_cat:1113396476232601670> 感谢 <a:844186727371374632:976498406254067732> 可爱迷人 <a:844186727371374632:976498406254067732> 的 <@{sender}> 送给 <@{receiver}> 的 \n\n " \
              "                                           🥁 INK公子与吉鼓 🥁 \n\n" \
              "                                              ┉ ∞ <:c_bunhappy:1113396507928973394> ￣ <:c_bunhappy:1113396507928973394> ∞ ┉ \n" \
              "                     <a:cinnamoroll_bubbles1:1113396533866536991> 赛龙舟，摆渡忙，一腔豪情满春江。 <a:cinnamoroll_bubbles1:1113396533866536991>\n" \
              "                                              ┉ ∞ <:c_bunhappy:1113396507928973394> ￣ <:c_bunhappy:1113396507928973394> ∞ ┉ \n\n" \
              "<:1a_sMashiSoobin21:1113396572693221476> 感谢老板 <a:9i_hearts1:1113396601566793808> \n<:Angel_Heart1:1113396635217702993> 心动值+140点\n<a:a_diamondrock1:1113396671544573963> 解锁【端午节限定一日冠】 "


    elif points == '380':
        res = "<a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914><a:sparklingheart:1115121028612505640><a:ag_twinstars1:1113396871801622611><a:emoji_581:1113396842781220914>\n\n" \
              f"              <a:__bunny_squishcheeks1:1113397088949112943> 感谢 <a:844186727371374632:976498406254067732> 可爱迷人 <a:844186727371374632:976498406254067732> 的 <@{sender}> 送给 <@{receiver}> 的 \n\n" \
              "                                       🍶 INK娘爱喝酒 🍶\n\n" \
              "                                              ┉ ∞ <:c_bunhappy:1113396507928973394> ￣ <:c_bunhappy:1113396507928973394> ∞ ┉ \n" \
              "                 🗻 万水千山总是情，粽子配酒行不行。 🗻 \n" \
              "                                              ┉ ∞ <:c_bunhappy:1113396507928973394> ￣ <:c_bunhappy:1113396507928973394> ∞ ┉ \n\n" \
              "<:1a_sMashiSoobin11:1113396744802275379>感谢老板 <a:a_heartswhite2:1113396769968095233> \n<:5_ink:1037637783411503135> 心动值+380点 \n<a:a_diamondrock1:1113396671544573963> 解锁【端午节限定三日冠】"

    elif points == '540':
        res = "<:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741><:chairoikoguma_friends1:1113397029813637140><a:p_butterfly041:1113396999732080741><a:p_butterfly041:1113396999732080741>" \
              f"\n\n               <:4_ink:1037637790965440592> 感谢 <a:844186727371374632:976498406254067732> 可爱迷人 <a:844186727371374632:976498406254067732> 的 <@{sender}>\n\n" \
              f"                   送给 <a:844186727371374632:976498406254067732> 迷人可爱 <a:844186727371374632:976498406254067732> 的 <@{receiver}>  的 \n\n" \
              "                              <:5_ink:1037637783411503135> 端午全家福 <:5_ink:1037637783411503135>\n\n" \
              "                                        ┉ ∞ <a:m3_cinnamon21:1113397049933709392> ￣ <a:m3_cinnamon21:1113397049933709392> ∞ ┉ \n" \
              "                 <a:Wind_Chime:1067555115210383370> 人生变化多“端”，也不过“午”味杂陈。 <a:Wind_Chime:1067555115210383370>\n" \
              "                                        ┉ ∞ <a:m3_cinnamon21:1113397049933709392> ￣ <a:m3_cinnamon21:1113397049933709392> ∞ ┉ \n\n" \
              "<a:__bunny_squishcheeks1:1113397088949112943> 感谢老板 <a:CWheartCinnamoroll1:1113397125154353202> \n<:fullofheart:1042404048533458944> 心动值+540点 \n<a:a_diamondrock1:1113396671544573963>  解锁【端午节限定五日冠】"


    elif points == '1160':
        res = "<a:RibbonWhite1:1113397170171826226>︶<a:abutterflyholo:1113397231849054261>︶<:sparklingpinkheart1:1113397193861242910>︶<a:RibbonWhite1:1113397170171826226>︶<a:abutterflyholo:1113397231849054261>︶<:sparklingpinkheart1:1113397193861242910>︶<a:RibbonWhite1:1113397170171826226>︶<a:abutterflyholo:1113397231849054261>︶<:sparklingpinkheart1:1113397193861242910>︶<a:RibbonWhite1:1113397170171826226>︶<a:abutterflyholo:1113397231849054261>︶<:sparklingpinkheart1:1113397193861242910>︶<a:RibbonWhite1:1113397170171826226>\n\n" \
              f"               <a:c_huggies1:1113397273452359680> 感谢 <a:844186727371374632:976498406254067732> 可爱迷人 <a:844186727371374632:976498406254067732> 的 <@{sender}>" \
              f"\n\n                   送给 <a:844186727371374632:976498406254067732> 迷人可爱 <a:844186727371374632:976498406254067732> 的 <@{receiver}>  的 \n\n" \
              "                                   <:rabbit:1113127803811012658> 端午节全套礼物 <:rabbit:1113127803811012658>" \
              "\n                   ♡ ｡..:･\n                                               <a:food_greentea:1113398255661879346> 艾草 :<a:food_greentea:1113398255661879346>\n" \
              "                                        <a:Agoat_eat:1113398046647124038> 甜咸小祖粽 <a:Agoat_eat:1113398046647124038>\n" \
              "                                     🥁 INK公子与吉鼓 🥁 \n                                       🍶 INK娘爱喝酒 🍶\n" \
              "                                         <:5_ink:1037637783411503135> 端午全家福 <:5_ink:1037637783411503135>\n                                                                                          ♡ ｡..:･\n" \
              "                                        ┉ ∞ <:heartwithwings:1042428010437034195> ￣ <:heartwithwings:1042428010437034195>: ∞ ┉\n                  <a:meowfallin1:1113397307304579092> 愿衣襟带花，岁月风平，深情皆不负。 \n                               愿所求皆所愿，所行化坦途。 <a:meowfallin1:1113397307304579092>\n                                        ┉ ∞ <:heartwithwings:1042428010437034195> ￣ <:heartwithwings:1042428010437034195> ∞ ┉ " \
              "\n\n<a:meowtietie:1113397329903497236> 感谢老板 <a:heartheart:1113397349176332318>\n<a:4302_angelhearts:1113397370646962197> 心动值+1160点 \n<a:a_diamondrock1:1113396671544573963> 解锁【端午节限定十日冠】+ 端午限定全套TAG 【꧁༒•⊹ 🎋 仲夏夜🤍之梦 ⊹•༒꧂】"


    elif points == '8888':
        res = f"""
        <a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884><:p_heart03:1164020832117469246><:p_heart03:1164020832117469246><a:p_bow12:1164020782171684884> 

<:p_heartsparkles01:1164020845711212554><:p_heartsparkles01:1164020845711212554> 感谢 <a:pr_spark01:1164020413777592371> 帅气可爱大方 <a:pr_spark01:1164020413777592371> 的 <a:804201856988348436:928185595648409630> <:hfk:1042620659139887165> <@{sender}> <:hfk:1042620659139887165> <a:a_wing_2:1164020874958078033> 

                         送给 <a:pr_spark01:1164020413777592371> 迷人可爱 <a:pr_spark01:1164020413777592371> 的 <@{receiver}>

                             <a:p_heart8:1164021357600837765> <:p_flowerdot01:1164021335224225852> 自然之力 • 𝕀ℕ𝕂专属季度冠名 <:p_flowerdot01:1164021335224225852> <a:p_heart8:1164021357600837765>

            ♡ ℑ'𝔪 𝔫𝔬𝔱 𝔞𝔩𝔬𝔫𝔢 𝔞𝔫𝔶𝔪𝔬𝔯𝔢. ℑ 𝔠𝔞𝔫 𝔱𝔯𝔲𝔰𝔱 𝔦𝔫 𝔬𝔱𝔥𝔢𝔯𝔰, 𝔞𝔫𝔡 𝔦𝔫 𝔪𝔶𝔰𝔢𝔩𝔣 ♡
                    ♡ 我不再恐惧，不再孤单，我的心好像有了归处 ♡

<a:p_heart8:1164021357600837765> 感谢老板！老板大气~ <a:Lumi_heart_popup:1164020663800041543> 
<:moon:1164021408905580625> 心动值+8888点
        """

    elif points == '3188':
        res = f"""
<a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966><a:y_star02:1042995847182426194><a:y_star02:1042995847182426194><a:regularyellow_rolling_star:922637744583376966>

<a:shiningstar:1042111840051789905><a:shiningstar:1042111840051789905> 感谢 <a:pr_spark01:1164020413777592371> 帅气可爱大方 <a:pr_spark01:1164020413777592371>: 的 <a:WingsWhite:1113396081301131287> <:hfk:1042620659139887165> <@{sender}> <:hfk:1042620659139887165> <a:WingsWhite:1113396081301131287> 

                         送给 <a:pr_spark01:1164020413777592371> 迷人可爱 <a:pr_spark01:1164020413777592371> 的 <@{receiver}>

                           <a:8_123213:1042996025486475298> <a:1_17:928211220945846362> 潘多拉的秘密 • 𝕀ℕ𝕂专属一月冠名 <a:1_17:928211220945846362> <a:8_123213:1042996025486475298> 

✩ ℑ𝔣 𝔫𝔬 𝔬𝔫𝔢 𝔱𝔢𝔩𝔩𝔰 𝔶𝔬𝔲 𝔰𝔬𝔪𝔢𝔱𝔥𝔦𝔫𝔤'𝔰 𝔦𝔪𝔭𝔬𝔰𝔰𝔦𝔟𝔩𝔢, 𝔱𝔥𝔢𝔫 𝔦𝔱'𝔰 𝔰𝔱𝔦𝔩𝔩 𝔭𝔬𝔰𝔰𝔦𝔟𝔩𝔢. 𝔖𝔬 𝔤𝔬 𝔡𝔬 𝔦𝔱 ✩
         ✩ 如果没人和你说不可能，那就仍然有可能，所以大胆去做吧 ✩

<a:Lumi_cutie_hearts:1164020727628972143> 感谢老板！老板大气~ <a:Lumi_heart_popup:1164020663800041543> 
<:3336cutesparkles:1164020756343181334> 心动值+3188点
"""

    elif points == '1588':
        res = f"""
<a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566><a:pr_spark01:1164020413777592371><a:pr_spark01:1164020413777592371><a:833789373539418113:1164020364599361566>

<a:Crystal_Ball:957806870339403806><a:Crystal_Ball:957806870339403806> 感谢 <a:pr_spark01:1164020413777592371> 帅气可爱大方 <a:pr_spark01:1164020413777592371>: 的 <a:bluewing_left:1113127591285633164> <:hfk:1042620659139887165> <@{sender}>  <:hfk:1042620659139887165> <a:bluewing_right:1113127657773731881> 

                         送给 <a:pr_spark01:1164020413777592371> 迷人可爱 <a:pr_spark01:1164020413777592371> 的 <@{receiver}>

                     <:8_heart3:1164020506232627310> <a:7_purple_3:1164020539694792744> 双生暗影 • 𝕀ℕ𝕂专属半月冠名 <a:7_purple_3:1164020539694792744> <:8_heart3:1164020506232627310> 

             ☽ 𝔗𝔥𝔢 𝔪𝔬𝔬𝔫 𝔤𝔞𝔱𝔥𝔢𝔯𝔰 𝔡𝔞𝔯𝔨𝔫𝔢𝔰𝔰 𝔬𝔫 𝔱𝔥𝔢 𝔠𝔯𝔢𝔰𝔠𝔢𝔫𝔱'𝔰 𝔢𝔡𝔤𝔢 ☾
                                    ☽ 黑暗落尽，月华满天 ☾

<a:heart_wing:1164020571311460454> 感谢老板！老板大气~ <a:Lumi_heart_popup:1164020663800041543> 
<a:pr_clouds03:1164020608351338546>  心动值+1588点

"""
    elif points == '888':
        res = f"""
<a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570><a:pinkmoon:1002837496062812200><a:pinkmoon:1002837496062812200><a:pinkrainbow:1113128090453954570>

<a:ag_heartpulse1:1113396353847005214><a:ag_heartpulse1:1113396353847005214> 感谢 <a:pr_spark01:1164020413777592371> 帅气可爱大方 <a:pr_spark01:1164020413777592371>: 的 <a:bluewing_left:1113127591285633164> <:hfk:1042620659139887165> <@{sender}>  <:hfk:1042620659139887165> <a:bluewing_right:1113127657773731881>

                         送给 <a:pr_spark01:1164020413777592371> 迷人可爱 <a:pr_spark01:1164020413777592371> 的 <@{receiver}>

                 <a:pumping_heart:1164021978877931610> <:904607117745455114:1136526838118752297> 炙热香炉 • 𝕀ℕ𝕂专属一周冠名 <:904607117745455114:1136526838118752297> <a:pumping_heart:1164021978877931610>

            ✿ 𝔄 𝔤𝔲𝔞𝔯𝔡𝔦𝔞𝔫 𝔪𝔞𝔶 𝔡𝔦𝔢, 𝔟𝔲𝔱 𝔱𝔥𝔢𝔦𝔯 𝔰𝔭𝔦𝔯𝔦𝔱 𝔫𝔢𝔳𝔢𝔯 𝔣𝔞𝔡𝔢𝔰 ✿
                                  ✿ 卫者可亡，星魂不逝 ✿

<a:771539740657844225:976499231772770334>感谢老板！老板大气~ <:3214flowerpink:1164021996112326756>
<a:angelWZeartcloud:1164022036784500837> 心动值+888点
"""

    elif points == '521':
        res = f"""
<:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492><:Lumi_bunny_cloud_peek:1164021429377974294><:Moon:962073340200251492>

<:DECOstar1:1164021446406836315><:DECOstar1:1164021446406836315> 感谢 <a:pr_spark01:1164020413777592371> 帅气可爱大方 <a:pr_spark01:1164020413777592371>: 的 <a:bluewing_left:1113127591285633164> <:hfk:1042620659139887165> <@{sender}>  <:hfk:1042620659139887165> <a:bluewing_right:1113127657773731881>

                          送给 <a:pr_spark01:1164020413777592371> 迷人可爱 <a:pr_spark01:1164020413777592371> 的 <@{receiver}>

                             <a:Wind_Chime:1067555115210383370> <a:jewel:1164021476832325632> 救赎 • 𝕀ℕ𝕂专属五日冠名 <a:jewel:1164021476832325632> <a:Wind_Chime:1067555115210383370> 

                                 ✧ 𝔗𝔥𝔢 𝔱𝔢𝔪𝔭𝔢𝔰𝔱 𝔦𝔰 𝔞𝔱 𝔶𝔬𝔲𝔯 𝔠𝔬𝔪𝔪𝔞𝔫𝔡 ✧
                                        ✧ 风之化身听候您的差遣 ✧

❤️ 感谢老板！老板大气~ <a:HyONLY_heart:1164021913006379021> 
<a:JigglingClouds:1164021956555833374> 心动值+521点
"""
    else:

        fixed = points
        if fixed == '6.62':
            fixed = '6.6'
        if fixed == '99.2':
            fixed = '99'
        if fixed == '6.61':
            fixed = '6.6'
        if fixed == '52.1':
            fixed = '52'
        if fixed == '33.44':
            fixed = '66.88'

        res = "<a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159><a:hy_petals:1042993303450288159>\n\n" \
              f"<a:4328heartpinkpuff:1042993563249676320><a:4328heartpinkpuff:1042993563249676320> 感谢  <a:804201856988348436:928185595648409630> <:hfk:1042620659139887165> 可爱迷人 <:hfk:1042620659139887165>  <a:804201962614292482:928185622303240253>  的 <@{sender}> \n\t\t送给 <@{receiver}> 的\n\n\t\t\t\t <a:hyheart:1042993724952686602>  {gifts[points]}！<a:hyheart:1042993724952686602> \n\n\t\t\t\t\t\t\t\t <a:712524119983259681:922646454642819103>  感谢老板！<a:1_17:928211220945846362>老板大气~\n <:853947868553543700:1042621451922051142>: 心动值+{fixed}点  <:star:1042621508629057586>"

    return res


def inputCheck(num):
    if num in gifts:
        return True
    return False


def breakString(string):
    res = []
    dummy = string[:2000]
    ind = string.rfind("\n")

    res.append(string[:ind])
    res.append(string[ind:])
    return res


@client.tree.command(name="songli")
@app_commands.describe(
    sender='送礼人',
    liwu='礼物名称',
    shouliren1='收礼人1',
    shouliren2='收礼人2',
    shouliren3='收礼人3',
    shouliren4='收礼人4',
    shouliren5='收礼人5',
    shouliren6='收礼人6',
    shouliren7='收礼人7',
    shouliren8='收礼人8',
    shouliren9='收礼人9',
    shouliren10='收礼人10',

)
async def songli(interaction: discord.Interaction, sender: discord.User, liwu: GiftName, shouliren1: discord.User, shouliren2: discord.User = client.user, shouliren3: discord.User = client.user, shouliren4: discord.User= client.user, shouliren5: discord.User= client.user, shouliren6: discord.User= client.user, shouliren7: discord.User= client.user, shouliren8: discord.User= client.user, shouliren9: discord.User= client.user, shouliren10: discord.User= client.user):

    sender = str(sender.id)
    receiverlist = [shouliren1, shouliren2, shouliren3, shouliren4, shouliren5, shouliren6, shouliren7, shouliren8, shouliren9, shouliren10]
    role = discord.utils.get(interaction.guild.roles, id= roleID)
    check = True

    if not role in interaction.user.roles:
        check = False

    if interaction.user.id == 717898166011297842:
        check = True

    if not check:
        await interaction.response.send_message(" 没有权限！", ephemeral=True)
        return




    num = 'error'

    for key, value in gifts.items():
        if value == liwu:
            num = key




    if not inputCheck(num):
        await interaction.response.send_message("礼物点数错误，请使用 !list 查看礼物对应点数", ephemeral=True)
        return


    points = num
    if num == '99.1':
        points = '99'
    if num == '99.2':
        points = '99'
    if num == '6.61' or num == '6.62':
        points = '6.6'
    if num == '52.1':
        points = '52'
    if num == '66.1':
        points = '66'

    if points == '33.44':
        points = '66.88'

    await interaction.response.send_message("送礼成功", ephemeral=True)


    l = []
    for i in receiverlist:
        if i is not None :
            if i != client.user:
                z = updateXDZ(sender, i.id, points)
                l.append('<@' + str(i.id)+">")









    tChannel = client.get_channel(tChanneln)
    dChannel = client.get_channel(dChanneln)
    oChannel = client.get_channel(oChanneln)

    logger.info(
        f"{interaction.user.name} 执行了送礼： {sender} ---->  {receiverlist}, 金额： {num}")






    ll = []
    for i in l:
        ll.append(i)

    formated = " ".join(ll)


    res = bobao(sender, formated, num)
    if len(res) >= 2000:
        res = breakString(res)
        for i in res:
            await tChannel.send(i)
    else:
        await tChannel.send(res)

    if float(num) >= 521:
        await tChannel.send("@everyone")

    if num == '1160':
        with open('./inkbot/img/25.png', 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)

        with open('./inkbot/img/75.png', 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)

        with open('./inkbot/img/140.png', 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)

        with open('./inkbot/img/380.png', 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)

        with open('./inkbot/img/540.png', 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)

    image_path = f'./inkbot/img/{num}.png'
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)
    elif num == '5.5':
        image_path = f'./inkbot/img/{num}.gif'
        with open(image_path, 'rb') as f:
            picture = discord.File(f)
        await tChannel.send(file=picture)
    elif num == '99':
        with open("./inkbot/img/33.png", 'rb') as f:
            p1 = discord.File(f)
        with open("./inkbot/img/66.png", 'rb') as f:
            p2 = discord.File(f)
        await tChannel.send(file=p1)
        await tChannel.send(file=p2)





# @client.command()
# async def drsl(ctx, sender, receiverlist: str, num):

#   if len(receiverlist) % 18 !=0:
#     await ctx.channel.send("bad format!")
#     return

#   l = [receiverlist[i:i+18] for i in range(0, len(receiverlist), 18)]
#   count = len(l)
#   for i in l:
#     await songli(ctx, sender, i, num)

'''
------------------------------------    抽奖   --------------------------------------------
'''
game_start_channels = {}



@client.tree.command(name='start')
@app_commands.describe()

async def start_game(interaction: discord.Interaction):
    """
    这是一个小游戏，可以抽取一些幸运用户
    """
    channel_id = interaction.channel_id
    if channel_id in game_start_channels:
        await interaction.response.send_message('抽奖已经开始了，请不要重复开始噢', ephemeral=True)
        return
    game_start_channels[channel_id] = {
        'start_time': datetime.now(),
        'participants': []
    }
    start_embed = discord.Embed(
        title='抽奖开始了',
        description='大家快来参加吧！',
        color=0xc991ae
    )
    try:
        await interaction.response.send_message('指令收到，开始抽奖', ephemeral=True)
    except Exception as e:
        chat_channel = client.get_channel(channel_id)
        await chat_channel.send(embed=start_embed)
        logger.error(f'start game error: {e}')
    logger.info(f'start game in channel: {interaction.channel.name}')


@client.tree.command(name='end')
@app_commands.describe(抽取几位='抽取几位幸运用户')

async def end_game(interaction: discord.Interaction, 抽取几位: int):
    """
    手动结束抽奖
    """
    # 1. /start 命令可以开始开始游戏，bot回复“开始游戏”。
    # 2. 其他用户可以在discord频道中回复任意字符串
    # 2. /end结束游戏，并统计从/start到/end命令中间的所有用户id，如果有重复的用户id需要去重，然后从中随机抽取一名用户，机器人回复：“幸运用户：@userid”

    channel_id = interaction.channel_id
    if channel_id not in game_start_channels:
        await interaction.response.send_message('抽奖还没有开始，请先开始抽奖噢', ephemeral=True)
        return
    game_users = game_start_channels[channel_id]['participants']
    game_start_time = game_start_channels[channel_id]['start_time']
    game_end_time = datetime.now()
    random_count = 抽取几位 if 抽取几位 <= len(game_users) else len(game_users)



    lucky_users = random.choices(game_users, k=random_count)
    chat_channel = client.get_channel(channel_id)
    lucky_users_str = ' '.join([f'<@{user}>' for user in lucky_users])
    lucky_embed = discord.Embed(
        title='抽奖结束了！',
        description=f'幸运鹅{lucky_users_str}.\n有奖竞猜的礼物被抱走啦！没抽中的宝贝不要灰心，没关系，人生处处是惊喜！｡･ﾟヾ(✦థ ｪ థ)ﾉ｡ﾟ･｡',
        color=0xc991ae,
    )
    logger.info(f'choice lucky guys and send message: {channel_id}')
    # lucky_embed.set_image(url='https://cdn.discordapp.com/attachments/921985463630299138/1106474302821380146/20.png')
    try:
        await chat_channel.send(embed=lucky_embed)

    except discord.errors.HTTPException:
        logger.error(f'failed to send lucky embed to chat channel')
    try:
        await interaction.response.send_message(f'游戏结束了，共有{len(game_users)}人参加了游戏。', ephemeral=True)
        logger.info(f'send game end message to interaction channel: {chat_channel.name}')
    except discord.errors.HTTPException:
        logger.error(f'failed to send game end message to interaction channel')

    # 私信中奖人
    logger.info(f'notify lucky guys: {lucky_users}')
    for user in lucky_users:
        try:
            user_obj = await client.fetch_user(user)
            await user_obj.send(f'恭喜你在频道 {chat_channel.mention} 中抽中奖了，速速去看吧！')
            logger.info(f'send lucky message to user {user_obj.name}')
        except discord.errors.HTTPException:
            logger.error(f'failed to send lucky message to user {user}')

    # 礼物播报



    # 结束后清理
    del game_start_channels[channel_id]



'''
-------------------------------------   xdz area.  ----------------------------------------- 
'''


@client.command()
async def e(ctx, sender, receiver, num):
    total = updateXDZ(sender, receiver, num)
    await ctx.channel.send(f"successfully editted from <@{sender}> to <@{receiver}>, their xdz now is {total}")


@client.command()
async def cl(ctx):
    data = {'client1': ['1'], 'client2': ['0'], 'value1': [0.0]}
    df = pd.DataFrame(data)
    df.to_csv('./inkbot/xdz.csv', index=False, header=True)
    await ctx.channel.send("xdz data reset!")


'''
-------------------------------------   下单 .  ----------------------------------------- 
'''


class anonymous(str, Enum):
    是 = '1',
    否 = '0'


class gender(str, Enum):
    男生 = '1',
    女生 = '0',
    男女不限 = '2'


@client.tree.command(name="order")
@app_commands.describe(
    是否匿名='是否匿名',
    男女='需要男陪 or 女陪',
    要求='其他要求， 如 游戏类目，段位要求'

)
async def order(interaction: discord.Interaction, 是否匿名: anonymous, 男女: gender, 要求: str):
    gender = ""
    ano = ""

    if 男女 == "1":
        gender = f"<@&{variables.knight}>"
    elif 男女 == "0":
        gender = f"<@&{variables.fairy}>"
    elif 男女 == "2":
        gender = f"<@&{variables.knight}> <@&{variables.fairy}>"

    if 是否匿名 == '1':
        ano = "匿名老板"
    else:
        ano = f"<@{interaction.user.id}>"

    res = gender + "本单由： " + ano + "下单， 具体要求为: " + 要求 + "\n 请点击表情开始扣单。本单将在10分钟后截止。"

    xdChanneln = 914690132718809118

    xdChannel = client.get_channel(xdChanneln)

    await interaction.response.send_message("下单成功！本单将会出现在下单区，使用/end 来结束本单", ephemeral=True)
    msg = await xdChannel.send(res)
    await msg.add_reaction('✅')

    cached_messages[msg.id] = interaction.user

    await asyncio.sleep(600)
    if msg.id in cached_messages:
        del cached_messages[msg.id]
        await xdChannel.send("本单结束。各位辛苦了。", reference=msg)


@client.tree.command(name="end_order")
async def end_order(interaction: discord.Interaction):
    # 本单终止。

    xdChanneln = 914690132718809118

    xdChannel = client.get_channel(xdChanneln)

    for id in cached_messages:
        user = cached_messages[id]
        if user == interaction.user:
            msg = await xdChannel.fetch_message(id)
            del cached_messages[id]
            await interaction.response.send_message("本单终止！", ephemeral=True)
            await xdChannel.send("本单结束。各位辛苦了。", reference=msg)
            break
    else:
        await interaction.response.send_message("目前并没有订单！", ephemeral=True)


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.id in cached_messages and str(reaction.emoji) == '✅' and user != client.user:
        laoban = cached_messages[reaction.message.id]
        name = user.nick
        await laoban.send(f" {name} <@{user.id}> 申请接单！")




'''
-------------------------------------   九月活动 .  ----------------------------------------- 
'''

FOODS = [f"food{i}" for i in range(1, 51)]
BOARD_SIZE = 25
START_CHANCES = 0






# Load all game data
def load_all_data():
    try:
        with open("./inkbot/food.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save all game data
def save_all_data(data):
    with open("./inkbot/food.json", "w") as f:
        json.dump(data, f)

# Get specific user's data
def get_user_data(user_id, all_data):
    return all_data.get(str(user_id), None)

# Set specific user's data
def set_user_data(user_id, user_data, all_data):
    all_data[str(user_id)] = user_data


@client.command()
async def startg(ctx):

    all_data = load_all_data()

    user_data = get_user_data(ctx.author.id, all_data)

    currStrike = 0
    currComp = 0
    currChance = START_CHANCES
    if user_data:
        if user_data['board']:
            await ctx.send(f"你已经有一个正在玩的板子了!")
            return
        currChance = user_data['chances']
        currComp = user_data['completed']
        currStrike = user_data['strikes']



    board = random.sample(list(variables.pureFoods.keys()), BOARD_SIZE)
    user_data = {
        "board": board,
        "chances": currChance,
        "strikes": currStrike,
        "misses": 0,
        "found": [],
        "completed": currComp
    }
    set_user_data(ctx.author.id, user_data, all_data)
    save_all_data(all_data)
    await ctx.send(f"{ctx.author.name} 开始了新的游戏!\n你的板子上有: {', '.join(board)}")


def check_bingo_win(board, found):
    stat = [[0] *5 for i in range(5)]

    test = []
    for i in range(5):
        for j in range(5):
            if board[i*5 + j] in found:
                stat[i][j] = 1

    count = 0
    # check horizontal:
    r = 0
    for row in stat:
        r +=1
        if row == [1, 1, 1, 1, 1]:
            count += 1
            test.append(['r', r])

    #check vertical:
    v = 0
    for i in range(5):
        v +=1
        curr = [stat[0][i], stat[1][i], stat[2][i], stat[3][i], stat[4][i]]
        if curr == [1, 1, 1, 1, 1]:
            count += 1
            test.append(['v', v])

    # check diagonals
    curr = []
    cur = []
    for i in range(5):
        curr.append(stat[i][i])
        cur.append(stat[4 - i][i])
    if curr == [1, 1, 1, 1, 1]:
        count += 1
        test.append(['shun'])
    if cur == [1, 1, 1, 1, 1]:
        count += 1
        test.append(['ni'])

    if count >=3:
        print(test)
        return True
    else:
        return False





@client.command()
async def bingo(ctx):
    all_data = load_all_data()
    user_data = get_user_data(ctx.author.id, all_data)

    if not user_data:
        await ctx.send("请使用 `!startg` 开始游戏.")
        return

    if user_data['board'] == []:
        await ctx.send("请使用 `!startg` 获取新的板子.")
        return


    food = random.choice(list(variables.foods.keys()))
    if user_data["chances"] <= 0:
        await ctx.send("没有机会了!")
        return

    if food in user_data["found"]:
        user_data["misses"] += 1
        user_data["strikes"] = 0  # Reset the strike count on a miss
        await ctx.send(f"{ctx.author.mention}在小小的花园里挖呀挖呀挖，挖呀挖呀挖，挖呀挖呀挖.....")
        result = "miss"
    elif food in user_data["board"]:
        user_data["found"].append(food)
        user_data["strikes"] += 1
        user_data["misses"] = 0  # Reset the miss count on a strike
        result = "strike"
        await ctx.send(f"{ctx.author.mention}啊啊啊啊！幸运总是降临在我身上！中奖咯！")
    else:
        user_data["misses"] += 1
        user_data["strikes"] = 0  # Reset the strike count on a miss

        await ctx.send(f"{ctx.author.mention}在小小的花园里挖呀挖呀挖，挖呀挖呀挖，挖呀挖呀挖.....")
        result = "miss"

        if food == "茅台":
            user_data["chances"] -= 1
            await ctx.send(f"{ctx.author.mention}恭喜你抽中 茅台! 啊啊啊啊！幸运总是降临在我身上！中奖咯！礼物是 损失一次抽奖机会。")
        if food == "杨枝甘露":
            user_data["chances"] += 1
            await ctx.send(f"{ctx.author.mention}恭喜你抽中 杨枝甘露，啊啊啊啊！幸运总是降临在我身上！中奖咯！礼物是 获得一次抽奖机会。")
        if food == "红烧猪蹄":
            user_data["chances"] += 3
            await ctx.send(f"{ctx.author.mention}恭喜你抽中 红烧猪蹄，啊啊啊啊！幸运总是降临在我身上！中奖咯！礼物是 获得3次抽奖机会。")


    user_data["chances"] -= 1

    # Check for 3 strikes or misses in a row
    if user_data["strikes"] == 3 or user_data["misses"] == 3:
        if user_data["strikes"] == 3:
            await ctx.send(f"{ctx.author.mention}<a:1_17:928211220945846362>连续抽中板子上的食物3次 - 获得<a:a_diamondrock1:1113396671544573963>小礼物 解暑慕斯 價值 (13.14）x1 + 幸运星活动𝐓𝐚𝐠 @还得dei是我鹅 ")
        else:
            unf = [food for food in user_data['board'] if food not in user_data['found']]
            free = random.choice(unf)
            user_data["found"].append(free)
            await ctx.send(f"{ctx.author.mention}<a:1_17:928211220945846362>连续Miss板子上的食物3次 - 获得<a:a_diamondrock1:1113396671544573963>小礼物 解暑慕斯 價值 (13.14）x1 + 倒霉蛋活动𝐓𝐚𝐠 @发财和发朋友圈我总要发一个吧，获得额外食物 [{free}] ")
        if user_data["misses"] == 3:
            user_data["chances"] += 1  # Add another roll chance for 3 misses in a row
        user_data["misses"] = 0  # Reset the miss count
        user_data["strikes"] = 0  # Reset the strike count

    await ctx.send(f"{ctx.author.mention}恭喜你抽到了: {food}. {variables.foods[food]} 剩余抽奖次数: {user_data['chances']}.")
    fnw = food.replace(" ", "")
    image_path = f'./inkbot/sepimg/{fnw}.png'
    if os.path.exists(image_path):

        with open(image_path, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)




    if check_bingo_win(user_data["board"], user_data["found"]):
        await ctx.send(f"{ctx.author.mention}恭喜你! 你已经完成了板子, 请使用 `!startg` 获取新的板子")
        user_data["completed"] += 1
        user_data["board"] = []

    set_user_data(ctx.author.id, user_data, all_data)
    save_all_data(all_data)




@client.command()
async def b10(ctx):
    all_data = load_all_data()
    user_data = get_user_data(ctx.author.id, all_data)

    if not user_data:
        await ctx.send("请使用 `!startg` 开始游戏.")
        return

    if user_data['board'] == []:
        await ctx.send("请使用 `!startg` 获取新的板子.")
        return


    if user_data["chances"] < 10:
        await ctx.send("机会不足!")
        return

    scount = 0
    sfoods = []


    for i in range(10):
        food = random.choice(list(variables.foods.keys()))

        if food in user_data["found"]:
            user_data["misses"] += 1
            user_data["strikes"] = 0  # Reset the strike count on a miss


        elif food in user_data["board"]:
            user_data["found"].append(food)
            user_data["strikes"] += 1
            user_data["misses"] = 0  # Reset the miss count on a strike
            scount += 1
            sfoods.append(food)

        else:
            user_data["misses"] += 1
            user_data["strikes"] = 0  # Reset the strike count on a miss



            if food == "茅台":
                user_data["chances"] -= 1
                await ctx.send(
                    f"{ctx.author.mention}恭喜你抽中 茅台! 啊啊啊啊！幸运总是降临在我身上！中奖咯！礼物是 损失一次抽奖机会。")
            if food == "杨枝甘露":
                user_data["chances"] += 1
                await ctx.send(
                    f"{ctx.author.mention}恭喜你抽中 杨枝甘露，啊啊啊啊！幸运总是降临在我身上！中奖咯！礼物是 获得一次抽奖机会。")
            if food == "红烧猪蹄":
                user_data["chances"] += 3
                await ctx.send(
                    f"{ctx.author.mention}恭喜你抽中 红烧猪蹄，啊啊啊啊！幸运总是降临在我身上！中奖咯！礼物是 获得3次抽奖机会。")

        user_data["chances"] -= 1

        # Check for 3 strikes or misses in a row
        if user_data["strikes"] == 3 or user_data["misses"] == 3:
            if user_data["strikes"] == 3:
                await ctx.send(
                    f"{ctx.author.mention}<a:1_17:928211220945846362>连续抽中板子上的食物3次 - 获得<a:a_diamondrock1:1113396671544573963>小礼物 解暑慕斯 價值 (13.14）x1 + 幸运星活动𝐓𝐚𝐠 @还得dei是我鹅 ")
            else:
                unf = [food for food in user_data['board'] if food not in user_data['found']]
                free = random.choice(unf)
                user_data["found"].append(free)
                await ctx.send(
                    f"{ctx.author.mention}<a:1_17:928211220945846362>连续Miss板子上的食物3次 - 获得<a:a_diamondrock1:1113396671544573963>小礼物 解暑慕斯 價值 (13.14）x1 + 倒霉蛋活动𝐓𝐚𝐠 @发财和发朋友圈我总要发一个吧，获得额外食物 [{free}] ")
            if user_data["misses"] == 3:
                user_data["chances"] += 1  # Add another roll chance for 3 misses in a row
            user_data["misses"] = 0  # Reset the miss count
            user_data["strikes"] = 0  # Reset the strike count

        if check_bingo_win(user_data["board"], user_data["found"]):
            await ctx.send(f"{ctx.author.mention}恭喜你! 你已经完成了板子, 请使用 `!startg` 获取新的板子")
            user_data["completed"] += 1
            user_data["board"] = []

            set_user_data(ctx.author.id, user_data, all_data)
            save_all_data(all_data)
            return

    set_user_data(ctx.author.id, user_data, all_data)
    save_all_data(all_data)
    await ctx.channel.send(f" 恭喜你在10连抽中 抽中了 {scount}次， 获得了 {sfoods}！！！")



@client.command()
async def status(ctx):
    all_data = load_all_data()
    user_data = get_user_data(ctx.author.id, all_data)

    if not user_data:
        await ctx.send(f"{ctx.author.mention}请使用 `!startg` 开始游戏.")
        return

    # Constructing the message
    board = user_data["board"]
    found = user_data["found"]
    if not found:
        found = "None"

    display = ""
    if board != []:
        for i in range(5):
            current_row = "|"
            for j in range(5):
                index = i*5 + j
                if board[index] in found:
                    current_row += f"{board[index]}|"
                else:
                    current_row += "         X         |"
            current_row += "\n"
            display += current_row

    unfound = [food for food in board if food not in found]

    status_message = (
        f"**{ctx.author.mention}的 数据：**\n"
        f"**Board:**\n{display}\n"
        f"**还未抽到:** {unfound}\n"
        f"**抽奖机会:** {user_data['chances']}\n"
        f"**抽中连击:** {user_data['strikes']}\n"
        f"**Miss连击:** {user_data['misses']}\n"
        f"**板子完成数量:** {user_data['completed']}"
    )
    await ctx.send(status_message)




@client.tree.command(name="add")
@commands.has_role("admin")
async def add(interaction:discord.Interaction, member: discord.Member, chances: int):
    logger.info(f"{interaction.user.nick} 执行了 /add， 给 {member.nick} 添加了 {chances}  次")
    all_data = load_all_data()
    user_data = get_user_data(member.id, all_data)

    if not user_data:
        await interaction.response.send_message(f"{member.name} hasn't started a game yet.")
        return

    user_data["chances"] += chances
    set_user_data(member.id, user_data, all_data)
    save_all_data(all_data)
    await interaction.response.send_message(f"Given {chances} additional chances to {member.name}.", ephemeral=True)







'''
-------------------------------------   warning .  ----------------------------------------- 
'''


def get_current_time_ny():
    # Define the New York timezone
    new_york_tz = pytz.timezone('America/New_York')
    # Get the current time in UTC
    utc_now = datetime.utcnow()
    # Convert the UTC time to New York time
    return datetime.now(new_york_tz)



def check_warning(user):
    res = False
    role1 = discord.utils.get(user.guild.roles, id=926640103764426812)
    role2 = discord.utils.get(user.guild.roles, id=966085269965119488)

    if user.id == 717898166011297842 or role1 in user.roles or role2 in user.roles:
        res = True

    return res




@client.tree.command(name="addwarning")
@commands.has_role("admin")
async def addwarning(interaction:discord.Interaction, member: discord.Member, reason: str):

    if not check_warning(interaction.user):
        await interaction.response.send_message("没有权限！", ephemeral=True)
        return
    logger.warning(f"{interaction.user} 对{member.mention} 添加了警告.")
    with open('./inkbot/warnings.json', 'r') as f:
        warnings = json.load(f)

    if str(member.id) not in warnings:
        warnings[str(member.id)] = []

    warnings[str(member.id)].append({"reason": reason, "timestamp": str(get_current_time_ny())})

    r = f"对 {member.mention} 的警告添加成功！"
    t = ""
    if len(warnings[str(member.id)]) >= 3:
        t = f"{member.mention} 已经在1个月内收到了3次警告！"

    with open('./inkbot/warnings.json', 'w') as f:
        json.dump(warnings, f)


    res = r+t
    await interaction.response.send_message(res, ephemeral=True)



@client.command()
async def warning(ctx):
    warning_channel = client.get_channel(variables.warning)
    if ctx.channel !=warning_channel:
        return

    with open('./inkbot/warnings.json', 'r') as f:
        warnings = json.load(f)

    member_id = str(ctx.author.id)
    if member_id in warnings:
        if len(warnings[member_id]) != 0:
            warning_text = [f"{i + 1}. {warn['reason']} (时间: {warn['timestamp'][:16]})\n" for i, warn in
                            enumerate(warnings[member_id])]
            await ctx.send(f"{ctx.author.mention} 收到的警告:\n{' '.join(warning_text)}")
        else:
            await ctx.send(f"{ctx.author.mention}  目前没有警告.")
    else:
        await ctx.send(f"{ctx.author.mention}  目前没有警告.")



@tasks.loop(hours=24)
async def auto_clear_warning():
    with open('./inkbot/warnings.json', 'r') as f:
        warnings = json.load(f)

    # Check and clear old warnings
    for user_id, user_warnings in warnings.items():


        if user_warnings and get_current_time_ny() - datetime.fromisoformat(user_warnings[0]['timestamp']) > timedelta(
                days=30):
            warnings[user_id] = []


    # Save the warnings back to file
    with open('./inkbot/warnings.json', 'w') as f:
        json.dump(warnings, f)



@client.tree.command(name="checkwarning")
@commands.has_role("admin")
async def checkwarning(interaction:discord.Interaction, member: discord.Member):
    if not check_warning(interaction.user):
        await interaction.response.send_message("没有权限！", ephemeral=True)
        return

    with open('./inkbot/warnings.json', 'r') as f:
        warnings = json.load(f)

    member_id = str(member.id)
    if member_id in warnings:
        if len(warnings[member_id]) != 0:
            warning_text = [f"{i + 1}. {warn['reason']} (时间：: {warn['timestamp']})\n" for i, warn in
                            enumerate(warnings[member_id])]
            await interaction.response.send_message(f"{member.mention} 收到的警告:\n{' '.join(warning_text)}", ephemeral=True)
        else:
            await interaction.response.send_message(f"{member.mention}  目前没有警告.", ephemeral=True)
    else:
        await interaction.response.send_message(f"{member.mention}  目前没有警告.", ephemeral=True)











@client.tree.command(name="clearwarning")
@commands.has_role("admin")
async def clearwarning(interaction:discord.Interaction, member: discord.Member, index: int):
    if not check_warning(interaction.user):
        await interaction.response.send_message("没有权限！", ephemeral=True)
        return
    logger.warning(f"{interaction.user.nick} 清除了 {member.nick} 的警告记录")

    with open('./inkbot/warnings.json', 'r') as f:
        warnings = json.load(f)

    res = ""

    if str(member.id) in warnings:
        l = len(warnings[str(member.id)])

        if index > l or index < 0:
            res = f"该用户只有{l}条警告！"
        else:

            warnings[str(member.id)].pop(index - 1)
        res = f"{member.mention} 的第{index}条警告已经清除"
    else:
        res = f"{member.mention} 目前还没有任何警告记录"


    with open('./inkbot/warnings.json', 'w') as f:
        json.dump(warnings, f)

    await interaction.response.send_message(res, ephemeral=True)


while __name__ == '__main__':
    try:

        client.run(variables.token)
    except discord.errors.HTTPException as e:
        print(e)
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system('kill 1')
