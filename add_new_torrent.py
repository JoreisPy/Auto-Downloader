import qbittorrentapi
import os

current_dir = os.getcwd()
downloads_folder = "/home/joreis/Downloads/"
anime_folder = "/home/joreis/Media/Anime"
series_folder = "/home/joreis/Media/Series"
movies_folder = "/home/joreis/Media/Movies"

qbt_client = qbittorrentapi.Client(host='localhost', port=8080)

downloads_folder = "/home/joreis/Downloads/"

def add_new_torrent(torrent_magnet = None, torrent_category= None):
    
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)

    add_torrent = qbt_client.torrents_add(urls= torrent_magnet, save_path= downloads_folder, category = torrent_category )

    if add_torrent == "Ok.":
        print("torrent Added Successfuly")

add_new_torrent(torrent_magnet = input("Enter torrent magnet link:"),torrent_category= input("Enter torrent category:"))

