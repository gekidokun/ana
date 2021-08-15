import discord
import random
import getenv
import traceback
from discord.ext import commands

client = commands.Bot(command_prefix = '!')


@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

    
@client.command()
async def nano_me(ctx):
    await ctx.send('強化完了！力を見せてやれ！')


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
