import pandas as pd
from collections import defaultdict
import random
# sudo apt install ffmpeg (ON LINUX)
# pip install pydub
from playsound import playsound


speakers = pd.read_csv("speakers.tsv", sep="\t").astype({"volume":'str', "muffled-ness":'str', "background_noise":'str'})

wav_dir = "speech/"

random.seed(1020)

df = pd.read_csv('speech.tsv', sep='\t')

d = defaultdict(list)

grouping = df.groupby('worker_id')


for index, row in df.iterrows():
    d[row['worker_id'].upper()].append(row['wav'])
    
    
r = 'y'

while r != 'n':
    quality = input('quality? ')
    value = input('value? ')
    examples = speakers.loc[speakers[quality] == value]["worker_id"].to_list()
    # sample without replacement
    samples = [random.choice(d[i.upper()]) for i in random.sample(examples, 3)]
    for sample in samples:
        file_name = wav_dir + sample + ".wav"
        print(file_name)
        playsound(file_name)

    r = input('press n to stop (or other to repeat)... ')