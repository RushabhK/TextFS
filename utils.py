import superblock as sb
import inode as ind
import chunks as ch
from constants import *
from random import randint as ri
from random import shuffle

def update_superblock(super_obj):
	s1 = super_obj.build_chunk()
	s2 = ""
	with open(FILEPATH) as read_obj:
		read_obj.seek(CHUNK_SIZE, 0)
		s2 = read_obj.read()
	write_obj = open(FILEPATH, "w")
	write_obj.write(s1+s2)
	write_obj.close()

def is_file_present(filename):
	super_obj = sb.Superblock()
	for i in range(1, MAX_FILES+1):
		if super_obj.inode_details[i] == 1:
			inode_obj = ind.Inode(i, 1)
			if filename == inode_obj.file_name:
				return True
	return False

def get_inode_number(filename):
	super_obj = sb.Superblock()
	for i in range(1, MAX_FILES+1):
		if super_obj.inode_details[i] == 1:
			inode_obj = ind.Inode(i, 1)
			if filename == inode_obj.file_name:
				return i	

def update_inode(inode_no, content):
	try:
		if len(content) != CHUNK_SIZE:
			raise Exception("Content of chunk is not valid!")
		if inode_no < 1 or inode_no > MAX_FILES:
			raise ValueError("Inode no is not valid!")
		read_obj = open(FILEPATH, 'r')
		s1 = read_obj.read(inode_no*CHUNK_SIZE) #Read contents above the inode chunk
		read_obj.seek(CHUNK_SIZE, 1) #Move file pointer by CHUNK_SIZE
		s3 = read_obj.read() #Read contents below the inode chunk
		read_obj.close()
		write_obj = open(FILEPATH, 'w')
		write_obj.write(s1 + content + s3) #Write new contents to file
		write_obj.close()
	except Exception as e:
		print e

def create_file(filename):
	try:
		if is_file_present(filename):
			raise Exception("Filename " + filename + " already exists!")
		super_obj = sb.Superblock()
		available_inodes = []     #Maintain list of available inodes 
		for i in range(1, MAX_FILES+1):
			if super_obj.inode_details[i] == 0:
				available_inodes.append(i)
		inode_no = available_inodes[ri(0, len(available_inodes)-1)] #Select a random available inode
		super_obj.set_inode_no(inode_no, 1) #Mark that inode as used
		available_chunks = []	#Maintain list of available chunks
		for i in range(1, MAX_CHUNKS+1):
			if super_obj.chunk_details[i] == 0:
				available_chunks.append(i)
		chunk_no = available_chunks[ri(0, len(available_chunks)-1)] #Select a random available chunk
		super_obj.set_chunk_no(chunk_no, 1) #Mark that chunk as used
		update_superblock(super_obj) #Update Superblock
		inode_obj = ind.Inode(inode_no, 0)  #Initialize inode object for the new file to be created
		content = inode_obj.build_chunk(filename, 0, chunk_no) #Get contents of inode chunk
		update_inode(inode_no, content)  #Update the inode table
	except Exception as e:
		print e

def update_chunk(chunk_no, content):
	try:
		if len(content) != CHUNK_SIZE:
			raise Exception("Content of chunk is not valid!")
		if chunk_no < 1 or chunk_no > MAX_CHUNKS:
			raise ValueError("Chunk no is not valid!")
		read_obj = open(FILEPATH, 'r')
		s1 = read_obj.read((MAX_FILES + chunk_no) * CHUNK_SIZE) #Read contents above the chunk
		read_obj.seek(CHUNK_SIZE, 1) #Move file pointer by CHUNK_SIZE
		s3 = read_obj.read() #Read contents below the chunk
		read_obj.close()
		write_obj = open(FILEPATH, 'w')
		write_obj.write(s1 + content + s3) #Write new contents to file
		write_obj.close()
	except Exception as e:
		print e

def write_to_file(filename, data):
	try:
		if is_file_present(filename) == False:
			raise Exception("File " + filename + " does not exist!")
		'''
		1. Get a list of all chunks used by the filename, 
		2. Mark all those chunks as available,
		3. Update the superblock.
		'''
		inode_no = get_inode_number(filename)
		inode_obj = ind.Inode(inode_no, 1)
		chunk_obj = ch.Chunk(inode_obj.chunk_start)
		available_chunks = chunk_obj.get_chunk_nos(inode_obj.file_size) #Get the list of chunk nos utilized by the file

		super_obj = sb.Superblock()
		for i in available_chunks:
			super_obj.set_chunk_no(i, 0) #Reset the chunks which were used
		count = 0 #Count of available chunks
		for i in super_obj.chunk_details:
			if i == 0:
				count += 1

		max_available = count * CHUNK_DATA_SIZE 
		if len(data) > max_available: #Check for available memory
			raise Exception("Not enough memory to write data to file!")

		update_superblock(super_obj) #Update the superblock

		super_obj = sb.Superblock() #Updated superblock objects
		available_chunks = []  #Get available chunks from updated superblock
		for i in range(1, MAX_CHUNKS+1):
			if super_obj.chunk_details[i] == 0:
				available_chunks.append(i)		
		shuffle(available_chunks) #To enable random selection of chunks
		chunk_start = available_chunks[0]
		inode_obj = ind.Inode(inode_no, 0) #New inode object
		inode_content = inode_obj.build_chunk(filename, len(data), chunk_start)
		update_inode(inode_no, inode_content) #Update the inode table

		#Fill the chunks with new data
		size = len(data)
		chunk_index = 0
		data_index = 0
		while size > CHUNK_DATA_SIZE:
			chunk_no = available_chunks[chunk_index]
			chunk_data = data[data_index : ]
			next_chunk = available_chunks[chunk_index + 1]
			chunk_content = ch.Chunk.build_chunk(chunk_data, next_chunk)
			update_chunk(chunk_no, chunk_content)
			size -= CHUNK_DATA_SIZE
			chunk_index += 1
			data_index += CHUNK_DATA_SIZE
		if size != 0:
			chunk_no = available_chunks[chunk_index]
			chunk_data = data[data_index : ]
			chunk_content = ch.Chunk.build_chunk(chunk_data)
			update_chunk(chunk_no, chunk_content)
	except Exception as e:
		print e

def list_all_files():
	l = []
	super_obj = sb.Superblock()
	for i in range(1, MAX_FILES+1):
		if super_obj.inode_details[i] == 1:
			inode_obj = ind.Inode(i, 1)
			l.append(inode_obj.file_name)
	return l

def get_file_contents(filename):
	try:
		if is_file_present(filename) == False:
			raise Exception("File " + filename + " does not exist!")
		inode_no = get_inode_number(filename)
		inode_obj = ind.Inode(inode_no, 1)
		chunk_obj = ch.Chunk(inode_obj.chunk_start)		
		return chunk_obj.get_data(inode_obj.file_size)
	except Exception as e:
		print e

def delete_file(filename):
	try:
		if is_file_present(filename) == False:
			raise Exception("File " + filename + " does not exist!")
		inode_no = get_inode_number(filename)
		inode_obj = ind.Inode(inode_no, 1)
		chunk_obj = ch.Chunk(inode_obj.chunk_start)
		chunk_nos = chunk_obj.get_chunk_nos(inode_obj.file_size)
		super_obj = sb.Superblock()
		super_obj.inode_details[inode_no] = 0 #Free this inode
		for i in chunk_nos: #Free all the chunks
			super_obj.chunk_details[i] = 0
		update_superblock(super_obj) #Update the superblock
	except Exception as e:
		print e