# Populate the pSQL table that contains the claims information
import psycopg2
import sys

row_of_data=[]
DB_NAME = 'healthnetdb'
DB_USER = 'josephrummel'

# Opens a handle to the file, but does not read anything yet.
fh=open('Data/Claims.csv')
con = None

try:
	con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
	cur = con.cursor()
	firstLine = True
	for line in fh:
		if firstLine:
			firstLine = False
			line = line.strip()
			header_row = line.split(',',)
			headString = "id SERIAL"
			for header in header_row:
				headString += ", %s varchar" % header
			query = "CREATE TABLE claims (%s);" % headString
			headString = ""
			for i in range(0, len(header_row)):
				header = header_row[i]
				if(i == 0):
					headString += header
				else:
					headString += ", %s" % header
		else:
			# Strip off leading and trailing white-space.
			line=line.strip()
			row_of_data = line.split(',' ,)
			valString = ""
			for i in range(0, len(row_of_data)):
				val = row_of_data[i]
				if(i == 0):
					valString += "'%s'" % val
				else:
					valString += ", '%s'" % val
			
			query = "INSERT INTO claims (%s) VALUES(%s);" % (headString, valString)
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
