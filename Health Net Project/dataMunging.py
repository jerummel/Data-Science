# Clean up the data and put the pertinent columns into new csv files
import psycopg2
import sys
import math
import csv

def main():
	genderCase = "CASE sex WHEN '' THEN 'Unknown' ELSE sex END"
	ageCase = "CASE ageatfirstclaim WHEN '' THEN 'Unknown' ELSE ageatfirstclaim END"
	memberDrugCountQueryY1 = "SELECT memberid, drugcount FROM drug_count WHERE year = 'Y1' ORDER BY memberid;"
	memberOutcomeQueryY1 = "SELECT memberid FROM days_hosp_y2 ORDER BY memberid;"
	memberLabCountQueryY1 = "SELECT memberid, labcount FROM lab_count WHERE year = 'Y1' ORDER BY memberid;"
	claimCountQueryY1 = "SELECT memberid, count(*) FROM claims WHERE year = 'Y1' GROUP BY memberid ORDER BY memberid;"
	sexAgeTargetQueryY1 = "SELECT members.memberid, %s, %s, daysinhospital FROM members JOIN days_hosp_y2 ON (members.memberid = days_hosp_y2.memberid) ORDER BY memberid;" % (genderCase, ageCase)
	condQueryY1 = "SELECT memberid, primaryconditiongroup FROM claims WHERE year = 'Y1' ORDER BY memberid;"
	memberDrugCountQueryY2 = "SELECT memberid, drugcount FROM drug_count WHERE year = 'Y2' ORDER BY memberid;"
	memberOutcomeQueryY2 = "SELECT memberid FROM days_hosp_y3 ORDER BY memberid;"
	memberLabCountQueryY2 = "SELECT memberid, labcount FROM lab_count WHERE year = 'Y2' ORDER BY memberid;"
	claimCountQueryY2 = "SELECT memberid, count(*) FROM claims WHERE year = 'Y2' GROUP BY memberid ORDER BY memberid;"
	sexAgeTargetQueryY2 = "SELECT members.memberid, %s, %s, daysinhospital FROM members JOIN days_hosp_y3 ON (members.memberid = days_hosp_y3.memberid) ORDER BY memberid;" % (genderCase, ageCase)
	condQueryY2 = "SELECT memberid, primaryconditiongroup FROM claims WHERE year = 'Y2' ORDER BY memberid;"
	memberDrugCountQueryY3 = "SELECT memberid, drugcount FROM drug_count WHERE year = 'Y3' ORDER BY memberid;"
	memberOutcomeQueryY3 = "SELECT memberid FROM days_hosp_y4 ORDER BY memberid;"
	memberLabCountQueryY3 = "SELECT memberid, labcount FROM lab_count WHERE year = 'Y3' ORDER BY memberid;"
	claimCountQueryY3 = "SELECT memberid, count(*) FROM claims WHERE year = 'Y3' GROUP BY memberid ORDER BY memberid;"
	sexAgeTargetQueryY3 = "SELECT members.memberid, %s, %s FROM members JOIN days_hosp_y4 ON (members.memberid = days_hosp_y4.memberid) ORDER BY memberid;" % (genderCase, ageCase)
	condQueryY3 = "SELECT memberid, primaryconditiongroup FROM claims WHERE year = 'Y3' ORDER BY memberid;"
	con = None
	DB_NAME = 'healthnetdb'
	DB_USER = 'josephrummel'

	try:
		con = psycopg2.connect("dbname=%s user=%s" % (DB_NAME, DB_USER))
		keyTuple = ('memberid', 'sex', 'age', 'condition', 'drugcount', 'labcount', 'claimcount', 'daysinhospital')
		createFile(con, "cleanDataFiles/trainingData.csv", keyTuple, memberDrugCountQueryY1, memberOutcomeQueryY1, memberLabCountQueryY1, claimCountQueryY1, sexAgeTargetQueryY1, condQueryY1)
		createFile(con, "cleanDataFiles/testData.csv", keyTuple, memberDrugCountQueryY2, memberOutcomeQueryY2, memberLabCountQueryY2, claimCountQueryY2, sexAgeTargetQueryY2, condQueryY2)
		keyTupleY3 = ('memberid', 'sex', 'age', 'condition', 'drugcount', 'labcount', 'claimcount')
		createFile(con, "cleanDataFiles/predictData.csv", keyTupleY3, memberDrugCountQueryY3, memberOutcomeQueryY3, memberLabCountQueryY3, claimCountQueryY3, sexAgeTargetQueryY3, condQueryY3)
		
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

def createFile(con, filename, keyTuple, memberDrugCountQuery, memberOutcomeQuery, memberLabCountQuery, claimCountQuery, sexAgeTargetQuery, condQuery):
	# Do all database queries
	drugMember = querydb(con, memberDrugCountQuery)
	memberOutcome = querydb(con, memberOutcomeQuery)
	outcomeList = [row[0] for row in memberOutcome]
	labMember = querydb(con, memberLabCountQuery)
	claimCount = querydb(con, claimCountQuery)
	sexAgeTarget = querydb(con, sexAgeTargetQuery)
	condMember = querydb(con, condQuery)

	# Create all dictionaries that will be needed
	# The highest bin for drugs is >7 prescriptions.  9 was used because it was greater than
	# 7, but not so much so that it will skew the data too much.
	drugDict = createAvgDict(drugMember, outcomeList, '7+', 9)
	# The highest bin for drugs is >10 lab tests.  12 was used because it was greater than
	# 10, but not so much so that it will skew the data too much.
	labDict = createAvgDict(labMember, outcomeList, '10+', 12)
	sexDict = createDict(sexAgeTarget, outcomeList, 1, 'Unknown')
	ageDict = createDict(sexAgeTarget, outcomeList, 2, 'Unknown')
	claimDict = createDict(claimCount, outcomeList, 1, '0')
	condDict = createCondDict(con, condMember, outcomeList, sexDict, ageDict)
	if(len(sexAgeTarget[0]) == 4):
		targetDict = createDict(sexAgeTarget, outcomeList, 3, 'Unknown')
		finalDictList = createFinalDictList(outcomeList, [sexDict, ageDict, condDict, drugDict, labDict, claimDict, targetDict], keyTuple)
	else:
		finalDictList = createFinalDictList(outcomeList, [sexDict, ageDict, condDict, drugDict, labDict, claimDict], keyTuple)
	writeToCSV(finalDictList, filename, keyTuple)

