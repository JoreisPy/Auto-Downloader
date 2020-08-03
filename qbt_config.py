import qbittorrentapi

downloads_folder = "/home/joreis/Downloads/"
anime_folder     = "/home/joreis/Media/Anime"
series_folder    = "/home/joreis/Media/Series"
movies_folder    = "/home/joreis/Media/Movies"
doc_folder       = "/home/joreis/Media/Documentaries/"

qbt_client = qbittorrentapi.Client(host='localhost', port=8080)
