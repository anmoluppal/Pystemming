from perform_stemming import *

inp = raw_input().split()
output = ""

for word in inp:
    word = word.lower()
    output =output + perform_stemming(word) + " "

print output

#Uncomment the follwoing lines to get the word by word detailed stemming process:

"""
print 
for i in inp:
    print i,"->",perform_stemming(i)
"""
