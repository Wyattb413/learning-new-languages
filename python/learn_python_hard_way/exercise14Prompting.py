from sys import argv
import hashlib

script, user_name, password = argv
prompt = '> '

hash_pass = hashlib.md5(password.encode())

post = raw_input("Do you want to post your password to all social medias? y/n \n")

if post == 'y' or post == 'yes':
    print "Well go do it yourself!"
else:
    print "Muhahahahaha your password %s has been posted...wait a minute...is that gibberish really your password???" % hash_pass.hexdigest()

print "Lol hi %s, I'm the %s script and it's fun to mess with people" % (user_name, script)

print "I'd like to ask you a few questions."

print "Do you like ice cream %s? y/n" % (user_name)
likes = raw_input(prompt)

if likes == 'y' or likes == 'yes':
    likes = 'yes' #Doing this for formatting
    print "Cool %s what flava flave?" % (user_name)
    fav_cream = raw_input(prompt)
    if fav_cream == 'vanilla' or fav_cream == 'Vanilla':
        print "Alrighty Plane Jane"
else:
    print "Well that's just garbage"

print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "Yea, I know."

print "What kind of computer do you have?"
computer = raw_input(prompt)
print "I'm just asking you these questions because I need to provide a reason for why I already have this information about you, %s" % user_name

print ""

print "Alright, so you said %s about liking ice cream." % likes
if likes == 'y' or likes == 'yes':
    print "And you said your favorite flavor was %s." % (fav_cream)
print "I already knew you live in %s, and that you have a %s computer; Which is a debateable selection." % (lives, computer)
