import psycopg2
import sys

row_of_data=[]
list_of_rows=[]
DB_NAME = 'healthnetdb'
DB_USER = 'josephrummel'

# Opens a handle to the file, but does not read anything yet.
#fh=open('Data/Lookup PrimaryConditionGroup.csv')
fh=open('Data/Lookup ProcedureGroup.csv')

con = None

try:
	con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
	cur = con.cursor()
	firstLine = True
	for line in fh:
		if firstLine:
			firstLine = False
			continue
		else:
			# Strip off leading and trailing white-space.
			line=line.strip()
			if(line.find('"') < 0):
				row_of_data=line.split(',',)
			else:
				row_of_data = line.split(',"',)
			valString = "'%s', '%s'" % (row_of_data[0], row_of_data[1])
			#query = "INSERT INTO primary_condition VALUES(%s);" % valString
			query = "INSERT INTO procedure_group VALUES(%s);" % valString
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
