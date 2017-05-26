from bs4 import BeautifulSoup 
# import urllib2 
import pickle
# import shutil
import requests
from allclasses import show
# from urlparse import urljoin
# import sys 
# from sys import argv
# import time
# import os 
FILENAME_TV_SHOW = 'tv_show_data.pkl'
FILENAME_MOVIES = 'movies.pkl'

URL = 'https://fmovies.se'
TV_SERIES_URL = 'https://fmovies.se/tv-series'
MOVIES_URL = 'https://fmovies.se/movies'

SOUP_URL = MOVIES_URL


# def make_soup (url) : 
# 	# to prevent 403 : FORBIDDEN error.
# 	req = urllib2.Request(url , headers = {'User-Agent' : 'Magic Browser'})
# 	html = urllib2.urlopen(req)
# 	return BeautifulSoup(html , 'html.parser')
r = requests.get(SOUP_URL)
soup = BeautifulSoup(r.content,"html.parser")

def makeSoup(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content,"html.parser")
	return soup


pages = soup.find('div',{'class' : 'paging'})
pages  = pages.findAll('li')
# i =0
# for page in pages :
# 	print page ,'\n', '-'*50
# 	i+= 1
# 	print 'NUMBER ',i
# print '-*'*50
LAST_PAGE = pages[11]
NEXT_PAGE = pages[12]
LAST_PAGE_NUMBER = int(LAST_PAGE.text)
# print LAST_PAGE_NUMBER
# print NEXT_PAGE.find('a').get('href')
# print LAST_PAGE
# print '-|'*30
PAGE_TAG = '?page='

DONE_SERIES = 1



with open(FILENAME_MOVIES,'wb') as output :
	for i in range(1,LAST_PAGE_NUMBER+1):
		print 'Done : ',DONE_SERIES , 'Page Number : ',i
		if i == 1 :
			url = SOUP_URL
		else :
			url = SOUP_URL + PAGE_TAG+str(i)

		soup = makeSoup(url)

		# status , poster , link , name
		links = soup.findAll('div' , {'class':'item'})
		for link in links :
			# print link , '\n' , '-'*50
			try :
				poster = link.find('img').get('src')
			except :
				poster = 'nan'
			
			try :	
				status = link.find('div' , {'class' : 'status'}).text.replace('Eps','')
			except :
				status = 'nan'
			try :
				DONE_SERIES += 1
				showlink = link.find('a' , {'class' : 'name'})
				showname = showlink.text
				showlink = showlink.get('href')
				showlink = URL + showlink
			except :
				continue
			# print status 
			# print poster
			# print showlink
			# print showname
			newShow = show(status,poster,showlink,showname)
			pickle.dump(newShow,output,pickle.HIGHEST_PROTOCOL)
			





























