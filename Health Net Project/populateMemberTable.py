import psycopg2
import sys

row_of_data=[]

# Opens a handle to the file, but does not read anything yet.
fh=open('Data/Members.csv')
con = None
DB_NAME = 'healthnetdb'
DB_USER = 'josephrummel'

try:
	con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
	cur = con.cursor()
	firstLine = True
	for line in fh:
		if firstLine:
			firstLine = False
			line = line.strip()
			row_of_data = line.split(',',)
			query = "CREATE TABLE members (%s varchar(10) PRIMARY KEY, %s varchar(5), %s varchar(1) );" % (row_of_data[0], row_of_data[1], row_of_data[2])
		else:
			# Strip off leading and trailing white-space.
			line=line.strip()
			row_of_data = line.split(',' ,)
			valString = "'%s', '%s', '%s'" % (row_of_data[0], row_of_data[1], row_of_data[2])
			query = "INSERT INTO members VALUES(%s);" % valString
			cur.execute(query)
			con.commit()
						
except psycopg2.DatabaseError, e:

	if con:
		con.rollback()

	print 'Error %s' % e
	sys.exit(1)

finally:

	if con:
		con.close()
