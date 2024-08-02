import re
from pygeodesy.namedTuples import LatLon3Tuple
from logging import getLogger


def parse_name(fullname: str):
    """
    Parse full names into given and family designations.
    """
    given, family = None, None
    if ', ' in fullname:
        [family, given] = fullname.title().split(', ')[:2]
    if (given == None) and (family == None):
        for q in [' del ', ' van ']:
            if q in fullname.lower():
                [given, family] = fullname.lower().split(q)
                given = given.title()
                family = f'{q.strip()}{family.title()}'
    if (given == None) and (family == None):
        nlist = fullname.title().split()
        family = nlist[-1]
        if len(nlist) >= 2:
            given = nlist[0]
            for i in range(1, len(nlist)-1):
                given = f'{given} {nlist[i]}'
    if (not given) or (not family):
        L = getLogger()
        L.warning(f'Could not parse name "{fullname}". Result of given name: "{given}" Family name: "{family}"')
    return given, family


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = float(degrees) + float(minutes)/60 + float(seconds)/3600
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal


def get_lat_lon(desc: str):
    """
    Parse latitude and longitude from description and convert to decimal degrees.
    Return all pairs found as a list of LatLon3Tuple objects.
    """
    patterns = [
        r'([+-]?\d+(\.\d+)?)°?\s*,?\s*([+-]?\d+(\.\d+)?)°?',  # 8.994410°, - 79.543000°
        r'([+-]?\d+(\.\d+)?)°?\s*([NS]),?\s*([+-]?\d+(\.\d+)?)°?\s*([EW])',  # 8.910718°N, -79.528919°
        r'(\d+)°\s*(\d+(\.\d+)?)\'?\s*([NS]),?\s*(\d+)°\s*(\d+(\.\d+)?)\'?\s*([EW])',  # 7° 38.422'N, 81° 42.079'W
        r'(\d+)°\s*(\d+)\'\s*(\d+(\.\d+)?)\"?\s*([NS]),?\s*(\d+)°\s*(\d+)\'\s*(\d+(\.\d+)?)\"?\s*([EW])',  # 9°9'42.36"N, 79°50'15.67"W
        r'(\d+)°\s*(\d+)′\s*([NS])\s*latitude,\s*(\d+)°\s*(\d+)′\s*([EW])\s*longitude',  # 9°41′ S latitude, 76°24′ W longitude
        r'(\d+)°\s*(\d+(\.\d+)?)\'?\s*([NS])\s+(\d+)°\s*(\d+(\.\d+)?)\'?\s*([EW])'  # 8° 38.743'N    79° 2.887'W
    ]
    
    latlon = []
    
    for pattern in patterns:
        matches = re.findall(pattern, desc)
        for match in matches:
            if len(match) == 4:
                # Decimal degrees format
                lat = float(match[0])
                lon = float(match[2])
            elif len(match) == 6:
                # Decimal degrees with direction
                lat = float(match[0]) * (-1 if match[2] == 'S' else 1)
                lon = float(match[3]) * (-1 if match[5] == 'W' else 1)
            elif len(match) == 8:
                # Degrees and decimal minutes with direction
                lat = dms_to_decimal(match[0], match[1], 0, match[3])
                lon = dms_to_decimal(match[4], match[5], 0, match[7])
            elif len(match) == 10:
                # Degrees, minutes, and seconds with direction
                lat = dms_to_decimal(match[0], match[1], match[2], match[4])
                lon = dms_to_decimal(match[5], match[6], match[7], match[9])
            latlon.append(LatLon3Tuple(lat, lon, 0))
    return latlon


def get_filelist(doi:str):
    """
    """
    dist_list = [] # distribution list
    # load list of datasets
    flist = []
    # iterat
    for f in flist:
 
        dist_list.append({
            'type': 'DataDownload',
            'encodingFormat': f['mimetype'],
            'name': f['filename'],
            'contentUrl': f['/object/'] 
        })