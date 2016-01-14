import dataPoints_Functions
import common
import json
import os
__author__ = 'Yafit'


# ========== PUBLISHERS =========
def publisherSetMangoPersistentTCPoint(points):
    """
    The function gets a lists of data points Xids and return a new list with a specific syntax.
    :param points:
    :return:
    """
    common.print_frame()
    newList = []
    for point in points:
        newList.append({"dataPointId": point})
    return newList


def publisherSetBACnetPoint(ip, reqCookie, points):
    common.print_frame()
    newList = []
    i = 0
    for point in points:
        pointData = dataPoints_Functions.getDataPointByXid(ip, reqCookie, point)
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
    common.print_frame()
    if not os.path.exists("publishers.txt"):
     craetePublishersFile()
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
    closePublishersFile()


def craetePublishersFile():
    """
    The function gets the type of the file to create: publishers or dataSources
     and creates the file with it's special text.
    """
    common.print_frame()
    with open('publishers.txt', 'w') as f:
        f.write("{\n")
        f.write('"publishers":[\n')


def closePublishersFile():
    """
    The function close the file and add some needed text.
    """
    common.print_frame()
    with open('publishers.txt', 'ab+') as f:
        f.write("]}")

        # this part is needed to parse boolean strings to boolean ex. "false" -> false
        f = open('publishers.txt', 'r')
        file_data = f.read()
        f.close()
        newdata = file_data.replace('"false"', "false")
        newdata2 = newdata.replace('"true"', "true")
        f2 = open('publishers.txt', 'w')
        f2.write(newdata2)
        f2.close()

