def convert():
    response = raw_input('Enter A Word: ')
    if not isinstance(response, str):
        print 'Please Enter A Valid Word'
        convert()
    else:
        first_letter = response[0]
        pygLatin = response[1:] + first_letter + 'ay'
        return 'The Pyglatin Translation is: %s' % pygLatin

print convert()
