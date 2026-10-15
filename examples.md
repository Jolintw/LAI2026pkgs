reader/readh1:
```
from LAI2026pkgs.reader.readh1 import read_h1_datas, print_h1_file_header

# get header from an arbitrary file given experiment name (e.g., EXP) and variable type (e.g., atm and lnd)
file = print_h1_file_header("CTR", "lnd")
ds = nc.Dataset(file)
print(ds["FIRA"])
ds.close()
file = print_h1_file_header("CTR", "atm")
ds = nc.Dataset(file)
print(ds["FLDS"])
ds.close()

# read datas given variables, experiment name, and yearlist
baseline_yearlist = [str(y) for y in range(1979, 2008+1, 1)]
datas, grid_infor = read_h1_datas(("FIRA", "FLDS"), "CTR", baseline_yearlist)
[print(key, datas[key].shape) for key in data.keys()]
[print(key, grid_infor[key].shape) for key in grid_infor.keys()]
```