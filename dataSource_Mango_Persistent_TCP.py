__author__ = 'Yafit'


class DataSource_MANGO_PERSISTENT_TCP:
    def __init__(self, xid="", name="", enabled="true", purgeType="YEARS", editPermission="superadmin",
                 purgeOverride="false", purgePeriod=1, logLevel="LOG_LEVEL_NONE", acceptPointUpdates="true",
                 authorizationKey="abra_cadabra", port=55, saveRealtimeData="true", socketTimeout=5000, useCompression="true",
                 useCrc="true"):
         self.xid = xid
         self.name = name
         self.enabled = enabled
         self.type = "PERSISTENT"
         self.alarmLevels = {"DATA_SOURCE_EXCEPTION_EVENT": "URGENT"}
         self.purgeType = purgeType
         self.editPermission = editPermission
         self.purgeOverride = purgeOverride
         self.purgePeriod = purgePeriod
         self.logLevel = logLevel
         self.acceptPointUpdates = acceptPointUpdates
         self.authorizationKey = authorizationKey
         self.port = port
         self.saveRealtimeData = saveRealtimeData
         self.socketTimeout = socketTimeout
         self.useCompression = useCompression
         self.useCrc = useCrc
