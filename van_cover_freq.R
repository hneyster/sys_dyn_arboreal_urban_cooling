## Code to calculate albedo and percentages of various land cover classes in Vancouver, BC
## Uses data outputed from 'van_cover_stats.py'
## Written by Harold Eyster
## eyster.com

library(foreign)
library(here)
dat <- read.dbf(here('van_cover_freq.dbf'))
tot <- sum(dat)
names(dat) <- c("buildings","paved","otherBuilt","barren","soil","coniferous","deciduous","shrubs", "modifiedGrassHerb","naturalGrassHerb","nonPhotoVeg", 'water', 'shadeow','cloudsIce') #other includes water, no data, shadow, and clouds/ice 
`dat/tot
`.0439+.159
dat$coniferous/(dat$coniferous+dat$deciduous) # 22%
tree = (dat$deciduous+dat$coniferous)/tot
decid_conf_rat <- dat$deciduous/dat$coniferous # 3.63
dat$deciduous/(dat$coniferous+dat$deciduous) # 78.4% 

nowat <- dat[,!names(dat) %in% c("water")]
tree = (nowat$deciduous+nowat$coniferous)/sum(nowat)
nowat/sum(nowat)

# albedo data from: 10.3390/atmos13050830
alb <- c(.11, .12, .12, .16, .17, .16, .1, .15)
subdat <- dat[,!names(dat) %in% c("water", "shadow", "cloudsIce", "coniferous","deciduous")]
alb_tot <- sum((subdat*alb)/sum(subdat))
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