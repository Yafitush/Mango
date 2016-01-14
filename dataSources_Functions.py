import requests
import sys
import common
import json
import os
__author__ = 'Yafit'


# ===== DATA SOURCES ==============
def dataSources(ip, reqCookie):
    """
    :param ip:
    :param reqCookie:
    :return: Get all data sources
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-sources/list', headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            return r.content
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)


def getDataSourceByXid(ip, reqCookie, xid):
    """
    :param ip:
    :param reqCookie:
    :param xid: data source Xid
    :return: Get data source by xid
    """
    common.print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}

    try:
        r = requests.get('http://' + ip + ':8080' + '/rest/v1/data-sources/' + str(xid), headers=myHeader, cookies=reqCookie)
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


def checkIfDataSourceExists(ip, reqCookie, source_name):
    common.print_frame()
    all_dataSources = dataSources(ip, reqCookie)
    jds = json.loads(all_dataSources)
    check_if_data_source_exists = "false"
    for source in jds:
        if source['name'] == source_name:
            check_if_data_source_exists = "true"
    return check_if_data_source_exists


def getDataSourceByName(ip, reqCookie, source_name):
    """
    The function gets a dataSource name and returns information about it.
    :param ip:
    :param reqCookie:
    :param source_name:
    :return:
    """
    if checkIfDataSourceExists(ip, reqCookie, source_name):
        all_dataSources = dataSources(ip, reqCookie)
        jds = json.loads(all_dataSources)
        for source in jds:
            if source['name'] == source_name:
                return source
    else:
        print "data source " + source_name + " doesn't exist!"


def addDataSourceToDataSourceFile(myDataSource):
    """
    The function get an instance of Data source and write it to a text file.
    :param myDataSource:
    """
    common.print_frame()
    if not os.path.exists('dataSource.txt'):
        craeteDataSourceFile()
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
                         'logLevel': myDataSource.logLevel,
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
                         'username': myDataSource.username,
                         'password': myDataSource.password,
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
        json.dump(addDataSource, f, indent=0)
    closeDataSourceFile()


def craeteDataSourceFile():
    """
    The function gets the type of the file to create: publishers or dataSources
     and creates the file with it's special text.
    """
    common.print_frame()
    with open('dataSource.txt', 'w') as f:
        f.write("{\n")
        f.write('"dataSources":[\n')


def closeDataSourceFile():
    """
    The function close the file and add some needed text.
    """
    common.print_frame()
    with open('dataSource.txt', 'ab+') as f:
        f.write("]}")

        # this part is needed to parse boolean strings to boolean ex. "false" -> false
        f = open('dataSource.txt', 'r')
        file_data = f.read()
        f.close()
        newdata = file_data.replace('"false"', "false")
        newdata2 = newdata.replace('"true"', "true")
        f = open('dataSource.txt', 'w')
        f.write(newdata2)
        f.close()


def getDataSourceXid(ip, reqCookie, dataSourceName):
    """
    The function gets a data source name and returns it's xid
    """
    common.print_frame()
    ds = dataSources(ip, reqCookie)
    jds = json.loads(ds)
    for source in jds:
        if source['name'] == dataSourceName:
            return source['xid']
    return 'Data source not found.'


def getDataSourcesXidsByType(ip, reqCookie, dataSourceType):
    '''  The function gets a dataSource type and returns the xids of all data sources of the same type.'''
    common.print_frame()
    if "bacnet_ip" in dataSourceType.lower():
        ds_type = "BACnetIP"
    elif "sql" in dataSourceType.lower():
        ds_type = "SQL"
    elif "http" in dataSourceType.lower():
        ds_type = "HTTP_RETRIEVER"
    elif "mango" in dataSourceType.lower():
        ds_type = "PERSISTENT"
    elif "modbus_ip" in dataSourceType.lower():
        ds_type = "MODBUS_IP"
    elif "modbus_serial" in dataSourceType.lower():
        ds_type = "MODBUS_SERIAL"
    elif "bacnet_mstp" in dataSourceType.lower():
        ds_type = "BACnetMSTP"
    else:
        print "Unknown data source type"
        return
    xidsList = []
    ds = dataSources(ip, reqCookie)
    jds = json.loads(ds)
    for source in jds:
        if source['modelType'] == ds_type:
            xidsList.append(source['xid'])
    return xidsList


