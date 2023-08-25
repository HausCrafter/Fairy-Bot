import nextcord
import wavelink
from nextcord import Interaction
from nextcord.ext import commands


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 