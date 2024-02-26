import sys
import os
import subprocess    

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 converter.py <songListFile> <songDirectory>")
        sys.exit(1)

    with open(sys.argv[1], "r") as songListFile:
        output = subprocess.run(["mkdir", sys.argv[2] + "/converted"])
        with open(sys.argv[2] + "/converted/log.txt", "a") as logFile:
            with open(sys.argv[2] + "/converted/commands.txt", "a") as commandFile:
                logFile.write("LOG RUN START\n")
                commandFile.write("COMMAND RUN START\n")
                garbageFirstLine = songListFile.readline()
                for line in songListFile:
                    try:
                        title, artist = line.strip().split(",")
                        title = ''.join(title.split())
                        artist = ''.join(artist.split())
                        logFile.write("CONVERTING: " + title + artist + "\n")
                        args = ['ffmpeg', '-i', sys.argv[2] + '/' + title + '-' + artist + '.*', sys.argv[2] + '/converted/' + title + '-' + artist + '.wav', '-y']
                        output = subprocess.run(" ".join(args), stdout=commandFile, stderr=commandFile, shell=True)
                        if output.returncode != 0:
                            logFile.write("FAILURE FFMPEG: " + title + artist + "\n")
                            raise Exception("FAILURE FFMPEG: " + title + artist)
                        if not os.path.isfile(sys.argv[2] + '/converted/' + title + '-' + artist + '.wav'):
                            logFile.write("FAILURE NOFILE: " + title + artist + "\n")
                            raise Exception("FAILURE NOFILE: " + title + artist)
                        args = ['rm', sys.argv[2] + '/' + title + '-' + artist + '.*']
                        output = subprocess.run(" ".join(args), stdout=commandFile, stderr=commandFile, shell=True)
                        if output.returncode != 0:
                            logFile.write("FAILURE RM: " + title + artist + "\n")
                            raise Exception("FAILURE RM: " + title + artist)
                    except Exception as e:
                        logFile.write("EXCEPTION: " + title + artist + "\nException: " + str(e) + "\n")
