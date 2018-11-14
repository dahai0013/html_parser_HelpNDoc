import os
import glob

path = 'C:\\Users\jkriker\Google Drive\FTUwebsite\O0O000OOO00O\migrate framed to unframed'
listfile = [x for x in os.listdir(path) if x.endswith(".html")]
print (listfile)

#listfile = ["Enablestats.html","IxiaTester.html"]
#print ( type(listfile))

for x in listfile:
    os.system("python html_parser_HelNDoc.py "+ x)
#print ( "done" )