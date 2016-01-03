import requests
import sys
import common
__author__ = 'Yafit'


# ============== THREADS ===============
def getThreads(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get all thread
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/threads?stackDepth=10&asFile=false', headers=myHeader, cookies=reqCookie,)
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

