#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import os
import urllib.request 
import sys
import time
import csv

def bayc():

    for i in range(4452, 9955):
        r1 = requests.get("https://gateway.pinata.cloud/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/" + str(i)) 
        soup = BeautifulSoup(r1.text,'lxml')
        ipfs_hash = str(soup)[32:78]
        image_url = 'https://gateway.pinata.cloud/ipfs/' + ipfs_hash

        try:
            urllib.request.urlretrieve(image_url, "BAYC-10000-image/" + str(i).zfill(4) + ".png")

            print(str(i).zfill(4) + ".png", "download succeed")
        
        except Exception as e:
            result = e

    
def mayc():

    no_token = []
    download_token = [21180,13688,18474,10866,24370,21880,23842,27766,19212]

    for i in download_token:
        time.sleep(2)

        r1 = requests.get("https://boredapeyachtclub.com/api/mutants/" + str(i)) 
        soup = BeautifulSoup(r1.text,'lxml')

        if str(soup) == "<html><body><p>Specified token has not been minted</p></body></html>":
            no_token.append(i)
            print(str(i).zfill(5), "token has not been minted")

        else:
            ipfs_hash = str(soup.find_all("p"))[21:67]
            image_url = 'https://gateway.pinata.cloud/ipfs/' + ipfs_hash

            try:
                urllib.request.urlretrieve(image_url, "MAYC-image/" + str(i).zfill(5) + ".png")

                print(str(i).zfill(5) + ".png", "download succeed")

            
            except Exception as e:
                result = e

def bakc():

    no_token = []

    for i in range(1022, 1023):
        time.sleep(2)
        r1 = requests.get("https://gateway.pinata.cloud/ipfs/QmTDcCdt3yb6mZitzWBmQr65AW6Wska295Dg9nbEYpSUDR/" + str(i)) 
        soup = BeautifulSoup(r1.text,'lxml')
        ipfs_hash = str(soup)[32:78]
        image_url = 'https://gateway.pinata.cloud/ipfs/' + ipfs_hash

        try:
            urllib.request.urlretrieve(image_url, "BAKC-image/" + str(i).zfill(4) + ".png")

            print(str(i).zfill(4) + ".png", "download succeed")
        
        except Exception as e:
            no_token.append(i)
            result = e


def main():
	# bayc()
    mayc()
    # bakc()

if __name__ == "__main__":
	main() 