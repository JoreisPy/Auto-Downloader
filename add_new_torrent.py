import qbittorrentapi
import os

current_dir = os.getcwd()
downloads_folder = "/home/joreis/Downloads/"
anime_folder = "/home/joreis/Media/Anime"
series_folder = "/home/joreis/Media/Series"
movies_folder = "/home/joreis/Media/Movies"


## Client connection ##
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
    print(t_list)

    # for torrents in t_list:
    #    if torrents[1] == "Anime":


#move_torrents()
add_new_torrent(torrent_magnet = input("Enter torrent magnet link:"),torrent_category= input("Enter torrent category:"))

