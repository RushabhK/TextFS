from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import inode as ind

s = ind.Inode(1, 0)
assert(s.build_chunk("abcd.txt", 5000, 2) == ("abcd.txt:5000:2:" + "0"*984))

print "Test ran successfully!"