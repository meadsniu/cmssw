import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing('analysis')

options.register('runNumber',
                 100, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Run number.")

options.register('datafnPosition',
                 3, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Data filename position in the positional arguments array 'data' in json file.")

options.register('runInputDir',
                 '/build1/micius/OnlineDQM_sample/', # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Directory where the DQM files will appear.")

options.register('streamLabel',
                 '_streamDQMHistograms_StorageManager', # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Stream label used in json discovery.")

options.register('delayMillis',
                 500, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of milliseconds to wait between file checks.")

options.register('nextLumiTimeoutMillis',
                 30000, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of milliseconds to wait before switching to the next lumi section if the current is missing, -1 to disable.")

options.register('skipFirstLumis',
                 False, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Skip (and ignore the minEventsPerLumi parameter) for the files which have been available at the begining of the processing. ")

options.register('deleteDatFiles',
                 False, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Delete data files after they have been closed, in order to save disk space.")

options.register('endOfRunKills',
                 False, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Kill the processing as soon as the end-of-run file appears, even if there are/will be unprocessed lumisections.")

options.parseArguments()

# Input source
DQMProtobufReader = cms.Source("DQMProtobufReader",
    runNumber = cms.untracked.uint32(options.runNumber),
    runInputDir = cms.untracked.string(options.runInputDir),
    streamLabel = cms.untracked.string(options.streamLabel),
    datafnPosition = cms.untracked.uint32(options.datafnPosition),

    delayMillis = cms.untracked.uint32(options.delayMillis),
    nextLumiTimeoutMillis = cms.untracked.int32(options.nextLumiTimeoutMillis),
    skipFirstLumis = cms.untracked.bool(options.skipFirstLumis),
    deleteDatFiles = cms.untracked.bool(options.deleteDatFiles),
    endOfRunKills  = cms.untracked.bool(options.endOfRunKills),
)
