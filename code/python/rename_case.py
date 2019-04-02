import os
import shutil

par_dirs = [name for name in os.listdir('.') if os.path.isdir(name)]


def rename(par_dir):
    print("Rename dir [{}] now!".format(par_dir))
    # get all mp4 file
    video_files = [
        video for video in os.listdir(par_dir) if video.endswith('.mp4')
    ]

    for video_file in video_files:
        newname = video_file.replace('_Downloadly.ir', '')  # delete something
        if not video_file.startswith(par_dir):
            newname = par_dir + ' - ' + video_file  # add par dir name before filename
        else:
            print("Pass add dir name")
        newname = os.path.join(par_dir, newname)
        oldname = os.path.join(par_dir, video_file)
        os.rename(oldname, newname)
        shutil.move(newname, '.')


for par_dir in par_dirs:
    rename(par_dir)