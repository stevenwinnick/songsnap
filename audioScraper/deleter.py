import sys
import os
import subprocess    

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 deleter.py <datasetFile> <songDirectory>")
        sys.exit(1)

    with open('./bucketed.csv', "a") as successFile:
        with open('./bucketLog.txt', "a") as logFile:
            with open(sys.argv[1], "r") as datasetFile:
                headerLine = datasetFile.readline()
                successFile.write(headerLine[:-1] + ",bucket\n")
                for line in datasetFile:
                    dataRow = line.strip().split(",")
                    title = ''.join(dataRow[0].split())
                    artist = ''.join(dataRow[1].split())

                    if os.path.isfile(sys.argv[2] + '/converted/' + title + '-' + artist + '.wav'):
                        successFile.write(line[:-1] + ',' + title + '-' + artist + '.wav' + '\n')
                        """
                        args = ['rm', sys.argv[2] + '/converted/' + title + '-' + artist + '.wav']
                        output = subprocess.run(" ".join(args), stdout=logFile, stderr=logFile, shell=True)
                        if output.returncode != 0:
                            logFile.write("FAILURE RM: " + title + artist + "\n")
                        else:
                            logFile.write("SUCCESS: " + title + artist + "\n")
                        """    
                    else:
                        logFile.write("FAILURE NOFILE: " + title + "-" + artist + "\n")