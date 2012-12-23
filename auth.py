import os
import time
import os.path
import getpass
import sys
from mechanize import Browser
import re
from glob import glob
from BeautifulSoup import BeautifulSoup

f1 = open("result.csv", 'w')

def DoAuth(address, password) :
	br = Browser()
	br.open(address)
	#find first form
	br.select_form(nr=0)
	#filling fields
	br["user_name"] = "user"
	br["user_pass"] = password
	br.submit()
	#find all links on page by regexp
	for link in br.links(url_regex="side"):
		link_url = '';
		link_text = '';
		page_text = '';
		req = br.click_link(link)
		link_url = link.url
		print('........... ............ ............')
		print("IN " + link_url)
		
		time.sleep(1)
		link_text = link.text;
		print("Link text: " + link.text)
		#create object for parsing page
		soup = BeautifulSoup(br.open(req))
		cols = soup.findAll('iframe')
		if (cols) :
			#create object for frame body
			fr = Browser()
			s = address;
			#remove index.php
			s = s[:-9]
			soupframe = BeautifulSoup(fr.open(s + cols[0]['src']))
			cols = soupframe.findAll('h3')
			if (cols) :
				page_text = cols[0].renderContents()
				print 'page text: ' + page_text
		RecordToFile(link_url, link_text, page_text)
	f1.close()

def RecordToFile(url, text, page) :
	diff = 0;
	if (text != page) :
		diff = 1;
	f1.write(url + ' ' + text + ' ' + page + ' ' + str(diff))
	f1.write("\n")
