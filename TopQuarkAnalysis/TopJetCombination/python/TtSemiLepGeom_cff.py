import FWCore.ParameterSet.Config as cms

#
# produce geom hypothesis with all necessary 
# ingredients
#

## configure geom hyothesis
from TopQuarkAnalysis.TopJetCombination.TtSemiLepGeom_cfi import *

## make hypothesis
makeHypothesis_geom = cms.Sequence(ttSemiLepGeom)

