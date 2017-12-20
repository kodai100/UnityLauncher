import os

def find_all_path(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def is_unity_exe(path):
    root, ext = os.path.splitext(path)
    return os.path.splitext(os.path.basename(path))[0] == 'Unity' and ext == '.exe'

def get_unity_exe_path(root_path):
    list = []

    for path in find_all_path(root_path):
        if is_unity_exe(path):
            list.append(path)

    return list

if __name__ == '__main__':
    unity_list = get_unity_exe_path('C:\\Program Files')
    for l in unity_list:
        print(l)