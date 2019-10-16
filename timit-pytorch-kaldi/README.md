# Train on TIMIT using pytorch-kaldi

In this tutorial I will be using the TIMIT dataset and I will be following the steps from [Pytorch-Kaldi](https://github.com/mravanelli/pytorch-kaldi) on how to train TIMIT. A basic prerequisite is that you have already successfully installed kaldi. I have tested the following only in a Debian 9 Windows Subsystem. 

You also need make sure that you have installed python, pip, pytorch (with CUDA if possible). In order to download pytorch go to [their official website](https://pytorch.org/get-started/locally/) and download the stable Linux version for your python and CUDA versions. If you haven't installed CUDA then you will probably encounter errors since kaldi DNN training works with CUDA. If you have no CUDA then we will only use the tri3 folder (though DNN is suggested). Since I am using a rather old computer for training, I will not be using CUDA in this tutorial (but you can easily configure this in order to use it).

## Getting the TIMIT dataset

1. I have downloaded TIMIT from this [github repo](https://github.com/philipperemy/timit) since the official dataset from LDC is not freely available unless you have membership. 
2. Extract TIMIT somewhere locally. Remember this path since you will need it later (it doesn't necessarily have to be insode `kaldi/egs/timit/s5`).

## Configuring the TIMIT kaldi recipe

1. In order for this to work, make sure that `$KALDI_ROOT` is exported inside `~/.bashrc`. If not (or if something is missing), then add the following into `~/.bashrc`: 
    ```
    export KALDI_ROOT=/home/{username}/v2t/kaldi
    export PATH=$PATH:~/.local/bin:$KALDI_ROOT/tools/openfst:$KALDI_ROOT/src/featbin:$KALDI_ROOT/src/gmmbin:$KALDI_ROOT/src/bin:$KALDI_ROOT//src/nnetbin
    ```
    
    For example, in my case `{username}` is `geoph`.

2. *(Optional)*: Since I am using a Linux subsystem inside my Windows distribution, I had some issues with the `$PATH` variable. In order to solve this I editted the already defined `PATH` and saved the changes into a new varibale `PATH_TEMP`. The issue here was that I had to remove all of the sub-paths that had to do with Windows. In particular, I had some paths 
