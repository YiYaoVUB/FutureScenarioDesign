#!/bin/bash

ml purge
ml CDO/2.0.5-gompi-2021b

# In ISIMIP3b global water sector, there are three Global Hydrological Models and each one are driven by meteorological data from five Global Climate Models
ghms=("CWatM" "H08" "WaterGAP2-2e")
gcms=("gfdl-esm4" "ipsl-cm6a-lr" "mpi-esm1-2-hr" "mri-esm2-0" "ukesm1-0-ll")
ssps=("ssp126" "ssp370" "ssp585")

# Firstly get both historical and future data
cd /data/brussel/vo/000/bvo00012/data/dataset/ISIMIP/ISIMIP3b/OutputData/water_global

# Select the years we need (historical 1996-2014; future 2015-2100) and move the output to our directory
for ghm in ${ghms[@]}
do
	for gcm in ${gcms[@]}
	do 
		for file in $ghm/$gcm/historical/"*historical_histsoc*tws*";
		do outfile=""
		outfile=$outfile$ghm/$gcm/historical/$ghm"_"$gcm"_historical_1996_2014.nc"
		cdo selyear,1996/2014 $file $outfile;
		mv $outfile /data/brussel/vo/000/bvo00012/vsc10154/scenarios_design/TWS_data/
		done
		
		for file in $ghm/$gcm/future/"*ssp126_2015soc_default*tws*";
		do outfile=""
		outfile=$outfile$ghm/$gcm/future/$ghm"_"$gcm"_future_ssp126_2015soc_2015_2100.nc"
		cdo selyear,2015/2100 $file $outfile;
		mv $outfile /data/brussel/vo/000/bvo00012/vsc10154/scenarios_design/TWS_data/
		done
		
		for file in $ghm/$gcm/future/"*ssp370_2015soc_default*tws*";
		do outfile=""
		outfile=$outfile$ghm/$gcm/future/$ghm"_"$gcm"_future_ssp370_2015soc_2015_2100.nc"
		cdo selyear,2015/2100 $file $outfile;
		mv $outfile /data/brussel/vo/000/bvo00012/vsc10154/scenarios_design/TWS_data/
		done
		
		for file in $ghm/$gcm/future/"*ssp585_2015soc_default*tws*";
		do outfile=""
		outfile=$outfile$ghm/$gcm/future/$ghm"_"$gcm"_future_ssp585_2015soc_2015_2100.nc"
		cdo selyear,2015/2100 $file $outfile;
		mv $outfile /data/brussel/vo/000/bvo00012/vsc10154/scenarios_design/TWS_data/
		done
	done
done

cd /data/brussel/vo/000/bvo00012/vsc10154/scenarios_design/TWS_data

# Merge the data to 1996-2100
for ghm in ${ghms[@]}
do
	for gcm in ${gcms[@]}
	do 
		for ssp in ${ssps[@]}
		do 
		cdo mergetime $ghm"_"$gcm"_historical_1996_2014.nc"  $ghm"_"$gcm"_future_"$ssp"_2015soc_2015_2100.nc" $ghm"_"$gcm"_"$ssp"_1996_2100.nc" 
		done
	done
done

rm *1996_2014*
rm *2015_2100*

