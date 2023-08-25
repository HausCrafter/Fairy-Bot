import os

import nextcord
from nextcord.ext import commands

from assets.config import F, S
from keep_alive import keep_alive

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)
bot.remove_command("help")

cogs = [
    "cogs.commands.ping",
    "cogs.commands.clear",
    "cogs.events.welcome",
    "cogs.events.on_error",
]

@bot.event
async def on_ready():
    os.system('clear')
    #print("--------------------------------------------------------------------------------------------------------------")
    #print(F.b + S.D + logo.logo + F.R_ALL)
    print("--------------------------------------------------------------------------------------------------------------")
    print(" ")
    print(F.g + S.B + "[SUCCESSFULY]" + F.R_ALL + " Bot wurde gestartet.")
    print(" ")
    print(F.y + "[INFO]" + F.R + " Eingelogt als:")
    print("       " + bot.user.name)
    print(" ")
    print(F.y + "[INFO]" + F.R + " Bot ID:")
    print("       " + str(bot.user.id))
    print(" ")
    print("--------------------------------------------------------------------------------------------------------------")
    print(" ")
    print(F.y + "[INFO]" + F.R + " Laden von Cogs . . .")
    for cog in cogs:
        if cog.startswith("cogs.commands"):
            try:
                bot.load_extension(cog)
            except Exception as e:
                cog=cog.split(".")
                print(F.r + "       [ERROR]" + F.R + " Could't load cog " + cog[2] + ": " + str(e) + "!")
                break
            cog = cog.split(".")
            print(F.g + S.B + "       [SUCCESSFULY]" + F.R_ALL + " Cog " + cog[2] + " was loaded.")
        elif cog.startswith("cogs.events"):
            try:
                bot.load_extension(cog)
            except Exception as e:
                cog=cog.split(".")
                print(F.r + "       [ERROR]" + F.R + " Could't load cog " + cog[2] + ": " + str(e) + "!")
                break
            cog = cog.split(".")
            print(F.g + S.B + "       [SUCCESSFULY]" + F.R_ALL + " Cog " + cog[2] + " was loaded.")
        elif cog.startswith("cogs.tasks"):
            try:
                bot.load_extension(cog)
            except Exception as e:
                cog=cog.split(".")
                print(F.r + "       [ERROR]" + F.R + " Could't load cog " + cog[2] + ": " + str(e) + "!")
                break
            cog = cog.split(".")
            print(F.g + S.B + "       [SUCCESSFULY]" + F.R_ALL + " Cog " + cog[2] + " was loaded.")
        else:
            print(F.r + "       [ERROR]" + F.R + " undefined directory")
    print(" ")
    print("--------------------------------------------------------------------------------------------------------------")
    await bot.sync_application_commands()
    guild_id = 1116654280548548638
    await bot.sync_application_commands(guild_id=guild_id)
    await bot.change_presence(
        activity=nextcord.Activity(
            type=nextcord.ActivityType.playing,
            name="!help"
        ),
        status=nextcord.Status.online
    )

keep_alive()
bot.run(os.environ["TOKEN"])