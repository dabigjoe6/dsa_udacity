import os

# print(os.listdir("./testdir"))

# print(os.path.isfile('./testdir'))

# print(os.path.isdir('./testdir'))

# print(os.listdir("./testdir")[5].endswith(".c"))

# print(os.path.join('testdir', 'subdir1'))

def find_files(suffix, path):
	# directory_list = os.listdir(path)
	path_list = list()

	def find_files_func(path, suffix):

		if not os.path.isdir(path):
			if path.endswith(suffix):
				path_list.append(path)
			return
		
		directory_list = os.listdir(path)

		for sub_path in directory_list:
			find_files_func(os.path.join(path, sub_path), suffix)

		# print(path)

	find_files_func(path, suffix)
		

	return path_list


print(find_files('.c', 'testdir'))