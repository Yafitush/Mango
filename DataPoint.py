class DataPoint:
    def __init__(self, enabled="true", templateXid="null", modelType= "DATA_POINT",
                 dataSourceId="", purgeperiods=1, purgePeriodType="YEARS", zeroLabel="zero", zeroColour="blue", oneLabel="one",
                 oneColour="black", textRenderertype="textRendererBinary", chartRendererlimit=10, chartRendererType="chartRendererTable",
                 tolerance=0, discardExtremeValues="false", discardLowLimit=-0,
                 discardHighLimit=0, loggingType="ON_CHANGE", intervalLoggingType="INSTANT",
                 overrideIntervalLoggingSamples="false", intervalLoggingSampleWindowSize=0, cacheSize=1, loggingperiods=15,
                 loggingtype="MINUTES", readPermission="", setPermission="", dataSourceName="", chartColour= "", plotType="",
                 purgeOverride="false", dataSourceXid="", pointFolderId=0, unit="C", useIntegralUnit="", integralUnit="", useRenderedUnit="",
                 renderedUnit="C", deviceName="", name="", xid="", id=0 ,setPointLocator={}):
        self.enabled = enabled
        self.templateXid = templateXid
        self.modelType = modelType
        self.dataSourceId = dataSourceId

        self. purgePeriod = {'periods': purgeperiods,
                             'type': purgePeriodType
                             }
        self.textRenderer = {'zeroLabel': zeroLabel,
                             'zeroColour': zeroColour,
                             'oneLabel': oneLabel,
                             'oneColour': oneColour,
                             'type': textRenderertype
                             }
        self.chartRenderer = {'limit': chartRendererlimit,
                              'type': chartRendererType
                              }
        self.loggingProperties = {'tolerance': tolerance,
                                  'discardExtremeValues':discardExtremeValues,
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
        self.pointLocator = setPointLocator
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
        self.id = id
        self.xid = xid
        self.name = name

