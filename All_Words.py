#################################################### BISMI ALLAH #################################################################
import argparse, sys, subprocess, time
parser = argparse.ArgumentParser(description = 'For an successfull bruteforce attack.')
parser.add_argument('-f','--file',dest = 'file', type = str, help = 'a file name to input.')
parser.add_argument('-n','--nchars', dest = 'nchars', type = int, help = 'Maximum lengh of characters.')
parser.add_argument('-l','--lengh', dest = 'lengh', type = int, help = 'Lengh of last words of last list which successfully wroten be carfull(you may miss so many words)')
args = parser.parse_args()
nchars, target_file = args.nchars, args.file
if None in (target_file, nchars):
   print(parser.print_help())
   sys.exit(1)
target_file2 = target_file.split('/')
target_file3 = '//'.join(target_file2)
chars = ''
for ORD in range(32, 127):
    chars += chr(ORD)
if args.lengh:
    lengh = args.lengh
else:
    lengh   = 1
    nchars -= 1
    print('[*] Words of lengh: %i ...' % (lengh))
    for char in range(len(chars)):
        subprocess.Popen('echo {} >> {}; exit 0'.format(chars[char], target_file3), shell = True, stdin = subprocess.PIPE, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
while nchars:
      time.sleep(3)
      print('[*] Words of lengh: %i ...' % (lengh + 1))
      r1 = open(target_file3, 'r')
      r2 = r1.readlines()
      r1.close()
      read = []
      for n1 in range(len(r2)):
          if len(r2[n1]) == lengh + 1:
             string = ''
             for n2 in range(len(r2[n1])):
                 if r2[n1][n2:n2 + 2] != '\n':
                    string += r2[n1][n2]
                 else:
                    break
             read.append(string)
      if not read:
         print('[!] wrong lengh value.')
         break
      for line in range(len(read)):
          for char in range(len(chars)):
              subprocess.Popen('echo {} >> {}; exit 0'.format(read[line] + chars[char], target_file3), shell = True, stdin = subprocess.PIPE, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
      nchars -= 1
      lengh = len(read[0]) + 1
##################################################### AL'HAMDU LILAH #############################################################
