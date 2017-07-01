from constants import *

class Superblock:
	def __init__(self):
		with open(FILEPATH) as read_obj:
			read_obj.seek(1, 0) #Leave the first byte
			self.inode_details = [0] + map(int, list(read_obj.read(MAX_FILES))) #1 indexed
			self.chunk_details = [0] + map(int, list(read_obj.read(MAX_CHUNKS))) #1 indexed

	def set_inode_no(self, inode_no, val):
		try:
			if inode_no < 1 or inode_no > MAX_FILES:
				raise ValueError("Invalid Inode number!")
			if val != 0 and val != 1:
				raise ValueError("Invalid value to be entered in Inode details!")
			self.inode_details[inode_no] = val
		except Exception as e:
			print e


	def set_chunk_no(self, chunk_no, val):
		try:
			if chunk_no < 1 or chunk_no > MAX_CHUNKS:
				raise ValueError("Invalid Chunk number!")
			if val != 0 and val != 1:
				raise ValueError("Invalid value to be entered in Chunk details!")
			self.chunk_details[chunk_no] = val
		except Exception as e:
			print e

	def build_chunk(self):
		start_string = "0"
		inode_string = ''.join(str(e) for e in self.inode_details[1:]) #1 indexed
		chunk_string = ''.join(str(e) for e in self.chunk_details[1:]) #1 indexed
		return (start_string + inode_string + chunk_string)