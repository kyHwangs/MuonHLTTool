# MuonHLT Ntupler

## Run3 140X Recipe
```
export SCRAM_ARCH=el8_amd64_gcc10
cmsrel CMSSW_14_0_0
cd CMSSW_14_0_0/src
cmsenv
git cms-init

git cms-addpkg HLTrigger/Configuration
git clone -b Run2024 git@github.com:wonpoint4/MuonHLTForRun3.git HLTrigger/Configuration/python/MuonHLTForRun3

## Data 2022, 2023 (Efficiency) - no L1 emul
hltGetConfiguration /dev/CMSSW_14_0_0/GRun \
 --process MYHLT \
 --data --globaltag 140X_dataRun3_HLT_for2024TSGStudies_v1 \
 --unprescale \
 --paths \
HLTriggerFirstPath,\
HLT_IsoMu24_v*,\
HLT_Mu50_v*,\
HLT_CascadeMu100_v*,\
HLT_HighPtTkMu100_v*,\
HLT_Mu15_v*,\
HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*,\
HLTriggerFinalPath,\
HLTAnalyzerEndpath \
 --input /store/data/Run2023D/Muon0/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/edf3f5f9-ca18-4985-bf2e-7aac083ec70e.root \
 --eras Run3 --l1-emulator uGT --l1 L1Menu_Collisions2023_v1_3_0_xml \
 --max-events -1 \
 --full --offline --no-output >hlt_muon_data_noDoublet.py

sed -i 's/numberOfThreads = 4/numberOfThreads = 1/g' hlt_muon_data_noDoublet.py
cat after_menu_data.sh >> hlt_muon_data_noDoublet.py

# With OUR Doublet Recovery
hltGetConfiguration /dev/CMSSW_14_0_0/GRun \
 --process MYHLT \
 --data --globaltag 140X_dataRun3_HLT_for2024TSGStudies_v1 \
 --unprescale \
 --paths \
HLTriggerFirstPath,\
HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*,\
HLT_IsoMu24_v*,\
HLT_Mu50_v*,\
HLT_CascadeMu100_v*,\
HLT_HighPtTkMu100_v*,\
HLT_Mu15_v*,\
HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*,\
HLTriggerFinalPath,\
HLTAnalyzerEndpath \
 --input /store/data/Run2023D/Muon0/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/edf3f5f9-ca18-4985-bf2e-7aac083ec70e.root \
 --eras Run3 --l1-emulator uGT --l1 L1Menu_Collisions2023_v1_3_0_xml \
 --max-events -1 \
 --customise \
HLTrigger/Configuration/MuonHLTForRun3/customizeMuonHLTForRun3.enableDoubletRecoveryInIOFromL1 \
 --full --offline --no-output >hlt_muon_data_Doublet.py

## Data (Timing)
### https://twiki.cern.ch/twiki/bin/viewauth/CMS/TriggerStudiesTiming
### Output will be at /eos/cms/store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/STEAM/timing_server_results/wjun/
hltGetConfiguration /dev/CMSSW_14_0_0/GRun \
 --process MYHLT \
 --data --globaltag 140X_dataRun3_HLT_for2024TSGStudies_v1 \
 --eras Run3 --timing \
 --full --offline --output minimal >hlt_muon_data_Timing.py

hltGetConfiguration /dev/CMSSW_14_0_0/GRun \
 --process MYHLT \
 --data --globaltag 140X_dataRun3_HLT_for2024TSGStudies_v1 \
 --eras Run3 --timing \
 --customise \
HLTrigger/Configuration/MuonHLTForRun3/customizeMuonHLTForRun3.enableDoubletRecoveryInIOFromL1 \
 --full --offline --output minimal >hlt_muon_data_Timing_Doublet.py

## Data 2022, 2023 (Efficiency) - Full L1 emul
hltGetConfiguration /dev/CMSSW_13_2_0/GRun \
 --process MYHLT \
 --data --globaltag 140X_dataRun3_HLT_for2024TSGStudies_v1 \
 --unprescale \
 --paths \
HLTriggerFirstPath,\
HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*,\
HLT_IsoMu24_v*,\
HLT_Mu50_v*,\
HLT_CascadeMu100_v*,\
HLT_HighPtTkMu100_v*,\
HLT_Mu15_v*,\
HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*,\
HLTriggerFinalPath,\
HLTAnalyzerEndpath \
 --input /store/data/Run2023D/Muon0/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/edf3f5f9-ca18-4985-bf2e-7aac083ec70e.root \
 --eras Run3 --l1-emulator Full --l1 L1Menu_Collisions2023_v1_3_0_xml \
 --max-events 100 \
 --full --offline --no-output >hlt_muon_data_Full.py

### MC (Efficiency)
hltGetConfiguration /dev/CMSSW_14_0_0/GRun \
 --process MYHLT \
 --mc --globaltag auto:phase1_2024_realistic \
 --unprescale \
 --paths \
HLTriggerFirstPath,\
HLT_IsoMu24_v*,\
HLT_Mu50_v*,\
HLT_CascadeMu100_v*,\
HLT_HighPtTkMu100_v*,\
HLT_Mu15_v*,\
HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*,\
HLTriggerFinalPath,\
HLTAnalyzerEndpath \
 --input /store/mc/Run3Winter24Reco/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/AODSIM/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50000/1066aeda-aac7-43ef-9599-f531496d32fd.root \
 --eras Run3 \
 --max-events 100 \
 --full --offline --no-output >hlt_muon_mc.py

# Full L1 emulation : --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_3_0_xml \

# Winter23 :  --input /store/mc/Run3Winter23Reco/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/AODSIM/KeepSi_RnD_126X_mcRun3_2023_forPU65_v1-v2/2540000/50afc1f9-64ad-4ae3-8cc3-a43f28776b94.root \
# Summer23BPix :  --input /store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/AODSIM/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/106765c3-6838-4ef8-bd9c-7487e3ab034e.root \

### 2018Data (Efficiency)
hltGetConfiguration /dev/CMSSW_13_0_0/GRun \
 --process MYHLT \
 --data --globaltag auto:run3_hlt \
 --unprescale \
 --paths \
HLTriggerFirstPath,\
HLT_IsoMu24_v*,\
HLT_Mu50_v*,\
HLT_CascadeMu100_v*,\
HLT_HighPtTkMu100_v*,\
HLT_Mu15_v*,\
HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*,\
HLTriggerFinalPath,\
HLTAnalyzerEndpath \
 --input /store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v6/40014/F7DED4A7-8B3A-574C-8805-2F4061C87ADA.root \
 --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
 --eras Run3 \
 --max-events 100 \
 --full --offline --no-output >hlt_muon_data_Run2018.py


## Test run
cmsRun hlt_muon_data_noDoublet.py
cmsRun hlt_muon_data_DoubletfromTRK.py
cmsRun hlt_muon_data_Doublet.py
```

