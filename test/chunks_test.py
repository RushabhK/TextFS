from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import chunks as ch

s = ch.Chunk.build_chunk("abcdefg")
assert(s == ("abcdefg" + "0" * 993))

print "Test ran successfully!"