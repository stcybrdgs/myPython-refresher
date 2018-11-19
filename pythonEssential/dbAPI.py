# python database api
# rem the python database api provides a common interface for various db engines;
#     python ships with SQLite--> fully functional, x-platform, and
#     suitable for online and mobile apps

import sqlite3

def main():
	print('connect to db')
	db = sqlite3.connect('db-api.db')



if __name__=='__main__': main()