## Ntupler
```
git clone -b Run3 git@github.com:snu-cms/MuonHLTTool.git
scram b -j8

vi after_menu_data.sh # See below
vi after_menu_mc.sh   #	See below

## Test run
cat after_menu_data.sh >> hlt_muon_data_Doublet.py
sed -i 's/numberOfThreads = 4/numberOfThreads = 1/g' hlt_muon_data_Doublet.py
cmsRun hlt_muon_data_Doublet.py

cat after_menu_mc.sh >> hlt_muon_mc_Run3.py
sed -i 's/numberOfThreads = 4/numberOfThreads = 1/g' hlt_muon_mc_Run3.py
cmsRun hlt_muon_mc_Run3.py
```

# after_menu_data.sh
```
isDIGI = False         # set True (False) for GEN-SIM-DIGI-RAW (GEN-SIM-RAW or Data)

from MuonHLTTool.MuonHLTNtupler.customizerForMuonHLTNtupler import *
process = customizerFuncForMuonHLTNtupler(process, "MYHLT", isDIGI)

#from MuonHLTTool.MuonHLTNtupler.customizerForMuonHLTSeedNtupler import *
#process = customizerFuncForMuonHLTSeedNtupler(process, "MYHLT", isDIGI)

# -- L2 seed stat recovery -- #
#process.hltIterL3MuonPixelTracksTrackingRegions.input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
#process.hltL3MuonsIterL3IO.L3TrajBuilderParameters.MuonTrackingRegionBuilder.input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
#process.HLTIterL3OIAndIOFromL2muonTkCandidateSequence = cms.Sequence(
#    process.HLTIterL3OImuonTkCandidateSequence +
#    process.hltIterL3OIL3MuonsLinksCombination +
#    process.hltIterL3OIL3Muons +
#    process.hltIterL3OIL3MuonCandidates +
#    #process.hltL2SelectorForL3IO +
#    process.HLTIterL3IOmuonTkCandidateSequence +
#    process.hltIterL3MuonsFromL2LinksCombination
#)

process.schedule = cms.Schedule(
     process.HLTriggerFirstPath,
     process.HLT_IsoMu24_v19,
     process.HLT_Mu50_v19,
     process.HLT_CascadeMu100_v9,
     process.HLT_HighPtTkMu100_v8,
     process.HLT_Mu15_v9,
     process.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v11,
     process.HLTriggerFinalPath,
     process.mypath,
     process.myendpath,
     #process.myseedpath
)
```
# after_menu_mc.sh
```
isDIGI = True         # set True (False) for GEN-SIM-DIGI-RAW (GEN-SIM-RAW or Data)

from MuonHLTTool.MuonHLTNtupler.customizerForMuonHLTNtupler import *
process = customizerFuncForMuonHLTNtupler(process, "MYHLT", isDIGI)

from MuonHLTTool.MuonHLTNtupler.customizerForMuonHLTSeedNtupler import *
process = customizerFuncForMuonHLTSeedNtupler(process, "MYHLT", isDIGI)

# -- L2 seed stat recovery -- #
#process.hltIterL3MuonPixelTracksTrackingRegions.input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
#process.hltL3MuonsIterL3IO.L3TrajBuilderParameters.MuonTrackingRegionBuilder.input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
#process.HLTIterL3OIAndIOFromL2muonTkCandidateSequence = cms.Sequence(
#    process.HLTIterL3OImuonTkCandidateSequence +
#    process.hltIterL3OIL3MuonsLinksCombination +
#    process.hltIterL3OIL3Muons +
#    process.hltIterL3OIL3MuonCandidates +
#    #process.hltL2SelectorForL3IO +
#    process.HLTIterL3IOmuonTkCandidateSequence +
#    process.hltIterL3MuonsFromL2LinksCombination
#)

process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/Run3Winter24Reco/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/AODSIM/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50000/1066aeda-aac7-43ef-9599-f531496d32fd.root ',
    ),
    secondaryFileNames=cms.untracked.vstring(
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/0a3a1e50-ae4e-4105-a88a-04108871b5b3.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/3e745ce9-88f1-4ac0-b945-d714acccfc4b.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/4e877d16-199b-440e-aede-c75e7228ef22.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/8723351d-8657-4cc7-8e47-38645f3f51f8.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/b05a5d60-89ec-497d-8620-ac7df9bcc66c.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/c91c215f-78d5-4e63-b425-bb0699b83186.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/cc63de5e-d7f5-4976-b2be-e64e03977eed.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/d9944467-85bd-4573-a001-72a9946b3199.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/ea271ea5-2f8f-4236-8d4d-81dcfebb5654.root',
        '/store/mc/Run3Winter24Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/50009/ef0f4597-9c8d-47ca-a5dd-8de787b3d975.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

process.schedule = cms.Schedule(
     process.HLTriggerFirstPath,
     process.HLT_IsoMu24_v19,
     process.HLT_Mu50_v19,
     process.HLT_CascadeMu100_v9,
     process.HLT_HighPtTkMu100_v8,
     process.HLT_Mu15_v9,
     process.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v11,
     process.HLTriggerFinalPath,
     process.mypath,
     process.myendpath,
     process.myseedpath
)
```