# Get the 20-year data and calculate the mean value
for ghm in ${ghms[@]}
do
	for gcm in ${gcms[@]}
	do 
		for ssp in ${ssps[@]}
		do 
		cdo selyear,1996/2015 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_1996_2015.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_1996_2015.nc"  $ghm"_"$gcm"_"$ssp"_1996_2015_timmean.nc" 
		
		cdo selyear,2001/2020 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2001_2020.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2001_2020.nc"  $ghm"_"$gcm"_"$ssp"_2001_2020_timmean.nc" 
		
		cdo selyear,2006/2025 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2006_2025.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2006_2025.nc"  $ghm"_"$gcm"_"$ssp"_2006_2025_timmean.nc" 
		
		cdo selyear,2011/2030 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2011_2030.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2011_2030.nc"  $ghm"_"$gcm"_"$ssp"_2011_2030_timmean.nc" 
		
		cdo selyear,2016/2035 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2016_2035.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2016_2035.nc"  $ghm"_"$gcm"_"$ssp"_2016_2035_timmean.nc" 
		
		cdo selyear,2021/2040 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2021_2040.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2021_2040.nc"  $ghm"_"$gcm"_"$ssp"_2021_2040_timmean.nc" 
		
		cdo selyear,2026/2045 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2026_2045.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2026_2045.nc"  $ghm"_"$gcm"_"$ssp"_2026_2045_timmean.nc" 
		
		cdo selyear,2031/2050 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2031_2050.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2031_2050.nc"  $ghm"_"$gcm"_"$ssp"_2031_2050_timmean.nc" 
		
		cdo selyear,2036/2055 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2036_2055.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2036_2055.nc"  $ghm"_"$gcm"_"$ssp"_2036_2055_timmean.nc" 
		
		cdo selyear,2041/2060 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2041_2060.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2041_2060.nc"  $ghm"_"$gcm"_"$ssp"_2041_2060_timmean.nc" 
		
		cdo selyear,2046/2065 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2046_2065.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2046_2065.nc"  $ghm"_"$gcm"_"$ssp"_2046_2065_timmean.nc" 
		
		cdo selyear,2051/2070 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2051_2070.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2051_2070.nc"  $ghm"_"$gcm"_"$ssp"_2051_2070_timmean.nc" 
		
		cdo selyear,2056/2075 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2056_2075.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2056_2075.nc"  $ghm"_"$gcm"_"$ssp"_2056_2075_timmean.nc" 
		
		cdo selyear,2061/2080 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2061_2080.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2061_2080.nc"  $ghm"_"$gcm"_"$ssp"_2061_2080_timmean.nc" 
		
		cdo selyear,2066/2085 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2066_2085.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2066_2085.nc"  $ghm"_"$gcm"_"$ssp"_2066_2085_timmean.nc" 
		
		cdo selyear,2071/2090 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2071_2090.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2071_2090.nc"  $ghm"_"$gcm"_"$ssp"_2071_2090_timmean.nc" 
		
		cdo selyear,2076/2095 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2076_2095.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2076_2095.nc"  $ghm"_"$gcm"_"$ssp"_2076_2095_timmean.nc" 
		
		cdo selyear,2081/2100 $ghm"_"$gcm"_"$ssp"_1996_2100.nc"  $ghm"_"$gcm"_"$ssp"_2081_2100.nc" 
		cdo timmean $ghm"_"$gcm"_"$ssp"_2081_2100.nc"  $ghm"_"$gcm"_"$ssp"_2081_2100_timmean.nc" 
		done
	done
done
		
rm *5.nc *0.nc

# Do the remap from 0.5x0.5 to 0.9x1.25
for ghm in ${ghms[@]}
do
	for gcm in ${gcms[@]}
	do 
		for ssp in ${ssps[@]}
		do 
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_1996_2015_timmean.nc" $ghm"_"$gcm"_"$ssp"_1996_2015_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2001_2020_timmean.nc" $ghm"_"$gcm"_"$ssp"_2001_2020_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2006_2025_timmean.nc" $ghm"_"$gcm"_"$ssp"_2006_2025_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2011_2030_timmean.nc" $ghm"_"$gcm"_"$ssp"_2011_2030_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2016_2035_timmean.nc" $ghm"_"$gcm"_"$ssp"_2016_2035_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2021_2040_timmean.nc" $ghm"_"$gcm"_"$ssp"_2021_2040_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2026_2045_timmean.nc" $ghm"_"$gcm"_"$ssp"_2026_2045_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2031_2050_timmean.nc" $ghm"_"$gcm"_"$ssp"_2031_2050_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2036_2055_timmean.nc" $ghm"_"$gcm"_"$ssp"_2036_2055_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2041_2060_timmean.nc" $ghm"_"$gcm"_"$ssp"_2041_2060_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2046_2065_timmean.nc" $ghm"_"$gcm"_"$ssp"_2046_2065_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2051_2070_timmean.nc" $ghm"_"$gcm"_"$ssp"_2051_2070_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2056_2075_timmean.nc" $ghm"_"$gcm"_"$ssp"_2056_2075_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2061_2080_timmean.nc" $ghm"_"$gcm"_"$ssp"_2061_2080_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2066_2085_timmean.nc" $ghm"_"$gcm"_"$ssp"_2066_2085_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2071_2090_timmean.nc" $ghm"_"$gcm"_"$ssp"_2071_2090_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2076_2095_timmean.nc" $ghm"_"$gcm"_"$ssp"_2076_2095_timmean_remapcon.nc"
		cdo remapcon,grid_0.9x1.25_for_cdo.nc $ghm"_"$gcm"_"$ssp"_2081_2100_timmean.nc" $ghm"_"$gcm"_"$ssp"_2081_2100_timmean_remapcon.nc"
		done
	done
done

rm *timmean.nc

cd /data/brussel/vo/000/bvo00012/vsc10154/scenarios_design/TWS_data

# Calculate the ensemble mean of different GHMs and GCMs
for ssp in ${ssps[@]}
do 
	for year in ${years[@]}
	do 
		cdo ensmean *$ssp"_"$year* $ssp"_"$year"_remapcon_ensmean.nc"
	done
done
	
rm *remapcon.nc