__author__ = 'Yafit'


class DataSource_SQL:
     def __init__(self, xid, name="", username="", password="", enable='false', purgeType="YEARS",
                  updatePeriodType="MINUTES", editPermission="superadmin", purgeOverride='false', purgePeriod=1,
                  updatePeriods=5, connectionUrl="someConnectionURL" , driverClassname="className", rowBasedQuery='false', selectStatement=""):
        self.xid = xid
        self.name = name
        self.username = username
        self.password = password
        self.enabled = enable
        self.type = "SQL"
        self.alarmLevels = {"POLL_ABORTED":"URGENT",
                            "STATEMENT_EXCEPTION":"URGENT",
                            "DATA_SOURCE_EXCEPTION":"URGENT"
                            }
        self.purgeType = purgeType
        self.updatePeriodType = updatePeriodType
        self.editPermission = editPermission
        self.purgeOverride = purgeOverride
        self.purgePeriod = purgePeriod
        self.updatePeriods = updatePeriods
        self.connectionUrl = connectionUrl
        self.driverClassname = driverClassname
        self.rowBasedQuery = rowBasedQuery
        self.selectStatement = selectStatement

