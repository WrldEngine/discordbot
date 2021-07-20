import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
Bot = commands.Bot(command_prefix='$')
mat = ['блять', 'сука', 'ебан', 'нахуй', 'заебал', 'похуй', 'далбаеб', 'долбаеб', 'пидр', 'пидор', 'пидораз', 'гандон', 'гондон', 'пиздец', 'спиздить', 'пизда', 'хуй', 'хуйня',
'Блять', 'Сука', 'Ебан', 'Нахуй', 'Заебал', 'Похуй', 'Далбаеб', 'Долбаеб', 'Пидр', 'Пидор', 'Пидораз', 'гандон', 'Гондон', 'Пиздец', 'Спиздить', 'Пизда', 'Хуй', 'Хуйня', 'бля', 'Бля', 'Нахуя', 'нахуя',
'сучка', 'Сучка', 'пиздабол','Пиздабол','Ебать', 'ебать','пиздюк','Пиздюк','Пидарас','пидарас','Уебан','уебан','уебок','Уебок', 'Трахал', 'трахал','жалаб','жалап']
yellow ='\033[33m'
back = """
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭╮╱╱╱╱╭╮
╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃┃╱╱╱╭╯╰╮
╱┃┃┃┣┳━━┳━━┳━━┳━┳━╯┃┃╰━┳━┻╮╭╯
╱┃┃┃┣┫━━┫╭━┫╭╮┃╭┫╭╮┃┃╭╮┃╭╮┃┃
╭╯╰╯┃┣━━┃╰━┫╰╯┃┃┃╰╯┃┃╰╯┃╰╯┃╰╮
╰━━━┻┻━━┻━━┻━━┻╯╰━━╯╰━━┻━━┻━╯
===
Pulatov Kamran(c) 2021
"""
print(yellow + back)
@Bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(Bot))

@Bot.event
async def on_message(message):
    if message.content == '!rand':
        await message.channel.send(random.randrange(0, 100))
    if message.content == '!ht':
        await message.channel.send(random.choice(['Орел', 'Решка']))
    if message.content == 'Привет бот':
        await message.channel.send(f'{message.author.mention}! Привет, рад тебя видеть😃😃😃')
    if message.content == 'Как дела? Бот':
        await message.channel.send(f'{message.author.mention}! Отлично, а у тебя?')
    if message.content == '!help':
        panel = discord.Embed(title='Возможности:', color=0x7417ff)
        mess = f"""Привет! {message.author.mention}
Я - Бот который модерирует и развлекает чат
!rand - Команда генерирует рандомное число
!ht - Орел или решка
Если вы напишете 'Привет бот', то он вам ответит сообщением
Если вы напишете 'Как дела? Бот', то он вам ответит сообщением
Остальные возможности будут скоро...
"""
        mess2 = """OLDs - Роль, которая дается участникам, которые уже 3 месяца с нами
У них есть доступ к нижнему совету
X подразделение - Это те люди, которых избрал мой создатель
У них есть доступ к высшему совету
И есть доступ к высшему голосовому каналу
Они могут удалять сообщения
"""
        panel.add_field(name='Что я могу?', value=mess, inline=False)
        panel.add_field(name='ROLES/Роли', value=mess2, inline=False)
        await message.channel.send(embed = panel)
    try:
        for x in mat:
            if x in message.content:
                await message.delete()
                await message.channel.send(f'{message.author.mention}! Прошу без мата')
        await Bot.process_commands(message)
    except: 
        pass
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx, member: discord.Member):
    await member.kick()
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member: discord.Member, time:int, reason):
    try:
        muterole = discord.utils.get(ctx.guild.roles, id=ROLEID) #Вставляете роль мута
        panel = discord.Embed(title='Muting', color=0xff0000)
        panel.add_field(name='Админ', value=ctx.message.author.mention, inline=False)
        panel.add_field(name='Нарушитель', value=member.mention, inline=False)
        panel.add_field(name='Причина', value=reason, inline=False)
        panel.add_field(name='Срок', value=time, inline=False)
        await member.add_roles(muterole)
        await ctx.send(embed = panel)
        await asyncio.sleep(time)
        await member.remove_roles(muterole)
    except:
        pass
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx, member: discord.Member):
    try:
        muterole = discord.utils.get(ctx.guild.roles, id=ROLEID) #Вставляете роль мута
        panel = discord.Embed(title='Unmuting', color=0x00ff00)
        panel.add_field(name='Админ', value=ctx.message.author.mention, inline=False)
        panel.add_field(name='Нарушитель', value=member.mention, inline=False)
        await ctx.send(embed = panel)
        await member.remove_roles(muterole)
    except:
        pass
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def old(ctx, member: discord.Member):
    try:
        old = discord.utils.get(ctx.guild.roles, id=ROLEID) #Вставляете роль олда
        panel = discord.Embed(title='Повышение роли[OLD]', color=0xff8000)
        panel.add_field(name='Назначил', value=ctx.message.author.mention, inline=False)
        panel.add_field(name='Участник', value=member.mention, inline=False)
        await ctx.send(embed = panel)
        await member.add_roles(old)
    except:
        pass
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unold(ctx, member: discord.Member):
    try:
        old = discord.utils.get(ctx.guild.roles, id=ROLEID) #Вставляете роль олда
        panel = discord.Embed(title='Отстронение от роли[OLD]', color=0xff8000)
        panel.add_field(name='Отстронил', value=ctx.message.author.mention, inline=False)
        panel.add_field(name='Участник', value=member.mention, inline=False)
        await ctx.send(embed = panel)
        await member.remove_roles(old)
    except:
        pass
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def xp(ctx, member: discord.Member):
    try:
        xp = discord.utils.get(ctx.guild.roles, id=ROLEID) #Вставляете роль админа
        panel = discord.Embed(title='Повышение роли[X]', color=0x4f0015)
        panel.add_field(name='Назначил', value=ctx.message.author.mention, inline=False)
        panel.add_field(name='Участник', value=member.mention, inline=False)
        await ctx.send(embed = panel)
        await member.add_roles(xp)
    except:
        await ctx.send("Неправильно использована команда")
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unxp(ctx, member: discord.Member):
    try:
        xp = discord.utils.get(ctx.guild.roles, id=ROLEID)#Вставляете роль админа
        panel = discord.Embed(title='Отстронение от роли[X]', color=0x4f0015)
        panel.add_field(name='Отстронил', value=ctx.message.author.mention, inline=False)
        panel.add_field(name='Участник', value=member.mention, inline=False)
        await ctx.send(embed = panel)
        await member.remove_roles(xp)
    except:
        await ctx.send("Неправильно использована команда")
Bot.run('Your token')
