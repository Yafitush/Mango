import DataPoint
import dataPoints_Functions
import dataPointSummary_Functions
import dataSource_Bacnet_Ip
import dataSource_Bacnet_Mstp
import dataSource_Http_Retriever
import dataSource_Mango_Persistent_TCP
import dataSource_Modbus_Ip
import dataSource_Modbus_Serial
import dataSource_sql
import dataSources_Functions
import events_Functions
import logging_Functions
import maillingLists_Functions
import pointsHierarchy_Functions
import pointsValues_functions
import publisher_Mango_Persistent_TCP
import publisher_Bacnet
import  publishers_Functions
import realTimeData_Functions
import threads_Functions
import user
import userAccess_Functions
import userComments_Functions
import users_Functions

import loginLogout_Functions
import json

__author__ = 'Yafit'

#ip = 'http://52.16.65.135:8080'
ip = '212.29.254.24'


username = 'admin'
password = 'admin'
myCookie = loginLogout_Functions.login(ip, username, password)  # must login before doing anything else!!!
print myCookie


bacnetXIDS = dataSources_Functions.getDataSourcesXidsByType(ip, myCookie, "BACNET_ip")
datapointsXIDS = []
for datasource in bacnetXIDS:
    a = dataPoints_Functions.getPointsXidBelongsToDataSource(ip, myCookie, datasource)
    datapointsXIDS.extend(a)
for dataPoint in datapointsXIDS:
    dp = dataPoints_Functions.getDataPointByXid(ip, myCookie, dataPoint)
    jdp = json.loads(dp)
    dataPoint_type = jdp['pointLocator']['modelType']
    if dataPoint_type == "PL.BACNET_IP":
        jdp['pointLocator']['useCovSubscription'] = "false"
        dataPoints_Functions.insertUpdateDataPoint_json(ip, myCookie, jdp)








'''
#==========================================================
dataSourceXID = getXid(ip, parsedCookie,  "CoolExpertBacnet")
dataSourceXID_RDM = getXid(ip, parsedCookie,  "RDM_DS")

dataPointsOfdataSourceXID = getPointsForPublisher(ip, parsedCookie, dataSourceXID)
dataPointsOfdataSourceXID_RDM = detPointsForPublisher(ip, parsedCookie, dataSourceXID_RDM)

dataPointsOfdataSourceXID.extend(dataPointsOfdataSourceXID_RDM)
publisherPoints = publisherSetMangoPersistentTCPoint(dataPointsOfdataSourceXID)
myMPTCPublisher = publisher_Mango_Persistent_TCP.Publisher_MANGO_PERSISTENT_TCP("PUB_762746", "ludwig_pub", "true",
                                                                                "MINUTES", "HOURS", "LOG_LEVEL_NONE",
                                                                                "abra_cadabra",60000,2, "10.1.0.1", 5000,
                                                                                10, 51010, "false", 30000, "0 0 1 * * ?",
                                                                                "true", "true", 3,
                                                                                1200000, "false", "false", "LUDWIG", 50000,
                                                                                5000, "false", "false", 5, publisherPoints)


craeteDataSourceOrPublishersFile("publishers")
addPublisher(myMPTCPublisher)
closeDataSourceOrPublisherFile("publishers")

#=========================================================================================
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

points = publisherSetBACnetPoint(ip, parsedCookie, ["DP_519610", "DP_991120"])

myMPTCPublisher = publisher_Mango_Persistent_TCP.Publisher_MANGO_PERSISTENT_TCP("PUB_123", "myPublisher", "true",
                                                                                "YEARS", "HOURS", "LOG_LEVEL_NONE",
                                                                                "yafit", 6000,2, "55.55.55.55", 5000, 10,
                                                                                42, "false", 3000, "", "true", "true", 3,
                                                                                1200000, "true", "false", "hiaia", 1000,
                                                                                100, "false", "false", 5, publisherPoints)
myBacnetPublisher = publisher_Bacnet.Publisher_BACNET("PUB_555", "myBACnetPublisher", "true", "MINUTES", 1000, 100,
                                                      "false", "false", 5, points)

craeteDataSourceOrPublishersFile("publishers")

addPublisher(myMPTCPublisher)
addPublisher(myBacnetPublisher)
closeDataSourceOrPublisherFile("publishers")


#myUser = user.User("fufu12", "fufu1212", "yafitush@mail.com", "NONE", "", "false", "false", "true", "Etc/UTC",
 #                  "Etc/UTC","false","superadmin", "", "INFORMATION", "")
#newUser(ip, parsedCookie, myUser)




#print myUser.validationMessages['level']
#newUser(ip, parsedCookie, myUser)
#myUser.email = "qggggggggggggggggggg"
#print myUser.email
#print myUser.username
#setUser(ip, parsedCookie, "fufu12", myUser)
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
#logoutApi(ip, parsedCookie)
# logoutUserByPOST(ip, parsedCookie, username)
'''
