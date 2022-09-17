# Spolylyr
Spolylyr is a polybar module that displays the current lyrics for a song playing on spotify. For this to work you have to install the SpotifyLyricServer via Spicetify.

## How it works
Spolylyr uses Flasks SocketIO to recieve the lyrics and the current time. Flask is served with gunicorn and the gventlet web socket backend.

## Installation
Download Spolylyr `git clone https://github.com/DarkVanityOfLight/Spolylyr.git`  
Copy it to your polybar config directory in my case that is:
`mv Spolylyr ~/.config/polybar/scripts`
Go to the Spolylyr directory
`cd ~/.config/polybar/scripts/Spolylyr`
Install the dependencies with `pipenv install`  
Now add a config section in a polybar ini file,
it should look smth like this:
```
[module/spolylyr]
type = custom/script
exec = scripts/Spolylyr/.venv/bin/gunicorn --worker-class geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b :5000 --log-level warning --chdir ~/.config/polybar/scripts/Spolylyr spolylyr:app
tail = true
```
