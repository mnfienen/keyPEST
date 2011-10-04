#keyPEST --- a JUPITER-like keyword to PST translator for PEST++
# a m!ke@usgs joint
# Mike Fienen --> mnfienen@usgs.gov

import numpy as np
from keyPESTdata import *

# initialize the main control
main_control = file_control('testcase.key',
                            'testcase.pst',
                            kwblocknames.keys(),
                            tabblocknames.keys())

# intialize keyword and table classes
allkws = list()
alltabs = list()

# read over the file once to evaluate blocknames
main_control.read_data(allkws,alltabs)

