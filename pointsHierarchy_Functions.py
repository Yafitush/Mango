import requests
import sys
import common
__author__ = 'Yafit'


# ========= POINT HIERARCHY ============
def getPointHierarchyFolderByName(ip, reqCookie, folderName):
    """
    :param ip:
    :param reqCookie:
    :param folderName:
    :return: Get point hierarchy folder by name
    """
    common.print_frame()
    numOfWOrdes = len(folderName.split())
    newName = ""
    i = 0
    while i < numOfWOrdes - 1:
        newName = newName + folderName.split()[i] + '%20'
        i += 1
    newName = newName + folderName.split()[i]
    print newName
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/hierarchy/by-name/' + newName, headers=myHeader, cookies=reqCookie)
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


def getPointHierarchy(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get full point hierarchy
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/hierarchy/full', headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            return r.content
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def getPathToPointByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: point data Xid
    :return: Get path to a point using point's XID
    """
    common.print_frame()
    numOfWOrdes = len(Xid.split())
    newXid = ""
    i = 0
    while i < numOfWOrdes - 1:
        newXid = newXid + Xid.split()[i] + '%20'
        i += 1
    newXid = newXid + Xid.split()[i]
    print newXid
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/hierarchy/path/' + newXid, headers=myHeader, cookies=reqCookie)
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

