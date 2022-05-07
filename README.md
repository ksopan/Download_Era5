# Introduction
Dowloading ERA5 0.25^o X 0.25^o resolution hourly reanalysis datasets for Climate model bias-correction. Python code downloads data from [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview). The code automatically download ERA5-Land data and calculates daily minimum, maximum and average Temperature(**t2m**), Dewpoint Temperature(**d2m**),surface winds(**u10,v10**), and surface pressure(**sp**) along with total daily accumulated precipitation (**tp**), evaporation (**e**) and total potential evaporation(**pev**). The donloaded and processed data is in **.grib** format.

# Prerequisites
1. cdsapi (pip install cdsapi)
2. CDS credentials (i.e. username and API-Key). Copy credentials at

```bash
~/.cdsapirc
```
If credentials not available; it can be obtained after creating an account at [LOGIN](https://cds.climate.copernicus.eu/user/login?destination=%2F%23!%2Fhome).
    
3. cdo (pip install cdo)

# Run Code
```python
from Download_Era5Land import *
start_date = date(2014, 1, 1)
end_date = date(2014, 1, 2)
dd = Download_data(c,cdo)
dd.calculate_daily_values(start_date1,end_date1)
```
Above code takes start and end date and download ERA5-Land data, name of the downloaded file will be 
> era5land_2014_01_01.grib


After using calculate_daily_values() function creates **4** files as follows
   >1. Daily_max_era5land_temp_dewtemp_winds_press_yyyy_mm_dd.grib
   >2. Daily_min_era5land_temp_dewtemp_winds_press_yyyy_mm_dd.grib
   >3. Daily_avg_era5land_temp_dewtemp_winds_press_yyyy_mm_dd.grib
   >4. Daily_accumulated_era5land_prcp_totalevap_pevap_yyyy_mm_dd.grib
        
### Note:

1. Though the above produced files have different file names, the variable names are still the same as variables names mentioned in the `Introduction` section. For example, **t2m**, **d2m** variable name is available in all the files but if we load `Daily_max_era5land_temp_dewtemp_winds_press_yyyy_mm_dd.grib` file, these variable represents **Daily Maximum** temperature and dewpoint temperature and so on.

