from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import json

class LyricSyncer:
    def __init__(self):
        self.lyrics = []
        self.time = 0
        self.currentLine = {"time": -1, "words": {"string": ""}}
        self.isSynced = False
        self.availableLyrics = False

    def update_time(self, time):
        if self.time != time:
            self.time = time
            self.update_current_line()

    def update_current_line(self):
        newLine = None
        if self.isSynced:
            for line in self.lyrics:
                if self.time >= line["time"]:
                    newLine = line
                else:
                    break
        else:
            newLine = self.stringify_lyrics()

        if newLine and newLine != self.currentLine:
            self.currentLine = newLine
            print(self.stringify_current_line())

    def stringify_lyrics(self):

        if not self.availableLyrics:
            return None

        lines = []
        for line in self.lyrics:
            line = "".join([word["string"] for word in line["words"]])
            lines.append(line)

        return "\n".join(lines)

    def stringify_current_line(self):

        if not self.currentLine:
            return "There is no active lyric line"
        
        elif self.isSynced:
            words =[]
            for word in self.currentLine["words"]:
                words.append(word["string"])

            return " ".join(words)
        else:
            return self.stringify_lyrics()



    def update_lyrics(self, lyrics):
        if lyrics != self.lyrics:
            if not lyrics:
                self.isSynced = False 
                self.availableLyrics = False 

            elif not lyrics[0].get("time", None):
                self.isSynced = False
                self.availableLyrics = True
                self.lyrics = lyrics
            
            else:
                self.isSynced = True
                self.availableLyrics = True
                self.lyrics = lyrics

            self.currentLine = None

lyric_syncer = LyricSyncer()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="https://xpui.app.spotify.com")

@socketio.on("connect")
def con():
    print("Connect")

@socketio.on("time-stamp")
def handle_time_stamp(time_stamp):
    pass

@socketio.on("lyrics")
def handle_lyrics(lyrics):
    lyricLines = json.loads(lyrics)["lyrics"]
    lyric_syncer.update_lyrics(lyricLines)

@socketio.on("time")
def handle_time(time):
    lyric_syncer.update_time(time)


if __name__ == "__main__":
    socketio.run(app)
