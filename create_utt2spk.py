import sys

"""
    execute:
        python create_utt2spk.py [train/test]
        e.g. `python create_utt2spk.py train` will create the utt2spk file for training
    format:
        <uterranceID> <speaker_id>
        e.g. 0_nicolas_10 nicolas
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
            utteranceID = line.split(" ")[0]  # e.g. 0_jackson_12
            speaker_id = utteranceID.split("_")[1]  # e.g. jackson
            # Convert to transcript
            to_write = utteranceID + " " + speaker_id
            fwrite.write(to_write + "\n")
            
