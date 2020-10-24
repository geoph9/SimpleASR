#!/bin/bash

if [ $# -ne 1 ] ; then
  echo "You must provide exactly one argument which shall be the path to the audio file"
  echo "you want to transcribe."
  echo "Usage: $0 <path-to-wav>"
  exit 1;
fi

wav=$1

if [ ! -f $wav ] ; then
  echo "The provided wav file ($wav) does not exist."
  echo "Aborting..."
  exit 1;
fi

vosk_decode_script=./decode.sh
if [ ! -f $vosk_decode_script ] ; then
  echo "The decoding script of the vosk directory could not be found under $vosk_decode_script."
  echo "Are you sure you are inside the unzipped vosk directory?"
  echo "Aborting..."
  exit 1;
fi

# Remove the old decoder-test.wav file and replace it with the provided wav file
rm -f ./decoder-test.wav && cp $wav ./decoder-test.wav

# Decode
./decode.sh
exit 0;