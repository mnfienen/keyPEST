
import numpy as np

ofp = open ('test','w')

for i in np.arange(6e6):
    ofp.write('%d %d %d %d %d %d \n' %(i,i,i,i,i,i))
ofp.close()
