import discord
import datetime
import time
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('/안녕'):
            await client.send_message(message.channel, "안녕하세요, 자갈입니다")

@client.event
async def on_member_join(member):
        fmt = '누가 새로 왔네요 {0.mention}이분'
        channel = member.server.get_channel("548630235008991252")
        await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(member):
        channel = member.server.get_channel("548630235008991252")
        fmt = '{0.mention} 님이 {1.name} 디스코드을 떠났습니다!'
        await client.send_message(channel, fmt.format(member, member.server))


    if message.content.startswith('/뭐해?'):
        await client.send_message(message.channel, "서버관리자가 시키는거 한다, 왜?")

    if message.content.startswith('/빠이'):
        await client.send_message(message.channel, "어, 알았어 잘가!")


    if message.content.startswith('/심심해'):
        await client.send_message(message.author, "가서 자갈게임 해!")

    if message.content.startswith("/선택해"):
        food = "햄버거 피자 치킨 밥 굶기 "
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('/핑'):
        before = time.monotonic()
        msg = await client.send_message(message.channel, ':ping_pong: 퐁!')
        ping = (time.monotonic() - before) * 1000
        text = ":ping_pong: 퐁!  `{0}`ms ".format((round(ping, 1)))
        await client.edit_message(msg, text)

    elif message.content.startswith('/주인님'):
            em = discord.Embed(title='↑ 애가 만듦', description='정보 없음', colour=0xDEADBF)
            em.set_author(name='! 바지리더', icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=em)

    elif message.content.startswith('/사전'):
     m = message.content
     await client.send_message(message.channel, 'http://krdic.naver.com/search.nhn?query=' + m[4:] + '&kind=all')

    if message.content.startswith("/투표"):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, "투표 - " + vote[0])
        for i in range(1, len(vote)):
           choose = await client.send_message(message.channel, "```" + vote[i] + "```")
        await client.add_reaction(choose, '⭕')

    if message.content.startswith('/골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('/게임추천'):
        await client.send_message(message.channel, "게임은, 역시 자갈게임이지!")

    if message.content.startswith('/이건좀아닌듯'):
        await client.send_message(message.channel, "미안")

    if message.content.startswith('/서버'):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.author, '\n'.join(list))

    if message.content.startswith('/주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0]) + 1):
            dice += random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('/정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(coler=0x00ffbb)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버이름", value=message.author.display_name, inline=True)
        embed.add_field(name="계정생성일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                        inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
access_token = os.environ["BOT TOKEN"]
client.run("access_token")
