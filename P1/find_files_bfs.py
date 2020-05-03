import os

def find_files(suffix, path):
	path_list = list()

	queue = []

	queue.append(path)

	result = list()

	while queue:
		current_path = queue.pop(0)

		if not os.path.isdir(current_path):
			if current_path.endswith(suffix):
				result.append(current_path)
		else:
			directory_list = os.listdir(current_path)

			for each_path in directory_list:
				queue.append(os.path.join(current_path, each_path))

	return result


print(find_files('.c', 'testdir'))