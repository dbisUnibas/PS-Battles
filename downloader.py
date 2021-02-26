#!/usr/bin/python
import csv
import os
import requests
import hashlib


def download(url, destination, checksum):
    if os.path.exists(destination):
        print("file already exist skipping  :  " + destination)
        return

    img_data = requests.get(url).content
    m = hashlib.sha256()
    m.update(img_data)
    hash = m.hexdigest()

    if not hash == checksum:
        print("hash :  " + hash + "  does not equal checksum from tsv : " + checksum)

    with open(destination, 'wb') as handler:
        handler.write(img_data)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    if not (os.path.exists("originals.tsv")):
        print("originals.tsv does not exist")
        exit(127)
    if not os.path.exists("photoshops.tsv"):
        print("photoshops.tsv does not exist")
        exit(127)

        # starting with originals
    file = open("originals.tsv")
    count: int = len(open("originals.tsv").readlines())
    percent: int = round(count / 100)

    if os.path.exists("originals"):
        print(" originals directory already existst")
        exit(127)

    os.mkdir("originals")

    print("starting with downloading originals.tsv")
    read_tsv = csv.reader(file, delimiter="\t")
    counter = 0
    pc = 0
    # skip header
    next(read_tsv)
    for row in read_tsv:
        # row= id	url	end	hash	filesize	score	author	link	timestamp	width	height
        filepath = "originals/" + row[0] + "." + row[2]  # originals/id.end
        url = row[1]
        hash = row[3]
        download(url, filepath, hash)
        counter += 1
        if counter >= percent:
            pc += 1
            print(pc, "% of orginals downloaded")
            counter = 0

    file.close()
    print("finished downloading originals")

    # starting with photoshops
    file = open("photoshops.tsv")
    count: int = len(open("photoshops.tsv").readlines())
    percent: int = round(count / 100)

    if os.path.exists("photoshops"):
        print(" photoshops directory already exist")
        exit(127)

    os.mkdir("photoshops")

    print("starting with downloading photoshops.tsv")
    read_tsv = csv.reader(file, delimiter="\t")
    counter = 0
    pc = 0  # percent counter

    # skip header
    next(read_tsv)
    for row in read_tsv:
        # row=id	original	url	end	hash	filesize	score	author	link	timestamp	width	height
        filepath = "photoshops/" + row[0] + "." + row[3]  # photoshops/id.end
        url = row[2]
        hash = row[4]
        download(url, filepath, hash)
        counter += 1
        if counter >= percent:
            pc += 1
            print(pc, "% of photoshops downloaded")
            counter = 0
    file.close()
    print("finished downloading photoshops")
