# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import receive
import reply
import data

class Handle(object):
   def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "ricky" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

   def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            #后台打日志
            recMsg = receive.parse_xml(webData)
            
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = ""
                #代表可以使用
                if " " in recMsg.Content :
                    db = data.Data()
                    str1 = recMsg.Content
                    index = str1.find(' ')
                    subject = str1[0: index]
                    num = str1[index + 1: len(str1)]
                    count = 0
                    foundClass = list()
                    for course in db.dataBase:
                        if course['Subject'].lower() == subject.lower() and course['Course'] == num :
                            count += 1
                            foundClass.append(course)
                    if count <= 0:
                        content ="Ricky找不到 " + recMsg.Content+ " 请重新输入！"
                    else:
                        avgGpa = 0.0
                        student = 0
                        for c1 in foundClass:
                            student += calculateStudentNum(c1)
                            avgGpa += (float(c1['Average Grade'])*calculateStudentNum(c1))
                        avgGpa /= student
                        content +="Average GPA of the course: "+ str(avgGpa) +"\n"
                        content +="Found "+ str(count)+ " sections!"+ "\n"
                        for c in foundClass:
                            content += c['Subject']+ c['Course']+" "+ c['Average Grade']+ "\n"
                            content += "Instructor: "+ c['Primary Instructor'] +"\n"

                else:
                    content = "Ricky无法识别课程ID, 请重新输入！"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
def checkOverlap(str):
        a = list(str)
        n = len(a)
        for i in range(n):
            if str.count(a[i]) != 1:
                return False
        return True

def calculateStudentNum(course):
    sum = 0;
    sum += int(course['A+'])
    sum += int(course['A'])
    sum += int(course['A-'])
    sum += int(course['B+'])
    sum += int(course['B'])
    sum += int(course['B-'])
    sum += int(course['C+'])
    sum += int(course['C'])
    sum += int(course['C-'])
    sum += int(course['D+'])
    sum += int(course['D'])
    sum += int(course['D-'])
    sum += int(course['F'])
    return sum
