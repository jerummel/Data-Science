# Add weights for each condition in the primary_condition table in the database

import psycopg2
import sys

def main():
	alterTableQuery = "ALTER TABLE primary_condition ADD COLUMN adminriskl70 int, ADD COLUMN adminriskg70 int;"
	con = None
	DB_NAME = 'healthnetdb'
	DB_USER = 'josephrummel'
	fh=open('Data/conditionWeights.csv')

	try:
		con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
		cur = con.cursor()
		cur.execute(alterTableQuery)
		con.commit()
		firstLine = True
		for line in fh:
			if firstLine:
				firstLine = False
				continue
			else:
				line=line.strip()
				row_of_data = line.split(',' ,)
				pcg = row_of_data[0]
				adminl70 = row_of_data[1]
				adming70 = row_of_data[2]
				cur.execute("UPDATE primary_condition SET adminriskl70 = %s, adminriskg70 = %s WHERE primcondgrp = '%s';" % (adminl70, adming70, pcg))
				con.commit()

		
	except psycopg2.DatabaseError, e:

		if con:
			con.rollback()

		print 'Error %s' % e
		sys.exit(1)

	finally:

		if con:
			con.close()
		
if __name__ == "__main__": main()