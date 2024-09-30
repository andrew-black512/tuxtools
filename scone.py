#!/usr/bin/python3
from random import random

def pronounce_scone() :
    # TODO make confugurable, but on what 
    prob = .25 

    words = [ "skoʊn (as in code)","skɒn (o as in body)", ]
    ra = random()  # 0<=x<1 
    print(F"{ra}")
    selector = 0 if  ra > prob else 1
    print(F"Pronounce as {words[selector]}")
    print()
    print("see https://en.wikipedia.org/wiki/Scone")

if __name__ == "__main__":
  pronounce_scone()

  