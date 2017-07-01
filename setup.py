from constants import *

fobj = open(FILEPATH, "w")
size = (CHUNK_SIZE) * (SUPERBLOCK_CHUNKS + MAX_FILES + MAX_CHUNKS)
fobj.write("0" * size)
fobj.close()