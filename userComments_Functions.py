import requests
import sys
import common
import json
__author__ = 'Yafit'


# ========== USER COMMENTS =========
def userComments(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Query User Comments
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/comments', headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            return r.content
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def createNewComment(ip, reqCookie, comment, commentType="POINT", level="INFORMATION"):
    """
    :param ip:
    :param reqCookie:
    :param comment:
    :param level: WARNING/ERROR/INFORMATION
    :param commentType: POINT
    :return: Create New User Comment
    """
    common.print_frame()
    payload = {"xid": "null",
               "name": "null",
               "timestamp": 0,
               "commentType": commentType,
               "comment": comment,
               "username": "",
               "modelType": "null",
               "userId": 0,
               "referenceId": 0,
               "validationMessages": [{"message": "",
                                       "level": level,
                                       "property": ""}]}
    parameters_json = json.dumps(payload)
    myHeader = {'Accept': 'application/json',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Content-Type': 'application/json; charset=UTF-8',
                'Connection': 'keep-alive'}
    try:
        r = requests.post(ip + '/rest/v1/comments', headers=myHeader, data=parameters_json, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The comment was saved!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def getCommentsExplainQuery(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get Explaination For Query
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/comments/explain-query', headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            return r.content
        else:
            print "error occured"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def getAllUserComments(ip, reqCookie, limit):
    """
    :param ip:
    :param reqCookie:
    :param limit:
    :return: Get all User Comments
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/comments/list?limit=' + str(limit), headers=myHeader, cookies=reqCookie)

        if r.status_code == 200 or r.status_code == 201:
            return r.content
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)
