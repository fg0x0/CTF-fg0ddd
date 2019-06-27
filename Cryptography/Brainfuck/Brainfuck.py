#!/usr/bin/env python3 
#Python3 дээр бичсэн шүү ;)
#Олон character дундаас Brainfuck -н тэмдэгтүүдийг ялгах

brainfuck_characters = [
    "[", "]", "+", "-", "." , "," , "<" , ">"       
] 


content = open('something.txt').read()


bf = []

for c in content:
    if c in brainfuck_characters:
        bf.append(c)

print ''.join(bf)






















