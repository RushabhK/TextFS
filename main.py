from utils import *

cmd = ""
while(True):
	cmd = raw_input("> ")
	if(cmd == ""):
		continue
	else:
		cmd = cmd.split()
		break

while(cmd[0] != "exit"):
	if cmd[0] == "touch":
		try:
			if len(cmd) == 1:
				raise ValueError("Invalid arguments to touch!")
			for i in range(1, len(cmd)):
				create_file(cmd[i])
		except Exception as e:
			print e
	
	elif cmd[0] == "ls":
		try:
			if len(cmd) > 1:
				raise ValueError("Invalid arguments to ls!")
			l = list_all_files()
			for i in l:
				print i
		except Exception as e:
			print e

	elif cmd[0] == "write":
		try:
			if len(cmd) != 2:
				raise ValueError("Invalid arguments to write!")
			filename = cmd[1]
			if is_file_present(filename) == False:
				raise ValueError("File " + filename + " is not created")
			data = ""
			while(True):
				ip = raw_input()
				if ip == "save":
					break
				data = data + ip + "\n"
			write_to_file(filename, data[:-1])
		except Exception as e:
			print e

	elif cmd[0] == "cat":
		try:
			if len(cmd) != 2:
				raise ValueError("Invalid arguments to echo!")
			filename = cmd[1]
			if is_file_present(filename) == False:
				raise ValueError("File " + filename + " is not present!")
			print get_file_contents(filename)
		except Exception as e:
			print e

	elif cmd[0] == "rm":
		try:
			if len(cmd) != 2:
				raise ValueError("Invalid arguments to rm!")
			filename = cmd[1]
			if is_file_present(filename) == False:
				raise ValueError("File " + filename + " is not present!")
			delete_file(filename)
		except Exception as e:
			print e

	else:
		print "Invlaid command!"

	while(True):
		cmd = raw_input("> ")
		if(cmd == ""):
			continue
		else:
			cmd = cmd.split()
			break