from discord.ext import commands
from main import client
import asyncio
import discord
import pandas as pd
from replit import db
import datetime

#%% Help
class ganghelp(commands.Cog, name="ganghelp"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def ganghelp(self,ctx):
        ganghelpEmbed = discord.Embed(
        title = "Çete Komutları",
        colour = discord.Colour.from_rgb(141,123,103)
        )
        ganghelpEmbed.add_field(name="Komutlar",value="""creategang: Bir çete oluşturmanızı sağlar
                                changegangname: Çetenizin ismini değiştirmenizi sağlar
                                ganglist: Oluşturulmuş tüm çetelerin listesini görmenizi sağlar
                                gangaction: Çetenizle kirli işlere bulaşmanızı sağlar                                
                                """)
        ganghelpEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884176668971921422/913156816911872030/pngwing.com_1.png")
        await ctx.send(embed=ganghelpEmbed)
        
#%% cooldown & para
class cooldown(commands.Cog, name="cooldown"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def cooldown(self,ctx):
        if ctx.message.author.id==142582012191047682:
            cooldown_db = []
            db["cooldown"] = cooldown_db
            await ctx.send("Cooldownlar sıfırlandı")
            
class addpara(commands.Cog, name="addpara"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def addpara(self,ctx):
        if ctx.message.author.id==142582012191047682:
            author = str(ctx.message.author)
            author = author.split("#")
            author = author[0]
            gangs_db = db["gangs"]
            gangs = pd.DataFrame(gangs_db,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
            member = gangs.loc[gangs.Lider==author]
            gangs.drop(gangs.index[gangs["Lider"]==author],axis=0,inplace=True)
            member["Para"] += 5000
            gangs = gangs.append(member,ignore_index=True)
            gangs = gangs.values.tolist()
            db["gangs"] = gangs
            await ctx.send("Para eklendi")

#%% gang oluşturuyor
class creategang(commands.Cog, name="creategang"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def creategang(self,ctx):
        author_name = ctx.message.author.id
        author = str(ctx.message.author)
        author = author.split("#")
        author = author[0]

        if "gangs" in db.keys():
            gangs_db = db["gangs"]
            gangs = pd.DataFrame(gangs_db,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
        else:
            gangs = pd.DataFrame(columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
            gangs_db = gangs.values.tolist()
            db["gangs"] = gangs_db
        
        member = gangs.loc[gangs.Lider==author]
        member = member.values.tolist()
        if member == []:
            try:
                await ctx.send("Çetenizin ismini girin")
                gang_name = await client.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 30)
                try: await gang_name.delete()
                except Exception: pass
                gang_name = str(gang_name.content)
            except asyncio.TimeoutError:
                await ctx.send("Zamanında cevap vermediniz çetenizi tekrar kurmayı deneyin.")                
            new_gang = {"Çete İsim":gang_name,"Lider":author,"Para":0,"Çete Üye Sayısı":1}
            gangs = gangs.append(new_gang,ignore_index=True)
            gangs = gangs.values.tolist()
            db["gangs"] = gangs
            await ctx.send(f"<@{author_name}> '{gang_name}' isimli çeteyi kurdu.")
        else:
            await ctx.send("Halihazırda bir çeteye sahipsiniz!!!") 
        
#%% gang listesini paylaşıyor
class ganglist(commands.Cog, name="ganglist"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def ganglist(self,ctx):
        gangs_db = db["gangs"]
        gangs = pd.DataFrame(gangs_db,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
        gangs = gangs.sort_values(by=["Para"],ascending=False)
        gangEmbed = discord.Embed(
            title = "Çetelerin Listesi",
            colour = discord.Colour.from_rgb(141,123,103)
            )
        gangEmbed.set_image(url="https://cdn.discordapp.com/attachments/884176668971921422/909879920849731614/ganglist.png")
        gangEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884176668971921422/909877752113532928/hat.png")
        gangEmbed.add_field(name="Çete İsim",value = gangs["Çete İsim"].to_string(index=False),inline=True)
        gangEmbed.add_field(name="Lider",value = gangs["Lider"].to_string(index=False),inline=True)
        gangEmbed.add_field(name="Para (₺)",value = gangs["Para"].to_string(index=False),inline=True)
        # gangEmbed.add_field(name="Çete Üye Sayısı",value = gangs["Çete Üye Sayısı"].to_string(index=False),inline=True)
        await ctx.send(embed=gangEmbed)
        
#%% gang listesini sıfırlıyor
class resetgang(commands.Cog, name="resetgang"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def resetgang(self,ctx):
        if ctx.message.author.id == 142582012191047682:
            gangs = pd.DataFrame(columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
            gangs_db = gangs.values.tolist()
            db["gangs"] = gangs_db
            await ctx.send("Çeteler sıfırlandı.")
        else:
            await ctx.send("Bu komutu kullanacak yetkiye sahip değilsiniz.")

#%% gang ismini değiştiriyor
class changegangname(commands.Cog, name="changegangname"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def changegangname(self,ctx):
        author_name = ctx.message.author.id
        author = str(ctx.message.author)
        author = author.split("#")
        author = author[0]
        gangs_db = db["gangs"]
        gangs = pd.DataFrame(gangs_db,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
        member = gangs.loc[gangs.Lider==author]
        member = member.values.tolist()
        if member == []:
            await ctx.send("Bir çeteye sahip değilsiniz.")
        else:
            try:
                await ctx.send("Çetenizin yeni ismini girin")
                gangName = await client.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 30)  
                try: await gangName.delete()
                except Exception: pass
                gangs.drop(gangs.index[gangs["Lider"]==author],axis=0,inplace=True)
                oldGangName = member[0][0]                          
                gangName = str(gangName.content)                
            except asyncio.TimeoutError:
                await ctx.send("Zamanında cevap vermediniz, çetenizin ismini tekrar değiştirmeyi deneyin.")                
            member[0][0] = gangName
            member = pd.DataFrame(member,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
            gangs = gangs.append(member,ignore_index=True)
            gangs = gangs.values.tolist()
            db["gangs"] = gangs
            await ctx.send(f"<@{author_name}> '{oldGangName}' isimli çetesinin ismini '{gangName}' olarak değiştirdi.")

#%% çeteye insan ekliyor
class addmember(commands.Cog, name="addmember"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def addmember(self,ctx):
        author = str(ctx.message.author)
        author = author.split("#")
        author = author[0]
        gangs_db = db["gangs"]
        gangs = pd.DataFrame(gangs_db,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
        member = gangs.loc[gangs.Lider==author]
        
        memberEmbed = discord.Embed(
            title = f"{(member['Çete İsim'].to_string(index=False))} isimli çetenize kaç adam almak istersiniz?",
            colour = discord.Colour.from_rgb(141,123,103)
            )
        memberEmbed.add_field(name="Komut kullanımı",value="Çetenize eklemek istediğiniz insan sayısını chate yazın. İnsan başına 5000₺ ödemeniz gerekmektedir.")
        msg = await ctx.send(embed=memberEmbed)
        
        memberEdEmbed = discord.Embed(
            title = f"{(member['Çete İsim'].to_string(index=False))} isimli çetenize kaç adam almak istersiniz?",
            colour = discord.Colour.from_rgb(141,123,103)
            )
        
        try:
            memberNumber = await client.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 30)
            try: await memberNumber.delete()
            except Exception: pass
            memberNumber = int(memberNumber.content)
            if int(member["Para"])>=(5000*memberNumber):
                gangs.drop(gangs.index[gangs["Lider"]==author],axis=0,inplace=True)
                member["Çete Üye Sayısı"] += memberNumber
                member["Para"] -= 5000*memberNumber
                gangs = gangs.append(member,ignore_index=True)
                gangs = gangs.values.tolist()
                db["gangs"] = gangs
                memberEdEmbed.add_field(name="Yeni Üye",value=f"{(member['Çete İsim'].to_string(index=False))} isimli çetenizin artık {(member['Çete Üye Sayısı'].to_string(index=False))} üyesi var.")                
            else:
                memberEdEmbed.add_field(name="Para Eksik",value=f"{(member['Çete İsim'].to_string(index=False))} isimli çetenizin {memberNumber} üye alacak parası yok.\n{5000*memberNumber}₺'ye ihtiyacınız var.")
            await msg.edit(embed=memberEdEmbed)
        except asyncio.TimeoutError:
            memberEdEmbed.add_field(name="Zaman aşımı!!!",value="Zamanında yanıt vermediniz. Komutu tekrar kullanmayı denyin.")
            await msg.edit(embed=memberEdEmbed)
        
#%%        
class gangaction(commands.Cog, name="gangaction"):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def gangaction(self,ctx):
        author_id = ctx.message.author.id
        author = str(ctx.message.author)
        author = author.split("#")
        author = author[0]
        gangs_db = db["gangs"]
        gangs = pd.DataFrame(gangs_db,columns=["Çete İsim","Lider","Para","Çete Üye Sayısı"])
        member = gangs.loc[gangs.Lider==author]
        gangs.drop(gangs.index[gangs["Lider"]==author],axis=0,inplace=True)
        cdAuthor = []
        print(cdAuthor)
        cooldown = db["cooldown"]
        for i in range(len(cooldown)):
            if cooldown[i][0] == author_id:
                cdAuthor = cooldown[i]
                cdTime = cdAuthor[1]
                cdTime = datetime.datetime.strptime(cdTime,"%Y-%m-%d %H:%M:%S")
                print(cdAuthor)
                cooldown.pop(i)
                break
        print(cdAuthor)
        currenttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        currenttime = datetime.datetime.strptime(currenttime,"%Y-%m-%d %H:%M:%S")
        addCt = datetime.timedelta(hours = 3)
        currenttime += addCt
        
        actionsEmbed = discord.Embed(
            title = f"{member['Çete İsim'].to_string(index=False)} isimli çetenizle alacağınız aksiyonu chate yazın!!!",
            colour = discord.Colour.from_rgb(141,123,103)
            )
        actionsEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884176668971921422/911279229918904350/dice.png")
        actionsEmbed.add_field(name="Aksiyonların kullanımı", value="Alınacak aksiyonu yazdıktan sonra bir boşluk bırakarak kaç kişiyle o işi yapmak istediğinizi yazın, bazı aksiyonlarda karşınızda kaç kişilik bir grubun olacağını da seçmeniz gerekebilir Örn: Yolkes 6 3",inline=False)
        actionsEmbed.add_field(name="Alınabilecek aksiyonlar",value="""YOLKES: Yolda önünü kestiğiniz insanların parasını almayı deneyin. Bu eylemi en fazla 10'a 10 olacak şekilde gerçekleştirebilirsiniz.\n
                               KAPKAÇ: İnsanların çantasını çalmaya çalışın. Bu eylemi (2-5) kişilik bir grupla 1 kişiye karşı gerçekleştirebilirisiniz.
                               """)
        msg = await ctx.send(embed=actionsEmbed)
                               
        actionsEdEmbed = discord.Embed(
            title = f"{member['Çete İsim'].to_string(index=False)} isimli çetenizle alacağınız aksiyonu chate yazın!!!",
            colour = discord.Colour.from_rgb(141,123,103)
            )
        actionsEdEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884176668971921422/911279229918904350/dice.png")
        
        allyCount = 1
        enemyCount = 1
        if len(cdAuthor)==0 or currenttime>=cdTime:
            try:
                actionMSG = await client.wait_for('message', check=lambda message: message.author == ctx.author,timeout = 60)
                try: await actionMSG.delete()
                except Exception: pass
                print(cooldown)
                actionMSG = str(actionMSG.content)
                actionMSG = actionMSG.lower()
                actionMSG = actionMSG.split(" ")
                action = actionMSG[0]
                allyCount= int(actionMSG[1])
                enemyCount = int(actionMSG[2])
                
                if action == "yolkes":
                    from gangFunction import yolkes
                    if allyCount>int(member["Çete Üye Sayısı"].values):
                        allyCount = int(member["Çete Üye Sayısı"].values)
                        
                    success,caught,moneyFound,string = yolkes(allyCount,enemyCount)
                    actionsEdEmbed.add_field(name="Karşı Karşıya Gelen Gruplar",value=string,inline=False)
                    if success == "Başardı" and caught == "Kaçtı":
                        actionsEdEmbed.add_field(name="Başardın ve Kaçtın!!!",value=f"Yolunu kestiğin insanlardan {moneyFound}₺ çalmayı başardın ve polis seni yakalayamadı.")
                        member["Para"] += moneyFound 
                        hours = 1
                    elif success == "Başaramadı" and caught == "Kaçtı":
                        actionsEdEmbed.add_field(name="Başaramadın ve Kaçtın!!!",value="Yolunu kestiğin insanlardan para almayı başaramadın fakat polis seni yakalayamadı.")
                        hours = 1
                    elif success == "Başardı" and caught == "Yakalandı":
                        actionsEdEmbed.add_field(name="Başardın ve Yakalandın!!!",value=f"Yolunu kestiğin insanlardan {moneyFound}₺ çalmayı başardın fakat çok geçmeden polis seni yakaladı ve çaldığın paraya el koydu.")
                        hours = 3
                    elif success == "Başaramadı" and caught == "Yakalandı":
                        actionsEdEmbed.add_field(name="Başaramadın ve Yakalandın!!!",value="Yolunu kestiğin insanlardan para almayı başaramadın ve kaçamadan polis seni yakaladı.")
                        hours = 3
                    gangs = gangs.append(member,ignore_index=True)
                    gangs = gangs.values.tolist()
                    db["gangs"] = gangs
                    
                    addHours = datetime.timedelta(hours = hours)
                    future = currenttime + addHours
                    futurestr = str(future)
                    futurestr = futurestr.split(".")
                    futurestr = futurestr[0]
                    gangsCD = [author_id,futurestr]
                    cooldown.append(gangsCD)
                    print(cooldown)
                    db['cooldown'] = cooldown
                    actionsEdEmbed.add_field(name="Cooldown",value=f"Bu komutu tekrar şu tarihte kullanabilirsiniz:\n{gangsCD[1]}",inline=False)
                    await msg.edit(embed=actionsEdEmbed)
                    print("yolkes used")                        
            except asyncio.TimeoutError:
                actionsEdEmbed.add_field(name="Zaman Aşımı",value="Zamanında yanıt vermediğiniz için komut zaman aşımına uğradı tekrar deneyin.",inline=False)
                await msg.edit(embed=actionsEdEmbed)
                print("yolkes used")
                
        else:
            actionsEdEmbed.add_field(name="Bu komut bekleme süresinde",value=f"Bu komutu kullanmadan önce şu tarihe kadar beklemelisiniz:\n{cdAuthor[1]}",inline=False)
            await msg.edit(embed=actionsEdEmbed)
            print("yolkes used")
        
#%% sets up commands
def setup(bot: commands.Bot):
    bot.add_cog(ganghelp(bot))
    bot.add_cog(creategang(bot))
    bot.add_cog(resetgang(bot))
    bot.add_cog(ganglist(bot))
    bot.add_cog(changegangname(bot))
    bot.add_cog(gangaction(bot))
    bot.add_cog(cooldown(bot))
    bot.add_cog(addpara(bot))
    bot.add_cog(addmember(bot))