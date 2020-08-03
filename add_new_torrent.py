import qbittorrentapi
import os
from qbt_config import qbt_client, downloads_folder

def add_new_torrent(torrent_magnet = None, torrent_category= None):
    
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)

    add_torrent = qbt_client.torrents_add(urls= torrent_magnet, save_path= downloads_folder, category = torrent_category )

    if add_torrent == "Ok.":
        print("torrent Added Successfuly")

add_new_torrent(torrent_magnet = input("Enter torrent magnet link:"),torrent_category= input("Enter torrent category:"))

