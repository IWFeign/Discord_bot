#%% Lol Takım Seçici
def valorantPickedTeam():
  import requests
  import pandas as pd
  import numpy as np

  valo_url = 'https://valorant.fandom.com/wiki/Agents'
  valo_html = requests.get(valo_url).content
  agentsData = pd.read_html(valo_html)

  agentsList = agentsData[-1]

  agents = agentsList.loc[4][1]
  valoPicks = agents.split("• ")

  Team = []
  agentCounter = 0

  while agentCounter<5:
      agentCounter = agentCounter+1
      agentPicker = valoPicks[np.random.randint(len(valoPicks))]
      Team.append(agentPicker)
      valoPicks.remove(agentPicker)
        
  return(Team)

#%% Lol Takım Seçici
def updateLol():
    import requests
    import pandas as pd
    from replit import db
    lol_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
    lol_html = requests.get(lol_url).content
    champsData = pd.read_html(lol_html)
    
    champsList = champsData[1]
    champs = champsList["Champion"]
    lolPicks = champs.values
    lolPicks = lolPicks.tolist()
    db['lolChamps'] = lolPicks
  
def lolPickedTeam():
    import numpy as np
    import pandas as pd
    from replit import db
    lolPicks = db['lolChamps']
    lolPicks = pd.Series(lolPicks)
    Team_lol = []
    champCounter = 0
    
    while champCounter<5:
      champCounter = champCounter+1
      champPicker = lolPicks[np.random.randint(len(lolPicks))]
      champPicker = champPicker.lower()
      champPicker = champPicker.replace("the"," the")
      #champPicker = champPicker[0]
      Team_lol.append(champPicker)
      lolPicks = lolPicks[lolPicks !=champPicker]
          
    return(Team_lol)