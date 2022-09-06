from discord.ext import commands
import pandas as pd
from numpy import random
import asyncio
import discord
from main import client

class enterdungeon(commands.Cog, name="enterdungeon"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def enterdungeon(self,ctx):
        author = ctx.message.author
        author_name = str(author)
        author_name = author_name.split("#")
        author_name = author_name[0]
        
        ed_embed = discord.Embed(
            title = "Enter Dungeon",
            description = """In this journey, you will face with ruthless enemies, you may find chests that will give you extra points or potions that will make your journey last longer. You can attack your enemies, defend their attacks. By typing:\n
                Attack: You will give&take more damage\n
                Defend: You will give&take less damage. You will have more chance to block their attacks. If you block damage """,
            colour = discord.Colour.from_rgb(255,255,0)
            )
        ed_embed.set_author(name=author_name)
        msg = await ctx.send(embed=ed_embed)
                        
        #%% Düşmanların infoları
        data_starter = [["Maggot",6,9,3,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/0/08/Maggot.png/revision/latest?cb=20150711041325"],
                ["Spitter",7,12,4,15,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/6/62/Spitter.png/revision/latest?cb=20150711041814"],
                ["Shambler Tentacle",8,30,10,18,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/f/f2/Shambler_Tentacle.png/revision/latest?cb=20150712115759"],
                ["Webber",7,15,5,15,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/c/cc/Webber.png/revision/latest?cb=20170710144533"],
                ["Bone Rabble",8,3,1,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/3/3c/Bone_Rabble.png/revision/latest?cb=20150711042215"]                ]
        starter_enemies = pd.DataFrame(data_starter,columns=["Name","HP","on Attack","on Defend","Block Chance","Photo"])
        
        data_easy = [["Cultist Brawler",15,15,5,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/4/47/Cultist_Brawler.png/revision/latest?cb=20171202185525"],
                     ["Collected Man-at-Arms",16,21,7,8,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/a/ab/Collected_Man-at-Arms.png/revision/latest?cb=20151202192441"],
                     ["Cultist Acolyte",13,21,7,13,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/a/ad/Cultist_Acolyte.png/revision/latest?cb=20171202185902"],
                     ["Madman",14,27,9,20,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/2/20/Madman.png/revision/latest?cb=20170220185618"],
                     ["Gatekeeper",12,15,5,21,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/4/42/Castellan.png/revision/latest?cb=20170622135550"]]
        easy_enemies = pd.DataFrame(data_easy,columns=["Name","HP","on Attack","on Defend","Block Chance","Photo"])
        
        data_medium = [["Rattler",24,27,18,27,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/1/1a/Rattler.png/revision/latest?cb=20171031003350"],
                       ["Brigand Raider",25,15,10,26,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/c/cd/Brigand_Raider.png/revision/latest?cb=20160524044205"],
                       ["Brigand Hunter",25,24,16,20,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/c/ca/Brigand_Hunter.png/revision/latest?cb=20160524044432"],
                       ["Bone Spearman",22,12,8,9,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/8/86/Bone_Solider.png/revision/latest?cb=20150711042239"],
                       ["Small Pew",25,6,4,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/2/28/Pew_Small.png/revision/latest?cb=20160526052255"]]
        medium_enemies = pd.DataFrame(data_medium,columns=["Name","HP","on Attack","on Defend","Block Chance","Photo"])
        
        data_hard = [["Bone Bearer",51,21,14,36,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/9/92/Bone_Bearer.png/revision/latest?cb=20170208063643"],
                     ["The Collector",70,15,10,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/3/37/The_Collector.png/revision/latest?cb=20151202191158"],
                     ["Uca Major",61,27,18,9,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/b/b8/Uca_Crusher.png/revision/latest?cb=20151202210456"],
                     ["Squiffy Ghast",55,24,16,34,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/a/ae/Squiffy_Ghast.png/revision/latest?cb=20170208062955"],
                     ["Shrieker",75,21,14,40,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/5/5e/Shrieker.png/revision/latest?cb=20170210070315"]]
        hard_enemies = pd.DataFrame(data_hard,columns=["Name","HP","on Attack","on Defend","Block Chance","Photo"])
        
        data_boss = [["Necromancer",105,24,16,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/c/c4/Bone_Necromancer.png/revision/latest?cb=20150711042427"],
                     ["Swine Prince",132,60,40,15,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/4/4e/Swine_Prince_Sprite.png/revision/latest?cb=20150711042807"],
                     ["Unclean Giant",102,30,20,48,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/a/a6/Unclean_Giant.png/revision/latest?cb=20150711041356"],
                     ["Siren",119,15,10,13,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/0/0a/Siren.png/revision/latest?cb=20151202192918"],
                     ["Drowned Crew",100,27,18,0,"https://static.wikia.nocookie.net/darkestdungeon_gamepedia/images/c/c7/Drowned_Crew.png/revision/latest?cb=20151202192949"]]
        boss_enemies = pd.DataFrame(data_boss,columns=["Name","HP","on Attack","on Defend","Block Chance","Photo"])
        
        #%% Kodun çalışması için gereken bilgiler
        life = 100
        room = 0
        points = -5
        chests = 0
        potions = 0
        e_hp = -1
        givenDamage = 0
        takenDamage = 0
        afk = 0
        await asyncio.sleep(5)
        
        #%% Kodun Başlangıcı
        while life>0:
            room = room + 1
            ed_embed_cp = discord.Embed(
            title = "Enter Dungeon",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            #%% Oda atlamayı kontrol ediyor
            if e_hp<=0:
                if room>1:
                    #%% Odanın sonunda potion/chest bulunan kısım
                    potNum = random.randint(101)
                    if potNum<=20:
                        potions = potions + 1
                        potionHP = random.randint(10,21)
                        life = life + potionHP
                        if life>100:
                            life = 100
                        ed_embed_cp.add_field(name = "Potion!!!",value = f"You have found a potion!!!\nGained {potionHP} extra life.",inline=False)
                        ed_embed_cp.set_image(url="https://cdn.discordapp.com/attachments/884176668971921422/908357435377455144/emojisky.com-232627.png")
                        await msg.edit(embed=ed_embed_cp)
                        await asyncio.sleep(2)
                                        
                    chestNum = random.randint(101)
                    if chestNum<=8:
                        chests = chests + 1
                        points = points + 25
                        ed_embed_cp.add_field(name = "Chest!!!",value = "You have found a chest!!!\nGained extra 25 points.",inline=False)
                        ed_embed_cp.set_image(url="https://cdn.discordapp.com/attachments/884176668971921422/908357436816101376/toppng.com-treasure-chest-439x339.png")
                        await msg.edit(embed=ed_embed_cp)
                        await asyncio.sleep(2)
                        
                #%% Oda durumuna göre puan ekleyen kısım
                if room>=2 and room<7:
                    points = points + 1
                elif room>=7 and room<9:
                    points = points + 25
                elif room>=9 and room<11:
                    points = points + 125
                elif room==11:
                    points = 3125
                    
                #%% Hangi odada olunduğuna göre bir düşman seçiyor
                if room<4:
                    enemy = starter_enemies.loc[random.randint(len(data_starter))]
                elif room>=4 and room<6:
                    enemy = easy_enemies.loc[random.randint(len(data_easy))]
                elif room>=6 and room<8:                   
                    enemy = medium_enemies.loc[random.randint(len(data_medium))]
                elif room>=8 and room<10:                   
                    enemy = hard_enemies.loc[random.randint(len(data_hard))]
                elif room==10:                   
                    enemy = boss_enemies.loc[random.randint(len(data_boss))]
                elif room==11:
                    break
                                    
                e_name = enemy[0]
                e_hp = enemy[1]
                e_a = enemy[2]
                e_d = enemy[3]
                e_bc = enemy[4]
            
            #%% Düşman seçildikten sonra düşmanın bilgilerini embede yazıyor
            ed_embed_up = discord.Embed(
            title = "Enter Dungeon",
            description = "You are against " + e_name + "\nWhat will you do?",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            ed_embed_up.set_author(name=f"{author_name}\tRoom: {room}\t\t🟢")
            ed_embed_up.set_footer(text="Usable Commands: 'Attack' and 'Defend'")       
            ed_embed_up.set_image(url=enemy[5])
            ed_embed_up.add_field(name="Your HP",value=life)
            ed_embed_up.add_field(name="Enemy HP",value=e_hp)
            ed_embed_up.add_field(name="Damages",value=f"Last Given Damage: {givenDamage}\nLast Taken Damage: {takenDamage}",inline=False)
            await msg.edit(embed=ed_embed_up)
            
            #%% Hangi aksiyonun seçildiğini öğrenen kısım
            try:
                tactics = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 20)                
                try: await tactics.delete()
                except Exception: pass
                tactics = tactics.content
                tactics = tactics.lower()
                if tactics == "attack":
                    bonus_attack = random.randint(11)
                    bonus_defence = 0
                    blockChance = e_bc
                    enemyDamage = random.randint(e_a+1)
                elif tactics == "defend":
                    bonus_attack = 0
                    bonus_defence = random.randint(11)
                    blockChance = e_bc + 25
                    enemyDamage = random.randint(e_d+1)
                else:
                    raise ValueError("Your imput was not an usable command")
            #%% Zaman aşımına cevap veren kısım
            except asyncio.TimeoutError:
                afk = 1
                ed_embed_up.add_field(name="You didn't reply in time <:Sadge:815607998222172191>",value="You were vulnurable for that you have taken more damage",inline=False)
                await msg.edit(embed=ed_embed_up)
                await asyncio.sleep(3)
            except ValueError:
                afk = 1
                await ctx.send("Your imput was not an usable command")
                            
            #%% Düşmana verilen hasar
            if afk==1:
                givenDamage = 0
            else:
                givenDamage = random.randint(5) + bonus_attack
            e_hp = e_hp - givenDamage
            if e_hp>0:
                room = room - 1
                
            #%% Blok şansına bağlı olarak alınan hasar hesaplanıyor ve alınan hasar candan düşüyor
            blockNum = random.randint(101)
            if afk==0:
                if blockNum>blockChance:
                    takenDamage = enemyDamage - bonus_defence
                    if takenDamage>0:
                        life = life - takenDamage
                    elif takenDamage<=0:                    
                        life = life
                        takenDamage = 0
                elif blockNum<=blockChance:
                    takenDamage = 0
                    life = life
                    ed_embed_up.add_field(name="Block!!!",value="Congratulations you have blocked the attack",inline=False)
                    await msg.edit(embed=ed_embed_up)
                    await asyncio.sleep(1)
            elif afk==1:
                takenDamage = e_a*2
                life = life - takenDamage
                afk = 0
                                
            #%% Son durumu göstermek için bir embed oluşturuyor
            ed_embed_up2 = discord.Embed(
            title = "Enter Dungeon",
            description = "You are against " + e_name + "\nWhat will you do?",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            ed_embed_up2.set_author(name=f"{author_name}\tRoom: {room}\t\t🔴")
            ed_embed_up2.set_footer(text="Usable Commands: 'Attack' and 'Defend'")       
            ed_embed_up2.set_image(url=enemy[5])
            ed_embed_up2.add_field(name="Your HP",value=life)
            ed_embed_up2.add_field(name="Enemy HP",value=e_hp)
            ed_embed_up2.add_field(name="Damages",value=f"Last Given Damage: {givenDamage}\nLast Taken Damage: {takenDamage}",inline=False)
            await msg.edit(embed=ed_embed_up2)
            await asyncio.sleep(2)
            
        if life<=0:            
            ed_embed_end = discord.Embed(
            title = "Enter Dungeon",
            description = "You Died. <:FeelsBatMan:815607995810840587>\nYour time will come, never give up fallen soldier.",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            ed_embed_end.set_author(name=f"{author_name}\tRoom: {room}")
            ed_embed_end.set_footer(text="Usable Commands: 'Attack' and 'Defend'")       
            ed_embed_end.set_image(url=enemy[5])
            ed_embed_end.add_field(name="Your HP",value=life)
            ed_embed_end.add_field(name="Enemy HP",value=e_hp)
            ed_embed_end.add_field(name="Damages",value=f"Last Given Damage: {givenDamage}\nLast Taken Damage: {takenDamage}",inline=False)
            ed_embed_end.add_field(name="Foundings",value=f"You have found {chests} chests\nYou have found {potions} potions.",inline=False)
            ed_embed_end.add_field(name="Points",value=f"You have gained {points} points.",inline=False)
            await msg.edit(embed=ed_embed_end)
        else:
            ed_embed_end = discord.Embed(
            title = "Enter Dungeon",
            description = "Congratulations you are able to walk away from this dungeon. <:EZ:815607997513728001>",
            colour = discord.Colour.from_rgb(255,255,0)
            )
            ed_embed_end.set_author(name=f"{author_name}\tRoom: {room}")
            ed_embed_end.set_footer(text="Usable Commands: 'Attack' and 'Defend'")
            ed_embed_end.set_image(url=enemy[5])
            ed_embed_end.add_field(name="Your HP",value=life)
            ed_embed_end.add_field(name="Enemy HP",value=e_hp)
            ed_embed_end.add_field(name="Damages",value=f"Last Given Damage: {givenDamage}\nLast Taken Damage: {takenDamage}",inline=False)
            ed_embed_end.add_field(name="Foundings",value=f"You have found {chests} chests\nYou have found {potions} potions.",inline=False)
            ed_embed_end.add_field(name="Points",value=f"You have gained {points} points.",inline=False)
            await msg.edit(embed=ed_embed_end)
        from leaderboard_test import pointadder_test
        pointadder_test(author_name,points)
            
                
                
                
        print("!enterdungeon used")
#%% Kodun "cog" (yan dosya) olarak çalışması için gerekiyor      
def setup(bot: commands.Bot):
    bot.add_cog(enterdungeon(bot))
    
#%% Reaksiyonlara cevap verebilir bunu kullanabilirsem

# sword = "<:pepeSword:815607996654288966>"
# shield = "<:peepoHide:847076616147435580>"
# await msg.add_reaction(sword)
# await msg.add_reaction(shield)

# @client.event
# async def on_reaction_add(reaction, author):
#     if author == ctx.author:
#         if str(reaction.emoji) == sword:
#             await msg.remove_reaction(sword,author)
#             await msg.add_reaction(sword)
#             print("sword")
#         elif str(reaction.emoji) == shield:
#             await msg.remove_reaction(shield,author)
#             await msg.add_reaction(shield)
#             print("shield")