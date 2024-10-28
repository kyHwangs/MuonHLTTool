# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Phase2 -s HLT:75e33 --processName=MYHLT --conditions auto:phase2_realistic_T21 --geometry Extended2026D95 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 --filein=/store/mc/Phase2Fall22DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0a5c8677-10c8-4cfe-a084-d45689504151.root -n 30 --nThreads 1 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('MYHLT',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D95Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_75e33_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/Phase2Fall22DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0a5c8677-10c8-4cfe-a084-d45689504151.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Phase2 nevts:30'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

#process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
#    dataset = cms.untracked.PSet(
#        dataTier = cms.untracked.string(''),
#        filterName = cms.untracked.string('')
#    ),
#    fileName = cms.untracked.string('Phase2_HLT.root'),
#    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
#    splitLevel = cms.untracked.int32(0)
#)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')

# Path and EndPath definitions
process.hltTriggerSummaryAOD.moduleLabelPatternsToMatch = cms.vstring( 'hlt*', 'L1Tk*')
process.L1T_DoubleNNTau52 = cms.Path(process.HLTL1Sequence+process.hltL1DoubleNNTau52)
process.L1T_SingleNNTau150 = cms.Path(process.HLTL1Sequence+process.hltL1SingleNNTau150)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
#process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

# -- Timing -- #
doTiming = False
if doTiming:
    # configure the FastTimerService
    process.load( "HLTrigger.Timer.FastTimerService_cfi" )
    # print a text summary at the end of the job
    process.FastTimerService.printEventSummary         = False
    process.FastTimerService.printRunSummary           = False
    process.FastTimerService.printJobSummary           = True

    # enable DQM plots
    process.FastTimerService.enableDQM                 = True

    # enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
    process.FastTimerService.enableDQMbyPath           = True

    # enable per-module DQM plots
    process.FastTimerService.enableDQMbyModule         = True

    # enable per-event DQM plots vs lumisection
    process.FastTimerService.enableDQMbyLumiSection    = False
    process.FastTimerService.dqmLumiSectionsRange      = 2500

    # set the time resolution of the DQM plots
    process.FastTimerService.dqmTimeRange              = 50000.
    process.FastTimerService.dqmTimeResolution         =    10.
    process.FastTimerService.dqmPathTimeRange          = 50000.
    process.FastTimerService.dqmPathTimeResolution     =     5.
    process.FastTimerService.dqmModuleTimeRange        = 50000.
    process.FastTimerService.dqmModuleTimeResolution   =     1.

    # set the base DQM folder for the plots
    process.FastTimerService.dqmPath                   = 'HLT/TimerService'
    process.FastTimerService.enableDQMbyProcesses      = False
# -- #

