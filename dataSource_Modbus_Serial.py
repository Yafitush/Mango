__author__ = 'Yafit'


class DataSource_MODBUS_SERIAL:
    def __init__(self, xid="", name="", enable='false',purgeType="YEARS",updatePeriodType="MINUTES", editPermission="superadmin",
                 purgeOverride='false', purgePeriod=1, updatePeriods=5,baudRate=9600, commPortId=52, dataBits=8, echo="false",
                 messageFrameSpacing=0, characterSpacing=0, parity=0, stopBits=1, contiguousBatches="false", createSlaveMonitorPoints="false",
                 overrideTiming="false", discardDataDelay=0, ioLogFileSizeMBytes=1.0, logIO="false", maxHistoricalIOLogs=1,
                 maxReadBitCount=2000, maxReadRegisterCount=125, maxWriteRegisterCount=120, multipleWritesOnly="false",
                 quantize="false",retries=2,timeout=500,encoding="RTU"):
        self.xid = xid
        self.name = name
        self.enabled = enable
        self.type = "MODBUS_SERIAL"
        self.alarmLevels = {"POLL_ABORTED":"URGENT",
                            "DATA_SOURCE_EXCEPTION":"URGENT",
                            "POINT_READ_EXCEPTION":"URGENT",
                            "POINT_WRITE_EXCEPTION":"URGENT"
                            }
        self.purgeType = purgeType
        self.updatePeriodType = updatePeriodType
        self.editPermission = editPermission
        self.purgeOverride = purgeOverride
        self.purgePeriod = purgePeriod
        self.updatePeriods = updatePeriods
        self.concurrency = "SYNC_TRANSPORT"
        self.baudRate = baudRate
        self.characterSpacing = characterSpacing
        self.commPortId = commPortId
        self.dataBits = dataBits
        self.echo = echo
        self.encoding = encoding
        self.flowControlIn = 0
        self.flowControlOut = 0
        self.messageFrameSpacing = messageFrameSpacing
        self.overrideTiming = overrideTiming
        self.parity = parity
        self.stopBits = stopBits
        self.contiguousBatches = contiguousBatches
        self.createSlaveMonitorPoints = createSlaveMonitorPoints
        self.discardDataDelay = discardDataDelay
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
