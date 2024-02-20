import sys
import subprocess
import requests
from fake_useragent import UserAgent

def getIdFromResponse(response):
    start = response.find(r'videoId\x22:\x22') + len(r'videoId\x22:\x22')
    end = response.find(r'\x22', start)
    return response[start:end]

def makeQuery(title, artist):
    return title.replace(' ', '+') + "+by+" + artist.replace(' ', '+')

def firstYouTubeID(title, artist):
    search_query = makeQuery(title, artist)
    url = "https://music.youtube.com/search?q=" + search_query
    response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    return getIdFromResponse(response.text)

def downloadAudio(id, outputDirectory, title, artist, logFile, commandFile):
    logFile.write("DOWNLOADING: " + title + artist + id + "\n")
    outputFile = outputDirectory + '/' + ''.join(title.split()) + '-' + \
                 ''.join(artist.split()) + '.%(ext)s'
    args = ['yt-dlp', '-f', 'bestaudio', '-o', outputFile, id]
    output = subprocess.run(args, stdout=commandFile, stderr=commandFile)
    if output.returncode != 0:
        logFile.write("FAILURE: " + title + artist + id + "\n")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 scraper.py <songListFile> <outputDirectory>")
        sys.exit(1)

    with open(sys.argv[1], "r") as songListFile:
        with open(sys.argv[2] + "/log.txt", "w") as logFile:
            with open(sys.argv[2] + "/commands.txt", "w") as commandFile:
                garbageFirstLine = songListFile.readline()
                for line in songListFile:
                    try:
                        title, artist = line.strip().split(",")
                        id = firstYouTubeID(title, artist)
                        downloadAudio(id, sys.argv[2], title, artist, logFile, commandFile)
                    except Exception as e:
                        logFile.write("EXCEPTION: " + title + artist + id + "\nException: " + str(Exception) + "\n")
