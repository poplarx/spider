class bad(Exception):pass

try:
    print '[[[-----------'
    raise bad()
    print '-----------]]]'
except bad:
    print "hello bad"
finally:
    print 'i am here ha'
print 'end the'
