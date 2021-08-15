from discord.ext import commands
from os import getenv
import traceback

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print("準備OK")
    print("---------------------------")

    
@client.command()
async def nano_me(ctx):
    await ctx.send('強化完了！力を見せてやれ！')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
