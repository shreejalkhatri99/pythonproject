import discord 
import random

TOKEN = 'OTI1NjAyODUwMzA0ODMxNTI5.Ycvg1A.b9RBpbjtprGSJfM7sfkx4dBtY-A'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'off-topic':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return

        elif user_message.lower() == 'tell me a joke':
            await message.channel.send(f"Why don't ants get sick? because they have ATINY body {username}!")
            return

        elif user_message.lower() == 'how are you?':
            await message.channel.send(f'I am fine thankyou. what about you? {username}!')
            return

        elif user_message.lower() == 'I am doing fine too':
            await message.channel.send(f'Good to know. {username}!')
            return
            
        
        elif user_message.lower() == '!random':
           response = f'This is your random number: {random.randrange(9000000)}'
           await message.channel.send(response)
           return
        

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return

    


client.run(TOKEN)
