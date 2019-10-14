# SimpleASR

## 1st Try: Free Spoken Digits Dataset with Kaldi

In this dataset we have one digit per wav file. See [here](https://github.com/Jakobovski/free-spoken-digit-dataset) for the data. The wave filename is of the form `{digitLabel}_{speakerName}_{index}.wav` (e.g. 7_jackson_32.wav means that jackson said the number 7 and this was his 32nd try).

All recordings are 8Khz. Other information about our data:

1. 4 different speakers
2. 2,000 recordings
3. 50 recordings of each digit
4. English pronounciation

## Train-Test Split
The test set officially consists of the first 10% of the recordings. Recordings numbered 0-4 (inclusive) are in the test and 5-49 are in the training set.

## Metadata 
Metadata as of 14th of October 2019:
  ```metadata = {
      'jackson': {
          'gender': 'male',
          'accent': 'USA/neutral',
          'language': 'english'
      },
      'nicolas': {
        'gender': 'male',
        'accent': 'BEL/French',
        'language': 'english'
      },
      'theo': {
        'gender': 'male',
        'accent': 'USA/neutral',
        'language': 'english'
      },
      'yweweler': {
        'gender': 'male',
        'accent': 'DEU/German',
        'language': 'english'
      }
  }
  ```

## Steps

We will be using the [Kaldi for dummies](http://kaldi-asr.org/doc/kaldi_for_dummies.html) tutorial steps. We assume an already installed kaldi system. (A basic prerequisite is that you are also using a Linux system. I am using a Linux subsystem inside my Windows 10 distribution.)

1. Clone the [FSDD](https://github.com/Jakobovski/free-spoken-digit-dataset) repository somewhere locally (I cloned it at `~/github`).
2. Go to `kaldi/egs` directory and create a new directory. I will be using the name `myfsdd`.
3. Copy the `recordings` directory of the github repo above in the `myfsdd` and rename it to `wave_files`.
4. Use the `split_train_test.py` script in order to split into train and test (as mentioned above).
5. Create 4 subdirectories in each of the `train` and `test` directories with the names of the speakers (yweweler, nicholas, jackson, theo):
   ```
   mkdir wave_files/train/nicolas
   mkdir wave_files/train/yweweler
   mkdir wave_files/train/jackson
   mkdir wave_files/train/theo
   mkdir wave_files/test/nicolas
   mkdir wave_files/test/yweweler
   mkdir wave_files/test/jackson
   mkdir wave_files/test/theo
   ```
6. Run `put_users_to_folders.py` in order to distribute the audio files.
7. Run `ln -s ../wsj/s5/utils/ .` to create a symbolic links to the kaldi utilities. After that run `cp ../wsj/s5/path.sh .`.
8. Run `mkdir data` and then `mkdir data/train` and `mkdir data/test`
9. Create a `spk2gender` file as shown in this repo and copy it to both `data/train` and `data/test`.
10. Run `create_train_wavscp.py full_path_to_train`. For me `full_path_to_train` is `/home/geoph/v2t/kaldi/egs/myfsdd/data/train`. Then  run `create_test_wavscp.py full_path_to_test`. For me `full_path_to_test` is `/home/geoph/v2t/kaldi/egs/myfsdd/data/test`. After running those two you should see 1800 lines in `data/train/wav.scp` and 200 lines in `data/test/wav.scp`.
11. Copy `number_transcript.py` to your current working directory and then run the `create_train_text.py` and `create_test_text.py` with an argument `full_path_to_train` and `full_path_to_test` as before. (e.g. `create_train_text.py /home/geoph/v2t/kaldi/egs/myfsdd/data/test`. This will create a `text` file in `./data/train` and `./data/test/`. The format of the text file is `utteranceID number` (e.g. `0_jackson_12 zero`)
12. Next step is to create a `utt2spk` file in both `data/train` and `data/test`. For this, run `python create_utt2spk.py [train/test]`. Do this twice once with `train` and with `test` (i.e. `python create_utt2spk.py train` and `python create_utt2spk.py test`)
13. Now, we need to create the `corpus.txt` file that contains our corpus (numbers from 0 to 9). **NOTE:** This stored in a new directory `./data/local/` which you need to create (`mkdir ./data/local`). Since in each audio file we only have one number, it is really easy to create this file by hand. Check the `corpus.txt` in this repo.

