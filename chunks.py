from constants import *

class Chunk:
	def __init__(self, chunk_no):
		try:
			if chunk_no < 0 or chunk_no > MAX_CHUNKS:
				raise ValueError("Invalid chunk no!")
			self.chunk_no = chunk_no
			self.start_address = (MAX_FILES + chunk_no)*CHUNK_SIZE	
		except Exception as e:
			print e
	
	def get_data(self, size):
		s = ""
		if size <= CHUNK_DATA_SIZE:
			with open(FILEPATH) as read_obj:
				read_obj.seek(self.start_address, 0)
				s = read_obj.read(size)
		else:
			with open(FILEPATH) as read_obj:
				read_obj.seek(self.start_address, 0)
				s = read_obj.read(CHUNK_DATA_SIZE)
				next_chunk = int(read_obj.read(CHUNK_ADDR_LEN))
				next_chunk_obj = Chunk(next_chunk)
				s = s + next_chunk_obj.get_data(size - CHUNK_DATA_SIZE)
		return s

	def get_chunk_nos(self, size):
		chunk_list = []
		if size <= CHUNK_DATA_SIZE:
			chunk_list = [self.chunk_no]
		else:
			with open(FILEPATH) as read_obj:
				read_obj.seek(self.start_address + CHUNK_DATA_SIZE, 0)
				next_chunk = int(read_obj.read(CHUNK_ADDR_LEN))
				chunk_list = [next_chunk]
				next_chunk_obj = Chunk(next_chunk)
				chunk_list = chunk_list + next_chunk_obj.get_chunk_nos(size - CHUNK_DATA_SIZE)
		return chunk_list		


	@staticmethod
	def build_chunk(data, next_chunk = 0):
		s = ""
		if len(data) <= CHUNK_DATA_SIZE:
			s = data + "0" * (CHUNK_SIZE - len(data))
		else:
			append_zeroes = "0" * (CHUNK_ADDR_LEN - len(str(next_chunk)))
			s = data[:CHUNK_DATA_SIZE] + append_zeroes + str(next_chunk)
		return s