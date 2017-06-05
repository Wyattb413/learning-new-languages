from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file, 'r').read()

print "The input file is %d bytes long" % len(indata)

to_file_exists = exists(to_file)
if to_file_exists == True:
    print "Does the output file exist? Yes."
else :
    print "Does the output file exist? No."
print "Ready, hit RETURN to continue, CTR-C to abort"
raw_input('> ')

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alrighty, all done."

out_file.close()
