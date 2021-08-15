from discord.ext import commands
from os import getenv
import traceback

client = commands.Bot(command_prefix = '!')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def nano_me(ctx):
    await ctx.send('強化完了！力を見せてやれ！')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
