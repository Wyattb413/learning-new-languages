from sys import argv

script, filename = argv

txt = open(filename)

print "=================== Seeeeeerving up %s ======================" % filename
print "================================================================================"
print txt.read()
txt.close()
