import discord
import joke_api
import asyncio
import time
from discord.ext import commands


client = discord.Client()
helpp = ('Potato Bot\n$joke for a joke')
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="%help"))



@client.event  # event decorator/wrapper
async def on_ready():
    global sentdex_guild
    sentdex_guild = client.get_guild(405403391410438165)
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author == client.user:
        return
    if message.author == client.user:
        return
    if message.content == "hi":
            await message.channel.send("Sup")
    if message.content == "Hello":
            await message.channel.send("Sup") ## Greetings
    if message.content == "Hey":
            await message.channel.send("Sup")
    if message.content == "Hay":
            await message.channel.send("Sup")
    if message.content == "hay":
            await message.channel.send("Sup")
    if message.content == "@Potato Bot":
            await message.channel.send("Sup")
    if message.content == "hello":
            await message.channel.send("Sup")
    if message.content == "Yo":
            await message.channel.send("Sup")
    if message.content == "yo":
            await message.channel.send("Sup")
    if message.content == "yoo":
            await message.channel.send("Sup")
    if message.content == "Yoo":
            await message.channel.send("Sup")
    if message.content == "Yooo":
            await message.channel.send("Sup")
    if message.content == "yooo":
            await message.channel.send("Sup")
    if message.content == "Yoooo":
            await message.channel.send("Sup")
    if message.content == "yoooo":
            await message.channel.send("Sup")
    if message.content == "hey":
            await message.channel.send("Sup")

    if message.content == "%help":
            await message.channel.send('Potato Bot\n%joke for a joke')

    if message.content.startswith('%joke'):
        joke = joke_api.get_joke()
        print(joke)

        if joke == False:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])



client.run("TOKEN")
