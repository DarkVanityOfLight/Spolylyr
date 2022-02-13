# Spolylyr
Spolylyr is a polybar module that displays the current lyrics for a song playing on spotify. For this to work you have to install the SpotifyLyricServer via Spicetify.

## How it works
Spolylyr uses Flasks SocketIO to recieve the lyrics and the current time. Flask is served with gunicorn and the gventlet web socket backend.
