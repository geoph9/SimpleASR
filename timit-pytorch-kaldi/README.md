# Train on TIMIT using pytorch-kaldi

In this tutorial I will be using the TIMIT dataset and I will be following the steps from [Pytorch-Kaldi](https://github.com/mravanelli/pytorch-kaldi) on how to train TIMIT. A basic prerequisite is that you have already successfully installed kaldi. I have tested the following only in a Debian 9 Windows Subsystem. 

You also need make sure that you have installed python, pip, pytorch (with CUDA if possible). In order to download pytorch go to [their official website](https://pytorch.org/get-started/locally/) and download the stable Linux version for your python and CUDA versions. If you haven't installed CUDA then you will probably encounter errors since kaldi DNN training works with CUDA. If you have no CUDA then we will only use the tri3 folder (though DNN is suggested). Since I am using a rather old computer for training, I will not be using CUDA in this tutorial (but you can easily configure this in order to use it). 

[Pytorch-Kaldi](https://github.com/mravanelli/pytorch-kaldi) recommends to use either version 1.0 or 0.4 of PyTorch.

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

2. *(Optional)*: Since I am using a Linux subsystem inside my Windows distribution, I had some issues with the `$PATH` variable. In order to solve this I editted the already defined `PATH` and saved the changes into a new varibale `PATH_TEMP`. The issue here was that I had to remove all of the sub-paths that had to do with Windows. In particular, I had some paths that were in the Windows format and this messed up everything. So, I coppied the current PATH into PATH_TEMP and I removed these kinds of paths from the latter. Then I exported the new `PATH_TEMP`.

3. Go to `$KALDI_ROOT/egs/timit/s5` and edit the `run.sh` file. I am using vim as my editor and so I did `vim run.sh`. Go at the top of the file and there you should a variable `timit=...`. Comment it and below it write `timit=/path/to/TIMIT/lisa/data/timit/raw/TIMIT`.

4. Edit `cmd.sh`. I ran everything locally and so I used `run.pl` instead of `queue.pl`. The if statement was the default one and it won't be executed (since the conditioned is not satisfied). (So, in this step just change `queue.pl` to `run.pl` everywhere.)

5. *(Optional)*: As mentioned at step 2, I have created a `PATH_TEMP` variable. If you are also using a Linux subsystem then you probably have to change `$PATH` to `$PATH_TEMP` in `path.sh`. So, the third line of this file would look like: `export PATH=$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$KALDI_ROOT/tools/irstlm/bin/:$PWD:$PATH_TEMP`.

6. *(Optional)*: Make sure that `bc` installed (type `bc` to test i). In order to install it (on Debian) do `sudo-apt-get install bc`.

7. Execute `./run.sh` in order to start training. This will take some time and it will produce several files. The training is fully informative, since it prints every steps. Since I did not use DNN training (and only trained a triphone model) I didn't wait for the whole script to finish (no harm in doing so). 
