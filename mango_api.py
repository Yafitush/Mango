import requests
import json
import sys
import os
import DataPoint
import dataSource_Bacnet_Ip
import dataSource_Http_Retriever
import dataSource_Mango_Persistent_TCP
import dataSource_Modbus_Ip
import dataSource_sql
import publisher_Mango_Persistent_TCP
import publisher_Bacnet
import user

__author__ = 'Yafit'

ip = 'http://52.16.65.135:8080'


def login(ip_add, user_name, password):
    """
         The function login to Mango and returns a cookie which needed to all API functions
    :param ip_add:
    :param user_name: The user name
    :param password: The password to login
    :return:
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'password': password}
    try:
        r = requests.get(ip_add + '/rest/v1/login/' + user_name, headers=myHeader)
        if r.status_code == 200 or r.status_code == 201:
            print "Successfully login"
            setCookie = r.headers['Set-Cookie']
            return setCookie
        else:
            print "Login was failed!"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


# ======= DATA POINT SUMMARY ==============
def dataPointsSummary(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: The function returns a partial information about all data points
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-point-summaries', headers=myHeader, cookies=reqCookie)
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


# ========== DATA POINTS ====================
''' There are different types of data points and for each type there is a different Point_Locator! '''

def setPointLocator_BacnetIp(mac, modelType="PL.BACNET_IP", dataType="BINARY", settable="false", relinquishable="false",
                             networkNumber=0, remoteDeviceInstanceNumber=0, objectTypeId="ANALOG_INPUT",
                             objectInstanceNumber=0, propertyIdentifierId="PRESENT_VALUE", useCovSubscription="false",
                             writePriority=16):
    return {'modelType': modelType,
            'dataType': dataType,
            'settable': settable,
            'relinquishable': relinquishable,
            'mac': mac,
            'networkNumber': networkNumber,
            'remoteDeviceInstanceNumber': remoteDeviceInstanceNumber,
            'objectTypeId': objectTypeId,
            'objectInstanceNumber': objectInstanceNumber,
            'propertyIdentifierId': propertyIdentifierId,
            'useCovSubscription': useCovSubscription,
            'writePriority': writePriority
            }


def setPointLocator_Modbus(modelType="PL.MODBUS", dataType="BINARY", settable="true", relinquishable="false", bit=0,
                           slaveId=1, additive=0, modbusDataType="BINARY", multiplier=1, slaveMonitor="false",
                           registerCount=0, charset="ASCII", writeType="SETTABLE", range="COIL_STATUS", offset=0):
    return {'modelType': modelType,
            'dataType': dataType,
            'settable': settable,
            'relinquishable': relinquishable,
            'bit': bit,
            'slaveId': slaveId,
            'additive': additive,
            'modbusDataType': modbusDataType,
            'multiplier': multiplier,
            'slaveMonitor': slaveMonitor,
            'registerCount': registerCount,
            'charset': charset,
            'writeType': writeType,
            'range': range,
            'offset': offset
            }


def setPointLocator_HttpRetriever(dataType="BINARY", settable="false", modelType="PL.HTTP_RETRIEVER",
                                  relinquishable="false", valueRegex="", ignoreIfMissing="false", valueFormat="",
                                  timeRegex="", timeFormat="", setPointName=""):
    return {'modelType': modelType,
            'dataType': dataType,
            'settable': settable,
            'relinquishable': relinquishable,
            'valueRegex': valueRegex,
            'ignoreIfMissing': ignoreIfMissing,
            'valueFormat': valueFormat,
            'timeRegex': timeRegex,
            'timeFormat': timeFormat,
            'setPointName': setPointName
            }


def setPointLocator_Sql(dataType="BINARY", settable="false", relinquishable="false", modelType="PL.SQL",
                        fieldName="", timeOverrideName="", updateStatement="", tableModifier="false",
                        parameters=[], dateParameterFormat="yyyy-MM-dd'T'HH:mm:ss"):
    return {'dataType': dataType,
            'settable': settable,
            'relinquishable': relinquishable,
            'modelType': modelType,
            'fieldName': fieldName,
            'timeOverrideName': timeOverrideName,
            'updateStatement': updateStatement,
            'tableModifier': tableModifier,
            'parameters': parameters,
            'dateParameterFormat': dateParameterFormat}


def pointLocator(type, *args):
    """
    The function gets the data point type and call the right function
    :param type:
    :param args:
    :return:
    """
    ans = {}
    if type == "SQL":
        ans = setPointLocator_Sql(*args)
    if type == "HttpRetriever":
        ans = setPointLocator_HttpRetriever(*args)
    if type == "Modbus":
        ans = setPointLocator_Modbus(*args)
    if type == "BacnetIp":
        ans = setPointLocator_BacnetIp(*args)
    return ans


def dataPoints(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: The function returns all information about all data points
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-points', headers=myHeader, cookies=reqCookie)
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


def insertUpdateDataPoint(ip, reqCookie, myDataPoint):
    """
    The function gets an instance of Data Point and inserts a new data point to Mango or updates the data points in Mango
     if it's already exits.
    :param ip:
    :param reqCookie:
    :param myDataPoint:
    """
    pointLocator = {}
    checkModelType = myDataPoint.pointLocator['modelType']
    print checkModelType
    if checkModelType == "PL.BACNET_IP":
        pointLocator = {"settable": myDataPoint.pointLocator['settable'],
                        "relinquishable": myDataPoint.pointLocator['relinquishable'],
                        "modelType": myDataPoint.pointLocator['modelType'],
                        "dataType": myDataPoint.pointLocator['dataType'],
                        "mac": myDataPoint.pointLocator['mac'],
                        "networkNumber": myDataPoint.pointLocator['networkNumber'],
                        "remoteDeviceInstanceNumber": myDataPoint.pointLocator['remoteDeviceInstanceNumber'],
                        "objectTypeId": myDataPoint.pointLocator['objectTypeId'],
                        "objectInstanceNumber": myDataPoint.pointLocator['objectInstanceNumber'],
                        "propertyIdentifierId": myDataPoint.pointLocator['propertyIdentifierId'],
                        "useCovSubscription": myDataPoint.pointLocator['useCovSubscription'],
                        "writePriority": myDataPoint.pointLocator['writePriority']}

    if checkModelType == "PL.MODBUS":
        pointLocator = {"modelType": myDataPoint.pointLocator['modelType'],
                        "bit": myDataPoint.pointLocator['bit'],
                        "slaveId": myDataPoint.pointLocator['slaveId'],
                        "additive": myDataPoint.pointLocator['additive'],
                        "modbusDataType": myDataPoint.pointLocator['modbusDataType'],
                        "multiplier": myDataPoint.pointLocator['multiplier'],
                        "slaveMonitor": myDataPoint.pointLocator['slaveMonitor'],
                        "registerCount": myDataPoint.pointLocator['registerCount'],
                        "charset": myDataPoint.pointLocator['charset'],
                        "writeType": myDataPoint.pointLocator['writeType'],
                        "range": myDataPoint.pointLocator['range'],
                        "offset": myDataPoint.pointLocator['offset'],
                        "dataType": myDataPoint.pointLocator['dataType'],
                        "relinquishable": myDataPoint.pointLocator['relinquishable'],
                        "settable": myDataPoint.pointLocator['settable']}

    if checkModelType == "PL.HTTP_RETRIEVER":
        pointLocator = {"dataType": myDataPoint.pointLocator['dataType'],
                        "modelType": myDataPoint.pointLocator['modelType'],
                        "ignoreIfMissing": myDataPoint.pointLocator['ignoreIfMissing'],
                        "setPointName": myDataPoint.pointLocator['setPointName'],
                        "settable": myDataPoint.pointLocator['settable'],
                        "timeFormat": myDataPoint.pointLocator['timeFormat'],
                        "timeGroup": myDataPoint.pointLocator['timeGroup'],
                        "timeRegex": myDataPoint.pointLocator['timeRegex'],
                        "valueFormat": myDataPoint.pointLocator['valueFormat'],
                        "valueGroup": myDataPoint.pointLocator['valueGroup'],
                        "valueRegex": myDataPoint.pointLocator['valueRegex']}

    if checkModelType == "PL.SQL":
        pointLocator = {"fieldName": myDataPoint.pointLocator['fieldName'],
                        "dataType": myDataPoint.pointLocator['dataType'],
                        "timeOverrideName": myDataPoint.pointLocator['timeOverrideName'],
                        "updateStatement": myDataPoint.pointLocator['updateStatement'],
                        "tableModifier": myDataPoint.pointLocator['tableModifier'],
                        "parameters": myDataPoint.pointLocator['parameters'],
                        "dateParameterFormat": myDataPoint.pointLocator['dateParameterFormat'],
                        "modelType": myDataPoint.pointLocator['modelType'],
                        "settable": myDataPoint.pointLocator['settable'],
                        "relinquishable": myDataPoint.pointLocator['relinquishable']
                        }
    payload = [{"enabled": myDataPoint.enabled,
                "templateXid": myDataPoint.templateXid,
                "loggingProperties": {"tolerance": myDataPoint.loggingProperties['tolerance'],
                                      "discardExtremeValues": myDataPoint.loggingProperties['discardExtremeValues'],
                                      "discardLowLimit": myDataPoint.loggingProperties['discardLowLimit'],
                                      "discardHighLimit": myDataPoint.loggingProperties['discardHighLimit'],
                                      "loggingType": myDataPoint.loggingProperties['loggingType'],
                                      "intervalLoggingType": myDataPoint.loggingProperties['intervalLoggingType'],
                                      "intervalLoggingPeriod": {
                                          "periods": myDataPoint.loggingProperties['intervalLoggingPeriod']['periods'],
                                          "type": myDataPoint.loggingProperties['intervalLoggingPeriod']['type']
                                          },
                                      "overrideIntervalLoggingSamples": myDataPoint.loggingProperties[
                                          'overrideIntervalLoggingSamples'],
                                      "intervalLoggingSampleWindowSize": myDataPoint.loggingProperties[
                                          'intervalLoggingSampleWindowSize'],
                                      "cacheSize": myDataPoint.loggingProperties['cacheSize']
                                      },
                "textRenderer": {"zeroLabel": myDataPoint.textRenderer['zeroLabel'],
                                 "zeroColour": myDataPoint.textRenderer['zeroColour'],
                                 "oneLabel": myDataPoint.textRenderer['oneLabel'],
                                 "oneColour": myDataPoint.textRenderer['oneColour'],
                                 "type": myDataPoint.textRenderer['type']
                                 },
                "chartRenderer": {"limit": myDataPoint.chartRenderer['limit'],
                                  "type": myDataPoint.chartRenderer['type']
                                  },
                "modelType": myDataPoint.modelType,
                "validationMessages": [],
                "dataSourceId": myDataPoint.dataSourceId,
                "deviceName": myDataPoint.dataSourceName,
                "chartColour": myDataPoint.chartColour,
                "plotType": myDataPoint.plotType,
                "purgeOverride": myDataPoint.purgeOverride,
                "purgePeriod": {"periods": myDataPoint.purgePeriod['periods'],
                                "type": myDataPoint.purgePeriod['type']
                                },
                "pointLocator": pointLocator,
                "readPermission": myDataPoint.readPermission,
                "setPermission": myDataPoint.setPermission,
                "dataSourceXid": myDataPoint.dataSourceXid,
                "pointFolderId": myDataPoint.pointFolderId,
                "unit": myDataPoint.unit,
                "useIntegralUnit": myDataPoint.useIntegralUnit,
                "integralUnit": myDataPoint.integralUnit,
                "useRenderedUnit": myDataPoint.useRenderedUnit,
                "renderedUnit": myDataPoint.renderedUnit,
                "dataSourceName": myDataPoint.dataSourceName,
                "id": '0',
                "xid": myDataPoint.xid,
                "name": myDataPoint.name}]

    parameters_json = json.dumps(payload)
    myHeader = {'Accept': 'application/json',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Content-Type': 'application/json; charset=UTF-8',
                'Connection': 'keep-alive'}
    try:
        r = requests.put(ip + '/rest/v1/data-points', data=parameters_json, headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The data point was added/ saved!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def dataPointById(ip, reqCookie, pointId):
    """
    :param ip:
    :param reqCookie:
    :param PointId:
    :return: returns information about a data point by ID
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-points/by-id/' + str(pointId), headers=myHeader, cookies=reqCookie)
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


def dataPointsForDataSourceByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid:  data source xid
    :return: Get all data points for data source
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-points/data-source/' + str(Xid), headers=myHeader, cookies=reqCookie)
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


def dataPointListWithLimit(ip, reqCookie, limit=100):
    """
    :param ip:
    :param reqCookie:
    :return: Get a few data points
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-points/list?limit=' + str(limit), headers=myHeader, cookies=reqCookie)
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


def deleteDataPointByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid:
    :return: Delete a data point
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.delete(ip + '/rest/v1/data-points/' + str(Xid), headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The data point was deleted!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def getDataPointByXid(reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: data point xid
    :return: Get data point by XID
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-points/' + str(Xid), headers=myHeader, cookies=reqCookie)
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


# ===== DATA SOURCES ==============
def dataSources(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get all data sources
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/data-sources/list', headers=myHeader, cookies=reqCookie)
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


def getDataSourceByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: data source Xid
    :return: Get data source by xid
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}

    try:
        r = requests.get(ip + '/rest/v1/data-sources/' + str(Xid), headers=myHeader, cookies=reqCookie)
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


def addDataSourceToDataSourceFile(myDataSource):
    """
    The function get an instance of Data source and write it to a text file.
    :param myDataSource:
    """
    dataSourceType = myDataSource.type
    addDataSource = {}
    if dataSourceType == "BACnetIP":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled,
                         'type': "BACnetIP",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'updatePeriodType': myDataSource.updatePeriodType,
                         'updatePeriods': myDataSource.updatePeriods,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'covSubscriptionTimeoutMinutes': myDataSource.covSubscriptionTimeoutMinutes,
                         'localDeviceConfig': myDataSource.localDeviceConfig
                         }
    if dataSourceType == "HTTP_RETRIEVER":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled,
                         'type': "HTTP_RETRIEVER",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'updatePeriodType': myDataSource.updatePeriodType,
                         'updatePeriods': myDataSource.updatePeriods,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'quantize': myDataSource.quantize,
                         'retries': myDataSource.retries,
                         'setPointUrl': myDataSource.setPointUrl,
                         'timeoutSeconds': myDataSource.timeoutSeconds,
                         'url': myDataSource.url
                         }
    if dataSourceType == "PERSISTENT":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled,
                         'type': "PERSISTENT",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'ogLevel': myDataSource.logLevel,
                         'acceptPointUpdates': myDataSource.acceptPointUpdates,
                         'authorizationKey': myDataSource.authorizationKey,
                         'port': myDataSource.port,
                         'saveRealtimeData': myDataSource.saveRealtimeData,
                         'socketTimeout': myDataSource.socketTimeout,
                         'useCompression': myDataSource.useCompression,
                         'useCrc': myDataSource.useCrc
                         }
    if dataSourceType == "MODBUS_IP":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled,
                         'type': "HTTP_RETRIEVER",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'updatePeriodType': myDataSource.updatePeriodType,
                         'updatePeriods': myDataSource.updatePeriods,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'transportType': myDataSource.transportType,
                         'encapsulated': myDataSource.encapsulated,
                         'host': myDataSource.host,
                         'port': myDataSource.port,
                         'contiguousBatches': myDataSource.contiguousBatches,
                         'createSlaveMonitorPoints': myDataSource.createSlaveMonitorPoints,
                         'discardDataDelay': myDataSource.discardDataDelay,
                         'ioLogFileSizeMBytes': myDataSource.ioLogFileSizeMBytes,
                         'logIO': myDataSource.logIO,
                         'maxHistoricalIOLogs': myDataSource.maxHistoricalIOLogs,
                         'maxReadBitCount': myDataSource.maxReadBitCount,
                         'maxReadRegisterCount': myDataSource.maxReadRegisterCount,
                         'maxWriteRegisterCount': myDataSource.maxWriteRegisterCount,
                         'multipleWritesOnly': myDataSource.multipleWritesOnly,
                         'quantize': myDataSource.quantize,
                         'retries': myDataSource.retries,
                         'timeout': myDataSource.timeout
                         }
    if dataSourceType == "SQL":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled.replace('"', ''),
                         'type': "SQL",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'updatePeriodType': myDataSource.updatePeriodType,
                         'updatePeriods': myDataSource.updatePeriods,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'connectionUrl': myDataSource.connectionUrl,
                         'driverClassname': myDataSource.driverClassname,
                         'rowBasedQuery': myDataSource.rowBasedQuery,
                         'selectStatement': myDataSource.selectStatement
                         }
    if dataSourceType == "MODBUS_SERIAL":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled.replace('"', ''),
                         'type': "MODBUS_SERIAL",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'updatePeriodType': myDataSource.updatePeriodType,
                         'updatePeriods': myDataSource.updatePeriods,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'concurrency': myDataSource.concurrency,
                         'baudRate': myDataSource.baudRate,
                         'characterSpacing': myDataSource.haracterSpacing,
                         'commPortId': myDataSource.commPortId,
                         'dataBits': myDataSource.dataBits,
                         'echo': myDataSource.echo,
                         'encoding': myDataSource.encoding,
                         'flowControlIn': myDataSource.flowControlIn,
                         'flowControlOut': myDataSource.flowControlOut,
                         'messageFrameSpacing': myDataSource.messageFrameSpacing,
                         'overrideTiming': myDataSource.overrideTiming,
                         'parity': myDataSource.parity,
                         'stopBits': myDataSource.stopBits,
                         'contiguousBatches': myDataSource.contiguousBatches,
                         'createSlaveMonitorPoints': myDataSource.createSlaveMonitorPoints,
                         'discardDataDelay': myDataSource.discardDataDelay,
                         'ioLogFileSizeMBytes': myDataSource.ioLogFileSizeMBytes,
                         'logIO': myDataSource.logIO,
                         'maxHistoricalIOLogs': myDataSource.maxHistoricalIOLogs,
                         'maxReadBitCount': myDataSource.maxReadBitCount,
                         'maxReadRegisterCount': myDataSource.maxReadRegisterCount,
                         'maxWriteRegisterCount': myDataSource.maxWriteRegisterCount,
                         'multipleWritesOnly': myDataSource.multipleWritesOnly,
                         'quantize': myDataSource.quantize,
                         'retries': myDataSource.retries,
                         'timeout': myDataSource.timeout
                         }
    if dataSourceType == "BACnetMSTP":
        addDataSource = {'xid': myDataSource.xid,
                         'name': myDataSource.name,
                         'enabled': myDataSource.enabled.replace('"', ''),
                         'type': "BACnetMSTP",
                         'alarmLevels': myDataSource.alarmLevels,
                         'purgeType': myDataSource.purgeType,
                         'updatePeriodType': myDataSource.updatePeriodType,
                         'updatePeriods': myDataSource.updatePeriods,
                         'editPermission': myDataSource.editPermission,
                         'purgeOverride': myDataSource.purgeOverride,
                         'purgePeriod': myDataSource.purgePeriod,
                         'covSubscriptionTimeoutMinutes': myDataSource.covSubscriptionTimeoutMinutes,
                         'localDeviceConfig': myDataSource.localDeviceConfig
                         }

    with open('dataSource.txt', 'ab+') as f:
        json.dump(addDataSource, f)
        f.write(',\n')


def craeteDataSourceOrPublishersFile(fileType):
    """
    The function gets the type of the file to create: publishers or dataSources
     and creates the file with it's special text.
    :param fileType:
    """
    if fileType == "dataSource" or fileType == "publishers":
        with open(fileType + '.txt', 'w') as f:
            f.write("{\n")
            f.write('"' + fileType + '":[\n')


def closeDataSourceOrPublisherFile(fileType):
    """
    The function close the file and add some needed text.
    :param fileType: can only be "dataSource" or "publishers"
    """
    if fileType == "dataSource" or fileType == "publishers":
        with open(fileType + '.txt', 'rb+') as f:
            f.seek(0, 2)  # end of file
            size = f.tell()  # the size...
            f.truncate(size - 2)
            f.write("]}")
        # this part is needed to parse boolean strings to boolean ex. "false" -> false
        f = open(fileType + '.txt', 'r')
        file_data = f.read()
        f.close()
        newdata = file_data.replace('"false"', "false")
        newdata2 = newdata.replace('"true"', "true")
        f = open(fileType + '.txt', 'w')
        f.write(newdata2)
        f.close()


# ========== PUBLISHERS =========
def publisherSetMangoPersistentTCPoint(points):
    """
    The function gets a lists of data points Xids and return a new list with a specific syntax.
    :param points:
    :return:
    """
    newList = []
    for point in points:
        newList.append({"dataPointId": point})
    return newList


def publisherSetBACnetPoint(reqCookie, points):
    newList = []
    i = 0
    for point in points:
        pointData = getDataPointByXid(reqCookie, point)
        deviceNameLocation = pointData.find('"deviceName"')
        endDeviceNameLocation = pointData.find(',', deviceNameLocation)
        daviceName = pointData[deviceNameLocation + 16: endDeviceNameLocation - 1]

        nameLocation = pointData.find('"name"')
        endNameLocation = pointData.find(',', nameLocation)
        name = pointData[nameLocation + 10: endNameLocation - 1]

        newList.append({"dataPointId": point,
                        "instanceNumber": i,
                        "objectName": daviceName + " - " + name})
        i += 1
    return newList


def addPublisher(myPublisher):
    add_publisher = {}
    publisher_type = myPublisher.type
    if publisher_type == "PERSISTENT":
        add_publisher = {"xid": myPublisher.xid,
                        "type": "PERSISTENT",
                        "points": myPublisher.points,
                        "snapshotSendPeriodType": myPublisher.snapshotSendPeriodType,
                        "historyCutoffPeriodType": myPublisher.historyCutoffPeriodType,
                        "logLevel": myPublisher.logLevel,
                        "authorizationKey": myPublisher.authorizationKey,
                        "connectionCheckPeriod": myPublisher.connectionCheckPeriod,
                        "historyCutoffPeriods": myPublisher.historyCutoffPeriods,
                        "host": myPublisher.host,
                        "maxPointValuesToSend": myPublisher.maxPointValuesToSend,
                        "parallelSyncTasks": myPublisher.parallelSyncTasks,
                        "port": myPublisher.port,
                        "reconnectSyncs": myPublisher.reconnectSyncs,
                        "socketTimeout": myPublisher.socketTimeout,
                        "syncPattern": myPublisher.syncPattern,
                        "syncPointHierarchy": myPublisher.syncPointHierarchy,
                        "syncRealTime": myPublisher.syncRealTime,
                        "syncRequestRetryAttempts": myPublisher.syncRequestRetryAttempts,
                        "syncResponseTimeout": myPublisher.syncResponseTimeout,
                        "useCompression": myPublisher.useCompression,
                        "useCrc": myPublisher.useCrc,
                        "xidPrefix": myPublisher.xidPrefix,
                        "cacheDiscardSize": myPublisher.cacheDiscardSize,
                        "cacheWarningSize": myPublisher.cacheWarningSize,
                        "changesOnly": myPublisher.changesOnly,
                        "enabled": myPublisher.enabled,
                        "name": myPublisher.name,
                        "sendSnapshot": myPublisher.sendSnapshot,
                        "snapshotSendPeriods": myPublisher.snapshotSendPeriods
                        }

    if publisher_type == "BACnet":
        add_publisher = {"xid": myPublisher.xid,
                        "type": "BACnet",
                        "points": myPublisher.points,
                        "enabled": myPublisher.enabled,
                        "name": myPublisher.name,
                        "snapshotSendPeriodType": myPublisher.snapshotSendPeriodType,
                        "localDeviceConfig": myPublisher.localDeviceConfig,
                        "cacheDiscardSize": myPublisher.cacheDiscardSize,
                        "cacheWarningSize": myPublisher.cacheWarningSize,
                        "changesOnly": myPublisher.changesOnly,
                        "sendSnapshot": myPublisher.sendSnapshot,
                        "snapshotSendPeriods": myPublisher.snapshotSendPeriods
                        }

    with open('publishers.txt', 'ab+') as f:
        json.dump(add_publisher, f)
        f.write(',\n')


# ============ EVENTS ============

def eventsApi(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Query Events
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/events', headers=myHeader, cookies=reqCookie)
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


def getActiveEventsSummary(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get the active events summary
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/events/active-summary', headers=myHeader, cookies=reqCookie)
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


def getEventsListWithLimit(ip, reqCookie, limit):
    """
    :param ip:
    :param reqCookie:
    :param limit:
    :return:Get all events
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/events/list?limit=' + str(limit), headers=myHeader, cookies=reqCookie)
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


