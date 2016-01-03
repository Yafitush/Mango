import requests
import sys
import common
__author__ = 'Yafit'


def login(ip_add, user_name, password):
    """
         The function login to Mango and returns a cookie which needed to all API functions
    :param ip_add:
    :param user_name: The user name
    :param password: The password to login
    :return:
    """
    common.print_frame()
    myHeader = {'Accept': 'application/json',
                'password': password}
    try:
        r = requests.get(ip_add + '/rest/v1/login/' + user_name, headers=myHeader)
        if r.status_code == 200 or r.status_code == 201:
            print "Successfully login"
            setCookie = r.headers['Set-Cookie']
            return parseMyCookie(setCookie)
        else:
            print "Login was failed!"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)




def logoutApi(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: logout
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/logout',headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "Logout!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def parseMyCookie(reqCookie):
    common.print_frame()
    tempCookie = reqCookie.split(',')
    myCookie = {(tempCookie[0].split(';')[0]).split('=')[0].strip(): (tempCookie[0].split(';')[0]).split('=')[1],
                (tempCookie[1].split(';')[0]).split('=')[0].strip(): (tempCookie[1].split(';')[0]).split('=')[1]}
    return myCookie