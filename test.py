# -*- coding: utf-8 -*-
import data

# db = data.Data()
# str = "AAS 100"
# index = str.find(' ')
# subject = str[0: index]
# num = str[index + 1: len(str)]
#
# count = 0
# foundClass = list()
# for course in db.dataBase:
#     if course['Subject'] == subject and course['Course'] == num :
#         count += 1
#         foundClass.append(course)
#
# print "found" , count , "classes"
# db = data.Data()
# str = "AAS 100"
# index = str.find(' ')
# subject = str[0: index]
# num = str[index + 1: len(str)]
#
# count = 0
# foundClass = list()
# for course in db.dataBase:
#     if course['Subject'] == subject and course['Course'] == num :
#         count += 1
#         foundClass.append(course)
#
# print "found" , count , "classes"
# db = data.Data()
# str = "AAS 100"
# index = str.find(' ')
# subject = str[0: index]
# num = str[index + 1: len(str)]
#
# count = 0
# foundClass = list()
# for course in db.dataBase:
#     if course['Subject'] == subject and course['Course'] == num :
#         count += 1
#         foundClass.append(course)
#
# print "found" , count , "classes"


# print db.dataBase[0]['Subject'] + "\n" + db.dataBase[0]['Subject']
# print db.dataBase[0]['Course']
# print db.dataBase[0]['Course Title']
# print db.dataBase[0]['A+']
# print db.dataBase[0]['A']
# print db.dataBase[0]['A-']
# print db.dataBase[0]['B+']
# print db.dataBase[0]['B']
# print db.dataBase[0]['B-']
# print db.dataBase[0]['C+']
# print db.dataBase[0]['C']
# print db.dataBase[0]['C-']
# print db.dataBase[0]['D+']
# print db.dataBase[0]['D']
# print db.dataBase[0]['D-']
# print db.dataBase[0]['F']
# print db.dataBase[0]['W']
# print db.dataBase[0]['Average Grade']
# print db.dataBase[0]['Primary Instructor']
#
# str = "CS 125"
# index = str.find(' ')
# subject = str[0: index]
# num = str[index + 1: len(str)]
#
# count = 0
# foundClass = list()
# for course in db.dataBase:
#     if course['Subject'] == subject and course['Course'] == num :
#         count += 1
#         foundClass.append(course)
#
# print "found" , count , "classes"
# for c in foundClass:
#     print c['Subject'] , c['Course'], c['Average Grade']
# count = 3
# content = ""
# content += "Found "+ str(count)+ " sections!"+ "\n"
# for c in db.dataBase:
#     content += c['Subject']+ c['Course']+ " "+ c['Average Grade']+ "\n"
# print content

db = data.Data()
avg = 0.0
s = [2,3,4]
avg += float(db.dataBase[0]['Average Grade'])
avg /= len(s)
print avg
a = 0
a = int(db.dataBase[0]['A+'])
print a
