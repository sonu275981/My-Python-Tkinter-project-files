ab = open("mytxt.txt","r")
ac = ab.read(); # for all line
# ac = ab.readline() # for single line
# ac = ab.readline()

print(ac)
ab.close()