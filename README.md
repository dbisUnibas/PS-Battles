# PS-Battles
Repository of the [PS-Battles dataset, an image collection for image manipulation detection](https://arxiv.org/abs/1804.04866).

# Download instructions

## Ubuntu
On ubuntu, simply run the provided ```download.sh``` script. It will download all images from the provided .tsv-files and verify them with the provided sha256sum.

## MacOS
On Mac, there is no ```sha256sum``` command.
 We recommend either running the following command first: ```function sha256sum() { shasum -a 256 "$@" ; } && export -f sha256sum```
 OR you can either change the command in the ```download.sh``` script to ```shasum -a 256```
 OR you can disable checksum-verification in the provided script.

## Windows
We do not provide a download script for windows, you can use your preferred scripting language and download tool to download images using the links in the provided .tsv-files.
