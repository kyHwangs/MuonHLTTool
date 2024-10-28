# MuonHLT Ntupler

## Setup (14_1_0_pre7)
```
cmsrel 14_1_0_pre7
cd 14_1_0_pre7/src
cmsenv
git cms-init

// Adding patatrack
git remote add luca https://github.com/lguzzi/cmssw
git fetch luca
git cherry-pick b4e8c86523


// Adding ntupler
git cms-addpkg HLTrigger/Configuration
git clone -b Phase2_2024 https://github.com/kyHwangs/MuonHLTTool.git
scram b -j8
```

## Configuration
### L1 re-emulate

```
// output result with 100 events on /eos/user/k/khwang/www/2024_HLT_Phase2/patatrack/L1_L1Trigger/ntuple_1.root

cmsDriver.py Phase2 -s L1,L1TrackTrigger \
--conditions auto:phase2_realistic_T33 \
--geometry Extended2026D110 \
--era Phase2C17I13M9 \
--eventcontent FEVTDEBUGHLT \
--datatier GEN-SIM-DIGI-RAW-MINIAOD \
--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT,L1Trigger/Configuration/customisePhase2TTOn110.customisePhase2TTOn110 \
--filein file:/eos/cms/store/mc/Phase2Spring24DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_140X_mcRun4_realistic_v4-v1/2810000/67e21bae-f9cd-43f1-8974-e163400220f7.root \
--fileout file:./ntuple_1.root \
--python_filename rerunL1_cfg.py \
--inputCommands="keep *, drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT" \
--outputCommands="drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT" \
--mc \
-n 100 --nThreads 1 \
--no_exec
```

### HLT re-emulate
```
// if want to enable patatrack, add '--procModifiers alpaka'

cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX \
--conditions auto:phase2_realistic_T33 \
--geometry Extended2026D110 \
--era Phase2C17I13M9 \
--eventcontent FEVTDEBUGHLT \
--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
--filein file:/eos/user/k/khwang/www/2024_HLT_Phase2/patatrack/L1_L1Trigger/ntuple_1.root \
--python_filename rerunHLT_cfg.py \
--inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' \
--mc \
-n 100 --nThreads 1 \
--procModifiers alpaka \
--no_exec
```
and then ntupler and seed-ntupler part should be added.
Added version for HLT re-emulation: [rerunHLT_cfg.py](https://github.com/kyHwangs/MuonHLTTool/blob/Phase2_2024/rerunHLT_cfg.py)

### problem with [rerunHLT_cfg.py](https://github.com/kyHwangs/MuonHLTTool/blob/Phase2_2024/rerunHLT_cfg.py)

```
----- Begin Fatal Exception 28-Oct-2024 16:18:24 CET-----------------------
An exception of category 'InvalidReference' occurred while
   [0] Processing  Event run: 1 lumi: 982 event: 981002 stream: 0
   [1] Running path 'myendpath'
   [2] Calling method for module MuonHLTNtupler/'ntupler'
Exception Message:
ClusterTPAssociation has OmniClusterRefs with ProductIDs 2:330,2:233 but got OmniClusterRef/ProductID with ID 5:115. This is typically caused by a configuration error.
----- End Fatal Exception -------------------------------------------------
```

should be fixed.


### L1 + HLT emulation
The output of L1 re-emulation has huge size (~60M per event, there are 1M event for each sample, that means ~60 TB for total sample)
We have to find by-pass the L1 re-emulation.

```
cmsDriver.py Phase2 -s L1,L1TrackTrigger,L1P2GT,HLT:75e33 --processName=HLTX \
--conditions auto:phase2_realistic_T33 \
--geometry Extended2026D110 \
--era Phase2C17I13M9 \
--eventcontent FEVTDEBUGHLT \
--datatier GEN-SIM-DIGI-RAW-MINIAOD \
--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT,L1Trigger/Configuration/customisePhase2TTOn110.customisePhase2TTOn110 \
--filein file:/eos/cms/store/mc/Phase2Spring24DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_140X_mcRun4_realistic_v4-v1/2810000/67e21bae-f9cd-43f1-8974-e163400220f7.root \
--python_filename rerunL1HLT_cfg.py \
--inputCommands="keep *, drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT" \
--inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' \
--outputCommands="drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT" \
--mc \
-n 100 --nThreads 1 \
--procModifiers alpaka \
--no_exec
```

### problem with original config: [rerunL1HLT_cfg.py](https://github.com/kyHwangs/MuonHLTTool/blob/Phase2_2024/rerunL1HLT_cfg.py)

```
----- Begin Fatal Exception 16-Sep-2024 19:48:05 CEST-----------------------
An exception of category 'FileReadError' occurred while
   [0] Processing  Event run: 1 lumi: 982 event: 981002 stream: 0
   [1] Running path 'MC_BTV'
   [2] Prefetching for module CSCRecHitDProducer/'hltCsc2DRecHits'
   [3] While reading from source MuonDigiCollection<CSCDetId,CSCStripDigi> simMuonCSCDigis 'MuonCSCStripDigi' HLT
   [4] Rethrowing an exception that happened on a different read request.
   [5] Processing  Event run: 1 lumi: 982 event: 981002 stream: 0
   [6] Running path 'HLTriggerFinalPath'
   [7] Prefetching for module TriggerSummaryProducerAOD/'hltTriggerSummaryAOD'
   [8] While reading from source std::vector<l1t::TrackerMuon> l1tTkMuonsGmt '' HLT
   [9] Reading branch l1tTrackerMuons_l1tTkMuonsGmt__HLT.
   Additional Info:
      [a] Fatal Root Error: @SUB=TStreamerInfo::BuildOld
Cannot convert l1t::TrackerMuon::muRef_ from type: vector<edm::Ref<BXVector<l1t::RegionalMuonCand>,l1t::RegionalMuonCand,edm::refhelper::FindUsingAdvance<BXVector<l1t::RegionalMuonCand>,l1t::RegionalMuonCand> > > to type: vector<edm::Ref<vector<l1t::SAMuon>,l1t::SAMuon,edm::refhelper::FindUsingAdvance<vector<l1t::SAMuon>,l1t::SAMuon> > >, skip element

----- End Fatal Exception -------------------------------------------------
```

