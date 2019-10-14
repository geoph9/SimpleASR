import sys
import glob
import os
from number_transcript import NUMBER_TANSCRIPT

"""
    format:
        <uterranceID> <text_transcription>
        e.g. 0_nicolas_10 zero
    notes:
        There is a number_transcript.py file has a dictionary with the matchings from numbers to transcripts. E.g. 1: "one".
"""

names = ['nicolas', 'jackson', 'theo', 'yweweler']
path_to_text = "./data/train/text"
try:
    full_path_to_train = sys.argv[1]
except IndexError:
    print("IndexError: Could not locate path from sys arguments. Switching to default...")
    full_path_to_train = "/home/geoph/v2t/kaldi/egs/myfsdd/wave_files/train"

for user_dir in names:
    path = os.path.join(full_path_to_train, user_dir)
    print(path)
    for filename in glob.glob(path + "/*.wav"):
        basename = os.path.basename(filename)
        with open(path_to_text, 'a') as f:
            to_write1 = basename.split(".")[0]  # e.g. 0_jackson_12
            to_write2 = basename.split(".")[0].split("_")[0]  # e.g. 0
            # Convert to transcript
            to_write2 = NUMBER_TANSCRIPT[int(to_write2)]
            to_write = to_write1 + " " + to_write2
            f.write(to_write + "\n")
            
