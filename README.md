# SpotifyToCSV
Converts the tracks in a Spotify Playlist to a CSV.
Just a little something I built to get all of the songs from a friends playlist.

<h1> Dependencies </h1>

This project uses <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"> BeautifulSoup v4.4.0</a> and Python 2.7.4. You must install BeautifulSoup before attempting to run the project. <br>
A simple:
<code>
sudo apt-get install python-bs4
</code>
or
<code>
pip install beautifulsoup4
</code>
should do the trick to install it.


<h1> Getting the playlist URL </h1>
First find the share button, here it is positioned in the top right corner.
<img src="https://github.com/ethanburrell/SpotifyToCSV/blob/master/Screenshots/SharePlaylist.png?raw=true" />
Then select the embed option (on the far right).
<img src="https://github.com/ethanburrell/SpotifyToCSV/blob/master/Screenshots/EmbedPlaylist.png?raw=true" />
Then the emebed code should be copied to your clipboard
<img src="https://raw.githubusercontent.com/ethanburrell/SpotifyToCSV/master/Screenshots/CopiedToClipboard.png" />
<br><br>
This is what was on my clipboard:
<code>
<iframe src="https://open.spotify.com/embed/user/indiefolkradio/playlist/37vt9W6xt5jsud9iaIMzeh"
              width="300" height="380" frameborder="0" allowtransparency="true"></iframe>
</code>
The URL you want to use is the source for the iFrame. Use the URL:
<code>
https://open.spotify.com/embed/user/indiefolkradio/playlist/37vt9W6xt5jsud9iaIMzeh
</code>
