import psycopg2
import sys

row_of_data=[]
list_of_rows=[]
DB_NAME = 'healthnetdb'
DB_USER = 'josephrummel'

# Opens a handle to the file, but does not read anything yet.
# fh=open('Data/DaysInHospital_Y2.csv')
# fh=open('Data/DaysInHospital_Y3.csv')
fh=open('Data/Target.csv')

con = None

try:
	con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
	cur = con.cursor()
	
	firstLine = True
	for line in fh:
		if firstLine:
			firstLine = False
			continue
		# Strip off leading and trailing white-space.
		line=line.strip()
		row_of_data=line.split(',',)
		#valString = "'%s', %s, %s" % (row_of_data[0], row_of_data[1], row_of_data[2])
		valString = "'%s', %s" % (row_of_data[0], row_of_data[1])
		#query = "INSERT INTO days_hosp_y2 VALUES(%s);" % valString
		#query = "INSERT INTO days_hosp_y3 VALUES(%s);" % valString
		query = "INSERT INTO days_hosp_y4 VALUES(%s);" % valString
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
