# ################################################ #
# Class to hold information about the in/out files #
# ################################################ #
class file_control:
    
    def __init__(self,infilename,outfilename,kws,tabs):
        self.infile = infilename
        self.outfile = outfilename
        self.kwblocksall = kws
        self.kwblocks = list()
        self.tabblocksall = tabs
        self.tabblocks = list()
    
    def check_block_integrity(self,allkws,alltabs):
        self.indat = open(self.infile,'r').readlines()
        cline = -1
        # first find all block names and types
        allbegins = list()
        allends = list()
        for line in self.indat:
            cline += 1
            tmp = line.lower().strip().split()
            if 'begin' in tmp:
                if 'keywords' in tmp:
                    allbegins.append([cline,tmp[1],'kw'])
                elif 'table' in tmp:
                    allbegins.append([cline,tmp[1],'tab'])
                else:
                    raise(BlockSyntaxError(cline))
            elif 'end' in tmp:
                if 'keywords' in tmp:
                    allends.append([cline,tmp[1]])
                elif 'table' in tmp:
                    allends.append([cline,tmp[1]])
        allbegins = np.array(allbegins)
        allends = np.array(allends)
        
        # now check that there are no duplicates
        kwbegins = allbegins[np.nonzero(allbegins[:,2]=='kw')[0]]
        eunichkwbegins = np.unique(kwbegins[:,1])
        tabbegins = allbegins[np.nonzero(allbegins[:,2]=='tab')[0]]
        eunichtabbegins = np.unique(tabbegins[:,1])
        kwends = allends[np.nonzero(allends[:,2]=='kw')[0]]
        eunichkwends = np.unique(kwends[:,1])
        tabends = allbegins[np.nonzero(allends[:,2]=='tab')[0]]
        eunichtabends = np.unique(tabends[:,1])

        if len(kwbegins) == len(eunichkwbegins):
            self.kw_block_duplicates = 0
        else:
            # find duplicates
            
        
        
        
        
'''                
            elif 'end' in tmp:
                for i in allkws:
                    if tmp[1] in i.blockname:
                        i.blockend = cline
                for j in alltabs:
                    if tmp[1] in j.blockname:
                        j.blockend = cline

                 if tmp[1] in self.kwblocksall:
                        self.kwblocks.append(tmp[1])
                        allkws.append(kw(tmp[1],kwblocknames[tmp[1]],blockstart=cline))
                elif 'table' in tmp:
                    if tmp[1] in self.tabblocksall:
                        self.tabblocks.append(tmp[1])
                        alltabs.append(tb(tmp[1],tabblocknames[tmp[1]],blockstart=cline))
                        '''
# ############# #
# Error classes # 
# ############# #
class BlockSyntaxError(Exception):
    def __init__(self,cline):
        self.value = cline
    def __str__(self):
        return('Block input syntax error. Illegal word on line: ' + str(self.value+1))

# ############################ #
# Class to hold keyword blocks # 
# ############################ #
class kw:
    
    def __init__(self, blockname,kwdict,blockstart=0,blockend=0):
        self.blockname = blockname   # name of the block
        self.kwdict = kwdict         # provided at initialization ---
                                     # dict with keys -> parname, vals -> values                                   
        self.blockstart = blockstart # starting line for block
        self.blockend = 0            # ending line for block

# ########################## #
# Class to hold table blocks # 
# ########################## #
class tb:
    
    def __init__(self,blockname,nrows,ncols,colnames,blockstart=0,blockend=0):
        self.blockname = blockname   # name of the block
        self.nrows = nrows           # number of rows to read
        self.ncols = ncols           # number of columns to read
        self.data = dict(colnames)   # set up a dict to hold cols and np arrays/lists of values
        self.extfile = UNINIT_STRING # external file in case of external
        self.blockstart = blockstart # starting line for block
        self.blockend = 0            # ending line for block
# set a few constants
UNINIT_STRING = 'unititialized'
UNINIT_REAL   = 9.9999e25
UNINIT_INT    = -99999

