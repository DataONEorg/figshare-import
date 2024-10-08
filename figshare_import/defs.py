import json
from pathlib import Path
from logging import getLogger
from logging.config import dictConfig

global CN_URL
CN_URL = "https://cn-stage.test.dataone.org/cn"
"""
The URL for the Coordinating Node.
Defaults to the DataONE staging CN: ``https://cn-stage.test.dataone.org/cn``
"""

global DATA_ROOT
DATA_ROOT = Path('')
"""
The root directory for the data files.
Defaults to the current directory but should be set appropriately in the
config file.
"""

global CONFIG
CONFIG = {
    "rightsholder_orcid": "http://orcid.org/0000-0001-5828-6070",
    "write_groups": ["CN=Test_Group,DC=dataone,DC=org"],
    "changePermission_groups": ["CN=Test_Group,DC=dataone,DC=org"],
    "nodeid": "urn:node:mnTestKNB",
    "mnurl": "https://dev.nceas.ucsb.edu/knb/d1/mn/",
    "cnurl": "https://cn-stage.test.dataone.org/cn",
    "metadata_json": "~/figshare-import/article-details-test.json",
    "data_root": "/mnt/ceph/repos/si/figshare/FIG-12/"
}
"""
The configuration dictionary. These values are read from the config file.
Defaults to the values above but should be set appropriately in the config file.
"""

CONFIG_LOC = Path('~/.config/figshare-import/').expanduser().absolute()
"""
The location of the configuration file.
Defaults to ``~/.config/figshare-import/``.
"""

LOGCONFIG = CONFIG_LOC.joinpath('log/config.json')
"""
The location of the logging configuration file.
Defaults to ``~/.config/figshare-import/log/config.json``.
"""

with open(LOGCONFIG, 'r') as lc:
    LOGGING_CONFIG = json.load(lc)
    """
    The logging configuration dictionary.
    Defaults to the values in the file specified by ``LOGCONFIG``.
    """

dictConfig(LOGGING_CONFIG)
WORK_LOC = Path('~/figshare-import/').expanduser().absolute()
"""
The location of the working directory.
Defaults to ``~/figshare-import/``.
"""

# a list of formats and their 
fmts = {
    '.xls': 'application/vnd.ms-excel',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.doc': 'application/msword',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.ppt': 'application/vnd.ms-powerpoint',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip',
    '.ttl': 'text/turtle',
    '.md': 'text/markdown',
    '.rmd': 'text/x-rmarkdown',
    '.csv': 'text/csv',
    '.bmp': 'image/bmp',
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.jp2': 'image/jp2',
    '.png': 'image/png',
    '.tif': 'image/geotiff',
    '.tiff': 'image/geotiff',
    '.svg': 'image/svg+xml',
    '.nc': 'netCDF-4',
    '.py': 'application/x-python',
    '.hdf': 'application/x-hdf',
    '.hdf5': 'application/x-hdf5',
    '.tab': 'text/plain',
    '.gz': 'application/x-gzip',
    '.html': 'text/html',
    '.htm': 'text/html',
    '.xml': 'text/xml',
    '.ps': 'application/postscript',
    '.tsv': 'text/tsv',
    '.rtf': 'application/rtf',
    '.mp4': 'video/mp4',
    '.r': 'application/R',
    '.rar': 'application/x-rar-compressed',
    '.fasta': 'application/x-fasta',
    '.fastq': 'application/x-fasta',
    '.fas': 'application/x-fasta',
    '.gpx': 'application/gpx+xml',
    '.json': 'application/json',
    '.geojson': 'application/geo+json',
    '.shp': 'application/x-qgis',
}
"""
A dictionary of file extensions and their corresponding MIME types.
"""

GROUP_ID = {
    46785: "Smithsonian Center for Folklife and Cultural Heritage",
    23468: "Smithsonian Museum Conservation Institute",
    23471: "Smithsonian National Air & Space Museum",
    35808: "Smithsonian National Museum of Asian Art",
    23477: "Smithsonian National Museum of Natural History",
    23492: "Smithsonian National Museum of American History",
    28985: "Smithsonian National Museum of the American Indian",
    23474: "National Zoo and Smithsonian Conservation Biology Institute",
    23480: "Snithsonian Office of the Chief Information Officer",
    48638: "Smithsonian Office of International Relations",
    23483: "Smithsonian Environmental Research Center",
    23489: "Smithsonian Libraries and Archives",
    23486: "Smithsonian Tropical Research Institute",
    23417: "Smithsonian Research Data"
}
"""
A dictionary of Figshare group IDs and their corresponding Smithsonian units.
This will be moved to a configuration file.
"""

