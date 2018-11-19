# python database API

# the python db api provides a common interface for various db engines
#
# when using SQLite, the sqlite db that you make
# will be fully contained in one file, which is completely portable;
# you can use the same file on windows, mac, or linux, etc,
# and then use it while interfacing with any SQL lite driver in any language
#
# rem the python db api interface is fine for casual usage, but if you need
# to do more significant stuff, then you will want to create a dedicated class
# and/or module that provides a more robust interface for your program needs
#

import sqlite3

def main():
    print('connect')
    
    # call connect on sqlite3 object to return a handle
    # and create .db file
    db = sqlite3.connect('db-api.db')
    
    # use handle to interface with db;
    # get a cursor from db handle to keep track of db loc as
    # we run db commands
    cur = db.cursor() 
    
    # create table: 'test'
    #     id    |    string    |    number
    #    (int)  |    (text)    |    (int)
    #           |    'one'     |      1
    #           |    'two'     |      2
    #           |    'three'   |      3    
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    
    # commit new rows to db.file
    print('commit')
    db.commit()
    
    # run a query on newly inserted table data
    print('count')
    
    # use cursor loc to grab a count of # rows in table 'test'
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    
    # select and print all rows in the test table
    print('read')
    print('id    |    str    |    num    ')
    for row in cur.execute("SELECT * FROM test"):
        # print(row)
        print(row[0], '        ', row[1], '        ', row[2])
        
    # drop the table 'test'
    print('drop')
    cur.execute("DROP TABLE test")
    
    # close the db connection    
    print('close')    
    db.close()

if __name__ == '__main__': main()
