import discord
from discord.ext import commands
from main import run_crew


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)
msg = ""

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print(bot.user.id)

@bot.event
async def on_message(message):
    print(f'Received message: {message.content}')
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        print(bot.user.id)
        run_crew(message.content)
        await message.reply('pong')

bot.run('MTI1NjQ4MDU5MDUzOTEzMjk3Mg.G9SAAM.1fitF7Jf5OmiSrLgVbwIZ82wvWZVkpfB8cm9QE')



