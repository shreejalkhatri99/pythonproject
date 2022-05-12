import discord 
from discord.ext import commands 
import random

client = commands.Bot(command_prefix = 'd!')

@client.event
async def on_ready():
    print('Bot is online')

@client.command(aliases = ['p'])
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(aliases= ['8ball','8b'])
async def eightball(ctx,*,question):
     responses = [
        'Probably no.',
        'Probably not.',
        'Idk bro.',
        'Prolly.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitaly.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Try again.',
        'Obviously yeah.',
        'Better not tell you know.',
        ]
     await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}')



client.run('OTI1Njc2MDYwNjUyMjMyNzA0.YcwlAw.prkc0dWqsXJqpXRY-19eJSlI2yA')

