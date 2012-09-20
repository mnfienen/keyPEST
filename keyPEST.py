#keyPEST --- a JUPITER-like keyword to PST translator for PEST++
# a m!ke@usgs joint
# Mike Fienen --> mnfienen@usgs.gov
import sys
import numpy as np
import keyPESTdata as kp
reload(kp)
# get the input filename from the command line
infile  = sys.argv[1]
if infile[-4:] != '.key':
    raise(InvalidInputExtension(infile))
else:
    casename = infile[:-4]
    

# initialize the main control
main_control = kp.file_control(casename+'.key',casename+'.pst')
                           

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