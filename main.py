import os
from keep_alive import keep_alive
from discord.ext import commands
import random


token = os.environ['TOKEN']

bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 318122785807269888  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def test2(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)



extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

#keep_alive()  # Starts a webserver to be pinged.


bot.run(token)  # Starts the bot