# Create the plots to be used for Exploratory Data Analysis

import psycopg2
import sys
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
	genderCase = "CASE sex WHEN '' THEN 'Unkown' ELSE sex END"
	ageCase = "CASE ageatfirstclaim WHEN '' THEN 'Unkown' ELSE ageatfirstclaim END"
	condCase = "CASE primaryconditiongroup WHEN '' THEN 'Unkown' ELSE primaryconditiongroup END"
	generalQueryY1 = "SELECT daysinhospital, count(memberid) from days_hosp_y2 GROUP BY daysinhospital ORDER BY daysinhospital;"
	generalQueryY2 = "SELECT daysinhospital, count(memberid) from days_hosp_y3 GROUP BY daysinhospital ORDER BY daysinhospital;"
	genderQueryY1 = "SELECT daysinhospital, %s, count(days_hosp_y2.memberid) from days_hosp_y2 JOIN members ON (members.memberid = days_hosp_y2.memberid) GROUP BY daysinhospital, sex ORDER BY daysinhospital, sex;" % genderCase
	genderQueryY2 = "SELECT daysinhospital, %s, count(days_hosp_y3.memberid) from days_hosp_y3 JOIN members ON (members.memberid = days_hosp_y3.memberid) GROUP BY daysinhospital, sex ORDER BY daysinhospital, sex;" % genderCase
	genderCountQueryY1 = "SELECT %s, count(*) from members JOIN days_hosp_y2 ON (members.memberID = days_hosp_y2.memberid) GROUP BY sex ORDER BY sex;" % genderCase
	genderCountQueryY2 = "SELECT %s, count(*) from members JOIN days_hosp_y3 ON (members.memberID = days_hosp_y3.memberid) GROUP BY sex ORDER BY sex;" % genderCase
	ageCountQueryY1 = "SELECT %s, count(*) from members JOIN days_hosp_y2 ON (members.memberID = days_hosp_y2.memberid) GROUP BY ageatfirstclaim ORDER BY ageatfirstclaim;" % ageCase
	ageCountQueryY2 = "SELECT %s, count(*) from members JOIN days_hosp_y3 ON (members.memberID = days_hosp_y3.memberid) GROUP BY ageatfirstclaim ORDER BY ageatfirstclaim;" % ageCase
	ageQueryY1 = "SELECT daysinhospital, %s, count(days_hosp_y2.memberid) from days_hosp_y2 JOIN members ON (members.memberid = days_hosp_y2.memberid) GROUP BY daysinhospital, ageatfirstclaim ORDER BY daysinhospital, ageatfirstclaim;" % ageCase
	ageQueryY2 = "SELECT daysinhospital, %s, count(days_hosp_y3.memberid) from days_hosp_y3 JOIN members ON (members.memberid = days_hosp_y3.memberid) GROUP BY daysinhospital, ageatfirstclaim ORDER BY daysinhospital, ageatfirstclaim;" % ageCase
	viewCreate1 = "CREATE OR REPLACE VIEW Condition_View1 AS SELECT DISTINCT memberid, primaryconditiongroup FROM claims WHERE year = 'Y1';"
	viewCreate2 = "CREATE OR REPLACE VIEW Condition_View2 AS SELECT DISTINCT memberid, primaryconditiongroup FROM claims WHERE year = 'Y2';"
	condCountQueryY1 = "SELECT %s, count(*) FROM Condition_View1 GROUP BY primaryconditiongroup ORDER BY primaryconditiongroup;" % condCase
	condCountQueryY2 = "SELECT %s, count(*) FROM Condition_View2 GROUP BY primaryconditiongroup ORDER BY primaryconditiongroup;" % condCase
	viewCreate3 = "CREATE OR REPLACE VIEW Condition_View3 AS SELECT DISTINCT claims.memberid, primaryconditiongroup, sex FROM claims JOIN members ON (claims.memberid = members.memberid) WHERE year = 'Y1';"
	viewCreate4 = "CREATE OR REPLACE VIEW Condition_View4 AS SELECT DISTINCT claims.memberid, primaryconditiongroup, sex FROM claims JOIN members ON (claims.memberid = members.memberid) WHERE year = 'Y2';"
	condGenderQueryY1 = "SELECT %s, %s, count(*) FROM Condition_View3 GROUP BY primaryconditiongroup, sex ORDER BY primaryconditiongroup, sex;" % (condCase, genderCase)
	condGenderQueryY2 = "SELECT %s, %s, count(*) FROM Condition_View4 GROUP BY primaryconditiongroup, sex ORDER BY primaryconditiongroup, sex;" % (condCase, genderCase)
	viewCreate5 = "CREATE OR REPLACE VIEW Condition_View5 AS SELECT memberid, count(*) AS claimcount FROM claims WHERE year = 'Y1' GROUP BY memberid;"
	claimQueryY1 = "SELECT daysinhospital, sum(claimcount) FROM days_hosp_y2 JOIN Condition_View5 ON (days_hosp_y2.memberid = Condition_View5.memberid) GROUP BY daysinhospital ORDER BY daysinhospital;"
	viewCreate6 = "CREATE OR REPLACE VIEW Condition_View6 AS SELECT memberid, count(*) AS claimcount FROM claims WHERE year = 'Y2' GROUP BY memberid;"
	claimQueryY2 = "SELECT daysinhospital, sum(claimcount) FROM days_hosp_y3 JOIN Condition_View6 ON (days_hosp_y3.memberid = Condition_View6.memberid) GROUP BY daysinhospital ORDER BY daysinhospital;"
	con = None
	DB_NAME = 'healthnetdb'
	DB_USER = 'josephrummel'

	try:
		con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
		generalDataY1 = querydb(con, generalQueryY1)
		generalSeriesY1 = getSeries(generalDataY1, True, False)
		plotFigure(generalSeriesY1, False, "bar", "Length of Hospital Stay In Year 1", "Number of Days In Hospital", "Number of People", False, False, (8, 8), 0, 1, "Plots/generalNoLogY1.png")
		generalDataY1 = querydb(con, generalQueryY1)
		generalSeriesY1 = getSeries(generalDataY1, True, True)
		plotFigure(generalSeriesY1, False, "bar", "Length of Hospital Stay In Year 1", "Number of Days In Hospital", "Log Base 10 of Number of People", False, False, (8, 8), 0, 1, "Plots/generalY1.png")
		generalDataY2 = querydb(con, generalQueryY2)
		generalSeriesY2 = getSeries(generalDataY2, True, True)
		plotFigure(generalSeriesY2, False, "bar", "Length of Hospital Stay In Year 2", "Number of Days In Hospital", "Log Base 10 of Number of People", False, False, (8, 8), 0, 1, "Plots/generalY2.png")
		genderDataY1 = querydb(con, genderQueryY1)
		genderDataFrameY1 = getDataFrame(genderDataY1, "Gender", True, True)
		plotFigure(genderDataFrameY1, True, "barh", "Length of Hospital Stay By Gender In Year 1", "Percent of People", "Number of Days In Hospital", True, True, (13, 10), 0, 3, "Plots/genderY1.png")
		genderDataY2 = querydb(con, genderQueryY2)
		genderDataFrameY2 = getDataFrame(genderDataY2, "Gender", True, True)
		plotFigure(genderDataFrameY2, True, "barh", "Length of Hospital Stay By Gender In Year 2", "Percent of People", "Number of Days In Hospital", True, True, (13, 10), 0, 3, "Plots/genderY2.png")
		genderCountDataY1 = querydb(con, genderCountQueryY1)
		genderCountSeriesY1 = getSeries(genderCountDataY1, False, False)
		plotFigure(genderCountSeriesY1, False, "bar", "Count of People By Gender In Year 1", "Gender", "Number of People", False, False, (8, 8), 0, 1, "Plots/genderCountY1.png")
		genderCountDataY2 = querydb(con, genderCountQueryY2)
		genderCountSeriesY2 = getSeries(genderCountDataY2, False, False)
		plotFigure(genderCountSeriesY2, False, "bar", "Count of People By Gender In Year 2", "Gender", "Number of People", False, False, (8, 8), 0, 1, "Plots/genderCountY2.png")
		ageCountDataY1 = querydb(con, ageCountQueryY1)
		ageCountSeriesY1 = getSeries(ageCountDataY1, False, False)
		plotFigure(ageCountSeriesY1, False, "bar", "Count of People By Age In Year 1", "Age", "Number of People", False, False, (8, 8), 0, 1, "Plots/ageCountY1.png")
		ageCountDataY2 = querydb(con, ageCountQueryY2)
		ageCountSeriesY2 = getSeries(ageCountDataY2, False, False)
		plotFigure(ageCountSeriesY2, False, "bar", "Count of People By Age In Year 2", "Age", "Number of People", False, False, (8, 8), 0, 1, "Plots/ageCountY2.png")
		ageDataY1 = querydb(con, ageQueryY1)
		ageDataFrameY1 = getDataFrame(ageDataY1, "Age", True, True)
		plotFigure(ageDataFrameY1, True, "barh", "Length of Hospital Stay By Age In Year 1", "Percent of People", "Number of Days In Hospital", True, True, (14, 8), 0, 10, "Plots/ageY1.png")
		ageDataY2 = querydb(con, ageQueryY2)
		ageDataFrameY2 = getDataFrame(ageDataY2, "Age", True, True)
		plotFigure(ageDataFrameY2, True, "barh", "Length of Hospital Stay By Age In Year 2", "Percent of People", "Number of Days In Hospital", True, True, (14, 8), 0, 10, "Plots/ageY2.png")
		querydb(con, viewCreate1)
		condCountDataY1 = querydb(con, condCountQueryY1)
		condCountSeriesY1 = getSeries(condCountDataY1, False, False)
		plotFigure(condCountSeriesY1, False, "bar", "Count of People By Condition In Year 1", "Condition", "Number of People", False, False, (22, 12), 90, 1, "Plots/condCountY1.png")
		querydb(con, viewCreate2)
		condCountDataY2 = querydb(con, condCountQueryY2)
		condCountSeriesY2 = getSeries(condCountDataY2, False, False)
		plotFigure(condCountSeriesY2, False, "bar", "Count of People By Condition In Year 2", "Condition", "Number of People", False, False, (22, 12), 90, 1, "Plots/condCountY2.png")
		querydb(con, viewCreate3)
		condGenderDataY1 = querydb(con, condGenderQueryY1)
		condGenderDataFrameY1 = getDataFrame(condGenderDataY1, "Gender", False, True)
		plotFigure(condGenderDataFrameY1, True, "barh", "Percentage In Each Gender Per Condition In Year 1", "Percent of People", "Condition", True, True, (14, 20), 0, 3, "Plots/condGenderCountY1.png")
		querydb(con, viewCreate4)
		condGenderDataY2 = querydb(con, condGenderQueryY2)
		condGenderDataFrameY2 = getDataFrame(condGenderDataY2, "Gender", False, True)
		plotFigure(condGenderDataFrameY2, True, "barh", "Percentage In Each Gender Per Condition In Year 2", "Percent of People", "Condition", True, True, (14, 20), 0, 3, "Plots/condGenderCountY2.png")
		querydb(con, viewCreate5)
		claimDataY1 = querydb(con, claimQueryY1)
		claimSeriesY1 = getSeries(claimDataY1, True, True)
		plotFigure(claimSeriesY1, False, "bar", "Number of Claims vs. Days in Hospital in Year 1", "Days in Hospital", "Log Base 10 of Number of Claims", False, False, (8, 8), 0, 1, "Plots/claimY1.png")
		querydb(con, viewCreate6)
		claimDataY2 = querydb(con, claimQueryY2)
		claimSeriesY2 = getSeries(claimDataY2, True, True)
		plotFigure(claimSeriesY2, False, "bar", "Number of Claims vs. Days in Hospital in Year 2", "Days in Hospital", "Log Base 10 of Number of Claims", False, False, (8, 8), 0, 1, "Plots/claimY2.png")
	except psycopg2.DatabaseError, e:

		if con:
			con.rollback()

		print 'Error %s' % e
		sys.exit(1)

	finally:

		if con:
			con.close()

