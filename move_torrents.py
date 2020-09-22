#!/usr/bin/python3

import qbittorrentapi
import PTN
from qbt_config import qbt_client, downloads_folder, movies_folder, series_folder, anime_folder, doc_folder
import os
import schedule
from time import sleep
import logging
import shutil

logging.basicConfig(filename='torrent_mover.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S' )
#logging.info("script started")

def move_torrents():
    all_torrents = qbt_client.torrents_info()
    #print(all_torrents)

    t_names       = []   #0
    t_category    = []   #1
    t_amount_left = []   #2
    t_hash        = []   #3

    for torrent in all_torrents:
        if torrent.amount_left == 0:
            t_names.append(torrent.name)
            t_category.append(torrent.category)
            t_amount_left.append(torrent.amount_left)
            t_hash.append(torrent.hash)

    t_list = list(zip(t_names,t_category,t_amount_left,t_hash))
    #print(t_list)

    #Those lists contain the file name and the title of the show/movie/anime/doc ##
    anime_title     = []
    anime_file_name = []
    anime_hash      = []

    serie_title     = []
    serie_file_name = []
    serie_season    = []
    serie_episode   = []
    serie_hash      = []

    movie_title     = []
    movie_file_name = []
    movie_hash      = []

    doc_title       = []
    doc_file_name   = []
    doc_hash        = []


    for torrents in t_list:

        if torrents[1] == "Anime":
            parsed_torrents = PTN.parse(torrents[0])
            anime_title.append(parsed_torrents['title'])
            anime_file_name.append(torrents[0])
            anime_hash.append(torrents[3])

        if torrents[1] == "Movies":
            parsed_torrents = PTN.parse(torrents[0])
            movie_title.append(parsed_torrents['title'])
            movie_file_name.append(torrents[0])
            movie_hash.append(torrents[3])

        if torrents[1] == "Series":
            parsed_torrents = PTN.parse(torrents[0])
            serie_title.append(parsed_torrents['title'])
            serie_season.append(parsed_torrents['season'])
            serie_episode.append(parsed_torrents['episode'])
            serie_file_name.append(torrents[0])
            serie_hash.append(torrents[3])

        if torrents[1] == "Documentary":
            parsed_torrents = PTN.parse(torrents[0])
            doc_title.append(parsed_torrents['title'])
            doc_file_name.append(torrents[0])
            doc_hash.append(torrents[3])

   
    anime_list  = list(zip(anime_title, anime_file_name,anime_hash))
    series_list = list(zip(serie_title,serie_season, serie_episode, serie_file_name,serie_hash))
    docs_list   = list(zip(doc_title, doc_file_name,doc_hash))
    movies_list = list(zip(movie_title, movie_file_name,movie_hash))

    #print(anime_list)
    #print("............")
    #print(series_list)
    # print("............")
    # print(docs_list)
    #print("............")
    #print(movies_list)



    for files in movies_list:

        try:
            #os.rename(downloads_folder + "/" + files[1], movies_folder + "/" + files[0] )
            shutil.move(downloads_folder + "/" + files[1], movies_folder + "/" + files[0] )
            print("Movie" + files[0] + " was moved to " + movies_folder)
            logging.info("Movie" + files[0] + " was moved to " + movies_folder)

            qbt_client.torrents_delete(torrent_hashes=str(files[2]), delete_files= False)
            print("torrent" + files[0] + "was deleted")
            logging.info("torrent" + files[0] + "was deleted")

        except OSError as err:
            print(err)
            logging.info(err)


    for files in series_list:

         try:
            os.mkdir(series_folder + "/" + files[0])
            os.mkdir(series_folder + "/" + files[0] + "/" "season " + str(files[1]))
            #os.rename(downloads_folder + "/" + files[3], series_folder + "/" + files[0] + "/" "season " + str(files[1]) + "/" + files[3])
            shutil.move(downloads_folder + "/" + files[3], series_folder + "/" + files[0] + "/" "season " + str(files[1]) + "/" + files[3])
            print("Serie" + files[0] + " was moved to " + series_folder)
            logging.info("Serie" + files[0] + " was moved to " + series_folder)

            qbt_client.torrents_delete(torrent_hashes=str(files[4]), delete_files= False)
            print("torrent " + files[0] + " was deleted")
            logging.info("torrent " + files[0] + " was deleted")

         except OSError as err:
            print(err)
            logging.info(err)

            #os.rename(downloads_folder + "/" + files[3], series_folder + "/" + files[0] + "/" "season " + str(files[1]) + "/" + files[3])
            shutil.move(downloads_folder + "/" + files[3], series_folder + "/" + files[0] + "/" "season " + str(files[1]) + "/" + files[3])
            print("Serie" + files[0] + " was moved to " + series_folder)
            logging.info("Serie" + files[0] + " was moved to " + series_folder)

            qbt_client.torrents_delete(torrent_hashes=str(files[4]), delete_files= False)
            print("torrent " + files[0] + " was deleted")
            logging.info("torrent " + files[0] + " was deleted")
            

while True:
    move_torrents()
    sleep(60)
