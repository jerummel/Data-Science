import psycopg2
import sys

row_of_data=[]
DB_NAME = 'healthnetdb'
DB_USER = 'josephrummel'

# Opens a handle to the file, but does not read anything yet.
#fh=open('Data/DrugCount.csv')
fh=open('Data/LabCount.csv')
con = None

try:
	con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
	cur = con.cursor()
	# This is more memory efficient.
	# Reads one line at a time.
	firstLine = True
	for line in fh:
		if firstLine:
			firstLine = False
			line = line.strip()
			header_row = line.split(',',)
			# query = "CREATE TABLE drug_count ( id SERIAL, %s varchar(10), %s varchar(2), %s varchar(15), %s varchar(2) );" % (header_row[0], header_row[1], header_row[2], header_row[3])
			query = "CREATE TABLE lab_count ( id SERIAL, %s varchar(10), %s varchar(2), %s varchar(15), %s varchar(3) );" % (header_row[0], header_row[1], header_row[2], header_row[3])
		else:
			# Strip off leading and trailing white-space.
			line=line.strip()
			row_of_data = line.split(',' ,)
			valString = "'%s', '%s', '%s', '%s'" % (row_of_data[0], row_of_data[1], row_of_data[2], row_of_data[3])
			#query = "INSERT INTO drug_count (%s, %s, %s, %s) VALUES(%s);" % (header_row[0], header_row[1], header_row[2], header_row[3], valString)
			query = "INSERT INTO lab_count (%s, %s, %s, %s) VALUES(%s);" % (header_row[0], header_row[1], header_row[2], header_row[3], valString)
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
