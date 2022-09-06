import pandas as pd
from replit import db
#%% Leaderboard oluşturuluyor
def update_leaderboard(author):
    if "leaderBoard" in db.keys():
        leaderBoard = db["leaderBoard"]
        leaderBoard = pd.DataFrame(leaderBoard,columns=["İsim","Puan","Oynanan Oyun"])
    else:
        leaderBoard = pd.DataFrame(columns=["İsim","Puan","Oynanan Oyun"])
        leaderBoard_db = leaderBoard.values.tolist()
        db["leaderBoard"] = leaderBoard_db

    # %% Leaderboarda isim ekliyor
    member = leaderBoard.loc[leaderBoard.İsim==author]
    member = member.values.tolist()
    if member == []:
        new_member = {"İsim":author,"Puan":0,"Oynanan Oyun":0}
        leaderBoard = leaderBoard.append(new_member,ignore_index=True)
        leaderBoard = leaderBoard.values.tolist()
        db["leaderBoard"] = leaderBoard
    else:
        member = member

    #%% Puan ekleyen ve oynanan oyunu arttıran kısım
def pointadder(author,points):
    leaderBoard = db["leaderBoard"]
    leaderBoard = pd.DataFrame(leaderBoard,columns=["İsim","Puan","Oynanan Oyun"])
    member = leaderBoard.loc[leaderBoard.İsim==author]
    member = member.values.tolist()
    member[0][1] = member[0][1] + points
    member[0][2] = member[0][2] + 1
    leaderBoard.loc[leaderBoard.İsim==author] = member
    leaderBoard = leaderBoard.values.tolist()
    db["leaderBoard"] = leaderBoard

def resetleaderboard():
    leaderBoard = pd.DataFrame(columns=["İsim","Puan","Oynanan Oyun"])
    leaderBoard_db = leaderBoard.values.tolist()
    db["leaderBoard"] = leaderBoard_db