from lxml import html
import urllib2
from bs4 import BeautifulSoup
import csv

'''
This function gets all tracks from a spotify emebed URL. Simply select to share
the Spotify playlist, and select to embed the playlist. Then use the URL that 
is embeded into the iFrame object. 

Pass that URL when this function is called as a string.
This function will return a multidimensional array with the song name located 
at index 0, and the artist at index 1.
Also, this prints all of the tracks out into the terminal

@param url: String, url of the Spotify playlist retrieved from the emebeded playlist
@param fullName: Array, Name of the song and the artist in an array
@param playlistArray: Array, all of the songs
'''
def getTracks(url):
    soup = BeautifulSoup(urllib2.urlopen(url), "lxml")
    playlistArray = []
    trackResult = soup.find_all("div", "track-row-info")
    for res in trackResult:
        #perform some string manipulation magic to format the strings in an array
        fullName = ''.join(s for s in res.text if ord(s)>31 and ord(s)<126).strip("                ").split("                                    ")
        print fullName
        playlistArray.append(fullName)
    return playlistArray
   
'''
This function takes an array, and converts that into a .csv file, which is then 
saved to disk

@param fileName: String, name of file to write
@param data: list of list of items
'''
def writeCSVFile(fileName, data, *permission, **kwpermission):
    myCSV = csv.writer(open(fileName, 'wb'), *permission, **kwpermission)
    for row in data:
        myCSV.writerow(row)

'''
This executes the 2 functions.
The result of getTracks is saved in playlist. Then the CSV file function is called
'''
playlist = getTracks("https://open.spotify.com/embed/user/indiefolkradio/playlist/37vt9W6xt5jsud9iaIMzeh")
writeCSVFile(r'test.csv', playlist)
