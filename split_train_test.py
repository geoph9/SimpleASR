import glob
import os
import shutil

path_to_waves = "./wave_files/"
test_range_indices = [0, 1, 2, 3, 4]
train_path = os.path.join(path_to_waves, "train")
test_path = os.path.join(path_to_waves, "test")
if os.path.exists(train_path): 
    pass
else:
    os.mkdir(train_path)
if os.path.exists(test_path): 
    pass
else:
    os.mkdir(test_path)
        

for filename in glob.glob(path_to_waves + "*.wav"):
    basename = os.path.basename(filename)
    index = int(basename.split("_")[-1].split(".")[0])
    if index in test_range_indices:
        shutil.move(filename, os.path.join(test_path, basename))
    else:
        shutil.move(filename, os.path.join(train_path, basename))
print("Success!")
