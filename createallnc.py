import xarray as xr
import numpy as np

ncbasin = xr.open_dataset("../basin master/lumip_SSP2_BaU_NoCC.nc")
ncregion = xr.open_dataset("../region master/lumip_SSP2_BaU_NoCC.nc")

for var in ncbasin.data_vars:
    