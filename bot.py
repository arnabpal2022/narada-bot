import os

import discord
from discord.ext import commands

from main import run_crew

# from main import executed_value
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)
msg = ""


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    print(bot.user.id)


@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        print(bot.user.id)
        await message.reply("Working on it!")
        exe = run_crew(message.content)
        if exe is not None:
            await message.reply("Task Completed <3")
        else:
            await message.reply("Task Failed :(")


bot.run(DISCORD_API_KEY)
<<<<<<< HEAD



=======
>>>>>>> 10885557 (updated and final)
