from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "=============================================================================="
print "If you don't want that, hit CTRL-C (^C)"
print "If you do what that, hit RETURN"
print "=============================================================================="

print "The file %s currently contains: " % filename
print "=============================================================================="
target = open(filename, 'r')
print target.read()
target.close()
print "=============================================================================="

raw_input("> ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file..."
target.truncate()

print "Now I'm going to ask you for three lines..."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = raw_input("line 4: ")
line5 = raw_input("line 5: ")

print "I'm going to write these to the file..."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5)

print "And finally, we close it..."
target.close()