def getEventById(ip, reqCookie, Eid):
    """
    :param ip:
    :param reqCookie:
    :param Eid: event id
    :return: Get event by ID
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/events/' + str(Eid), headers=myHeader, cookies=reqCookie)
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


# ============ LOGGING =================
def getRecentLogsFromFile(ip, reqCookie, fileName):
    """
    :param ip:
    :param reqCookie:
    :param fileName:
    :return: Returns a list of recent logs
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/logging/by-filename/' + fileName, headers=myHeader, cookies=reqCookie)
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


def getLogFilesNames(ip, reqCookie, limit):
    """
    :param ip:
    :param reqCookie:
    :return: Returns a list of logfile names
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/logging/files?limit=' + str(limit), headers=myHeader, cookies=reqCookie)
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


# =========== MAILLING LISTS ==================
def getMaillingList(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get Mailing List
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/mailing-lists', headers=myHeader, cookies=reqCookie)
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


def getMaillingListByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: mailling list xid
    :return: Get Mailing List by XID
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/mailing-lists/' + Xid, headers=myHeader, cookies=reqCookie)
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


# ========= POINT HIERARCHY ============
def getPointHierarchyFolderByName(ip, reqCookie, folderName):
    """
    :param ip:
    :param reqCookie:
    :param folderName:
    :return: Get point hierarchy folder by name
    """
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
        r = requests.get(ip + '/rest/v1/hierarchy/by-name/' + newName, headers=myHeader, cookies=reqCookie)
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
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/hierarchy/full', headers=myHeader, cookies=reqCookie)
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
        r = requests.get(ip + '/rest/v1/hierarchy/path/' + newXid, headers=myHeader, cookies=reqCookie)
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


# =========== POINT VALUES =============
def getPointValuesHistoryByTimeRange(ip, reqCookie, Xid, fromDate, endDate, rollup, timePeriodType):
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
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(
            ip + '/rest/v1/point-values/' + Xid + '?useRendered=true&unitConversion=true&from=' + newFromDate +
            '&to=' + newEndDate + '&rollup=' + rollup + '&timePeriodType=' + timePeriodType, headers=myHeader,
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


def CountPointvaluesInTimeRange(ip, reqCookie, Xid, fromDate, endDate, rollup, timePeriodType):
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
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/point-values/' + Xid + '/count?from=' + newFromDate + '&to=' + newEndDate +
                         '&rollup=' + rollup + '&timePeriodType=' + timePeriodType, headers=myHeader, cookies=reqCookie)
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


def getFirstAndLastPointValuesInTimeRange(ip, reqCookie, Xid, fromDate, endDate):
    """
    :param ip:
    :param reqCookie:
    :param Xid:
    :param fromDate:
    :param endDate:
    :return:
    """
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(
            ip + '/rest/v1/point-values/' + Xid + '/first-last?useRendered=false&unitConversion=false&from=' + newFromDate +
            '&to=' + newEndDate, headers=myHeader, cookies=reqCookie)
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


def getLatestPointValues(ip, reqCookie, Xid, limit):
    """
    :param ip:
    :param reqCookie:
    :param Xid:
    :param limit:
    :return: Get Latest Point Values
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(
            ip + '/rest/v1/point-values/' + Xid + '/latest?useRendered=false&unitConversion=false&limit=' + str(
                limit) + '&useCache=true',
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


def getPointStatistics(ip, reqCookie, Xid, fromDate, endDate):
    """
    :param ip:
    :param reqCookie:
    :param Xid:
    :param fromDate:
    :param endDate:
    :return: Get Point Statistics
    """
    newFromDate = str(fromDate).replace(':', '%3A')
    newEndDate = str(endDate).replace(':', '%3A')
    print newFromDate
    print newEndDate
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/point-values/' + Xid + '/statistics?useRendered=false&unitConversion=false'
                                                               '&from=' + newFromDate + '&to=' + newEndDate,
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


# =========== REAL TIME DATA =============
def realTimeData(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return:Query realtime values
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/realtime', headers=myHeader, cookies=reqCookie)
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


def realTimeDataByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: data point Xid
    :return:
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/realtime/by-xid/' + str(Xid), headers=myHeader, cookies=reqCookie)
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


def realTimeList(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return:List realtime values
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/realtime/list?limit=100', headers=myHeader, cookies=reqCookie)
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


# ============== THREADS ===============


def getThreads(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get all thread
    """
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


# ======== USER ACCESS ============
def getDataPointAccessListByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: data point Xid
    :return: Get Data Point Access List
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/access/data-point/' + Xid, headers=myHeader, cookies=reqCookie)
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


def getDataSourceAccessListByXid(ip, reqCookie, Xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: data source Xid
    :return: Get Data Source Access List
    """
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get(ip + '/rest/v1/access/data-source/' + Xid, headers=myHeader, cookies=reqCookie)
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


# ========== USER COMMENTS =========
def userComments(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Query User Comments
    """
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


# ============ USERS ============


def newUser(ip, reqCookie, myuser):
    """
    :param ip:
    :param reqCookie:
    :param myuser:
    :return: create  a new user
    """
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


# =======================================

def logoutApi(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: logout
    """
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


def logoutUserByPOST(ip, reqCookie, userName):
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.post(ip + '/rest/v1/logout/' + userName, headers=myHeader, cookies=reqCookie)
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


# ====================================
def parseMyCookie(reqCookie):
    tempCookie = reqCookie.split(',')
    myCookie = {(tempCookie[0].split(';')[0]).split('=')[0].strip(): (tempCookie[0].split(';')[0]).split('=')[1],
                (tempCookie[1].split(';')[0]).split('=')[0].strip(): (tempCookie[1].split(';')[0]).split('=')[1]}
    return myCookie




username = 'admin'
password = 'admin'
myCookie = login(ip, username, password)  # must login before doing anything else!!!
parsedCookie = parseMyCookie(myCookie)



setPointLocator = pointLocator("SQL", "BINARY", "false", "false", "PL.SQL", "some_id", " ", " ", "false", [],
                               "yyyy-MM-dd'T'HH:mm:ss")

myDataPoint = DataPoint.DataPoint("true", "Binary_Default", "DATA_POINT", '12', '1', "YEARS", "zero", "blue", "one",
                                  "black", "textRendererBinary", '10', "chartRendererTable", '0', "false",
                                  '-1.7976931348623157e+308', '1.7976931348623157e+308', "ON_CHANGE", "INSTANT", "false",
                                  '0', '1', '15', "MINUTES", "superadmin", "superadmin", "yafitSQL", "blue", "STEP",
                                  "false", 'DS_487892', '0', " ", "false", "s", "false", " ", "yafitSQL", "asasasasas",
                                  "DP_asasasasasa", setPointLocator)



mySQLds = dataSource_sql.DataSource_SQL("DS_1212121", "pythonSQLds121212", "bar", "bar123", "false", "YEARS", "MINUTES",
                                        "user",
                                        'false', 1, 5, "url", "someClassName", 'false', "")
myBacknetIPds = dataSource_Bacnet_Ip.DataSource_BACNET_IP("ds_bb", "pythonBckIp", "true", "YEARS", "MINUTES",
                                                          "superadmin", "false", 1, 5, 60)

craeteDataSourceOrPublishersFile("dataSource")

addDataSourceToDataSourceFile(mySQLds)
addDataSourceToDataSourceFile(myBacknetIPds)
closeDataSourceOrPublisherFile("dataSource")

publisherPoints = publisherSetMangoPersistentTCPoint(["DP_519610", "DP_991120"])
points = publisherSetBACnetPoint(parsedCookie, ["DP_519610", "DP_991120"])
myMPTCPublisher = publisher_Mango_Persistent_TCP.Publisher_MANGO_PERSISTENT_TCP("PUB_123", "myPublisher", "true", "YEARS",
                                                                                "HOURS", "LOG_LEVEL_NONE", "yafit", 6000,
                                                                                2, "55.55.55.55", 5000, 10, 42,"false",
                                                                                3000, "", "true", "true",3, 1200000, "true",
                                                                                "false", "hiaia", 1000, 100, "false", "false",
                                                                                5, publisherPoints)
myBacnetPublisher = publisher_Bacnet.Publisher_BACNET("PUB_555", "myBACnetPublisher", "true", "MINUTES", 1000, 100, "false",
                                                      "false", 5, points)
craeteDataSourceOrPublishersFile("publishers")

addPublisher(myMPTCPublisher)
addPublisher(myBacnetPublisher)
closeDataSourceOrPublisherFile("publishers")


myUser = user.User("fufu12", "fufu1212", "yafitush@mail.com", "NONE", "", "false", "false", "true", "Etc/UTC",
                   "Etc/UTC","false","superadmin", "", "INFORMATION", "")
#newUser(ip, parsedCookie, myUser)




#print myUser.validationMessages['level']
#newUser(ip, parsedCookie, myUser)
myUser.email = "qggggggggggggggggggg"
print myUser.email
print myUser.username
setUser(ip, parsedCookie, "fufu12", myUser)
#setUser(ip, parsedCookie, "fufu", "fufu", "12312345", myUser.email, "WARNING")


# insertUpdateDataPoint(ip, parsedCookie, myDataPoint)
# myDataPoint.readPermission="User"
# insertUpdateDataPoint(ip, parsedCookie, myDataPoint)






# usersApi(ip, parsedCookie)
# currentUser(ip, parsedCookie)
# deleteUser(ip, parsedCookie,'yafit')
# newUser(ip, parsedCookie, 'test', 'test123', 'test123@mail','WARNING' )
# getUserByName(ip, parsedCookie, 'test')
# setUser(ip, parsedCookie, 'yafit', 'test', '12345', '@mail','WARNING')
# setUserHomePage(ip, parsedCookie,'test','www.123.com')
# setUserMuteSettings(ip, parsedCookie,'test','false')
# dataPointsApi(ip, parsedCookie)
# getDataPointExplainQuery(ip, parsedCookie)
# dataPointListWithLimit(ip, parsedCookie,100)
# deleteDataPointByXid(ip, parsedCookie)
# getDataPointByXid(ip, parsedCookie)
# getAllDataPointsForDataSourceByXid(ip, parsedCookie)
# getDataPointById(ip, parsedCookie)
# dataPointsSummary(ip, parsedCookie)
# dataPointSummExplainQuery(ip, parsedCookie)
# dataSources(ip, parsedCookie)
# getDataSourceByXid(ip, parsedCookie)
# eventsApi(ip, parsedCookie)
# getEventById(ip, parsedCookie, 170)
# getEventsListWithLimit(ip, parsedCookie, 170)
# userComments(ip, parsedCookie)
# createNewComment(ip, parsedCookie, "BLA BLA BLA BLA BLA", 'WARNING','POINT')
# getCommentsExplainQuery(ip, parsedCookie)
# getAllUserComments(ip, parsedCookie,3)
# getDataPointAccessListByXid(ip, parsedCookie,'DP_519610')
# getDataSourceAccessListByXid(ip, parsedCookie,'DS_110513')
# getMaillingList(ip, parsedCookie)
# getMaillingListByXid(ip, parsedCookie, "ML_091391")
# realTimeData(ip, parsedCookie)
# realTimeList(ip, parsedCookie)
# realTimeDataByXid(ip, parsedCookie,'DP_519610')
# getThreads(ip, parsedCookie)
# getPointHierarchy(ip, parsedCookie)
# getLogFilesNames(ip, parsedCookie, 20)
# getRecentLogsFromFile(ip, parsedCookie,'ma.log')
# getLatestPointValues(ip, parsedCookie, 'DP_519610', 100 )
# getPointHierarchyFolderByName(ip, parsedCookie,'Demo Data' )
# getPathToPointByXid(ip, parsedCookie,'teat 2-watts')
# getPointStatistics(ip, parsedCookie, 'DP_653257', '2014-08-10T00:00:00.000-10:00', '2015-12-11T23:59:59.999-10:00')
# getPointValuesHistoryByTimeRange(ip, parsedCookie,'DP_653257', '2014-08-10T00:00:00.000-10:00', '2015-12-11T23:59:59.999-10:00', "", "")
# CountPointvaluesInTimeRange(ip, parsedCookie,'DP_653257', '2014-08-10T00:00:00.000-10:00', '2015-12-11T23:59:59.999-10:00', 'NONE', 'HOURS')
# getFirstAndLastPointValuesInTimeRange(ip, parsedCookie,'DP_653257', '2014-08-10T00:00:00.000-10:00', '2015-12-11T23:59:59.999-10:00')
logoutApi(ip, parsedCookie)
# logoutUserByPOST(ip, parsedCookie, username)

