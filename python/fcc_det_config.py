
import os

from Gaudi.Configuration import *
path_to_detector = "/usr/local/"


detectors_to_use=[
                    path_to_detector+'Detector/DetFCChhBaseline1/compact/FCChh_DectEmptyMaster.xml',
                    path_to_detector+'Detector/DetFCChhTrackerTkLayout/compact/Tracker.xml',
                  path_to_detector+'/Detector/DetFCChhECalInclined/compact/FCChh_ECalBarrel_withCryostat.xml',
                  #path_to_detector+'/Detector/DetFCChhHCalTile/compact/FCChh_HCalBarrel_TileCal.xml',
                  #path_to_detector+'/Detector/DetFCChhHCalTile/compact/FCChh_HCalExtendedBarrel_TileCal.xml',
                  #path_to_detector+'/Detector/DetFCChhCalDiscs/compact/Endcaps_coneCryo.xml',
                  #path_to_detector+'/Detector/DetFCChhCalDiscs/compact/Forward_coneCryo.xml',
                  #path_to_detector+'/Detector/DetFCChhTailCatcher/compact/FCChh_TailCatcher.xml',
                  #path_to_detector+'/Detector/DetFCChhBaseline1/compact/FCChh_Solenoids.xml',
                  #path_to_detector+'/Detector/DetFCChhBaseline1/compact/FCChh_Shielding.xml',
                  ]

from Configurables import GeoSvc
geoservice = GeoSvc("GeoSvc")
geoservice.detectors = detectors_to_use
geoservice.OutputLevel = WARNING
