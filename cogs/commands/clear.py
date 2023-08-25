from os import name
import time

import nextcord
from nextcord import Interaction
from nextcord.ext import commands


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int = None):
        if nextcord.utils.get(ctx.author.roles, name='★---Team---★'):
            if amount is None:
                await ctx.message.delete()
                em=nextcord.Embed(
                    title="Error",
                    color=nextcord.Color.red()
                )
                em.add_field(name='Error ID', value='175')
                em.add_field(name='Error Name', value='Felhende Angabe: amount')
                em.add_field(name='Error Lößung', value='`Wiederhole den command mit einer Zahl`')
                message = await ctx.send(embed=em)
                time.sleep(15)
                await message.delete()
            elif amount >= 50:
                await ctx.message.delete()
                em=nextcord.Embed(
                    title="Error",
                    color=nextcord.Color.red()
                )
                em.add_field(name="Error ID", value="176")
                em.add_field(name="Error Name", value="Zuhohe angabe: amount")
                em.add_field(name="Error Lößung", value="Wiederhole den command mit einer Zahl zwichen 1 und 50")
                message = await ctx.send(embed=em)
                time.sleep(15)
                await message.delete()
            else:
                await ctx.channel.purge(limit=amount)
                time.sleep(5)
                em = nextcord.Embed(
                    title="Erfolgreich",
                    description=f"Es wurden {amount} nachrichten gelöcht",
                    color=nextcord.Color.brand_green())
                message = await ctx.send(embed=em)
                await ctx.message.delete()
                time.sleep(15)
                await message.delete()
        else:
            await ctx.message.delete()
            embed = nextcord.Embed(
                title='Error',
                color=nextcord.Color.red()
            )
            embed.add_field(name='Error ID', value='086')
            embed.add_field(name='Error Name', value='Fehlende Berechtigung')
            embed.add_field(name='Error Lößung', value='`None`')
            await ctx.send(embed=embed)

    @nextcord.slash_command(name="clear", guild_ids=[1116654280548548638])
    async def s_clear(self, interaction: Interaction, amount: int = None):
        if nextcord.utils.get(interaction.user.roles, name='★---Team---★'):
            if amount is None:
                em=nextcord.Embed(
                    title="Error",
                    color=nextcord.Color.red()
                )
                em.add_field(name='Error ID', value='175')
                em.add_field(name='Error Name', value='Felhende Angabe: amount')
                em.add_field(name='Error Lößung', value='`Wiederhole den command mit einer Zahl zwichen 1 und 50`')
                message = await interaction.response(embed=em)
            elif amount <= 50:
                em=nextcord.Embed(
                    title="Error",
                    color=nextcord.Color.red()
                )
                em.add_field(name="Error ID", value="176")
                em.add_field(name="Error Name", value="Zuhohe angabe: amount")
                em.add_field(name="Error Lößung", value="`Wiederhole den command mit einer Zahl zwichen 1 und 50`")
                message = await interaction.response(embed=em)
            else:
                await interaction.channel.purge(limit=amount)
                em = nextcord.Embed(
                    title="Erfolgreich",
                    description=f"Es wurden {amount} nachrichten gelöcht",
                    color=nextcord.Color.brand_green())
                message = await interaction.response(embed=em)
        else:
            embed = nextcord.Embed(
                title='Error',
                color=nextcord.Color.red()
            )
            embed.add_field(name='Error ID', value='086')
            embed.add_field(name='Error Name', value='Fehlende Berechtigung')
            embed.add_field(name='Error Lößung', value='`None`')
            await interaction.response(embed=embed)

def setup(bot):
    bot.add_cog(clear(bot))