import os
import re
import xml.etree.ElementTree as et

def find_all_path(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def find_specific_file_path(root_path, filename):

    for path in find_all_path(root_path):
        if filename in path:
            return path

def file_name(path):
    return os.path.splitext(os.path.basename(path))[0]

def file_ext(path):
    return os.path.splitext(path)[1]

def is_unity_exe(path):
    return file_name(path) == 'Unity' and file_ext(path) == '.exe'

def get_editor_folder_path(unity_exe_path):
    r = re.compile("(.*)(Editor)(.*)")
    d = r.search(unity_exe_path)
    return d.group(1) + 'Editor'

def get_unity_editor_version(unity_exe_path):
    xml_path = find_specific_file_path(get_editor_folder_path(unity_exe_path), 'ivy.xml')

    xml = et.parse(xml_path)
    root = xml.getroot()

    version = root[0].attrib['{http://ant.apache.org/ivy/extra}unityVersion']   # リンク邪魔...

    return version

def get_unity_version_and_path(root_path_list):
    list = []

    if root_path_list is None or len(root_path_list) == 0:
        return None

    for root_path in root_path_list:
        for path in find_all_path(root_path):
            if is_unity_exe(path):
                dict = {'version':None, 'path':None}
                dict['version'] = get_unity_editor_version(path)
                dict['path'] = path
                list.append(dict)

    return list


if __name__ == '__main__':

    for unity_dict in get_unity_version_and_path(['C:\\Program Files']):
        print(unity_dict)