__author__ = 'Yafit'

class User:
     def __init__(self, username="", password="123", email ="", receiveAlarmEmails="NONE", homeUrl="", disabled="false",
                  muted="true",admin="false", systemTimezone="Etc/UTC", timezone="Etc/UTC", receiveOwnAuditEvents="false",
                  permissions="superadmin", message="", level="INFORMATION", property=""):
        self.username = username
        self.email = email
        self.receiveAlarmEmails = receiveAlarmEmails
        self.password = password
        self.homeUrl = homeUrl
        self.disabled = disabled
        self.muted = muted
        self.admin = admin
        self.systemTimezone = systemTimezone
        self.timezone = timezone
        self.receiveOwnAuditEvents = receiveOwnAuditEvents
        self.permissions = permissions
        self.validationMessages = {'message': message,
                                   'level': level,
                                   'property': property}




