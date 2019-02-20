import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello Guys...Welcome in TRivia Crack Thankyou for joining...If u want trivia answers from this group type-"₹help"')
    print('Sent message to ' + member.name)
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="subscription process||₹help", type = 3))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '₹no':
        await client.send_message(message.channel,'ok no problem You can contact us anytime')
    if message.content == '₹done':
        await client.send_message(message.channel,'Ok thank you for paying to TRIVIA CRACK NEW we will maintain your support and please give the payment proof in #:euro:ᴘᴀʏ-ᴘʀᴏᴏғ channel..!! also dont do fake payment as we can Ban you')  
    if message.content == '₹yes':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/547376492947177474/547392283541110824/IMG-20190219-WA0010.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '₹yes':
        await client.send_message(message.channel,'Pay Rs150 on this code OR click on this link to pay-https://p-y.tm/u3Ar-u0 and give screenshot in #:euro:ᴘᴀʏ-ᴘʀᴏᴏғ channel..!!..PLEASE type-"₹done" once you have done payment')
    if message.content == '₹help':
        await client.send_message(message.channel,'Hello..this bot helps you to buy our access for answers of all trivia  just type-"₹buy"')
    if message.content == '₹buy':
        await client.send_message(message.channel,'Thank you for contacting our subscription bot:blush: :blush:  Pay 150 RS and enjoy all games answer in this server and drop you payment screenshot in #:euro:ᴘᴀʏ-ᴘʀᴏᴏғ channel..!! Do you want(₹yes/₹no)')
client.run('NTQ3Mzk4NDQyMjkzNTI2NTQz.D02MUg.Kxsmmpjt_fKCGL3mu6w7Daxf0XA')
