from pathlib import Path

IGEM = Path("/work10/archive/Simulations/IGEM/IGEM_Model_Output")
def EXP_folder(exp_name):
    folder = IGEM / f"IGEM_{exp_name}_1949_2008_F_AMIP_CAM5_f19_f19"
    return folder
