from constants import *

class Inode:
	def __init__(self, file_no, file_present):	
		self.file_no = file_no
		self.start_address = file_no*CHUNK_SIZE
		if file_present == 1:
			with open(FILEPATH) as read_obj:
				read_obj.seek(self.start_address, 0)
				chunk_string = read_obj.read(CHUNK_SIZE)
				l = chunk_string.split(DELIMITER)
				self.file_name = l[0]
				self.file_size = int(l[1])
				self.chunk_start = int(l[2])

	def build_chunk(self, filename, size, chunk_start):
		chunk_string = ""
		try:
			with open(FILEPATH) as read_obj:
				read_obj.seek(self.start_address, 0)
				chunk_string = read_obj.read(CHUNK_SIZE)
			if len(filename) > MAX_FILENAME_LENGTH:
				raise ValueError("Filename length cannot be more than " + str(MAX_FILENAME_LENGTH))
			if size > MAX_FILE_SIZE:
				raise ValueError("File size cannot be more than " + str(MAX_FILE_SIZE))
			if DELIMITER in filename:
				raise Exception("Filename cannot contain the symbol " + DELIMITER)

			chunk_string =  filename + DELIMITER + \
							str(size) + DELIMITER + \
							str(chunk_start) + DELIMITER
			len_string = len(chunk_string)
			chunk_string = chunk_string + "0"*(CHUNK_SIZE - len_string) # 0 Padding
		except Exception as e:
			print e
		return chunk_string