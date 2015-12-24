__author__ = 'Yafit'


class DataSource_MODBUS_IP:
    def __init__(self, xid="", name="", enabled="false", purgeType="YEARS", updatePeriodType="MINUTES",
                 editPermission="superadmin", purgeOverride="false", purgePeriod=1, updatePeriods=5, transportType="TCP",
                 encapsulated="false", host="192.16.5.25", port=502, contiguousBatches="false", createSlaveMonitorPoints="false",
                 discardDataDelay=0, ioLogFileSizeMBytes=1.0, maxHistoricalIOLogs=1, maxReadBitCount=2000, maxReadRegisterCount=125,
                 maxWriteRegisterCount=120, multipleWritesOnly="false", quantize="false", retries=2, timeout=500, logIO="false"):
        self.xid = xid
        self.name = name
        self.enabled = enabled
        self.type = "MODBUS_IP",
        self.alarmLevels = {"POLL_ABORTED":"URGENT",
                            "DATA_SOURCE_EXCEPTION":"URGENT",
                            "POINT_READ_EXCEPTION":"URGENT",
                            "POINT_WRITE_EXCEPTION":"URGENT"
                            }
        self.purgeType = purgeType
        self.updatePeriodType = updatePeriodType
        self.updatePeriods = updatePeriods
        self.editPermission = editPermission
        self.purgeOverride = purgeOverride
        self.purgePeriod = purgePeriod
        self.transportType = transportType
        self.encapsulated = encapsulated
        self.host = host
        self.port = port
        self.contiguousBatches = contiguousBatches
        self.createSlaveMonitorPoints = createSlaveMonitorPoints
        self.discardDataDelay = discardDataDelay,
        self.ioLogFileSizeMBytes = ioLogFileSizeMBytes
        self.logIO = logIO
        self.maxHistoricalIOLogs = maxHistoricalIOLogs
        self.maxReadBitCount = maxReadBitCount
        self.maxReadRegisterCount = maxReadRegisterCount
        self.maxWriteRegisterCount = maxWriteRegisterCount
        self.multipleWritesOnly = multipleWritesOnly
        self.quantize = quantize
        self.retries = retries
        self.timeout = timeout
