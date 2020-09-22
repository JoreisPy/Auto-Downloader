import qbittorrentapi

downloads_folder = "/Downloads"
anime_folder     = "/plex-media/Anime"
series_folder    = "/plex-media/Series"
movies_folder    = "/plex-media/Movies"
doc_folder       = "/plex-media/Documentaries"

qbt_client = qbittorrentapi.Client(host='192.168.0.164', port=8080, username='admin', password='adminadmin')
