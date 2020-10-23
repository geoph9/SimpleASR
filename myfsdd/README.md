# Free Spoken Digits Dataset with Kaldi

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
```json
{
      "jackson": {
          "gender": "male",
          "accent": "USA/neutral",
          "language": "english"
      },
      "nicolas": {
        "gender": "male",
        "accent": "BEL/French",
        "language": "english"
      },
      "theo": {
        "gender": "male",
        "accent": "USA/neutral",
        "language": "english"
      },
      "yweweler": {
        "gender": "male",
        "accent": "DEU/German",
        "language": "english"
      }
  }
```

## First Steps

We will be using the [Kaldi for dummies](http://kaldi-asr.org/doc/kaldi_for_dummies.html) tutorial steps. 

1. Clone the [FSDD](https://github.com/Jakobovski/free-spoken-digit-dataset) repository somewhere locally (I cloned it at `~/github`).
2. Go to `kaldi/egs` directory and create a new directory. I will be using the name `myfsdd`.

__NOTE:__ Whenever I do not mention the current working directory, I suppose that you are located in `kaldi/egs/myfsdd`.

## Creating Kaldi files

1. Create a new `wave_files` (`mkdir wave_files`) directory where you will put all of the recordings. Let's say that your recordings from the FSDD repository where saved at `~/github/free-spoken-digit-dataset/recordings`. Then you should do `cp ~/github/free-spoken-digit-dataset/recordings /path/to/kaldi/egs/myfsdd`.
2. Use the `split_train_test.py` script in order to split into train and test (as mentioned above).
3. Create 4 subdirectories in each of the `train` and `test` directories with the names of the speakers (yweweler, nicholas, jackson, theo):
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
4. Run `put_users_to_folders.py` in order to distribute the audio files.
5. Run `ln -s ../wsj/s5/utils/ .` to create a symbolic links to the kaldi utilities. After that run `cp ../wsj/s5/path.sh .`. We also need to create a symbolic link to the `steps` folder. Do that by `ln -s ../wsj/s5/steps/ .`. We will need those later.
6. Run `mkdir data` and then `mkdir data/train` and `mkdir data/test`.
7. Create a `spk2gender` file as shown in this repo and copy it to both `data/train` and `data/test`. The format should be: `speakerID gender` where gender is either `m` or `f`.
8. Run `create_train_wavscp.py full_path_to_train`. For me `full_path_to_train` is `/home/geoph/v2t/kaldi/egs/myfsdd/data/train`. Then  run `create_test_wavscp.py full_path_to_test`. For me `full_path_to_test` is `/home/geoph/v2t/kaldi/egs/myfsdd/data/test`. After running those two you should see 1800 lines in `data/train/wav.scp` and 200 lines in `data/test/wav.scp`. 

    This `wav.scp` file follows the following pattern: `recordingID full_path_to_audio`. For us, `recordingID` is the same as `utteranceID` since in our audio samples we only have 1 word per audio.
9. Copy `number_transcript.py` to your current working directory and then run the `create_train_text.py` and `create_test_text.py` with an argument `full_path_to_train` and `full_path_to_test` as before. (e.g. `create_train_text.py /home/geoph/v2t/kaldi/egs/myfsdd/data/test`. This will create a `text` file in `./data/train` and `./data/test/`. The format of the text file is `utteranceID number` (e.g. `0_jackson_12 zero`). The format of the `text` file is: `utteranceID text` where `text` denotes the transcription for that utterance.
10. Next step is to create a `utt2spk` file in both `data/train` and `data/test`. 

    This file follows the pattern: `utteranceID speakerID`. 

    Run `./create_utt2spk.sh train` and `./create_utt2spk.sh test` in order to create a sorted `utt2spk` file.
    > If this step won't work then use the below version which provides sorted output (kaldi needs the output to be sorted):

    For the train data:
    ```     
    cat data/train/wav.scp | cut -f 1 -d ' ' | \ 
    perl -ane 'chomp; @F = split "-", $_; print $_ . " " . @F[0] . "\n";' > data/train/utt2spk
    ```
    For the test data:
    ```
    cat data/test/wav.scp | cut -f 1 -d ' ' | perl -ane 'chomp; @F = split "-", $_; print $_ . " " . @F[0] . "\n";' > data/test/utt2spk
    ```
    
11. Now, we need to create the `corpus.txt` file that contains our corpus (numbers from 0 to 9). **NOTE:** This stored in a new directory `./data/local/` which you need to create (`mkdir ./data/local`). Since in each audio file we only have one number, it is really easy to create this file by hand. Check the `corpus.txt` in this repo.

12. Run `utils/fix_data_dir.sh data/train` and `utils/fix_data_dir.sh data/test` in order to make sure that everything is in a kaldi-readable format. This will also create a file `spk2utt` which is of the format: `speakerID utt1ID utt2ID ... `.

13. Run `utils/validate_data_dir.sh data/train` and `utils/validate_data_dir.sh data/test` in order to make sure that everything is okay. If step 12 was successful then you shouldn't have any problem here.

## Language Modelling
We have created the main structure that is based solely on our data. Now, we will create language related data. Steps:

1. Create a new directory `dict`. Execute: `mkdir ./data/local/dict`
2. In `./data/local/dict` create a new `lexicon.txt`which contains all the words in our dictionary and their phoneme transcriptions. If you have another, more complex, dataset then I highly reccommend [the CMU sphinx acoustic and language models](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/). In our case, our lexicon is really small and we are going to copy only the 10 words we have plus a silence phoneme and an OOV (out of vocabulary) words phoneme. Check the `lexicon.txt` in this repo in order to see how it should look like. Since we follow the Kaldi for dummies tutorial, we are also going to use the lexicon used in `/egs/voxforge`.
3. Create `nonsilence_phones.txt`. This file consists of the nonsilence phones that are present in our data.
4. Create `silence_phones.txt`. This consists of the silence phones (which is either silence or OOV words).
5. Create `optional_silence.txt`. Optional silence phones (only `sil` in our case).

## Final Steps
1. Install a language modelling toolkit: 
    * We will use the SRI Language Modeling Toolkit (SRILM). For installation see `kaldi/tools/install_srilm.sh`. 
    * In order to download SRILM go to [their website](http://www.speech.sri.com/projects/srilm/download.html), fill the download form and you will be able to download a `.tar.gz` file (tarball).
    * Copy this file in `kaldi/tools`
    * Go to the `kaldi/tools` directory.
    * Run `./install_srilm.sh`. Make sure that you have followed the steps above and that the installtion was succesful before doing that (otherwise you will get an error).
    * Make sure that you have `GNU awk` installed (`sudo apt-get install gawk`).
2. From `kaldi/egs/voxforge/s5/local` copy the script `score.sh` into `kaldi/egs/myfsdd/local`. So, at first create a `local` dir by `mkdir local` and then `cp ../vocforge/s5/local/score.sh ./local/` 
3. Create configuration files:
    * Go back to `kaldi/egs/myfsdd`.
    * Create a new directory `conf`.
    * Create the following two files inside `conf`:
        - decode.config:
            ```
            first_beam=10.0
            beam=13.0
            lattice_beam=6.0
            ```
        - mfcc.conf:
            ```
            --use-energy=false
            --sample-frequency=8000
            ```
        sample-frequency is 8000 for our audio files. Adjust for your own.
4. Create running scripts. We will use 2 training methods: MONE (monophone training) and TRI1(simple triphone training (first triphone pass):
    * In `kaldi/egs/myfsdd` create the following:
        - `cmd.sh`:
            ```
            # Setting local system jobs (local CPU - no external clusters)
            export train_cmd=run.pl
            export decode_cmd=run.pl
            ```
        - `path.sh`:
        - `run.sh` (look at the `run.sh` file in this repo)
5. Execute `run.sh`. This file is a copy-paste from the kaldi-for-dummies tutorial. If anything unexpected happens see the messages from the logs.
6. The above command shall create and new directory `exp`. From the tutorial:  
    > You may notice there folders with mono and tri1 results as well - directories structure are the same. Go to mono/decode directory. Here you may find result files (named in a wer_{number} way). Logs for decoding process may be found in log folder (same directory).

**NOTE: ** I am using a Linux Debian subsystem in Windows 10. The PATH variable contained some broken paths that wrongly used windows paths. For me, this solved this:
`export PATH_TEMP=$PATH_TEMP:...` where with the 3 dots I denote the PATH variable as it would appear if you ran echo PATH but you should delete all the Windows files (the ones that start with `C:\Users\...`.
Execute the above command before the `run.sh`. In order to accept it go to `path.sh` and change `$PATH` to `$PATH_TEMP` (this export will only last for the current session). 

# Test trained model (Work in progress...)
Let's say we have a new audio file `audio.wav`. This must be a mono channel 8Khz audio file. In order to convert it, we will use SoX. At first make sure whether there is a need to change the above with `soxi audio.wav`. If *Channels* is 1 and *Sample Rate* is 8000 then we are ok. Otherwise, use `sox -t wav audio.wav -c 1 -r 8000 -t wav > audio.wav`.
