import qbittorrentapi

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


move_torrents()