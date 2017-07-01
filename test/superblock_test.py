from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import superblock as sb

s = sb.Superblock()

details = s.build_chunk()
assert(details == '0'*1000)

s.set_inode_no(1, 1)
assert(s.inode_details[1] == 1)

s.set_chunk_no(100, 1)
assert(s.chunk_details[100] == 1)

print "Tests ran successfully!"