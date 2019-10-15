#!/bin/bash

# Author: Giorgos K.

# The first argument should be either train or test 
if [ $# != 1 ]; then
    echo "Usage: create_utt2spk [train/test]"
    echo "Use train in order to create utt2spk in data/train"
    echo "Use test in order to create utt2spk in data/test"
    exit 1
fi

echo "Getting utteranceIDs from $data/$1/${wav.scp}..."

cat $data/$1/${wav.scp} | cut -f 1 -d ' ' | \
    perl -ane 'chomp; @F = split "-", $_; print $_ . " " . @F[0] . "\n";' > $data/$1/$utt2spk
    
echo "Saving utt2spk at $data/$1/$utt2spk..."