# -- Ntuple, DQMOutput, and EDMOutput -- #
doNtuple = True
if doNtuple:
    from MuonHLTTool.MuonHLTNtupler.customizerForMuonHLTNtupler import *
    process = customizerFuncForMuonHLTNtupler(process, "MYHLT", False)

    process.ntupler.offlineMuon                   = cms.untracked.InputTag("slimmedMuons")
    process.ntupler.TkMuonToken                   = cms.InputTag("l1tTkMuonsGmt", "", "HLT")
    # process.ntupler.hltIter2IterL3FromL1MuonPixelSeeds                = cms.untracked.InputTag("hltIter2Phase2L3FromL1TkMuonPixelSeeds", "", "MYHLT")
    process.ntupler.doMVA                         = cms.bool(True)
    # Isolation study
    # process.ntupler.trkIsoTags                    = cms.untracked.vstring(   trkIsoTags )
    # process.ntupler.trkIsoLabels                  = cms.untracked.VInputTag( trkIsoLabels )
    # process.ntupler.pfIsoTags                     = cms.untracked.vstring(   pfIsoTags )
    # process.ntupler.pfIsoLabels                   = cms.untracked.VInputTag( pfIsoLabels )

    from MuonHLTTool.MuonHLTNtupler.customizerForMuonHLTSeedNtupler import *
    process = customizerFuncForMuonHLTSeedNtupler(process, "MYHLT", True)

    process.seedNtupler.L1TrackInputTag = cms.InputTag("TTTracksFromTrackletEmulation", "", "MYHLT")
    process.seedNtupler.L1TrackInputTag = cms.InputTag("TTTracksFromTrackletEmulation", "Level1TTTracks", "RECO")

    process.TFileService.fileName = cms.string("seedNtuple_D95Geo_DYToLL.root")
    
    # from HLTrigger.MuonHLTSeedMVAClassifierPhase2.customizerForMuonHLTSeeding import *
    # WPNAME = 'noMVAcut_noSeedMax'
    # doSort = False
    # nSeedMax_B = (-1,)
    # nSeedMax_E = (-1,)
    # mvaCuts_B = (0,)
    # mvaCuts_E = (0,)
    # process = customizerFuncForMuonHLTSeeding(process, "MYHLT", WPNAME, doSort, nSeedMax_B, nSeedMax_E, mvaCuts_B, mvaCuts_E )
    # process.hltIter2Phase2L3FromL1TkMuonPixelSeedsFiltered.L1TkMu = cms.InputTag("l1tTkMuonsGmt", "", "MYHLT")

#process.l1tTkMuonsGmt.applyQualityCuts = cms.bool(False)

doDQMOut = False
if doDQMOut:
    process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('DQMIO'),
            filterName = cms.untracked.string('')
        ),
        fileName = cms.untracked.string("DQMIO.root"),
        outputCommands = process.DQMEventContent.outputCommands,
        splitLevel = cms.untracked.int32(0)
    )
    process.DQMOutput = cms.EndPath( process.dqmOutput )

doEDMOut = False
if doEDMOut:
    process.writeDataset = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string('edmOutput.root'),
        outputCommands = cms.untracked.vstring(
            'drop *',
            'keep *_*_*_MYHLT'
        )
    )
    process.EDMOutput = cms.EndPath(process.writeDataset)
# -- #

process.schedule = cms.Schedule(
    # process.L1simulation_step,
    process.L1T_SingleTkMuon_22,
    process.L1T_DoubleTkMuon_15_7,
    process.L1T_TripleTkMuon_5_3_3,
    process.HLT_Mu50_FromL1TkMuon,
    process.HLT_IsoMu24_FromL1TkMuon,
    process.HLT_Mu37_Mu27_FromL1TkMuon,
    process.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_FromL1TkMuon,
    process.HLT_TriMu_10_5_5_DZ_FromL1TkMuon,
    # process.HLT_IsoStudy,
    process.HLTriggerFinalPath,
    # process.Gen_QCDBCToEFilter,
    # process.Gen_QCDEmEnrichingFilter,
    # process.Gen_QCDEmEnrichingNoBCToEFilter,
    # process.Gen_QCDMuGenFilter,
    # process.Gen_QCDMuNoEmGenFilter,
    # process.Gen_QCDEmNoMuGenFilter,
    # process.myana,
    process.mypath,
    # process.valpath,
    process.myendpath,
    process.myseedpath
    # process.DQMOutput
    # process.EDMOutput
)

# -- #

process.options.wantSummary = cms.untracked.bool( True )
if 'MessageLogger' in process.__dict__:
    process.MessageLogger.TriggerSummaryProducerAOD = cms.untracked.PSet()
    process.MessageLogger.L1GtTrigReport = cms.untracked.PSet()
    process.MessageLogger.L1TGlobalSummary = cms.untracked.PSet()
    process.MessageLogger.HLTrigReport = cms.untracked.PSet()
    process.MessageLogger.FastReport = cms.untracked.PSet()
    process.MessageLogger.ThroughputService = cms.untracked.PSet()
    process.MessageLogger.cerr.FwkReport.reportEvery = 1000
