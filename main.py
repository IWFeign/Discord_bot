import discord
import os
from replit import db
from discord.ext import commands
import numpy as np
import pandas as pd
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix="!")
client.remove_command('help')
TOKEN = os.environ['TOKEN']

#%% Prints a message lets you understand bot is on
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#%%
client.load_extension('numberGuessingGame')
client.load_extension('hangmanBot')
#client.load_extension('enterdungeon')
client.load_extension('numberGuessingGame_test')
#client.load_extension('gang')
client.load_extension('droll')


#%% Help command
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author.id

    helpEmbed = discord.Embed(colour=discord.Colour.orange())
    helpEmbed.set_author(name="Help")
    helpEmbed.add_field(name="!valotakım",
                        value="Rastgele bir valorant takımı oluşturur",
                        inline=False)
    helpEmbed.add_field(name="!loltakım",
                        value="Rastgele bir lol takımı oluşturur",
                        inline=False)
    helpEmbed.add_field(name="!yazıtura", value="Yazı tura atar", inline=False)
    helpEmbed.add_field(
        name="!leaderboard",
        value=
        "Oyunlarda kazanılan puanlarla oluşan sıralamayı gösteren bir liste",
        inline=False)
    helpEmbed.add_field(
        name="!updateleaderboard",
        value="Leaderboarda isminizi yazdırmak için kullanmanız gereken komut",
        inline=False)
    helpEmbed.add_field(
        name="Oyunlar",
        value=
        "!guessgame: 0-100 aralığında seçilen sayının bilinmeye çalıştığı oyun\n!enterdungeon: Dungeonda maceraya çıktığınız bir oyun",
        inline=False)
    helpEmbed.add_field(name="!video",
                        value="Rastgele bir video paylaşır",
                        inline=False)
    helpEmbed.add_field(name="!ifşa",
                        value="Rastgele bir ses kaydı paylaşır",
                        inline=False)
    helpEmbed.add_field(
        name="!film",
        value="IMDB Top1000 listesinden rastgele bir film seçer",
        inline=False)

    await ctx.send(f'<@{author}>', embed=helpEmbed)


#%% Picks random valorant team
@client.command()
async def valotakım(ctx):
    from valorantTeamPickerOnline import valorantPickedTeam
    valorantTeam = valorantPickedTeam()
    await ctx.send(valorantTeam[0] + "\n" + valorantTeam[1] + "\n" +
                   valorantTeam[2] + "\n" + valorantTeam[3] + "\n" +
                   valorantTeam[4] + "\n")
    print("!valotakım used")


#%% Picks random lol team
@client.command()
async def loltakım(ctx):
    from valorantTeamPickerOnline import lolPickedTeam
    lolTeam = lolPickedTeam()
    await ctx.send(lolTeam[0] + "\n" + lolTeam[1] + "\n" + lolTeam[2] + "\n" +
                   lolTeam[3] + "\n" + lolTeam[4] + "\n")
    print("!lolotakım used")


@client.command()
async def updateloltakım(ctx):
    username = ctx.message.author.id
    if username == 142582012191047682:
        from valorantTeamPickerOnline import updateLol
        await ctx.send(
            "Lol şampiyonları güncelleniyor.  Bu işlem biraz uzun sürebilir.")
        await ctx.send("<:KEKWAIT:830964663188848690>")
        updateLol()
        await ctx.send("Lol şampiyonları güncellendi")
        await ctx.send("<:peepoHappy:815645629534437417>")
        print("!updateloltakım used")


#%% Heads or Tails
@client.command()
async def yazıtura(ctx):
    ht_chance = np.random.randint(2)
    if ht_chance == 0:
        await ctx.send("Yazı")
        time = str(datetime.now().time())
    else:
        await ctx.send("Tura")
        time = str(datetime.now().time())
    print(time)


#%% Posts random video
@client.command()
async def video(ctx):
    from medias import videoPoster
    video = videoPoster()
    await ctx.send(video)
    print("!video used")


#%% Posts video list
@client.command()
async def videolar(ctx):
    from medias import videoList
    videolar = videoList()

    videolarEmbed = discord.Embed(colour=discord.Colour.blue())
    videolarEmbed.set_author(name="Videolar")
    for video in videolar:
        videolarEmbed.add_field(name="-----", value=video, inline=False)

    await ctx.send(embed=videolarEmbed)
    print("!videolar used")


#%% Posts random voice recording
@client.command()
async def ifşa(ctx):
    from medias import soundPoster
    sound = soundPoster()
    await ctx.send(sound)
    print("!ifşa used")


#%% Collects Top 1000 movie data and picks random one
@client.command()
async def film(ctx):
    from movies import movie_picker
    movie = movie_picker()
    await ctx.send(movie[0][1] + " isimli film " + movie[0][2] +
                   " yılında vizyona girmiş " + movie[0][3] + " uzunluğunda " +
                   movie[0][4] + " türündedir. IMDB puanı " + movie[0][5] +
                   " olan film IMDB top 1000 listesinde " + movie[0][0] +
                   " sıradadır.")
    print("!film used")


@client.command()
async def updatefilm(ctx):
    username = ctx.message.author.id
    if username == 142582012191047682:
        from movies import movie_updater
        await ctx.send("Filmler güncelleniyor.  Bu işlem biraz uzun sürebilir."
                       )
        await ctx.send("<:KEKWAIT:830964663188848690>")
        movie_updater()
        await ctx.send("Filmler güncellendi")
        await ctx.send("<:peepoHappy:815645629534437417>")
        print("!updatefilm used")