def createAvgDict(countList, members, maxString, maxCount):
	newDict = {}
	for memberID, counts in memberIter(countList, 'labDrug', [maxString, maxCount]):
			countSum = sum(counts)
			countAvg = float(countSum)/float(len(counts))
			roundedAvg = int(roundedNum(countAvg))
			if(roundedAvg >= int(maxString[:len(maxString)-1])):
				newDict[memberID] = maxString
			else:
				newDict[memberID] = str(roundedAvg)

	#find the members who had 0 for a count
	membersWithCounts = set([row[0] for row in countList])
	diffList = [memberID for memberID in members if memberID not in membersWithCounts]
	for memberID in diffList:
		newDict[memberID] = '0'
	return newDict

def roundedNum(floatNum):
	testNum =  floatNum - math.floor(floatNum)
	if(testNum >= 0.5):
		return math.ceil(floatNum)
	else:
		return math.floor(floatNum)

def createDict(countList, members, valueColNum, nullVal):
	newDict = {row[0]: row[valueColNum] for row in countList}
	#find the members who had 0 for a count
	membersWithCounts = set([row[0] for row in countList])
	diffList = [memberID for memberID in members if memberID not in membersWithCounts]
	for memberID in diffList:
		newDict[memberID] = nullVal
	return newDict

def createCondDict(con, condList, members, sexDict, ageDict):
	newDict = {}
	binaryList = []
	for memberID, conditions in memberIter(condList, 'condition', [sexDict, ageDict]):
		if(ageDict[memberID] == '70-79' or ageDict[memberID] == '80+'):
			columnName = 'adminriskg70'
		else:
			columnName = 'adminriskl70'
		allConditions = querydb(con, "SELECT primcondgrp from primary_condition ORDER BY %s DESC, primcondgrp;" % columnName)
		conditionsList = [row[0] for row in allConditions]
		for cond in conditionsList:
			if cond in conditions:
				binaryList.append('1')
			else:
				binaryList.append('0')
		binaryString = "".join(binaryList)
		newDict[memberID] = binaryString
		binaryList = []

	#find the members who had 0 conditons, if any
	membersWithCounts = set([row[0] for row in condList])
	diffList = [memberID for memberID in members if memberID not in membersWithCounts]
	for memberID in diffList:
		binaryList = ['0' for i in conditionsList]
		binaryString = "".join(binaryList)
		newDict[memberID] = binaryString
	return newDict

def memberIter(thisList, action, paramsList):
	newList = []
	oldID = thisList[0][0]
	for row in thisList:
		if(row[0] == oldID):
			if(action == 'labDrug'):
				if(row[1] == paramsList[0]):
					newList.append(paramsList[1])
				else:
					newList.append(int(row[1]))
			elif(action == 'condition'):
				# Check for conditions that make no sense (i.e. pregnant men) and don't include them
				if(isBadData(paramsList[0], paramsList[1], row[0], row[1])):
					continue
				else:
					newList.append(row[1])
		else:
			yield [oldID, newList]
			# reset newList and oldID for the next member
			if(action == 'labDrug'):
				if(row[1] == paramsList[0]):
					newList = [paramsList[1], ]
				else:
					newList = [int(row[1])]
			elif(action == 'condition'):
				if(isBadData(paramsList[0], paramsList[1], row[0], row[1])):
					newList = []
				else:
					newList = [row[1], ]
			oldID = row[0]
	yield [oldID, newList]

def isBadData(sexDict, ageDict, memberid, condition):
	sex = sexDict[memberid]
	age = ageDict[memberid]
	# Check for males that have gyencological issues, female breast cancer, or pregnancy
	if(sex == 'M' and (condition == 'GYNEC1' or condition == 'GYNECA' or condition == 'PRGNCY')):
		return True
	# Check for people that are pregnant or perinatal and over 80, between 70-79, or between 60-69 years old
	elif((condition == 'PRGNCY'  or condition == 'PERINTL') and (age == '80+' or age == '70-79' or age == '60-69')):
		return True
	# Check for males that are not between 0-9 years old and are under the perinatal period condition
	# The perinatal period covers treatment for both mother and baby (including male babies), so
	# that is why males 0-9 are OK
	elif(sex == 'M' and condition == 'PERINTL' and age != '0-9'):
		return True
	# Check for children under 10 who are pregnant
	elif(condition == 'PRGNCY' and age == '0-9'):
		return True
	else:
		return False

def createFinalDictList(members, list_of_dicts, list_of_keys):
	newDict = {}
	dictList = []
	for memberID in members:
		newDict[list_of_keys[0]] = memberID
		for i in range(1, len(list_of_keys)):
			newDict[list_of_keys[i]] = list_of_dicts[i-1][memberID]
		dictList.append(newDict)
		newDict = {}	
	return dictList

def writeToCSV(dictData, fileName, headers):
	writer = csv.DictWriter(open(fileName, 'w'), headers, delimiter=',')
	writer.writeheader()

	for memberInfo in dictData:
		writer.writerow(memberInfo)
		
if __name__ == "__main__": main()