def querydb(connection, query):
	cur = connection.cursor()
	cur.execute(query)
	if(cur.rowcount != -1):
		tableData = cur.fetchall()
		return tableData

def getSeries(data, changeIdxToString, takeLog):
	dataList = [[row[i] for row in data] for i in range(len(data[0]))]
	if(changeIdxToString):
		dataList[0] = [str(data) for data in dataList[0]]
		dataList[0][len(dataList[0])-1] = dataList[0][len(dataList[0])-1] + "+"
	if(takeLog):
		dataList[1] = [math.log(data, 10) for data in dataList[1]]
	return Series(dataList[1], index=dataList[0])

def getDataFrame(data, legendName, changeIdxToString, takePercent):
	columnList = []
	indexList = []
	for row in data:
		if(row[1] not in columnList):
			columnList.append(row[1])
		if(row[0] not in indexList):
			indexList.append(row[0])
	dataList = [[] for idx in indexList]
	for i, idx in enumerate(indexList):
		for col in columnList:
			resultList = [row[2] for row in data if row[0] == idx and row[1] == col]
			if(resultList == []):
			 	dataList[i].append(0)
			else:
			 	dataList[i].append(resultList[0])
	if(changeIdxToString):
		indexList = [str(idx) for idx in indexList]
		indexList[len(indexList)-1] = indexList[len(indexList)-1] + '+'
	if(takePercent):
		for i, row in enumerate(dataList):
			rowSum = sum(row)
			newRow = [float(value)/rowSum*100 for value in row]
			dataList[i] = newRow
	return DataFrame(np.array(dataList), index=indexList, columns=pd.Index(columnList, name=legendName))


