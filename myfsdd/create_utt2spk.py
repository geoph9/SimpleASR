import sys

"""
    execute:
        python create_utt2spk.py [train/test]
        e.g. `python create_utt2spk.py train` will create the utt2spk file for training
    format:
        <uterranceID> <speaker_id>
        e.g. nicolas_0_10 nicolas
"""

names = ['nicolas', 'jackson', 'theo', 'yweweler']
path_to_text = "./data/train/text"
try:
    path_to_save = sys.argv[1]
    path_to_save = "./data/" + path_to_save + "/utt2spk"
except IndexError:
    print("IndexError: Could not locate path from sys arguments. Cannot continue...")
    raise IndexError("Please provide either train or test in the arguments")

# Get the first first element of text file which is the utteranceID
with open(path_to_text, 'r') as fread:
    for line in fread.readlines():
        with open(path_to_save, 'a') as fwrite:
            utteranceID = line.split(" ")[0]  # e.g. jackson_0_12
            print(utteranceID)
            speaker_id = utteranceID.split("-")[0]  # e.g. jackson
            # Convert to transcript
            to_write = utteranceID + " " + speaker_id
            fwrite.write(to_write + "\n")
            