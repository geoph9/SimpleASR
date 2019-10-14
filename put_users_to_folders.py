import glob
import os
import shutil

path_to_waves = "./wave_files/"
train_path = os.path.join(path_to_waves, "train")
test_path = os.path.join(path_to_waves, "test")

for filename in glob.glob(train_path + "/*.wav"):
    basename = os.path.basename(filename)
    speaker_id = basename.split("_")[1]
    shutil.move(filename, os.path.join(train_path, speaker_id, basename))

for filename in glob.glob(test_path + "/*.wav"):
    basename = os.path.basename(filename)
    speaker_id = basename.split("_")[1]
    shutil.move(filename, os.path.join(test_path, speaker_id, basename))
print("Success")
