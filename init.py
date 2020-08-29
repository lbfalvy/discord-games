from discord.ext import commands
from random import seed
from dice import roll

seed()
bot = commands.Bot(command_prefix=",")

bot.add_command(roll)


bot.run("NzMxODYzOTM1NTk0MDA0NTEy.XwsR_Q.fCO19DD5BEpxX8moJ2pKHCghZXc")