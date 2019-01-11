
from Gaudi.Configuration import *
from GaudiKernel import SystemOfUnits as units

from Configurables import GaussSmearVertex, ConstPtParticleGun, GenAlg
smeartool = GaussSmearVertex("GaussSmearVertex")
smeartool.xVertexSigma = 0.5*units.mm
smeartool.yVertexSigma = 0.5*units.mm
smeartool.zVertexSigma = 40*units.mm
smeartool.tVertexSigma = 180*units.picosecond

from Configurables import GaussSmearVertex, ConstPtParticleGun, GenAlg
pgun_tool = ConstPtParticleGun("ParticleProviderTool")
pgun_tool.PdgCodes = [11, 13]

from Configurables import GenAlg
genalg_pgun = GenAlg("ParticleGun")
genalg_pgun.SignalProvider = pgun_tool
genalg_pgun.VertexSmearingTool = smeartool
genalg_pgun.hepmc.Path = "hepmc"

#from Configurables import PythiaInterface
#pythia8gentool = PythiaInterface("Pythia8Tool")
#genalg_pythia = GenAlg("Pythia8Algorithm")
#genalg_pythia.SignalProvider = pythia8gentool
#genalg_pythia.VertexSmearingTool=smeartool 
#genalg_pythia.hepmc.Path = "hepmc"

from Configurables import HepMCToEDMConverter
hepmc_converter = HepMCToEDMConverter("Converter")
hepmc_converter.hepmc.Path="hepmc"
hepmc_converter.genparticles.Path="allGenParticles"
hepmc_converter.genvertices.Path="GenVertices"

from Configurables import GenParticleFilter
### Filters generated particles
# accept is a list of particle statuses that should be accepted
genfilter = GenParticleFilter("StableParticleFilter")
genfilter.accept = [1]
genfilter.OutputLevel = DEBUG 
genfilter.allGenParticles.Path = "allGenParticles"
genfilter.filteredGenParticles.Path = "GenParticles"