#%% Leaderboard
@client.command()
async def leaderboard(ctx):
    leaderboard = db["leaderBoard"]
    leaderboard = pd.DataFrame(leaderboard,
                               columns=["İsim", "Puan", "Oynanan Oyun"])
    leaderboard = leaderboard.sort_values(by=["Puan"], ascending=False)

    lead_embed = discord.Embed(title="Leaderboard",
                               colour=discord.Colour.green())
    lead_embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/884176668971921422/906200901889437726/ss2.png"
    )
    lead_embed.set_image(
        url=
        "https://media.discordapp.net/attachments/884176668971921422/906200909065912420/s1.png"
    )
    lead_embed.add_field(name="İsim",
                         value=leaderboard["İsim"].to_string(index=False),
                         inline=True)
    lead_embed.add_field(name="Puan",
                         value=leaderboard["Puan"].to_string(index=False),
                         inline=True)
    lead_embed.add_field(
        name="Oynanan oyun",
        value=leaderboard["Oynanan Oyun"].to_string(index=False),
        inline=True)
    lead_embed.set_footer(
        text=
        "İsminizin bu listede yer alması için !updateleaderboard komutunu kullanmanız gerekmektedir"
    )

    await ctx.send(embed=lead_embed)
    print("!leaderboard used")


@client.command()
async def updateleaderboard(ctx):
    from leaderboard import update_leaderboard
    author = str(ctx.message.author)
    author = author.split("#")
    author = author[0]
    update_leaderboard(author)
    await ctx.send("leaderboard güncellendi")
    print("!updateleaderboard used")


@client.command()
async def resetleaderboard(ctx):
    from leaderboard import resetleaderboard
    author = str(ctx.message.author)
    if author == "AtakanTekatan#3654":
        resetleaderboard()
        await ctx.send("leaderboard resetlendi")
        print("!resetleaderboard used")
    else:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok.")


#%% Leaderboard test
@client.command()
async def leaderboard_test(ctx):
    leaderboard = db["leaderBoard_test"]
    leaderboard = pd.DataFrame(leaderboard,
                               columns=["İsim", "Puan", "Oynanan Oyun"])

    author = "Mahmut"
    new_member = {"İsim": author, "Puan": 100, "Oynanan Oyun": 1}
    leaderboard = leaderboard.append(new_member, ignore_index=True)
    author = "Mehmet"
    new_member = {"İsim": author, "Puan": 100, "Oynanan Oyun": 1}
    leaderboard = leaderboard.append(new_member, ignore_index=True)
    author = "Ahmet"
    new_member = {"İsim": author, "Puan": 200, "Oynanan Oyun": 1}
    leaderboard = leaderboard.append(new_member, ignore_index=True)
    leaderboard = leaderboard.sort_values(by=["Puan"], ascending=False)

    lead_embed = discord.Embed(title="Leaderboard",
                               colour=discord.Colour.green())
    lead_embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/884176668971921422/906200901889437726/ss2.png"
    )
    lead_embed.set_image(
        url=
        "https://media.discordapp.net/attachments/884176668971921422/906200909065912420/s1.png"
    )
    lead_embed.add_field(name="İsim",
                         value=leaderboard["İsim"].to_string(index=False),
                         inline=True)
    lead_embed.add_field(name="Puan",
                         value=leaderboard["Puan"].to_string(index=False),
                         inline=True)
    lead_embed.add_field(
        name="Oynanan oyun",
        value=leaderboard["Oynanan Oyun"].to_string(index=False),
        inline=True)
    lead_embed.set_footer(
        text=
        "İsminizin bu listede yer alması için !updateleaderboard komutunu kullanmanız gerekmektedir"
    )
    await ctx.send(embed=lead_embed)
    print("!leaderboard used")


@client.command()
async def updateleaderboard_test(ctx):
    from leaderboard_test import update_leaderboard_test
    author = str(ctx.message.author)
    author = author.split("#")
    author = author[0]
    update_leaderboard_test(author)
    await ctx.send("leaderboard güncellendi")
    print("!updateleaderboard used")


@client.command()
async def resetleaderboard_test(ctx):
    from leaderboard_test import resetleaderboard_test
    author = str(ctx.message.author)
    if author == "AtakanTekatan#3654":
        resetleaderboard_test()
        await ctx.send("leaderboard resetlendi")
        print("!resetleaderboard used")
    else:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok.")


@client.command()
async def database(ctx):
    from replit import db
    keys = db.keys()
    print(keys)


#%% dolar kurunu atıyor
@client.command()
async def dolar(ctx):
    def get_content(url):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="chromedriver",
                                  options=options)
        driver.get(url)
        return driver.page_source

    def parse(content):
        bs = BeautifulSoup(content, "html.parser")
        return bs.find("div",
                       attrs={
                           "class":
                           "tv-symbol-price-quote__value js-symbol-last"
                       }).text

    counter = 0
    while counter == 0:
        price = parse(
            get_content('https://tr.tradingview.com/symbols/USDTRY/'))
        price = str(price)
        if len(price) == 0:
            counter = 0
            print("it will try again")
        else:
            counter = 1
            await ctx.send("Dolar: " + str(price) +
                           "<:Sadge:815607998222172191>")


# @called_once_a_day.before_loop
# async def before():
#     await client.wait_until_ready()
#     print("Finished waiting")

# called_once_a_day.start()

try:
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
