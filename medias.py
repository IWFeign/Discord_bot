import numpy as np
# from replit import db

#%% Video Postlayan Kısım
videos = [
      "https://youtu.be/pM2nM-aqWHc","https://youtu.be/gjp4OQ2OPqA","https://youtu.be/QqDED66mjMQ","https://youtu.be/ZbprctBpKCo",
      "https://youtu.be/nDxHWSAL5p0","https://youtu.be/izLf-Xs_C-8","https://youtu.be/vM3Uku6kUfY","https://youtu.be/gKVy7YAPy6k"
    ]

def videoPoster():
    videoPick = videos[np.random.randint(len(videos))]
    return(videoPick)

def videoList():
    videolist = ["Lol türkiyenin gerçek hali v1: https://youtu.be/pM2nM-aqWHc",
                 "Lol türkiyenin gerçek hali v2: https://youtu.be/gjp4OQ2OPqA",
                 "Valo gerçek hali v1: https://youtu.be/QqDED66mjMQ",
                 "Valo gerçek hali v2: https://youtu.be/gKVy7YAPy6k",
                 "Furkan Kurum merminin tadına bakıyor: https://youtu.be/ZbprctBpKCo",
                 "😳: https://youtu.be/nDxHWSAL5p0",
                 "Furkan Kurum frag movie: https://youtu.be/izLf-Xs_C-8",
                 "Furkan Kurum Q basmıyor: https://youtu.be/vM3Uku6kUfY",
                 "Halısaha.exe not found.mp4: https://youtu.be/TZMPKzKqHgA"
        ]
    return(videolist)
#%% Videoları Güncelleyen Kısım
def videoAdder(video_link):
    if "videos" in db.keys():
        videos = db["videos"]
        videos.append(video_link)
        db["videos"] = videos
    else:
        db["videos"] = [video_link]

def videoRemover(index):
    videos = db["videos"]
    if len(videos)>index:
        del videos[index]
    db["videos"] = videos
