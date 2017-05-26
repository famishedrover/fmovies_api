import pickle
from allclasses import show
FILENAME_TV_SHOW = 'tv_show_data.pkl'
FILENAME_MOVIES = 'movies.pkl'


def printDetails(x) :
	print x.name
	# print x.status
	# print x.poster
	print x.link

def findMyShow(showname , FILENAME = FILENAME_TV_SHOW) :
	foundDict = {}
	i = 0 
	flag = False
	with open(FILENAME , 'rb') as inp :
		while True :
			try :
				xs = pickle.load(inp)
			except :
				break
			
			if showname in (xs.name).lower() :
				i+= 1
				flag = True 
				foundDict[i] = xs
				print i,'---',
				print xs.name


	return flag,foundDict
def findMyShowIO(showname,FILENAME) :
	f,fdict = findMyShow(showname)
	if f is True :
		num = raw_input('<Which Show (by number)>')
		print '-'*50
		printDetails(fdict[int(num)])
		print '-'*50
	else :
		print 'No such shows found..'

# movie or tv :: mt
mt = raw_input('< 1.Movie || 2.TV Show >')
if int(mt) == 1 :
	mt = True 
	print 'Movie Selected.'
elif int(mt) == 2 :
	mt = False
	print 'TV selected.' 
else :
	mt = False 
	print 'Default : TV selected.'

if mt is True :
	FILENAME = FILENAME_MOVIES
else :
	FILENAME = FILENAME_TV_SHOW


myShowName = raw_input('<ShowName>')

findMyShowIO(myShowName,FILENAME)








