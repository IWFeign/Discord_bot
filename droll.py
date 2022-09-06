from discord.ext import commands
from numpy import random
import asyncio
import discord

class droll(commands.Cog, name="dice roll"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def droll(self,ctx):
        ngg_embed = discord.Embed(
            title = "Rolling Dice",
            colour = discord.Colour.from_rgb(248,79,0)
            )
                
        ngg_embed.add_field(name="Computer can roll dice",value="D4-6-8-10-12-20",inline=False)
        ngg_embed.add_field(name="Using this command",value="1d4 or 2d6 3d20\nBoth possible",inline=False)
        msg = await ctx.send(embed=ngg_embed)
        
        author = ctx.message.author
        author = str(author)
        author = author.split("#")
        author = author[0]
        
        ngg_embed_cor = discord.Embed(
        title = "Rolling Dice",
        colour = discord.Colour.from_rgb(248,79,0)
        )
        ngg_embed_cor.set_author(name=author)
        
        try:
            dice = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 20)
            try: await dice.delete()
            except Exception: pass
            dice = dice.content
            dice = str(dice)
            dice = dice.split(' ')
            numlist = []
            vallist = []
            for i in dice:
                counter = 1
                dstr = i.lower()
                dstr = dstr.split("d")
                dnum = dstr[0]
                dsize = dstr[1]
                
                if int(dnum)>3:
                    ngg_embed_cor.add_field(name="ERROR!!!",value="You can't roll more than 3 dices.",inline=True)
                    await msg.edit(embed=ngg_embed_cor)
                    break
                if dsize=="4" or dsize=="6" or dsize=="10" or dsize=="12" or dsize=="20":
                    print("yes")
                else:
                    ngg_embed_cor.add_field(name="ERROR!!!",value="You can't roll this dice.",inline=True)
                    await msg.edit(embed=ngg_embed_cor)
                    break
                while counter<=int(dnum):
                    counter += 1
                    number = random.randint(dsize)
                    number += 1
                    number = str(number)
                    numlist.append(number)
                    vallist.append(dsize)
            for j in range(0,len(numlist)):
                ngg_embed_cor.add_field(name=f"D{vallist[j]}",value=numlist[j],inline=True)
            await msg.edit(embed=ngg_embed_cor)

        except asyncio.TimeoutError:
            ngg_embed_cor.add_field(name="ERROR!!!",value="Sorry, you didn't reply in time.",inline=True)
            await msg.edit(embed=ngg_embed_cor) 
        except ValueError:
            await ctx.send("Sorry, your input was not a number")
        print("!droll used")
        
def setup(bot: commands.Bot):
    bot.add_cog(droll(bot))