# ###################################################### #
# DICTIONARY OF KEWYWORD BLOCK NAMES, PARS, AND DEFAULTS #
# ###################################################### #
kwblocknames = {'control_data' :
                {'RSTFLE' : UNINIT_STRING, 
                'PESTMODE' : UNINIT_STRING,
                'NPAR' : UNINIT_INT,
                'NOBS' : UNINIT_INT,
                'NPARGP' : UNINIT_INT,
                'NPRIOR' : UNINIT_INT, 
                'NOBSGP' : UNINIT_INT,
                'MAXCOMPDIM' : UNINIT_INT,
                'NTPLFLE' : UNINIT_INT,
                'NINSFLE' : UNINIT_INT,
                'PRECIS' : 'single',
                'DPOINT' : 'point',
                'NUMCOM' : UNINIT_INT,
                'JACFILE' : UNINIT_INT,
                'MESSFILE' : UNINIT_INT,
                'RLAMBDA1' : UNINIT_REAL,
                'RLAMFAC' : -3,
                'PHIRATSUF' : UNINIT_REAL,
                'PHIREDLAM' : UNINIT_REAL,
                'NUMLAM' : 10,
                'JACUPDATE' : 999,
                'LAMFORGIVE' : 'lamforgive',
                'RELPARMAX' : UNINIT_REAL,
                'FACPARMAX' : UNINIT_REAL,
                'FACORIG' : UNINIT_REAL,
                'IBOUNDSTICK' : UNINIT_INT,
                'UPVECBEND' : UNINIT_INT,
                'PHIREDSWH' : UNINIT_REAL,
                'NOPTSWITCH' : UNINIT_INT,
                'SPLITSWH' : UNINIT_REAL,
                'DOAUI' : 'noaui',
                'DOSENREUSE' : 'senreuse',
                'NOPTMAX' : 25,
                'PHIREDSTP' : UNINIT_REAL,
                'NPHISTP' : UNINIT_INT,
                'NPHINORED' : UNINIT_INT,
                'RELPARSTP' : UNINIT_REAL,
                'NRELPAR' : UNINIT_INT,
                'PHISTOPTHRESH' : UNINIT_REAL,
                'LASTRUN' : 1,
                'PHIABANDON' : UNINIT_REAL,
                'ICOV' : 1,
                'ICOR' : 1,
                'IEIG' : 1,
                'IRES' : 1,
                'JCOSAVE' : 'jcosave',
                'VERBOSEREC' : 'verboserec',
                'JCOSAVEITN' : 'nojcosaveitn',
                'REISAVEITN' : 'reisaveitn',
                'PARSAVEITN' : 'parsaveitn'},
                'automatic_user_intervention' :
                {'MAXAUI' : UNINIT_INT,
                'AUISTARTOPT' : UNINIT_INT,
                'NOAUIPHIRAT' : UNINIT_REAL,
                'AUIRESTITN' : UNINIT_INT,
                'AUISENSRAT' : UNINIT_REAL,
                'AUIHOLDMAXCHG' : UNINIT_INT,
                'AUINUMFREE' : UNINIT_INT,
                'AUIPHIRATSUF' : UNINIT_REAL,
                'AUIPHIRATACCEPT' : UNINIT_REAL,
                'NAUINOACCEPT' : UNINIT_INT},
                'singular_value_decomposition' :
                {'SVDMODE': 1,
                'MAXSING' : UNINIT_INT,
                'EIGTHRESH': 0.5e-7,
                'EIGWRITE' : 0},
                'lsqr' :
                {'LSQRMODE' : UNINIT_INT,
                'LSQR_ATOL' : UNINIT_REAL,
                'LSQR_BTOL' : UNINIT_REAL,
                'LSQR_CONLIM' : UNINIT_REAL,
                'LSQR_ITNLIM' : UNINIT_INT,
                'LSQRWRITE' : UNINIT_INT},
                'svd_assist' :
                {'BASEPESTFILE' : UNINIT_STRING,
                'BASEJACFILE' : UNINIT_STRING,
                'SVDA_MULBPA' : 1,
                'SVDA_SCALADJ' : UNINIT_INT,
                'SVDA_EXTSUPER' : UNINIT_INT,
                'SVDA_SUPDERCALC' : 1,
                'SVDA_PAR_EXCL' : UNINIT_INT},
                'sensitivity_reuse':
                {'SENRELTHRESH' : UNINIT_REAL,
                'SENMAXREUSE' : UNINIT_INT,
                'SENALLCALCINT' : UNINIT_INT,
                'SENPREDWEIGHT' : UNINIT_REAL,
                'SENPIEXCLUDE' : UNINIT_STRING},
                'derivatives_command_line':
                {'DERCOMLINE' : UNINIT_STRING,
                'EXTDERFLE' : UNINIT_STRING},
                'model_command_line' :
                {'COMLINE' : UNINIT_STRING},
                'predictive_analysis' :
                {'NPREDMAXMIN' : UNINIT_INT,
                'PREDNOISE' : UNINIT_INT,
                'PD0' : UNINIT_REAL, 
                'PD1' : UNINIT_REAL, 
                'PD2' : UNINIT_REAL,
                'ABSPREDLAM' : UNINIT_REAL,
                'RELPREDLAM' : UNINIT_REAL,
                'INITSCHFAC' : UNINIT_REAL,
                'MULSCHFAC' : UNINIT_REAL,
                'NSEARCH' : UNINIT_INT,
                'ABSPREDSWH' : UNINIT_REAL,
                'RELPREDSWH' : UNINIT_REAL,
                'NPREDNORED' : UNINIT_INT,
                'ABSPREDSTP' : UNINIT_REAL,
                'RELPREDSTP' : UNINIT_REAL,
                'NPREDSTP' : UNINIT_INT},
                'regularisation' :
                {'PHIMLIM' : UNINIT_REAL,
                'PHIMACCEPT' : UNINIT_REAL, 
                'FRACPHIM' : UNINIT_REAL, 
                'MEMSAVE' : 'nomemsave',
                'WFINIT' : UNINIT_REAL, 
                'WFMIN' : UNINIT_REAL, 
                'WFMAX' : UNINIT_REAL, 
                'LINREG' : UNINIT_STRING, 
                'REGCONTINUE' : 'nocontinue',
                'WFFAC' : UNINIT_REAL, 
                'WFTOL' : UNINIT_REAL, 
                'IREGADJ' : UNINIT_INT, 
                'NOPTREGADJ' : UNINIT_INT, 
                'REGWEIGHTRAT' : UNINIT_REAL, 
                'REGSINGTHRESH' : UNINIT_REAL},
                'pareto' :
                {'PARETO_OBSGROUP' : UNINIT_STRING,
                'PARETO_WTFAC_START' : UNINIT_REAL, 
                'PARETO_WTFAC_FIN' : UNINIT_REAL, 
                'NUM_WTFAC_INC' : UNINIT_INT,
                'NUM_ITER_START' : UNINIT_INT, 
                'NUM_ITER_GEN' : UNINIT_INT, 
                'NUM_ITER_FIN' : UNINIT_INT,
                'ALT_TERM' : UNINIT_INT,
                'OBS_TERM' : UNINIT_REAL, 
                'ABOVE_OR_BELOW' : UNINIT_STRING, 
                'OBS_THRESH' : UNINIT_REAL, 
                'NUM_ITER_THRESH' : UNINIT_INT, 
                'NOBS_REPORT' : UNINIT_STRING}}

# ################################################# #
# DICTIONARY OF TABLE BLOCK NAMES WITH COLUMN NAMES #
# ################################################# #
tabblocknames = {'paramater_groups' :
                ['PARGPNME', 'INCTYP', 'DERINC', 'DERINCLB', 'FORCEN', 
                'DERINCMUL', 'DERMTHD', 'SPLITTHRESH', 'SPLITRELDIFF', 'SPLITACTION'],
                'paramater_data' :
                ['PARNME', 'PARTRANS', 'PARCHGLIM', 'PARVAL1', 'PARLBND', 
                'PARUBND', 'PARGP', 'SCALE', 'OFFSET', 'DERCOM'],
                'parameter_tied_data' :
                ['PARNME', 'PARTIED'],
                'observation_groups' :
                ['OBGNME', 'GTARG', 'COVFLE'],
                'model_command_line' :
                ['COMLINE'],
                'model_input' :
                ['TEMPFLE', 'INFLE'],
                'model_output' :
                ['INSFLE', 'OUTFLE'],
                'prior_information' :
                ['PILINES']}
