from discord.ext import commands
from numpy import random
from numpy import floor
import asyncio
import discord
import numpy as np

class guessgame(commands.Cog, name="guessgame"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def guessgame(self,ctx):
        chances = 5
        number_r = random.randint(100)
        number = floor(number_r)
        last_guess = []
        ngg_embed = discord.Embed(
            title = "Number Guessing Game",
            colour = discord.Colour.from_rgb(255,255,0)
            )
                
        ngg_embed.add_field(name="Computer choosed a number between 0-100",value="You have " + str(chances) + " chances left.\n Guess it!!!",inline=True)
        ngg_embed.add_field(name="Your last guess",value="--")
        msg = await ctx.send(embed=ngg_embed)

        while chances>0:
            chances = chances - 1
            author = ctx.message.author
            author = str(author)
            author = author.split("#")
            author = author[0]
            points = 0
            
            ngg_embed_cor = discord.Embed(
            title = "Number Guessing Game",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            ngg_embed_cor.set_author(name=author)
            
            try:
                guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 10)
                try: await guess.delete()
                except Exception: pass
                guess = guess.content
                guess = int(guess)
                last_guess.append(guess)
                if guess==number:
                    if chances==4:
                        points = 3125
                    elif chances==3:
                        points = 625
                    elif chances==2:
                        points = 125
                    elif chances==1:
                        points = 25
                    elif chances==0:
                        points = 5
                    ngg_embed_cor.add_field(name="Computer choosed a number between 0-100",value="Your guess was right.\nYou gained "+str(points)+" points",inline=True)
                    ngg_embed_cor.add_field(name="Your last guess",value=str(last_guess)[1:-1])
                    await msg.edit(embed=ngg_embed_cor)
                    from leaderboard import pointadder
                    pointadder(author,points)
                    break
                elif chances>1:
                    if number>guess:
                        ngg_embed_cor.add_field(name="Computer choosed a number between 0-100",value="You have "+str(chances)+" chances left.\nYour guess is LOWER than computers number.",inline=True)
                        ngg_embed_cor.add_field(name="Your last guess",value=str(last_guess)[1:-1])
                        await msg.edit(embed=ngg_embed_cor)
                    elif number<guess:
                        ngg_embed_cor.add_field(name="Computer choosed a number between 0-100",value="You have "+str(chances)+" chances left.\nYour guess is HIGHER than computers number.",inline=True)
                        ngg_embed_cor.add_field(name="Your last guess",value=str(last_guess)[1:-1])
                        await msg.edit(embed=ngg_embed_cor)
                elif chances==1:
                    ngg_embed_cor.add_field(name="Computer choosed a number between 0-100",value="You have "+str(chances)+" chance left.\nComputers number is between "+str(number-random.randint(5))+" and "+str(number+random.randint(5)),inline=True)
                    ngg_embed_cor.add_field(name="Your last guess",value=str(last_guess)[1:-1])
                    await msg.edit(embed=ngg_embed_cor)
                elif chances==0:
                    ngg_embed_cor.add_field(name="Computer choosed a number between 0-100",value="You have "+str(chances)+" chances left.\nComputer's choosen number was "+str(number)+"\nOut of chances but don't worry your time will come.",inline=True)
                    ngg_embed_cor.add_field(name="Your last guess",value=str(last_guess)[1:-1])
                    await msg.edit(embed=ngg_embed_cor)
                    from leaderboard import pointadder
                    pointadder(author,points)
            except asyncio.TimeoutError:
                ngg_embed_cor.add_field(name="Computer choosed a number between 0-100",value="You have "+str(chances)+" chances left.\nSorry, you didn't reply in time.",inline=True)
                last_guess.append("--")
                ngg_embed_cor.add_field(name="Your last guess",value=str(last_guess)[1:-1])
                await msg.edit(embed=ngg_embed_cor)
                if chances==0:
                  from leaderboard import pointadder
                  pointadder(author,points)
            except ValueError:
                await ctx.send("Sorry, your input was not a number")
        print("!guessgame used")
        
def setup(bot: commands.Bot):
    bot.add_cog(guessgame(bot))