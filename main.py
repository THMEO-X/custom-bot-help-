import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập dưới tên {bot.user}')
    await bot.change_presence(activity=discord.Game(name="!help"))

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
