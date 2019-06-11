import subprocess
import os


def burn_subtitle(video, subtitle):
    ffmpeg = "/home/zousiyu1/bin/ffmpeg/ffmpeg"
    exec_list = [ffmpeg, "-i"]

    # parameters
    exec_list.append(video)  # video file
    exec_list.append("-vf")  # subtitle
    vf_args = "ass=" + subtitle
    exec_list.append(vf_args)

    # output
    exec_list.append(video[0:-4] + "-batch" + ".mp4")
    print("\n", exec_list, "\n")

    # run
    subprocess.call(exec_list)


# main

videos = []
subtitles = []

# get files
for _file in os.listdir("."):
    if _file.endswith("batch.mp4"):
        continue
    elif _file.endswith(".mp4"):
        videos.append(_file)
    elif _file.endswith(".ass"):
        subtitles.append(_file)

videos = sorted(videos)
subtitles = sorted(subtitles)

print(videos)
print(subtitles)

for num in range(len(videos)):
    burn_subtitle(videos[num], subtitles[num])
