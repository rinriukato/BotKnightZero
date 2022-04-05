#import os
import discord, datetime
import gpt_2_simple as gpt2
import asyncio, random, string
from discord.ext import commands

# Load GPT-2 model
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')

# bot user ID
#client = commands.Bot(command_prefix='.')
client = discord.Client()

def genQuote():
    print("Generating quote")
    results = gpt2.generate(sess, run_name='run1', temperature=0.3, nsamples=5, batch_size=1, length=30, include_prefix=False, return_as_list=True)
    splitRes = results[random.randint(0, len(results) - 1)].split('\n')
    return splitRes[random.randint(0, len(splitRes) - 1)]

def genMoreQuotes():
    print("Generating quote")
    results = gpt2.generate(sess, run_name='run1', temperature=0.6, nsamples=5, batch_size=1, length=30, include_prefix=False, return_as_list=True)
    splitRes = results[random.randint(0, len(results) - 1)].split('\n')
    return splitRes


# On initialize
@client.event
async def on_ready():
    print("Logged on as user:{}".format(client))
    game = discord.Game("428: Shibuya Scramble")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return
    
    if client.is_ready:
        if msg.startswith("Botkz, say something funny"):
            async with message.channel.typing():
                await message.channel.send(genQuote())
                print("Task complete")

        if msg.startswith("Botkz, say more stuff"):
            async with message.channel.typing():
                quotelist = genMoreQuotes()
                for quote in quotelist:
                    await message.channel.send(quote)
                print("Task complete")
        
        if msg.startswith("Botkz, about"):
            async with message.channel.typing():
                abtembed = discord.Embed(
                author = "rinri",
                title = "BotKnightZero about page",
                descripton = "I am a chatbot created by @rinri on the GPT-2 Text generation model. Training on user: BlackKnightZero\n I was finetuned on the 124M model size, with a dataset of approxiamately 30K messages over the course of 5 years\n...I am the funny\n",
                color = discord.Colour.blue()
                )
                abtembed.add_field(name='Commands',value='',inline=False)
                abtembed.add_field(name='about',value="Displays the about page/command list", inline=False)            
                abtembed.add_field(name='BotKnightZero, say something funny',value="Generates a random quote with no context (Spell the commamnd exactly)", inline=False)
                abtembed.add_field(name='BotKnightZero, response [#]',value="BotKnightZero will generate a message in context to the [#] of message sent in history (up to 9 most recent messages)", inline=False)
                await message.channel.send(embed=abtembed)

    else:
        return

#@client.command(pass_context=True)
#async def about():
#    embed = discord.Embed(
#                author = "rinri",
#                title = "BotKnightZero about page",
#                descripton = "I am a chatbot created by @rinri on the GPT-2 Text generation model. Training on user: BlackKnightZero\n I was finetuned on the 124M model size, with a dataset of approxiamately 30K messages over the course of 5 years\n...I am the funny\n",
#                color = discord.Colour.blue()
#            )
#    embed.add_field(name='Commands',value='',inline=False)
#    embed.add_field(name='about',value="Displays the about page/command list", inline=False)            
#    embed.add_field(name='BotKnightZero, say something funny',value="Generates a random quote with no context (Spell the commamnd exactly)", inline=False)
#    embed.add_field(name='BotKnightZero, response [#]',value="BotKnightZero will generate a message in context to the [#] of message sent in history (up to 9 most recent messages)", inline=False)
#
#    await client.say(embed=embed)

# Run bot
#LOGIN = os.environ['TOKEN']
client.run("OTM4ODExOTM3Mzk4MDkxNzg2.YfvuwA.7Fgakd8TJ7X3gIbMi2PVDS1xjKE")