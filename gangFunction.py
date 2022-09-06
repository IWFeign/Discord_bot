import pandas as pd
import numpy as np
import random
def yolkes(allyCount=1,enemyCount=1):
    if allyCount>10:
        allyCount = 10
    if enemyCount>10:
        enemyCount = 10
    enemyCountStart = enemyCount
    totPoliceBonus = 0;totSuccessBonus = 0;totMinMoney = 0;totMaxMoney = 0;totBucks = 0;rich = 0; old = 0; mOld = 0; lgPers = 0; nPers = 0;student = 0;keko = 0
    enemies = pd.DataFrame(columns=["Tip","MinPara","MaxPara","Banknot","Polis Bonusu","Başarı Bonusu"])
    while enemyCount>0:
        enemyCount -= 1
        personNum = np.random.randint(101)
        if personNum<=5:
            personType = [["Zengin",200,2000,200,10,0]]
        elif personNum>5 and personNum<=15:
            oldNum = np.random.randint(1,32)
            if oldNum==15:
                personType = [["Maaşını Yeni Çekmiş Yaşlı",2000,3000,200,0,20]]
            else:
                personType = [["Yaşlı",0,200,10,0,20]]
        elif personNum>15 and personNum<=50:
            personType = [["Güzel Giyimli",0,400,20,10,0]]
        elif personNum>50 and personNum<=80:
            personType = [["Normal Giyimli",0,100,20,10,0]]
        elif personNum>80 and personNum<=90:
            personType = [["Öğrenci",0,100,5,20,0]]
        elif personNum>90:
            personType = [["Keko",0,50,1,0,10]]
        personType = pd.DataFrame(personType,columns=["Tip","MinPara","MaxPara","Banknot","Polis Bonusu","Başarı Bonusu"])
        enemies = enemies.append(personType,ignore_index=True)
    
    for i in range(len(enemies)):
        totPoliceBonus += enemies["Polis Bonusu"][i]
        totSuccessBonus += enemies["Başarı Bonusu"][i]
        totMinMoney += enemies["MinPara"][i]
        totMaxMoney += enemies["MaxPara"][i]
        totBucks += enemies["Banknot"][i]
        enemyType = enemies["Tip"][i]
        if enemyType == "Zengin":
            rich += 1
        elif enemyType == "Maaşını Yeni Çekmiş Yaşlı":
            mOld += 1
        elif enemyType == "Yaşlı":
            old += 1
        elif enemyType == "Güzel Giyimli":
            lgPers += 1
        elif enemyType == "Normal Giyimli":
            nPers += 1
        elif enemyType == "Öğrenci":
            student += 1
        elif enemyType == "Keko":
            keko += 1

    string = f"{allyCount} kişilik bir grupla\n"
    if rich>0:
        strRich = f"{rich} zengin "
        string += strRich
    if mOld>0:
        strmOld = f"{mOld} maaşını yeni çekmiş "
        string += strmOld
    if old>0:
        strold = f"{mOld+old} yaşlı "
        string += strold
    if lgPers>0:
        strlgPers = f"{lgPers} güzel giyimli "
        string += strlgPers
    if nPers>0:
        strnPers = f"{nPers} normal giyimli "
        string += strnPers
    if student>0:
        strstudent = f"{student} öğrenci "
        string += strstudent
    if keko>0:
        strkeko = f"{keko} keko "
        string += strkeko    
        
    successBonus = totSuccessBonus/enemyCountStart; policeBonus = totPoliceBonus/enemyCountStart
    success = successChance(successBonus,allyCount,enemyCountStart)
    if success=="Başardı":
        policeBonus += 0
    else:
        policeBonus += 25
    
    caught = prisonChance(policeBonus)
    moneyFound = random.randrange(totMinMoney,totMaxMoney,totBucks)
    return(success,caught,moneyFound,string)

def prisonChance(policeBonus):
    policeNum = np.random.randint(101)
    if policeNum<20+policeBonus:
        caught = "Yakalandı"
    else:
        caught = "Kaçtı"
    return(caught)

def successChance(successBonus,allyCount,enemyCount):
    successNum = np.random.randint(101)
    difference = (allyCount-enemyCount)
    
    if difference<0:
        rate = 50-(2**-difference)
    else:
        rate = 50+(2**difference)
        
    if rate<=0:
        rate = 5
    elif rate>=100:
        rate = 95
        
    if successNum<rate:
        success = "Başardı"
    else:
        success = "Başaramadı"
    return(success)