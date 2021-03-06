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
path_to_text = "./data/test/text"
if os.path.exists(path_to_text):
    os.unlink(path_to_text)
try:
    full_path_to_test = sys.argv[1]
except IndexError:
    print("IndexError: Could not locate path from sys arguments. Switching to default...")
    full_path_to_test = "/home/geoph/v2t/kaldi/egs/myfsdd/wave_files/test"

for user_dir in names:
    path = os.path.join(full_path_to_test, user_dir)
    print(path)
    for filename in glob.glob(path + "/*.wav"):
        basename = os.path.basename(filename)
        with open(path_to_text, 'a') as f:
            to_write1 = basename.split(".")[0]  # e.g. jackson_0_12
            to_write1 = to_write1.split("_")[1] + "_" + to_write1.split("_")[0] + "_" + to_write1.split("_")[2]  # e.g. jackson_0_12
            utteranceID = to_write1.replace("_", "-")  # e.g. jackson-0-12
            to_write2 = basename.split(".")[0].split("_")[0]  # e.g. 0
            # Convert to transcript
            speakerID = NUMBER_TANSCRIPT[int(to_write2)]
            to_write = utteranceID + " " + speakerID
            f.write(to_write + "\n")
            