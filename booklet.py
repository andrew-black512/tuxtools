#!/usr/bin/env python3
import sys

p=int(sys.argv[1]) # Get page no from command line (argv)

for i in range(0,int(p/2),2):
   print( f"Spread {i}")
   print( f"{p-i},{i+1},{i+2},{p-i-1},",  end=" " ) 
   print()

print('')