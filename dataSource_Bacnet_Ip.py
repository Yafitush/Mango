__author__ = 'Yafit'


class DataSource_BACNET_IP:
    def __init__(self, xid="", name="", enabled="false", purgeType="YEARS", updatePeriodType="MINUTES",
                 editPermission="superadmin", purgeOverride="false", purgePeriod=1, updatePeriods=5,
                 covSubscriptionTimeoutMinutes=60):
        self.xid = xid
        self.name = name
        self.enabled = enabled
        self.type = "BACnetIP"
        self.alarmLevels = {"POLL_ABORTED":"URGENT",
                            "DEVICE_EXCEPTION":"URGENT",
                            "INITIALIZATION_EXCEPTION":"URGENT",
                            "MESSAGE_EXCEPTION":"URGENT"
                            }
        self.purgeType = purgeType
        self.updatePeriodType = updatePeriodType
        self.updatePeriods = updatePeriods
        self.editPermission = editPermission
        self.purgeOverride = purgeOverride
        self.purgePeriod = purgePeriod
        self.covSubscriptionTimeoutMinutes = covSubscriptionTimeoutMinutes
        self.localDeviceConfig = "48c4f966-d0b6-46dd-a327-bdd5f9bb5446"




