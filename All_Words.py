#!/usr/bin/python3
############################################### BISMI ALLAH #################################################################
import argparse, sys, subprocess
parser = argparse.ArgumentParser(description = 'For a successfull bruteforce attack.')
parser.add_argument('-f','--file',dest = 'file', type = str, help = 'a file name to input.')
parser.add_argument('-m','--max', dest = 'max', type = int, help = 'Maximum lengh of characters.')
parser.add_argument('-l','--lengh', dest = 'lengh', type = int, help = 'Lengh of last words of last list which successfully wroten be carfull(you may lost so many words)')
args = parser.parse_args()
nchars, file1 = args.max, args.file
if None in (file1, nchars):
   print(parser.print_help())
   sys.exit(1)
if "/" in file1:
   file2 = file1.split('/')
   file3 = '//'.join(file2)
else:
   file3 = file1
chars = ''
for ORD in range(32, 127):
    chars += chr(ORD)
total = 0
if args.lengh:
    lengh = args.lengh
else:
    lengh   = 1
    nchars -= 1
    for char in range(len(chars)):
        total += 1
        subprocess.Popen('echo {} >> {}; exit 0'.format(chars[char], file3), shell = True, stdin = subprocess.PIPE, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
        sys.stdout.write("[%s] [word count: %i]\r" % (chars[char], total))
        sys.stdout.flush()
while nchars:
   try:
      r1 = open(file3, 'r')
      r2 = r1.readlines()
      r1.close()
      read = []
      for n1 in range(len(r2)):
          if len(r2[n1]) == lengh + 1:
             string = ''
             for n2 in range(len(r2[n1])):
                 if r2[n1][n2:n2 + 2] != '\n':
                    string += r2[n1][n2]
                    continue
                 break
             read.append(string)
      if not read:
         print('[!] Wrong lengh value!')
         break
      for line in range(len(read)):
          for char in range(len(chars)):
              total += 1
              subprocess.Popen('echo {} >> {}; exit 0'.format(read[line] + chars[char], file3), shell = True, stdin = subprocess.PIPE, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
              sys.stdout.flush()
              sys.stdout.write('[%s] [word count: %i]\r' % (read[line] + chars[char], total))
      nchars -= 1
      lengh = len(read[0]) + 1
   except KeyboardInterrupt:
      print('\n') 
      sys.exit(1)
################################################## AL'HAMDU LILAH #############################################################
