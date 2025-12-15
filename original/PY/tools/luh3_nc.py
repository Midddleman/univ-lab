import xarray as xr

real = xr.open_dataset("./NC/luh3.nc")

ds_2005 = real.sel(time="2005-01-01")

ds_2005.to_netcdf("./NC/luh32005.nc")