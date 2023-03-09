## Code for: Arboreal Urban Cooling Is Driven by Leaf Area Index, Leaf Boundary Layer Resistance, and Dry Leaf Mass per Leaf Area: Evidence from a System Dynamics Model
Harold N. Eyster (1\*) & Brian Beckage (1)

\* Corresponding author | haroldeyster@gmail.com

1.  Gund Institute for Environment and Department of Plant Biology,  University of Vermont, Burlington, VT 


## Repository information
This repository accompanies the paper "Arboreal Urban Cooling Is Driven by Leaf Area Index, Leaf Boundary Layer Resistance, and Dry Leaf Mass per Leaf Area: Evidence from a System Dynamics Model" published in *Atmosphere* (Eyster & Beckage, 2023). It provides  code for reproducing all statistical analyses and model visualizations. 

## License and citation information
If you use the code or data provided here, please cite our work.

## Article abstract 
Heat waves are becoming more frequent due to climate change. Summer heat waves can be particularly deadly in cities, where temperatures are already inflated by abundant impervious, dark surfaces (i.e., the heat island effect). Urban heat waves might be ameliorated by planting and maintaining urban forests. Previous observational research has suggested that conifers may be particularly effective in cooling cities. However, the observational nature of these studies has prevented the identification of the direct and indirect mechanisms that drive this differential cooling. Here, we develop a systems dynamics representation of urban forests to model the effects of the percentage cover of either conifers or broadleaf trees on temperature. Our model includes physiological and morphological differences between conifers and broadleaf trees, and physical feedback among temperature and energy fluxes. We apply the model to a case study of Vancouver, BC, Canada. Our model suggests that in temperate rainforest cities, conifers may by 1.0 &deg;C cooler than broadleaf trees; this differential increases to 1.2 &deg;C when percentage tree cover increases from 17\% to 22\% and to 1.7 &deg;C at 30\% cover. Our model suggests that these differences are due to three key tree traits: leaf area index, leaf boundary layer resistance, and dry mass per leaf area. Creating urban forests that optimize these three variables may not only sequester CO<sub>2</sub> to mitigate global climate change but also be most effective at locally minimizing deadly urban heat waves.

### Repository contents
- ``van_cover_stats.py`` PyQGIS code to calculate the frequency of each land cover type in Vancouver, BC based on data from: Metro Vancouver (2019). Land cover classification. http://www.metrovancouver.org/data/regional-planning/Land Cover Classification 2014 - 2m LiDAR (Raster). 
- ``van_cover_freq.dbf`` output of ``van_cover_stats.py`` indicating the percent cover of each land cover type. 
- ``van_cover_freq.R`` takes ``can_cover_freq.dbf`` and albedo data from  https://doi.org/10.3390/atmos13050830 and calculates albedo and land cover percentages in Vancouver, BC. 
- ``20200801_DNI.csv`` contains the direct normal irradiance (DNI) values for Vancouver, BC on 1 August 2020. Data from Physical Solar Model (PSM3) of the National Solar Radiation Database (NSRDB; https://nsrdb.nrel.gov/data-viewer; accessed on 24 May 2022) for 1 August 2020 in Vancouver, BC (location ID = 262013).
- ``vanheat_array.stmx`` contains the Stella system dynamics model. Uses data from ``10100801_DNI.csv``.