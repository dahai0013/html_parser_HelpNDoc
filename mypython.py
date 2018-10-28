#!/usr/bin/python

import sys, getopt


"""https://www.tutorialspoint.com/python/python_command_line_arguments.htm"""
def main(argv):
   directory = ''

   try:
      opts, args = getopt.getopt(argv,"hd:o:","dir=")
   except getopt.GetoptError:
      print ('1test.py -d <directory>' )
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('2test.py -d <directory>')
         sys.exit()
      elif opt in ("-d", "--dir"):
         directory = arg
      elif opt :
          print('3test.py -d <directory>')
          sys.exit(2)

   print ('Directory is :', directory)
#   print ('Output file is "', outputfile)
   sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])