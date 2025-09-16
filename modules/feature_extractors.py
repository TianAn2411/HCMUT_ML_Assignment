import re          
import numpy as np 
import pandas as pd

#-----------------------------------Connectivity-----------------------------#

        #----dual sim----#
def extract_is_dual_sim (connectivity):
    if pd.isna(connectivity):
        return 0
    s = connectivity.lower()
    if 'dual sim' in s:
        return 1
    else:
        return 0

        #----5g----#
def extract_is_5g (connectivity):
    if pd.isna(connectivity):
        return 0
    s = connectivity.lower()
    if '5g' in s:
        return 1
    else:
        return 0

        #----nfc----#
def extract_is_nfc (connectivity):
    if pd.isna(connectivity):
        return 0
    s = connectivity.lower()
    if 'nfc' in s:
        return 1
    else:
        return 0

#-----------------------------------CPU-----------------------------#

        #----cpu's brand----#
def extract_cpu_brand (cpu):
    if pd.isna(cpu):
        return 'unknown'
    s = cpu.lower()
    if re.search (r'.*,\s*.*core', s):
        return s.split(' ')[0]
    else:
        return 'unknown'

        #----cpu's speed----#
def extract_cpu_speed (cpu):
    if pd.isna(cpu):
        return None
    s = cpu.lower()
    match = re.search(r'([\d\.]+)\s*(ghz|mhz)', s)
    if match:
        value = float(match.group(1))
        unit = match.group(2)
        if unit == 'mhz':
            value /= 1000
        return round(value, 2)
    return None

        #---cpu's core ammount----#
def extract_cpu_core (cpu):
    if pd.isna(cpu):
        return None
    s = cpu.lower()
    if  "dual core" in s:
        return 2
    elif "single core" in s:
        return 1
    elif "quad core" in s:
        return 4
    elif "hexa core" in s:
        return 6
    elif "octa core" in s:
        return 8
    elif "deca core" in s:
        return 10
    return None

#-----------------------------------Ram - Rom---------------------------------#

        #----Ram----#
def extract_ram(ram):
    if pd.isna(ram):
        return None
    s = ram.lower()
    match = re.search(r'(\d+)\s*gb ram', s)
    return int(match.group(1)) if match else None

        #----Rom----#
def extract_rom(ram):
    if pd.isna(ram):
        return None
    s = ram.lower()
    match = re.search(r'(\d+)\s*(gb|tb) inbuilt', s)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        if unit == 'tb':
           value *= 1024
        return value
    return None

#-----------------------------------Battery-----------------------------#


        #----battery---#
def extract_battery(battery):
    if pd.isna(battery):
        return None
    match = re.search(r'(\d+)\s*mAh', battery)
    return int(match.group(1)) if match else None

        #-----has fast charging---#
def extract_fast_charging(battery):
    if pd.isna(battery):
        return None
    s = battery.lower()
    if 'fast charging' in s:
        return 1
    else:
        return 0


#-----------------------------------Display-----------------------------#

        #----screen's size---#
def extract_screen_size(display):
    if pd.isna(display):
        return None
    s = display.lower()
    match = re.search(r'(\d+\.\d+)\s*inches', s)
    return float(match.group(1)) if match else None


        #----refresh rate----#
def extract_refresh_rate(display):
    if pd.isna(display):
        return None
    s = display.lower()
    match = re.search(r'(\d+)\s*hz', s)
    return int(match.group(1)) if match else None

        #---ppi---#
def extract_ppi(display):
    if pd.isna(display):
        return None
    size_inch = extract_screen_size(display)
    if not size_inch:
        return None

    s = display.lower()
    res_match = re.search(r"(\d+)\s*[x×]\s*(\d+)", s)
    if not res_match:
        return None
    w, h = int(res_match.group(1)), int(res_match.group(2))


    return round(np.sqrt(w**2 + h**2) / size_inch, 2)

#-----------------------------------Camera-----------------------------#

        #---Rear camera---#
def extract_rear (camera):
    if pd.isna(camera):
        return None
    match = re.search(r'(\d+)\s*MP.*Rear', camera)
    return int(match.group(1)) if match else None

    #----Front camera---#
def extract_front_camera(camera):
    if pd.isna(camera):
        return None
    if '&' in camera:
        front_cam = camera.split('&')[-1]
    else:
        front_cam = camera

    match = re.search(r'(\d+)\s*MP.*Front', front_cam)
    return int(match.group(1)) if match else None


#-----------------------------------Storage-----------------------------#

            #---Expandable storage---#
def extract_expandable_storage(expandable):
    if pd.isna(expandable):
        return None
    s = expandable.lower()
    if 'memory card not supported' in s:
        return 0
    match = re.search(r'(\d+)\s*(gb|tb)', s)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        if unit == 'tb':
            value *= 1024
        return value
    return None

#-----------------------------------OS-----------------------------#


def extract_os (os):
    if pd.isna(os):
        return 'other'
    s = os.lower()
    if 'android' in s:
        return 'android'
    elif 'ios' in s:
        return 'ios'
    else:
        return 'other'
