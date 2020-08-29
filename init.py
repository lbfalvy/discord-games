from discord.ext import commands
from random import seed
from dice import roll

seed()
bot = commands.Bot(command_prefix=",")

bot.add_command(roll)

with open("token.txt") as tokenfile:
    bot.run(tokenfile.read())
