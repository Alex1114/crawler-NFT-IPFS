import requests
from bs4 import BeautifulSoup
import lxml
import os
import urllib.request 
import sys
import time
import csv

mayc_dir = "M-0-10000/"
file_name = os.listdir(mayc_dir)

# for a in range(len(file_name)):
# 	os.rename(mayc_dir + file_name[a], mayc_dir + "0" + file_name[a])
# 	print(mayc_dir + "0" + file_name[a])


c = 0

with open('0~10000.csv', newline='') as csvfile:
	rows = csv.reader(csvfile)
	
	for row in rows:
		

		for i in range(len(row)):
			o = 0

			for j in range(len(file_name)):
				if (str(row[i]).zfill(5) == str(file_name[j].split(".")[0])):
					o = 1

			if (o == 0):
				c += 1
				time.sleep(2)
				r1 = requests.get("https://boredapeyachtclub.com/api/mutants/" + str(row[i])) 
				soup = BeautifulSoup(r1.text,'lxml')
				ipfs_hash = str(soup.find_all("p"))[21:67]
				image_url = 'https://gateway.pinata.cloud/ipfs/' + ipfs_hash
				urllib.request.urlretrieve(image_url, "MAYC-image/" + str(row[i]).zfill(5) + ".png")
				print(str(row[i]).zfill(5) + ".png", "download succeed")

	print(c)
				


		
		
		

