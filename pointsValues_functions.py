import requests
import sys
import common
__author__ = 'Yafit'

# =========== POINT VALUES =============
def getPointValuesHistoryByTimeRange(ip, reqCookie, xid, fromDate, endDate, rollup, timePeriodType):
    """
    :param ip:
    :param reqCookie:
    :param xid:
    :param fromDate:
    :param endDate:
    :param rollup: NONE/AVERAGE/DELTA/MINIMUM/MAXIMUM/ACCUMULATOR/SUM/FIRST/LAST/COUNT/INTEGRAL/FFT
    :param timePeriodType: MILLISECONDES/SECONDES/MINUTES/HOURS/DAYS/WEEKS/MONTHS/YEARS
    :return:
    """
    common.print_frame()
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(
            'http://' + ip + ':8080' + '/rest/v1/point-values/' + xid + '?useRendered=true&unitConversion=true&from='
             + newFromDate + '&to=' + newEndDate + '&rollup=' + rollup + '&timePeriodType=' + timePeriodType,
            headers=myHeader, cookies=reqCookie)
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


def CountPointvaluesInTimeRange(ip, reqCookie, xid, fromDate, endDate, rollup, timePeriodType):
    """
    :param ip:
    :param reqCookie:
    :param Xid:
    :param fromDate:
    :param endDate:
    :param rollup: NONE/AVERAGE/DELTA/MINIMUM/MAXIMUM/ACCUMULATOR/SUM/FIRST/LAST/COUNT/INTEGRAL/FFT
    :param timePeriodType: MILLISECONDES/SECONDES/MINUTES/HOURS/DAYS/WEEKS/MONTHS/YEARS
    :return:
    """
    common.print_frame()
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/point-values/' + xid + '/count?from=' + newFromDate +
                         '&to=' + newEndDate + '&rollup=' + rollup + '&timePeriodType=' + timePeriodType, headers=myHeader, cookies=reqCookie)
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


def getFirstAndLastPointValuesInTimeRange(ip, reqCookie, xid, fromDate, endDate):
    """
    :param ip:
    :param reqCookie:
    :param xid:
    :param fromDate:
    :param endDate:
    :return:
    """
    common.print_frame()
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(
            'http://' + ip + ':8080' + '/rest/v1/point-values/' + xid +
            '/first-last?useRendered=false&unitConversion=false&from=' + newFromDate + '&to=' + newEndDate,
            headers=myHeader, cookies=reqCookie)
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


def getLatestPointValues(ip, reqCookie, xid, limit):
    """
    :param ip:
    :param reqCookie:
    :param xid:
    :param limit:
    :return: Get Latest Point Values
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(
            'http://' + ip + ':8080' + '/rest/v1/point-values/' + xid +
            '/latest?useRendered=false&unitConversion=false&limit=' + str(limit) + '&useCache=true', headers=myHeader,
            cookies=reqCookie)
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


def getPointStatistics(ip, reqCookie, xid, fromDate, endDate):
    """
    :param ip:
    :param reqCookie:
    :param xid:
    :param fromDate:
    :param endDate:
    :return: Get Point Statistics
    """
    common.print_frame()
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/point-values/' + xid +
                         '/statistics?useRendered=false&unitConversion=false'
                         '&from=' + newFromDate + '&to=' + newEndDate, headers=myHeader, cookies=reqCookie)

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


