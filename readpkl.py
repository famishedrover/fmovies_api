import pickle
from allclasses import show
FILENAME = 'tv_show_data.pkl'


i = 0 
with open(FILENAME , 'rb') as inp :
	while True :
		try :
			xs = pickle.load(inp)
		except :
			break
		# print xs.status
		# print xs.name
		# print xs.link
		# print xs.poster
		# print '-'*40
		i += 1

print i 