from discord.ext import commands
import numpy as np
import pandas as pd
import asyncio
import discord

class hangman(commands.Cog, name="guessgame"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def hangman(self,ctx):
        word_list = pd.read_csv(r"word_list_out.csv")
        #%% Picking a word from list
        word = word_list.loc[[np.random.randint(len(word_list))]]
        word = word.values.tolist()
        word = word[0][0]
        
        #%% Picking letters for hinting player
        wordSize = len(word)
        hint = round(wordSize*0.33)
        # wordScreen = "-"*wordSize
        # print(f"Kelimeniz {wordSize} harften oluşmaktadır.(Boşluk içerebilir)")
        hintList = list(range(1,wordSize))
        hintListNew = []
        
        while hint>0:
            hint -= 1
            picker = hintList[np.random.randint(len(hintList))]
            hintListNew.append(picker)
            hintList.remove(picker)
        hintListNew.sort()
        
        # for x in hintListNew:
        #     letter = word[x-1]
        #     hintListLetters.append(letter)
        
        #%% Shows word with hint
        def showWord(word,hintListNew):
            hintListNew.append(99) #Prevents an IndexError caused by hLN>hintListNew length
            hLN = 0
            wordScreen = ""
            for x in range(0,len(word)):
                if x+1 == hintListNew[hLN]:
                    wSL = word[x]
                    wordScreen += wSL
                    hLN += 1
                elif word[x] == " ":
                    wordScreen += " "
                else:
                    wordScreen += "?"
            return(wordScreen)
            
            # print(wordScreen)
        #%%
        showWordDC = showWord(word,hintListNew) #Sends wordScreen for the first time
        chances = round(wordSize*0.4)
        
        hangmanEmbed = discord.Embed(
        title = "HANGMAN",
        colour = discord.Colour.from_rgb(255,255,0)
        )
            
        hangmanEmbed.add_field(name=f"Kelimeniz {wordSize} harften oluşmaktadır.",value="You have " + str(chances) + " chances left.\n Guess it!!!",inline=True)
        hangmanEmbed.add_field(name="Tahmin edeceğiniz kelime",value=showWordDC,inline=True)
        msg = await ctx.send(embed=hangmanEmbed)
       
        print(word)
        # print(f"You have {chances} chances left.")
        while chances>0:
            chances -= 1
            # wordGuess = input()
            author = ctx.message.author
            author = str(author)
            author = author.split("#")
            author = author[0]
            
            hangmanEmbedCor = discord.Embed(
            title = "Hangman",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            hangmanEmbedCor.set_author(name=author)
            
            try:
                guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 30)
                try: await guess.delete()
                except Exception: pass
                guess = guess.content
                wordGuess = str(guess)
                
                if wordGuess == word:
                    # print("Your guess was right")
                    hangmanEmbedCor.add_field(name=f"Kelimeniz {wordSize} harften oluşmaktadır.",value="Your guess was right.🟢",inline=True)
                    hangmanEmbedCor.add_field(name="Tahmin edeceğiniz kelime",value=showWordDC,inline=True)
                    hangmanEmbedCor.add_field(name="KELİMENİZ",value=word,inline=True)
                    await msg.edit(embed=hangmanEmbedCor)
                    break
                else:
                    # print("Your guess wasn't right try again")
                    if chances == 0:
                        # print("You have run out of chances")
                        # print(f"Your word was '{word}'")
                        hangmanEmbedCor.add_field(name=f"Kelimeniz {wordSize} harften oluşmaktadır.",value="You have "+str(chances)+" chances left.\nYour guess was wrong.🔴",inline=True)
                        hangmanEmbedCor.add_field(name="Tahmin edeceğiniz kelime",value=showWordDC,inline=True)
                        hangmanEmbedCor.add_field(name="KELİMENİZ",value=word,inline=True)
                        await msg.edit(embed=hangmanEmbedCor)
                        break
                    else:
                        picker = hintList[np.random.randint(len(hintList))]
                        hintListNew.append(picker)
                        hintList.remove(picker)
                        hintListNew.sort()
                        showWordDC = showWord(word,hintListNew)
                        hangmanEmbedCor.add_field(name=f"Kelimeniz {wordSize} harften oluşmaktadır.",value="You have "+str(chances)+" chances left.\nYour guess was wrong.🟡",inline=True)
                        hangmanEmbedCor.add_field(name="Tahmin edeceğiniz kelime",value=showWordDC,inline=True)
                        await msg.edit(embed=hangmanEmbedCor)
            except asyncio.TimeoutError:
                hangmanEmbedCor.add_field(name=f"Kelimeniz {wordSize} harften oluşmaktadır.",value="You have "+str(chances)+" chances left.\nSorry, you didn't reply in time.",inline=True)
                hangmanEmbedCor.add_field(name="Tahmin edeceğiniz kelime",value=showWordDC,inline=True)
                await msg.edit(embed=hangmanEmbedCor)
            except ValueError:
                await ctx.send("Sorry, your input was not a string")

def setup(bot: commands.Bot):
    bot.add_cog(hangman(bot))