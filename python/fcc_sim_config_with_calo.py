
from fcc_sim_config import *


calo_readouts = {
                  "EcalBarrel": ["ECalBarrelEta"],
                  #"HcalBarrel": ["HCalBarrelReadout"],
                  #"MiscCalo":   [
                  #                "ECalBarrelPhiEta",
                  #                "EMECPhiEta",
                  #                "EMFwdPhiEta",
                  #                "HCalExtBarrelReadout",
                  #                "HECPhiEta",
                  #                "HFwdPhiEta",
                  #                "Muons_Readout",
                  #              ]
                  }



from Configurables import SimG4SaveCalHits
for calo_name in calo_readouts:
  savecaltool = SimG4SaveCalHits(calo_name)
  savecaltool.readoutNames = calo_readouts[calo_name]
  savecaltool.positionedCaloHits.Path = calo_name + "PositionedHits"
  savecaltool.caloHits.Path = calo_name + "Hits"
  geant_output_tool_list += [savecaltool]


geantsim.outputs = geant_output_tool_list
