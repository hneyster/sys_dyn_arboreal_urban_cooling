## Code to calculate the amount of each land cover type in Vancouver, BC

# PyQGIS code 
# For use in the Python Console in QGIS. 


# Written by Harold N. Eyster, 2023. 
#########################################
from qgis.analysis import QgsZonalHistogram

########################
## Land cover processing
########################
# Land cover data is Downloadable from the Metro Vancvouer website:
# # # Metro Vancouver (2019). Land cover classification.
# # # http://www.metrovancouver.org/data/regional-planning/Land Cover Classification 2014 - 2m LiDAR (Raster)
cover = '/home/harold/Dropbox/gitfiles/MV_landcover/LCC2014_5m_Hybrid1.tif'
iface.addRasterLayer(cover)

van_bound = '/home/harold/github/stella-vanheat/van_bound.kml'
# from the Metro Vancovue Data website:  http://www.metrovancouver.org/data/

# Each value in the raster has the following meaning: 
#1: Buildings
#2: Paved
#3: Other Built
#4: Barren
#5: Soil
#6: Coniferous
#7: Deciduous
#8: Shrub
#9: Modified Grass-herb
#10: Natural Grass-herb
#11: Non-photosynthetic vegetation
#12: Water
#13: Shadow
#14: Clouds/Ice

#specify polygon shapefile vector
polygonLayer = QgsVectorLayer(van_bound, 'zonepolygons', "ogr") 

# specify zonal histogram
rasterLayer = QgsRasterLayer(cover)
# Calculate the frequency of each land cover class within the city limits: 
processing.runAndLoadResults('gdal:zonalhistogram',{ 'COLUMN_PREFIX' : 'HISTO_', 'INPUT_RASTER' : cover, 'INPUT_VECTOR' : van_bound, 'OUTPUT' : 'van_cover_freq.shp', 'RASTER_BAND' : 1 }

zoneStat = QgsZonalStatistics(polygonLayer, rasterLayer, 'pre-', 1)
zoneStat.calculateStatistics(None)
