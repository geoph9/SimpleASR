import sys
import glob
import os

names = ['nicolas', 'jackson', 'theo', 'yweweler']
path_to_scp = "./data/test/wav.scp"
if os.path.exists(path_to_scp):
    os.unlink(path_to_scp)
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
        with open(path_to_scp, 'a') as f:
            to_write = basename.split(".")[0]  # e.g. 0_jackson_12 as utteranceID
            to_write = to_write.split("_")[1] + "_" + to_write.split("_")[0] + "_" + to_write.split("_")[2]  # e.g. jackson_0_12
            to_write = to_write.replace("_", "-")  # replace underscore with dash
            to_write = to_write + " " + os.path.join(full_path_to_test, user_dir) + "/" + basename
            f.write(to_write + "\n")
            