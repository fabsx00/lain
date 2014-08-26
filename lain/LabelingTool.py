
import os, csv

class LabelingTool:
        
    def label(self, filename):
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                (traversal, tagName, tagValue) = row
                cmd = """echo "%s" | joern-lookup -g | awk '{print $_ "\t%s"}' | joern-tag -t %s
                """ % (traversal, tagValue, tagName) 
                
                os.system(cmd)
    
