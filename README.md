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
  }```
