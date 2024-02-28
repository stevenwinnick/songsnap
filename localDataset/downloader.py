import subprocess    
import pandas as pd
import numpy as np

if __name__ == "__main__":

    output = subprocess.run(["mkdir", './audio'])
    df = pd.read_csv('bucketed.csv')
    rows = np.random.choice(df.shape[0], 100, replace=False)

    for row in rows:
        songFile = df.loc[df.index[row], 'bucket']
        """
        output = subprocess.run(['gsutil', 'cp', 'gs://songsnap-try-bucket-1/' + songFile, './audio/' + songFile])
        if output.returncode != 0:
            print("Failed:", songFile)
        """

    df.iloc[rows.tolist()].to_csv('localDataset.csv')
