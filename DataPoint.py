class DataPoint:
    def __init__(self, published="true", enabled="true", modelType= "DATA_POINT",
                 purgeperiods=1, purgePeriodType="YEARS", tolerance=0, discardExtremeValues="false",
                 discardLowLimit=1.7976931348623157e+308,discardHighLimit=-1.7976931348623157e+308, loggingType="INTERVAL",
                 intervalLoggingType="INSTANT", overrideIntervalLoggingSamples="false", intervalLoggingSampleWindowSize=10,
                 cacheSize=1, loggingperiods=2, loggingtype="MINUTES", readPermission=" ", setPermission=" ",
                 dataSourceName="", chartColour= "", plotType="STEP",purgeOverride="false", dataSourceXid="",
                 pointFolderId=0, unit="C", useIntegralUnit="false", integralUnit="",useRenderedUnit="false",
                 renderedUnit="C", deviceName="", name="", xid="", setPointLocator={}):
        self.enabled = enabled
        self.modelType = modelType
        self. purgePeriod = {'periods': purgeperiods,
                             'type': purgePeriodType
                             }
        self.textRenderer = setPointLocator['textRenderer']
        self.loggingProperties = {'tolerance': tolerance,
                                  'discardExtremeValues': discardExtremeValues,
                                  'discardLowLimit': discardLowLimit,
                                  'discardHighLimit': discardHighLimit,
                                  'loggingType': loggingType,
                                  'intervalLoggingType': intervalLoggingType,
                                  'overrideIntervalLoggingSamples': overrideIntervalLoggingSamples,
                                  'intervalLoggingSampleWindowSize': intervalLoggingSampleWindowSize,
                                  'cacheSize': cacheSize,
                                  'intervalLoggingPeriod': {'periods': loggingperiods,
                                                            'type': loggingtype
                                                            }
                                  }
        self.pointLocator = setPointLocator['pointLocator']
        self.readPermission = readPermission
        self.setPermission = setPermission
        self.deviceName = deviceName
        self.chartColour = chartColour
        self.plotType = plotType
        self.purgeOverride = purgeOverride
        self.dataSourceXid = dataSourceXid
        self.pointFolderId = pointFolderId
        self.unit = unit
        self.useIntegralUnit = useIntegralUnit
        self.integralUnit = integralUnit
        self.useRenderedUnit = useRenderedUnit
        self.renderedUnit = renderedUnit
        self.dataSourceName = dataSourceName
        self.xid = xid
        self.name = name
        self.published = published
