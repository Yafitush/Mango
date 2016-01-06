__author__ = 'Yafit'


class Publisher_MANGO_PERSISTENT_TCP:
     def __init__(self, xid="", name="", enabled="true",snapshotSendPeriodType="MINUTES",
                  historyCutoffPeriodType="HOURS", logLevel="LOG_LEVEL_NONE", authorizationKey="abra_cadabra", connectionCheckPeriod=60000,
                  historyCutoffPeriods=2, host="127.0.0.1", maxPointValuesToSend=5000, parallelSyncTasks=10, port=0,
                  reconnectSyncs="false", socketTimeout=30000, syncPattern="", syncPointHierarchy="true", syncRealTime="true",
                  syncRequestRetryAttempts=3, syncResponseTimeout=1200000, useCompression="true", useCrc="false",
                  xidPrefix="",cacheDiscardSize=1000, cacheWarningSize=100, changesOnly="false", sendSnapshot="false",
                  snapshotSendPeriods=5, points=[]):
         self.xid = xid
         self.name = name
         self.enabled = enabled
         self.type = "PERSISTENT"
         self.points = points
         self.snapshotSendPeriodType=snapshotSendPeriodType
         self.historyCutoffPeriodType=historyCutoffPeriodType
         self.logLevel = logLevel
         self.authorizationKey = authorizationKey
         self.connectionCheckPeriod = connectionCheckPeriod
         self.historyCutoffPeriods = historyCutoffPeriods
         self.host = host
         self.maxPointValuesToSend = maxPointValuesToSend
         self.parallelSyncTasks = parallelSyncTasks
         self.port = port
         self.reconnectSyncs = reconnectSyncs
         self.socketTimeout = socketTimeout
         self.syncPattern = syncPattern
         self.syncPointHierarchy = syncPointHierarchy
         self.syncRealTime = syncRealTime
         self.syncRequestRetryAttempts = syncRequestRetryAttempts
         self.syncResponseTimeout = syncResponseTimeout
         self.useCompression = useCompression
         self.useCrc = useCrc
         self.xidPrefix = xidPrefix
         self.cacheDiscardSize = cacheDiscardSize
         self.cacheWarningSize = cacheWarningSize
         self.changesOnly = changesOnly
         self.sendSnapshot = sendSnapshot
         self.snapshotSendPeriods = snapshotSendPeriods


