# Auto-Renamer/File-Mover
This project aims to automate de file management after a download is completed. moving the complete download to its folder in plex midea library. if the folder doesnt exist, the script will create the directory before the move.

Requirements:

- It only works with Qbitorrent
- It depends on the user creating 2 categories in qbittorrent(Series and Movies)
- Every time the user starts a download it must state the category


Process:

- for Series the Script will create a Folder with the Series Name and Season number based on the torrent name with the help od PTN library and send the serie inside the Season folder.
- For Movies, will simple create a folder with the movie name and year and move the movie inside. 
- When the container is running, it will detect via a the qbitorrwnt API that the download is complete and start the process.
- The script checkes for torrents every minute
- In the end it deletes the torrent from the torrent list.

I am still in the learning process and the code might look bad, please be nice ;)

