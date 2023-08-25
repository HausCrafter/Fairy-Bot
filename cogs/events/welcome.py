import nextcord
from nextcord.ext import commands

class Welcome_(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        Channel_Welcome = self.bot.get_channel(1134163969137971342)
        Channel_Regeln = self.bot.get_channel(1134164062209581087)
        #Channel_Chat = self.bot.get_channel()
        #Channel_Rollen = self.bot.get_channel()
        em = nextcord.Embed(
            title="Fairy Community",
            description=f"""**Willkommen {member.mention} zum Fairy Clan.**
            **Dieser Clan basiert auf den Anime *Fairy Tail* und steht dafür, dass wir**
            **eine Anime Community im MineVale Server sind.**
            **Wir lieben den Anime Style und haben uns diese Serie ausgesucht, da es dort**
            **||um eine Gilde geht, die wie eine Familie bei Problemen zusammenhält.||**


            **Um dich bei uns wohlzufühlen, brauchst einfach nur ehrlich sein und wir helfen dir auch gerne bei Anregungen und Problemen weiter.**

            **Lies die Regeln gerne mal durch damit es zu keinen Fehlern des Verhaltens kommt (keine sorge sind nicht zu lang)**  {Channel_Regeln.mention}

            **Sag doch gerne mal *Hallo!* zu den anderen**  

            **Gib dir doch selbst ein paar Rollen** """,
            colour=0x00a3e0
        )
        await Channel_Welcome.send(embed=em)
        
def setup(bot):
  bot.add_cog(Welcome_(bot))