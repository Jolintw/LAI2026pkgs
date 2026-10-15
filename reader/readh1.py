import netCDF4 as nc
import numpy as np
from pathconfig import EXP_folder

h1_var_list = {}
h1_var_list["atm"] = ['FLDS', 'FLNSC', 'FSDS', 'FSDSC', 'LHFLX', 'PRECC', 'PRECT', 'SHFLX', 'ch4vmr', 'co2vmr']
h1_var_list["lnd"] = ['FIRA', 'FSA', 'HCSOI', 'SOILWATER_10CM']

h1_file_fmts = {}
h1_file_fmts["atm"] = "IGEM_{:s}_1949_2008_F_AMIP_CAM5_f19_f19.cam2.h1.{:s}-01-01-00000.nc4" # 1: exp name, 2: year
h1_file_fmts["lnd"] = "IGEM_{:s}_1949_2008_F_AMIP_CAM5_f19_f19.clm2.h1.{:s}-01-01-00000.nc4"

def read_h1_datas(read_var_list, exp_name, read_years_list):
    datas = {}
    for read_var in read_var_list:
        print(f"read {read_var}")
        datas[read_var] = read_h1_1var(read_var, exp_name, read_years_list)
    grid_infor = read_grid_infor(exp_name)
    return datas, grid_infor

def find_h1_var(read_var):
    for key in h1_var_list:
        if read_var in h1_var_list[key]:
            return key

def read_h1_1var(read_var, exp_name, read_years_list):
    exp_path = EXP_folder(exp_name)
    vartype = find_h1_var(read_var)
    data_path = exp_path / vartype / "hist"
    fn_fmt = h1_file_fmts[vartype]
    datalist = []
    for year in read_years_list:
        file = data_path / fn_fmt.format(exp_name, year)
        ds = nc.Dataset(file)
        datalist.append(ds[read_var][:])
        ds.close()
    return np.array(datalist)

def read_grid_infor(exp_name):
    read_grid_infor_names = ["lon", "lat", "area", "areaatm", "landfrac", "landmask", "topo"]
    exp_path = EXP_folder(exp_name)
    vartype = "lnd"
    data_path = exp_path / vartype / "hist"
    fn_fmt = h1_file_fmts[vartype]
    file = data_path / fn_fmt.format(exp_name, "1995")

    ds = nc.Dataset(file)
    grid_infor = {name:ds[name][:] for name in read_grid_infor_names}
    ds.close()
    return grid_infor
    
def print_h1_file_header(exp_name, vartype):
    exp_path = EXP_folder(exp_name)
    data_path = exp_path / vartype / "hist"
    fn_fmt = h1_file_fmts[vartype]
    file = data_path / fn_fmt.format(exp_name, "1995")
    print(file)
    ds = nc.Dataset(file)
    print(ds)
    ds.close()
    return file
