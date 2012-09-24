#keyPEST --- a JUPITER-like keyword to PST/XML translator for PEST and PEST++
# Mike Fienen --> mnfienen@usgs.gov
# Jeremy White --> jtwhite@usgs.gov
import sys
import numpy as np
import keyPESTdata as kp
reload(kp)
# get the input filename from the command line
infile  = sys.argv[1]
if infile[-4:] != '.kyp':
    raise(InvalidInputExtension(infile))
else:
    casename = infile[:-4]
    
# initialize the main control
main_control = kp.file_control()

# read, check, and parse the input file
main_control.read(casename+'.kyp')


# write the output file in PST form
main_control.write(casename+'.pst')

# write the output file in XML form
main_control.write(casename+'.xml')
