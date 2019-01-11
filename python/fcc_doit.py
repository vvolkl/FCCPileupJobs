
from fcc_gen_config import *
from fcc_det_config import *
from fcc_sim_config import *
from fcc_sim_config_with_calo import *

# PODIO algorithm
from Configurables import FCCDataSvc
podioevent = FCCDataSvc("EventDataSvc")

from Configurables import PodioOutput
out = PodioOutput("out")
out.filename = "output.root"
out.outputCommands = [
                      "keep *",
                      ]


list_of_algorithms = [
                        genalg_pgun, 
                        hepmc_converter, 
                        genfilter,  
                        geantsim,
                        out,
                      ]

list_of_services = [
                     podioevent, 
                     geoservice, 
                     geantservice,
                    ]

from Configurables import ApplicationMgr
ApplicationMgr(
    TopAlg = list_of_algorithms,
    EvtSel = 'NONE',
    EvtMax = 10,
    ExtSvc = list_of_services,
)
