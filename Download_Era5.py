import cdsapi
from datetime import timedelta, date
from cdo import *

c = cdsapi.Client()
cdo = Cdo()
class Download_data:
    def __init__(self,c,cdo):
        self.c = c
        self.cdo = cdo

    def download_eradata(self,dd,mm,yr,file_name):
        self.c.retrieve(
            'reanalysis-era5',
            {
                'variable': [
                '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
                '2m_temperature', 'potential_evaporation', 'surface_pressure',
                'total_evaporation', 'total_precipitation',
                ],
                'year': yr,
                'month': mm,
                'day': dd,
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],
                'format': 'grib',
            },
            file_name)

    def daterange(self,start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def calculate_daily_values(self,start_date,end_date):
        for single_date in self.daterange(start_date, end_date):
            try:
                dd=f'{single_date.day:02d}'
                mm=f'{single_date.month:02d}'
                yr=f'{single_date.year:04d}'
                file_name=f"era5land_{yr}_{mm}_{dd}.grib"
                print(file_name)
                self.download_eradata(dd,mm,yr,file_name)
                ofile_daymax=f"Daily_max_era5land_temp_dewtemp_winds_press_{yr}_{mm}_{dd}.grib"
                ofile_daymin=f"Daily_min_era5land_temp_dewtemp_winds_press_{yr}_{mm}_{dd}.grib"
                ofile_dayavg=f"Daily_avg_era5land_temp_dewtemp_winds_press_{yr}_{mm}_{dd}.grib"
                ofile_dayacc=f"Daily_accumulated_era5land_prcp_totalevap_pevap_{yr}_{mm}_{dd}.grib"
                cdo.daymax(input="-selcode,165,166,168,167,134 " + file_name, output=ofile_daymax)
                print("Finish producing: ",ofile_daymax)
                cdo.daymin(input="-selcode,165,166,168,167,134 " + file_name, output=ofile_daymin)
                print("Finish producing: ",ofile_daymin)
                cdo.dayavg(input="-selcode,165,166,168,167,134 " + file_name, output=ofile_dayavg)
                print("Finish producing: ",ofile_dayavg)
                cdo.daysum(input="-selcode,251,182,228 " + file_name, output=ofile_dayacc)
                print("Finish producing: ",ofile_dayacc)
            except:
                print("Data not available")
