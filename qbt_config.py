import qbittorrentapi

downloads_folder = "/home/joreis/Downloads"
anime_folder     = "/home/joreis/plex-media/Anime"
series_folder    = "/home/joreis/plex-media/Series"
movies_folder    = "/home/joreis/plex-media/Movies"
doc_folder       = "/home/joreis/plex-media/Documentaries"

qbt_client = qbittorrentapi.Client(host='192.168.0.164', port=8080, username='admin', password='1ns2deout')
