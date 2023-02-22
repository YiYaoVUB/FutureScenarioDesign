import scipy.io as scio

hist_AREA_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP226\AREA.mat')
hist_AREA = hist_AREA_dict['AREA']

hist_PCT_CROP_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP226\PCT_CROP.mat') # no problem
hist_PCT_CROP = hist_PCT_CROP_dict['PCT_CROP']

all_CROP_AREA_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP226\\CROP_AREA.mat') # irrigated actually
all_CROP_AREA = all_CROP_AREA_dict['CROP_AREA']

all_real_CROP_AREA_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP226\\real_CROP_AREA.mat') # all cropland actually
all_real_CROP_AREA = all_real_CROP_AREA_dict['real_CROP_AREA']

