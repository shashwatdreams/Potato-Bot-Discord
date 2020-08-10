import discord
import joke_api
import asyncio
import time
from discord.ext import commands

messages = joined = 0

client = discord.Client()
helpp = ('Potato Bot\n$joke for a joke')
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="%help")) ## Change status

@client.event
async def on_message(message):

    if message.content.startswith('%joke'): # joke commands
        joke = joke_api.get_joke()
        print(joke)

        if joke == False:
            await message.channel.send("Couldn't get joke from API. Try again later.") # joke failed
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])
@client.event
async def on_message(message):
    if message.content.startswith('%help'):
        embedVar = discord.Embed(title="Potato Bot", description="%joke for a joke", color=0x00ff00)
        embedVar.add_field(name="Created by Oshawot", value="oshawot#7410", inline=False)
        await message.channel.send(embed=embedVar)

client.run("TOKEN")
