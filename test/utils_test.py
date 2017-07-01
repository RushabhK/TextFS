from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils import *

assert(is_file_present("abc.txt") == False)
create_file("abc.txt")
assert(is_file_present("abc.txt") == True)

write_to_file("abc.txt", "My file text")

assert(["abc.txt"] == list_all_files())

assert(get_file_contents("abc.txt") == "My file text")

write_to_file("abc.txt", "a"*2000)
assert(get_file_contents("abc.txt") == "a"*2000)

delete_file("abc.txt")
assert(is_file_present("abc.txt") == False)

print "Test ran successfully!"