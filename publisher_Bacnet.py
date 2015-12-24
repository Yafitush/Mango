__author__ = 'Yafit'


class Publisher_BACNET:
    def __init__(self, xid="", name="", enabled="true", snapshotSendPeriodType="MINUTES", cacheDiscardSize=1000,
                 cacheWarningSize=100, changesOnly="false", sendSnapshot="false", snapshotSendPeriods=5, points=[]):
        self.xid = xid
        self.name = name
        self.enabled = enabled
        self.type = "BACnet"
        self.points = points
        self.snapshotSendPeriodType = snapshotSendPeriodType
        self.localDeviceConfig = "48c4f966-d0b6-46dd-a327-bdd5f9bb5446"
        self.cacheDiscardSize = cacheDiscardSize
        self.cacheWarningSize = cacheWarningSize
        self.changesOnly = changesOnly
        self.sendSnapshot = sendSnapshot
        self.snapshotSendPeriods = snapshotSendPeriods
