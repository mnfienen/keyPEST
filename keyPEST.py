#keyPEST --- a JUPITER-like keyword to PST translator for PEST++
# a m!ke@usgs joint
# Mike Fienen --> mnfienen@usgs.gov

import numpy as np

# ################################################ #
# Class to hold information about the in/out files #
# ################################################ #
class file_control:
    
    def __init__(self,infilename,outfilename,kws,tabs):
        self.infile = infilename
        self.outfile = outfilename
        self.kwblocks = kws
        self.tabblocks = tabs
               

# ############################ #
# Class to hold keyword blocks # 
# ############################ #
class kw:
    
    def __init__(self, blockname,kwnames,kwvals):
        self.blockname = blockname  # name of the block
        self.kwnames = kwnames      # kwnames --- provided at initialization
        self.kwvals  = kwvals       # kwvals --- starts at defaults. 
        self.blockstart = 0         # starting line for block
        self.blockend = 0           # ending line for block

# ########################## #
# Class to hold table blocks # 
# ########################## #
class tb:
    
    def __init__(self,blockname,nrows,ncols,colnames):
        self.blockname = blockname   # name of the block
        self.nrows = nrows           # number of rows to read
        self.ncols = ncols           # number of columns to read
        self.data = dict(colnames)   # set up a dict to hold cols and np arrays/lists of values
        self.extfile = UNINIT_STRING # external file in case of external
        
# set a few constants
UNINIT_STRING = 'unititialized'
UNINIT_REAL   = 9.9999e25
UNINIT_INT    = -99999

#
kwnames = list('control_data',
                'automatic_user_intervention',
                'singular value decomposition',
                'lsqr',
                'svd assist',
                'sensitivity reuse',
                'derivatives command line',
                'predictive analysis',
                'regularisation',
                'pareto')

tabnames = list('paramater_groups',
                'paramater_data',
                'observation_groups',
                'model_command_line',
                'model_input/output',
                'prior_information')