def plotFigure(df, isDataFrame, graphKind, figTitle, xLabel, yLabel, hasLegend, isStacked, figureSize, rotation, num_colors, fileName):
	fig = plt.figure()
	colors = plt.get_cmap('jet')(np.linspace(0, 1.0, num_colors))
	subplot = fig.add_subplot(111)
	if(isStacked):
		df.plot(kind = graphKind, stacked = True, color=colors, ax=subplot, title=figTitle, legend=hasLegend, figsize = figureSize, rot=rotation)
	else:
		df.plot(kind = graphKind, color=colors, ax=subplot, title=figTitle, legend=hasLegend, figsize = figureSize, rot=rotation)
	subplot.set_xlabel(xLabel)
	subplot.set_ylabel(yLabel)

	# Create the scale to be used for the y-axis
	if(isDataFrame):
		if(isStacked):
			dSeries = df.sum(1)
		else:
			dSeries = df.max(1)
	else:
		dSeries = df
	maxVal = dSeries.max()
	step = pow(10, int(math.log(maxVal, 10)))
	if(maxVal - step < int(maxVal/2)):
		step /= 10
	scale = np.arange(0, maxVal+3*step, step)
	if(graphKind == 'barh'):
		plt.xticks(scale)
	else:
		plt.yticks(scale)
		
	fig.savefig(fileName)

if __name__ == "__main__": main()