# SimpleASR

This tutorial aims at providing some first steps for creating your own kaldi model. 


I will provide different folders with different datasets. My current work includes the following:

1. [`fsdd`](myfsdd): I have uploaded a guide on building your own digit recognition system by the freely available [Free Spoken Digits Dataset](https://github.com/Jakobovski/free-spoken-digit-dataset). 
2. [`timit`](timit-pytorch-kaldi): Here, I used Pytorch-Kaldi with kaldi alignments. I am not 100% sure this will work. 
3. (Work In Progress) [`greek-vosk`](greek-vosk): This is the **most recent** directory and will probably work better than the others. It uses 
the already trained Greek model from [alphacephei](https://alphacephei.com/vosk/models) (you may also checkout the [vosk](https://alphacephei.com/vosk/) documentation). 

**NOTE1:** I assume that you have already successfully installed kaldi (if not, then check [this tutorial](https://jrmeyer.github.io/asr/2016/01/26/Installing-Kaldi.html) by Josh Meyer.
If you are on Windows then you may try WSL. When I created the first directories I was using WSL but some things have changed
and I am not sure if everything will work.

**NOTE2:** I created the first two directories (`fsdd`, `timit`) a really long time ago and I have most probably made a lot of mistakes.
If something doesn't run feel free to contact me or make a PR (or open an issue and I will fix it).

