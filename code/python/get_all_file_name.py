from os import listdir, walk
from os.path import isfile, isdir, join


def get_all_file_name(path):

    file_list = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    sub_dir = [join(path, d) for d in listdir(path) if isdir(join(path, d))]

    for i in range(len(sub_dir)):
        next_dir = sub_dir[i]
        file_list.extend(get_all_file_name(next_dir))

    return file_list


def get_all_file_name_generator(path):

    for folder, subdirs, files in walk(path):
        for f in files:
            yield join(folder, f)
