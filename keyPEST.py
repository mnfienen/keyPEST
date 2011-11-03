#keyPEST --- a JUPITER-like keyword to PST translator for PEST++
# a m!ke@usgs joint
# Mike Fienen --> mnfienen@usgs.gov

import numpy as np
from keyPESTdata import *

# initialize the main control
main_control = file_control('testcase.key',
                            'testcase.pst',
                            kwblocks.keys(),
                            tabblocks.keys(),
                            tabblockdicts)


# read over the file once to evaluate blocknames and detect major syntax errors
main_control.check_block_integrity()

# initialize lists of block types and check that all are valid
main_control.initialize_blocks()

# read in the keyword blocks
main_control.read_keyword_blocks()

# read in the tables
main_control.read_table_blocks()

# write out the PST file
main_control.write_pst_file()