#%% Ses Postlayan Kısım
sounds = [
      "Sıkıştım -Altaş: https://soundcloud.com/user-268499888/s-k-t-m-alta/s-d3ITIiAZZAR?si=0fd3eddaf07a4e7b86d844f7367a9450",
      "Satranç Anıları -Altaş&Emre: https://soundcloud.com/user-268499888/satran-an-lar-alta-emre/s-A62u5esLdwz?si=db0f5d88329a4acd9411aaf6a6406a9f",
      "Oğuz Abi Draveni -Emre: https://soundcloud.com/user-268499888/o-uz-abi-draveni-emre/s-9CcNnu9Bg9m?si=768ca74e5fa341edb0ad4f12a06b7392",
      "Top -Serkan: https://soundcloud.com/user-268499888/top-serkan/s-vg09OMud3Tu?si=89d16945640e4eff94f11f7cac03c977",
      "Serkan Abiyi Şişlemişler: https://soundcloud.com/user-268499888/serkan-abiyi-sislemisler/s-qD4Yt4OF53T?si=94017ce630bf46959a352639de652aef",
      "Ses Yapma -Pamuk: https://soundcloud.com/user-268499888/ses-yapma-pamuk/s-cdzqGg4yXGr?si=33ab1eaa371f45fe8ec8db3884e2db08",
      "Saldırı -Pamuk: https://soundcloud.com/user-268499888/sald-r-pamuk/s-GVMrNBarLZZ?si=1edceebe9ba44ba0a344afb8e262ddbc",
      "Böyle Yersin Kafana -Pamuk: https://soundcloud.com/user-268499888/boyle-yersin-kafana-pamuk/s-Kguhz5nGKVT?si=baff41e5da0142f4adbd0fd7fee2e799",
      "Adamlar Bana Girdi -Okan: https://soundcloud.com/user-268499888/adamlar-bana-girdi-okan/s-5xiNYDQndAw?si=b783fde46431433bb4114547e2885242",
      "Vurcaz -Furkan: https://soundcloud.com/user-268499888/vurcaz-furkan/s-uZXTIfzhQsg?si=d64c268b480442f19b69259773974513",
      "Tutacaklar -Furkan: https://soundcloud.com/user-268499888/tutacaklar-furkan/s-3GOZNvSADap?si=f5e2062987a54ffc981b7d1b9adb8269",
      "Körüklüyorum -Furkan: https://soundcloud.com/user-268499888/koerueklueyorum-furkan/s-Fy4MGKbeAWM?si=4fd6afa0655142b799b72eb00e77e34a",
      "Kör ol -Altaş: https://soundcloud.com/user-268499888/k-r-ol-alta/s-AHbDxXCmfu0?si=23ccd0e2e61b40fc9bf128006981899d",
      "Giriyorlar bana -Altaş: https://soundcloud.com/user-268499888/giriyorlar-bana-alta/s-Cf4P4DExrzV?si=b6d55d22381944ed91f688efd01ae3da",
      "Bana tten -Altaş: https://soundcloud.com/user-268499888/bana-gotten-altas/s-m4q7NsjcUnX?si=54f788a3e101434e8fe12b07a20775d0",
      "Adam bana girdi -Altaş: https://soundcloud.com/user-268499888/adam-bana-girdi-altas/s-bfj9swhGI7B?si=dcc0d28e1f4a4ee0b844e6004676401d",
      "Bana bi vursanız tten -Altaş: https://soundcloud.com/user-268499888/bana-bi-vursaniz-gotten-altas/s-rMelbp4325d?si=eefddd88c43f4ea7847a3da328874097",
      "Tten giriyorlar bize -Altaş: https://soundcloud.com/user-268499888/gotten-giriyolar-bize-altas/s-c8vNB5jphR5?si=90ae35f8bd6b4778b3099c2037446aaf",
      "Tten vursanıza -Altaş: https://soundcloud.com/user-268499888/gotten-vursaniza-altas/s-NMIvoP6oA8Z?si=eeac3c24458b4b359b3259ed895b2ed4",
      "İçime girdin -Altaş: https://soundcloud.com/user-268499888/icime-altas/s-5FjRJj6X8Yy?si=241bb1d0e4f544148475018fe9068f31",
      "Oğuza verdim -Altaş: https://soundcloud.com/user-268499888/oguza-verdim-altas/s-owp5kAoFaRg?si=0bc9059f40504252a7df3a460ef9bc00",
      "Pasif -Pamuk: https://soundcloud.com/user-268499888/pasif-pamuk/s-BObPkDkM3nK?si=ec4b405f0e6f4fa8b3cfa97e3ef79b58",
      "Emre dolandırıcı -Pamuk: https://soundcloud.com/user-268499888/emre-dolandirici-pamuk/s-uDSCB1VnwG4?si=d22a58c7a15d4ce1a19671ab99a0f46d",
      "Emreyle tanışma -Oğuz: https://soundcloud.com/user-268499888/emre-dolandirici-pamuk/s-uDSCB1VnwG4?si=d22a58c7a15d4ce1a19671ab99a0f46d",
      "Tten vurdu -Furkan: https://soundcloud.com/user-268499888/tten-vurdu-furkan/s-s4Cxh3ARXTv?si=e7541ce93e134146947db5acbef076df",
      "Ağzıma... -Furkan: https://soundcloud.com/user-268499888/agiza-alamaca-furkan/s-G5vBl6h1LDj?si=0e6de3ddbeb848a8a038062970521215",
      "Fizz cosplay -Aziz: https://soundcloud.com/user-268499888/fizz-aziz/s-obwzimm00GO?si=e3c08872ceab439cbc045278939cb9de",
      "Kalkmıyor -Atakan: https://soundcloud.com/user-268499888/kalkm-yor-atakan/s-KhoN6xiHZox?si=58c2b237059f4fcb859dc23e81718609",
      "Bülbül ötmüyor -Atakan: https://soundcloud.com/user-268499888/bulbul-otmuyo-atakan/s-ASeSW6TDjFz?si=9c4275ae479e4a5c8298193a2593d3d3",
      "Vur bana -Altaş: https://soundcloud.com/user-268499888/vur-bana-altas/s-RxDMclBnGY6?si=8d74520aec8a4347857e3f59adb3afd8",
      "Tten veresim geldi -Altaş: https://soundcloud.com/user-268499888/tten-veresim-geldi-altas/s-WY7Es3iKCOv?si=c4fc405cd385417f89f7d7a21c2cf72e",
      "Pasif -Altaş: https://soundcloud.com/user-268499888/pasif-altas/s-rDI3LTYVUFe?si=cc8fcdcc012d47d981cd8346a4cd4eb9",
      "Orospu oldum -Altaş: https://soundcloud.com/user-268499888/orospu-altas/s-2B5WPecKVo9?si=622b02ff62a148669010388fddba36c6"
    ]
def soundPoster():
    soundPick = sounds[np.random.randint(len(sounds))]
    return(soundPick)
