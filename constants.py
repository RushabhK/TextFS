import os, sys

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = "filesystem.txt"
FILEPATH = os.path.join(CURR_DIR, FILENAME)
SUPERBLOCK_CHUNKS = 1
MAX_FILES = 100
MAX_CHUNKS = 899
CHUNK_SIZE = 1000
CHUNK_ADDR_LEN = len(str(MAX_CHUNKS))
CHUNK_DATA_SIZE = CHUNK_SIZE - CHUNK_ADDR_LEN
DELIMITER = ":"
MAX_FILENAME_LENGTH = 200
MAX_FILE_SIZE = CHUNK_SIZE * 100