import dataSources_Functions as ds_f
import requests
import publishers_Functions as p_f
import sys
import json
import common
import os

__author__ = 'Yafit'


# ========== DATA POINTS ====================
''' There are different types of data points and for each type there is a different Point_Locator! '''


def point_locator(type, **kwrgs):
    """
    The function gets the data point type and call the right function
    :param type:
    :param args:
    :return:
    """
    common.print_frame()
    ans = {}
    if type == "SQL":
        ans = setPointLocator_Sql(**kwrgs)
    if type == "HttpRetriever":
        ans = setPointLocator_HttpRetriever(**kwrgs)
    if type == "Modbus":
        ans = setPointLocator_Modbus(**kwrgs)
    if type == "BacnetIp":
        ans = setPointLocator_BacnetIp(**kwrgs)
    return ans


def setPointLocator_BacnetIp(mac, modelType="PL.BACNET_IP", dataType="BINARY", settable="false", relinquishable="false",
                             networkNumber=0, remoteDeviceInstanceNumber=0, objectTypeId="ANALOG_INPUT",
                             objectInstanceNumber=0, propertyIdentifierId="PRESENT_VALUE", useCovSubscription="false",
                             writePriority=16):
    common.print_frame()
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
    common.print_frame()
    textRenderer = setTextRenderer(dataType)
    pointLocator = {'modelType': modelType,
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
    return {'textRenderer': textRenderer, 'pointLocator': pointLocator}


def setPointLocator_HttpRetriever(dataType="BINARY", settable="false", modelType="PL.HTTP_RETRIEVER",
                                  relinquishable="false", valueRegex="", ignoreIfMissing="false", valueFormat="",
                                  timeRegex="", timeFormat="", setPointName=""):
    common.print_frame()
    textRenderer = setTextRenderer(dataType)
    pointLocator = {'modelType': modelType,
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
    return {'textRenderer': textRenderer, 'pointLocator': pointLocator}


def setPointLocator_Sql(dataType="BINARY", settable="false", relinquishable="false", modelType="PL.SQL",
                        fieldName="", timeOverrideName="", updateStatement="", tableModifier="false",
                        parameters=[], dateParameterFormat="yyyy-MM-dd'T'HH:mm:ss"):
    common.print_frame()
    textRenderer = setTextRenderer(dataType)
    pointLocator = {'dataType': dataType,
                    'settable': settable,
                    'relinquishable': relinquishable,
                    'modelType': modelType,
                    'fieldName': fieldName,
                    'timeOverrideName': timeOverrideName,
                    'updateStatement': updateStatement,
                    'tableModifier': tableModifier,
                    'parameters': parameters,
                    'dateParameterFormat': dateParameterFormat}
    return {'textRenderer': textRenderer, 'pointLocator': pointLocator}


def setTextRenderer(dataType):
    if dataType == "ALPHANUMERIC":
        return {'useUnitAsSuffix': 'true',
                'unit': 'C',
                'renderedUnit': 'C',
                'suffix': ' ',
                'type': 'textRendererPlain'
                }
    if dataType == "NUMERIC":
        return {"useUnitAsSuffix": 'true',
                "unit": "",
                "renderedUnit": "",
                "format": "0.00",
                "suffix": "",
                "type": "textRendererAnalog"
                }
    if dataType == "BINARY":
        return {'type': 'textRendererBinary',
                'oneColour': 'black',
                'oneLabel': 'one',
                'zeroColour': 'blue',
                'zeroLabel':'zero'
                }
    if dataType == "MULTISTATE":
        return {"multistateValues": [{"key": 0,
                                      "text": "off",
                                      "colour": "#ff0000"},
                                     {"key": 1,
                                      "text": "on",
                                      "colour": "null"}],
                "type": "textRendererMultistate"
                }


def dataPoints(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: The function returns all information about all data points
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-points', headers=myHeader, cookies=reqCookie)
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
    The function gets an instance of Data Point and inserts a new data point to Mango or updates the data points in
    Mango if it's already exits.
    :param ip:
    :param reqCookie:
    :param myDataPoint:
    """
    common.print_frame()
    pointLocator = {}
    textRender = {}
    chartRender = {}
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

    if myDataPoint.pointLocator['dataType'] == "NUMERIC":
        textRender = {"useUnitAsSuffix": myDataPoint.textRenderer['useUnitAsSuffix'],
                      "unit": myDataPoint.textRenderer['unit'],
                      "renderedUnit": myDataPoint.textRenderer['renderedUnit'],
                      "format": myDataPoint.textRenderer['format'],
                      "suffix":  myDataPoint.textRenderer['suffix'],
                      "type":  myDataPoint.textRenderer['type']
                      }


    if myDataPoint.pointLocator['dataType'] == 'ALPHANUMERIC':
        textRender = {"useUnitAsSuffix": myDataPoint.textRenderer['useUnitAsSuffix'],
                      "unit": myDataPoint.textRenderer['unit'],
                      "renderedUnit": myDataPoint.textRenderer['renderedUnit'],
                      "suffix": myDataPoint.textRenderer['suffix'],
                      "type": myDataPoint.textRenderer['type']
                      }

    if myDataPoint.pointLocator['dataType'] == "BINARY":
        textRender = {"type": myDataPoint.textRenderer['type'],
                      "oneColour": myDataPoint.textRenderer['oneColour'],
                      "oneLabel": myDataPoint.textRenderer['oneLabel'],
                      "zeroColour": myDataPoint.textRenderer['zeroColour'],
                      "zeroLabel":  myDataPoint.textRenderer['zeroLabel']
                      }

    if myDataPoint.pointLocator['dataType'] == "MULTISTATE":
        textRender = {"multistateValues": [{"key": myDataPoint.textRenderer['multistateValues'][0]['key'],
                                      "text": myDataPoint.textRenderer['multistateValues'][0]['text'],
                                      "colour": myDataPoint.textRenderer['multistateValues'][0]['colour']},
                                     {"key": myDataPoint.textRenderer['multistateValues'][1]['key'],
                                      "text": myDataPoint.textRenderer['multistateValues'][1]['text'],
                                      "colour": myDataPoint.textRenderer['multistateValues'][1]['colour']}],
                      "type": myDataPoint.textRenderer['type']
                      }


    payload = [{"enabled": myDataPoint.enabled,
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
                "textRenderer": textRender,
                "modelType": myDataPoint.modelType,
                "validationMessages": [],
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
                "xid": myDataPoint.xid,
                "name": myDataPoint.name}]
    print payload
    parameters_json = json.dumps(payload)

    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                'Content-Type': 'application/json; charset=UTF-8',
                'Connection': 'keep-alive'}
    try:
        r = requests.put('http://' + ip + ':8080' + '/rest/v1/data-points', data=parameters_json, headers=myHeader,
                         cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "The data point was added/ saved!"
            if myDataPoint.published == "true":
                add_point_to_publisher(myDataPoint.xid)
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print str(r.text)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)


def add_point_to_publisher(data_point_xid):
    parsed_xid = p_f.publisherSetMangoPersistentTCPoint([data_point_xid])
    print parsed_xid
    with open("publishers.txt")as namesFile:
        file_data = namesFile.read()
        json_file = json.loads(file_data)
        for jPoint in json_file['publishers']:
            jPoint['points'].extend(parsed_xid)
    with open("publishers.txt", 'w+')as namesFile:
        namesFile.write(json.dumps(json_file, ensure_ascii=False))


def insertUpdateDataPoint_json(ip, reqCookie, json_data):
    common.print_frame()
    print json.dumps(json_data)
    myHeader = {'Accept': 'application/json',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Content-Type': 'application/json; charset=UTF-8',
                'Connection': 'keep-alive'}
    r = requests.put('http://' + ip + ':8080' + '/rest/v1/data-points', data=json.dumps([json_data]), headers=myHeader,
                     cookies=reqCookie)
    print r.status_code


def dataPointById(ip, reqCookie, pointId):
    """
    :param ip:
    :param reqCookie:
    :param pointId:
    :return: returns information about a data point by ID
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-points/by-id/' + str(pointId), headers=myHeader,
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


def dataPointsForDataSourceByXid(ip, reqCookie, xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid:  data source xid
    :return: Get all data points for data source
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-points/data-source/' + str(xid), headers=myHeader,
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


def dataPointListWithLimit(ip, reqCookie, limit=100):
    """
    :param ip:
    :param reqCookie:
    :return: Get a few data points
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-points/list?limit=' + str(limit), headers=myHeader,
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


def deleteDataPointByXid(ip, reqCookie, xid):
    """
    :param ip:
    :param reqCookie:
    :param xid:
    :return: Delete a data point
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.delete('http://' + ip + ':8080' + '/rest/v1/data-points/' + str(xid), headers=myHeader,
                            cookies=reqCookie)
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


def getDataPointByXid(ip, reqCookie, xid):
    """
    :param ip:
    :param reqCookie:
    :param Xid: data point xid
    :return: Get data point by XID
    """
    common.print_frame()
    print xid
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-points/' + str(xid), headers=myHeader,
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


def getPointsXidBelongsToDataSource(ip, reqCookie, d_xid):
    ''' The function gets dataSource xid and returns a list of all it\'s dataPoints xids.'''
    common.print_frame()
    dp = dataPointsForDataSourceByXid(ip, reqCookie, d_xid)
    jds = json.loads(dp)
    xids_list = []
    for source in jds:
        xids_list.append(source['xid'])
    return xids_list


def getDataPointsXidFromJson(json_data):
    '''The function gets a json file and returns a list of data points xids.'''
    common.print_frame()
    jds = json.loads(json_data)
    xids_list = []
    print(jds['total'])
    for row in jds['items']:
        xids_list.append(row['xid'])
    return xids_list


def changeCOVvalueToFalse(ip, reqCookie):
    common.print_frame()
    bacnetXIDS = ds_f.getDataSourcesXidsByType(ip, reqCookie, "BACNET_ip")
    datapointsXIDS = []
    for datasource in bacnetXIDS:
        datapints_belongesTodatasource = getPointsXidBelongsToDataSource(ip, reqCookie, datasource)
        datapointsXIDS.extend(datapints_belongesTodatasource)
    for dataPoint in datapointsXIDS:
        dp = getDataPointByXid(ip, reqCookie, dataPoint)
        jdp = json.loads(dp)
        dataPoint_type = jdp['pointLocator']['modelType']
        if dataPoint_type == "PL.BACNET_IP":
            jdp['pointLocator']['useCovSubscription'] = "false"
            insertUpdateDataPoint_json(ip, reqCookie, jdp)








