from pydub import AudioSegment
from pydub.playback import play
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication



fig,ax=plt.subplots()

AudioSegment.converter=r'D:\ffmpeg\ffmpeg-2024-04-04-git-478d97f303-full_build\ffmpeg-2024-04-04-git-478d97f303-full_build\bin\ffmpeg.exe'
AudioSegment.ffprobe=r'D:\ffmpeg\ffmpeg-2024-04-04-git-478d97f303-full_build\ffmpeg-2024-04-04-git-478d97f303-full_build\bin\ffprobe.exe'
path=r'G:\我的雲端硬碟\audio'
# value=os.listdir(path)
# print(value,os.getcwd())
# for i in value:
#     if '.mp3' in i:
#         mp3path=r'{}\{}'.format(path,i)
#         song=AudioSegment.from_mp3(mp3path)
#         out=song[:]+10
#         out.export('test.mp3')


# 丟入 AudioSegment.from_file 讀取到的檔案
def match_target_amplitude(file,volume):
    return file.apply_gain(volume)
import time
import datetime
song=AudioSegment.from_file(r'{}\TESTAUDIO.mp3'.format(path))
date1=datetime.datetime.now()
play(song[:5000])
date2=datetime.datetime.now()
print(date2-date1)
# sound=AudioSegment.from_file(r"{}\TESTAUDIO.mp3".format(path))
# db=sound.dBFS
# normalized_sound=match_target_amplitude(sound,db+20)
# normalized_sound.export('test.mp3',format='mp3')

