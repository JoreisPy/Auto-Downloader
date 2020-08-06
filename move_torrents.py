import qbittorrentapi
import PTN
from qbt_config import qbt_client, downloads_folder, movies_folder, series_folder, anime_folder, doc_folder
import os

current_dir = os.getcwd()

def move_torrents():
    all_torrents = qbt_client.torrents_info()

    t_names       = []   #0
    t_category    = []   #1
    t_amount_left = []   #2

    for torrent in all_torrents:
        if torrent.amount_left == 0:
            t_names.append(torrent.name)
            t_category.append(torrent.category)
            t_amount_left.append(torrent.amount_left)

    t_list = list(zip(t_names,t_category,t_amount_left))
    #print(t_list)

##  Those lists contain the file name and the title of the show/movie/anime/doc ## 
    anime_title     = []
    anime_file_name = []
    
    serie_title     = []
    serie_file_name = []
    serie_season    = []
    serie_episode   = []
    

    movie_title     = []
    movie_file_name = []

    doc_title       = []
    doc_file_name   = []


    for torrents in t_list:
        if torrents[1] == "Anime":
            parsed_torrents = PTN.parse(torrents[0])
            anime_title.append(parsed_torrents['title'])
            anime_file_name.append(torrents[0])

    
        if torrents[1] == "Movies":
            parsed_torrents = PTN.parse(torrents[0])
            movie_title.append(parsed_torrents['title'])
            movie_file_name.append(torrents[0])


        if torrents[1] == "Series":
            parsed_torrents = PTN.parse(torrents[0])
            serie_title.append(parsed_torrents['title'])
            serie_season.append(parsed_torrents['season'])
            serie_episode.append(parsed_torrents['episode'])
            serie_file_name.append(torrents[0])

        
        if torrents[1] == "Documentary":
            parsed_torrents = PTN.parse(torrents[0])
            doc_title.append(parsed_torrents['title'])
            doc_file_name.append(torrents[0])



    anime_list  = list(zip(anime_title, anime_file_name))
    series_list = list(zip(serie_title,serie_season, serie_episode, serie_file_name))
    docs_list   = list(zip(doc_title, doc_file_name))
    movies_list = list(zip(movie_title, movie_file_name))

    print(series_list)
    
    for files in movies_list:
      os.rename(downloads_folder + "/" + files[1], movies_folder + "/" + files[0] )

    for files in series_list:
        os.mkdir(series_folder + "/" + files[0])
        os.mkdir(series_folder + "/" + "season " + files[1])


        
        #os.rename(downloads_folder + "/" + files[3])

move_torrents()