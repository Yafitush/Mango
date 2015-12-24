__author__ = 'Yafit'


class DataSource_HTTP_RETRIEVER:
    def __init__(self, xid="", name="", enabled="false", purgeType="YEARS", updatePeriodType="MINUTES",
                 editPermission="superadmin", purgeOverride="false", purgePeriod=1, updatePeriods=5, quantize="false",
                 retries=2, setPointUrl="", timeoutSeconds=30, url=""):
          self.xid = xid
          self.name = name
          self.enabled = enabled
          self.type = "HTTP_RETRIEVER"
          self.alarmLevels = {"POLL_ABORTED": "URGENT",
                              "PARSE_EXCEPTION": "URGENT",
                              "DATA_RETRIEVAL_FAILURE": "URGENT",
                              "SET_POINT_FAILURE": "URGENT"
                              }
          self.purgeType = purgeType
          self.updatePeriodType = updatePeriodType
          self.editPermission = editPermission
          self.purgeOverride = purgeOverride
          self.purgePeriod = purgePeriod
          self.updatePeriods = updatePeriods
          self.quantize = quantize
          self.retries = retries
          self.setPointUrl = setPointUrl
          self.timeoutSeconds = timeoutSeconds
          self.url = url
