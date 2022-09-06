import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from replit import db

#%% Film listesini toplayan kısım
def movie_updater():
    urls = ['https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=101&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=201&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=301&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=401&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=501&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=601&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=701&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=801&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=901&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=1001&ref_=adv_nxt']
    
    movie_list = pd.DataFrame(index=range(1000),columns=["Ranking","Name","Year","Duration","Genre","IMDB Rating"])
    
    counter = 0
    while counter<999:
        if counter==0 and counter<=99:
            movie_url = urls[0]
        elif counter>99 and counter<=199:
            movie_url = urls[1]
        elif counter>199 and counter<=299:
            movie_url = urls[2]
        elif counter>299 and counter<=399:
            movie_url = urls[3]
        elif counter>399 and counter<=499:
            movie_url = urls[4]
        elif counter>499 and counter<=599:
            movie_url = urls[5]
        elif counter>599 and counter<=699:
            movie_url = urls[6]
        elif counter>699 and counter<=799:
            movie_url = urls[7]
        elif counter>799 and counter<=899:
            movie_url = urls[8]
        elif counter>899 and counter<=999:
            movie_url = urls[9]
    
        movie_html = requests.get(movie_url)
        bs = BeautifulSoup(movie_html.content, "html.parser")
        top1000_data = bs.find("div",{"class":"lister-list"})
    
        for movies in top1000_data.find_all("div","lister-item-content"):
            ranking = movies.find("span",attrs="lister-item-index unbold text-primary").text
            name = movies.find("a",href=re.compile("^/title/")).text
            year = movies.find("span",attrs = {"class":"lister-item-year text-muted unbold"}).text
            duration = movies.find("span",attrs = {"class":"runtime"}).text
            genre = movies.find("span",attrs = {"class":"genre"}).text
            genre = genre.replace(" ","")
            genre = genre.replace("\n","")
            rating = movies.find("div","inline-block ratings-imdb-rating").text
            rating = rating[2]+rating[3]+rating[4]
            movie_list["Ranking"][counter] = ranking
            movie_list["Name"][counter] = name
            movie_list["Year"][counter] = year
            movie_list["Duration"][counter] = duration
            movie_list["Genre"][counter] = genre
            movie_list["IMDB Rating"][counter] = rating
            counter = counter + 1
            
    
    #if "movieList" in db.keys():
    #  movie_list_update = db["movieList"]
    #  del movie_list_update
    #  db["movieList"] = movie_list
    #else:
    movie_list = movie_list.values.tolist()
    db["movieList"] = movie_list

#%% Film seçen kısım
def movie_picker():
    movie_list = db["movieList"]
    movie_list = pd.DataFrame(movie_list,columns=["Ranking","Name","Year","Duration","Genre","IMDB Rating"])
    movie_number = np.random.randint(len(movie_list["Ranking"]))
    picked_movie = movie_list.loc[[movie_number]]
    picked_movie = picked_movie.astype(str).values.tolist()
    return picked_movie