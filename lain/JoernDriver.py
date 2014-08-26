
import os, sys

class JoernDriver:
    
    def __init__(self, joern):
        self.joern = joern

    def parse(self, codeDir, outDir, addToDatabase = False):

        if not addToDatabase and os.path.exists(outDir):
            print 'Not parsing because .joernIndex exists'
            print 'Using available database.'
            return
            
        cmd = '%s -outdir %s %s' % (self.joern, outDir, codeDir)
        os.system(cmd)
        
