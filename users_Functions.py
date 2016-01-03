import requests
import sys
import common
import json
__author__ = 'Yafit'


# ============ USERS ============
def newUser(ip, reqCookie, myuser):
    """
    :param ip:
    :param reqCookie:
    :param myuser:
    :return: create  a new user
    """
    common.print_frame()
    payload = {'username': myuser.username,
               'email': myuser.email,
               'admin': myuser.admin,
               'disabled': myuser.disabled,
               'homeUrl': myuser.homeUrl,
               'muted': myuser.muted,
               'password': myuser.password,
               'permissions': myuser.permissions,
               'receiveAlarmEmails': myuser.receiveAlarmEmails,
               'receiveOwnAuditEvents': myuser.receiveOwnAuditEvents,
               'systemTimezone': myuser.systemTimezone,
               'timezone': myuser.timezone,
               'validationMessages': [{'message': myuser.validationMessages['message'],
                                       'level': myuser.validationMessages['level'],
                                       'property': myuser.validationMessages['property']
                                       }]
               }
    parameters_json = json.dumps(payload)
    myHeader = {'Accept': 'application/json',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Content-Type': 'application/json; charset=UTF-8',
                'Connection': 'keep-alive'}
    try:
        r = requests.post(ip + '/rest/v1/users', headers=myHeader, data=parameters_json, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "New user was added!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def usersApi(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Query Users
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users', headers=myHeader, cookies=reqCookie)
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


def currentUser(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get current user
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users/current', headers=myHeader, cookies=reqCookie)
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


def usersList(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return:Get all user
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users/list', headers=myHeader, cookies=reqCookie)
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


def getNewUser(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return:Get new user
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users/new/user', headers=myHeader, cookies=reqCookie)
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


def usersPremissions(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get User Permissions Information for all users
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users/permissions', headers=myHeader, cookies=reqCookie)
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


def usersPremissionsGroups(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get All User Groups
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users/permissions-groups', headers=myHeader, cookies=reqCookie)
        print r.status_code
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


def deleteUser(ip, reqCookie, userName):
    """
    :param ip:
    :param reqCookie:
    :param userName:
    :return:
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.delete(ip + '/rest/v1/users/' + userName, headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The user was deleted from Mango!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def getUserByName(ip, reqCookie, userName):
    """
    :param ip:
    :param reqCookie:
    :param userName:
    :return:Get user info by name
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/users/' + userName, headers=myHeader, cookies=reqCookie)
        print r.status_code
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


def setUser(ip, reqCookie, oldName, myUser):
    """
    :param ip:
    :param reqCookie:
    :param currentUserName:
    :param newUserName:
    :param newPass:
    :param newMail:
    :return: Updates a user
    """
    common.print_frame()
    payload = {'username': myUser.username,
               'email': myUser.email,
               'admin': 'false',
               'disabled': myUser.disabled,
               'homeUrl': myUser.homeUrl,
               'muted': 'false',
               'password': myUser.password,
               'permissions': myUser.permissions,
               'receiveAlarmEmails': myUser.receiveAlarmEmails,
               'receiveOwnAuditEvents': 'false',
               'systemTimezone': myUser.systemTimezone,
               'timezone': myUser.timezone,
               'validationMessages':[{'message': myUser.validationMessages['message'],
                                      'level': myUser.validationMessages['level'],
                                      'property': myUser.validationMessages['property']}]
               }
    print payload['validationMessages']
    parameters_json = json.dumps(payload)
    myHeader = {'Accept': 'application/json',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Content-Type': 'application/json; charset=UTF-8',
                'Connection': 'keep-alive'}
    try:
        r = requests.put(ip + '/rest/v1/users/' + oldName, headers=myHeader, data=parameters_json,
                         cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The user was updated!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def setUserHomePage(ip, reqCookie, myUser, newUrl):
    """
    :param ip:
    :param reqCookie:
    :param userName:
    :param newUrl:
    :return: Update a user's home url
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.put(ip + '/rest/v1/users/' + myUser.username + '/homepage?url=' + newUrl, headers=myHeader,
                         cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The user home page was set!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def setUserMuteSettings(ip, reqCookie, userName, mute):
    """
    :param ip:
    :param reqCookie:
    :param userName:
    :param mute: true/false
    :return: Update a user's audio mute setting
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.put(ip + '/rest/v1/users/' + userName + '/mute?mute=' + mute, headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "User's audio mute setting was set!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)
