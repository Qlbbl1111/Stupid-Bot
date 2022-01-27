import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import random


token = os.environ['TOKEN']
author_id = os.environ['author_id']
dancers = ['https://media.giphy.com/media/tsX3YMWYzDPjAARfeg/giphy.gif', 'https://media.giphy.com/media/14qb1Uhf40ndw4/giphy.gif', 'https://media.giphy.com/media/l2QZSjo0lwEMC0GVG/giphy.gif', 'https://media.giphy.com/media/5xaOcLGvzHxDKjufnLW/giphy.gif']


bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = author_id  # Change to your discord id!!!


@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


#Random dance command.
@bot.command(name='dance', help='Sends random dance gif.')
async def dance(ctx):
    await ctx.send(random.choice(dancers))

@dance.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Something went wrong.')

#Yell command.
@bot.command(name='yell', help='Yell at another member.')
async def yell(ctx, *, member:discord.Member):
  await ctx.send(f"Dear <@{member.id}>, AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")

@yell.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: There is no member by that name.')


#other command
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