from PyQt5 import QtWidgets,QtGui,QtCore
from audioui import Ui_Form
import sys
from pydub import AudioSegment
from pydub.playback import play
import PyQt5


## 這兩行用來處理下面錯誤
# qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
# This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
import os
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(message)s')

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=r'G:\我的雲端硬碟\audio\audioenv\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

temp_path=r'./Temp'
if not os.path.isdir(temp_path):
    os.mkdir(temp_path)

AudioSegment.converter=r'.\ffmpeg.exe'
AudioSegment.temp_dir=r'./Temp'




class MainWindow(QtWidgets.QＷidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.value.setText('0')
        self.filePath=None
        
        ## 禁止點擊
        self.ui.playbutton1.setEnabled(False)
        self.ui.playbutton2.setEnabled(False)
        self.ui.savebackbutton.setEnabled(False)
        self.ui.savefilebutton.setEnabled(False)
        self.ui.addbutton.setEnabled(False)
        self.ui.subtractbutton.setEnabled(False)

        try:
            self.ui.audiofilebutton.clicked.connect(self.openFile)
        except Exception as e:
            print("讀檔後的錯誤是:",e)

        self.ui.playbutton1.clicked.connect(self.original_play1)
        self.ui.addbutton.clicked.connect(self.add_function)
        self.ui.subtractbutton.clicked.connect(self.subtract_function)
        self.ui.playbutton2.clicked.connect(self.audio_play2)

        self.ui.savebackbutton.clicked.connect(self.saveback)
        self.ui.savefilebutton.clicked.connect(self.savefile)


    def openFile(self):
        text=self.ui.audiopath.toPlainText()
        # print(text)
        if not text:
            open = QtWidgets.QFileDialog.Options()
            filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "選擇要開啟的檔案", "", "檔案(*.mp3)",
                                                           options=open)
            # print(filePath)
            if filePath:
                self.filePath=filePath
                self.ui.audiopath.setText(self.filePath)

        else:
            if ".mp3" in text and os.path.isfile(text):
                self.filePath=text
            # print(self.filePath)
        self.audio=AudioSegment.from_file(self.filePath)

        ## 按鈕開放
        self.ui.playbutton1.setEnabled(True)
        self.ui.playbutton2.setEnabled(True)
        self.ui.savebackbutton.setEnabled(True)
        self.ui.savefilebutton.setEnabled(True)
        self.ui.addbutton.setEnabled(True)
        self.ui.subtractbutton.setEnabled(True)
        return self.audio

    # 取得播放秒數並播放
    def original_play1(self):
        self.ui.playbutton2.setEnabled(False)
        self.music = self.openFile()
        value=self.ui.play1value.text()
        if value=="":
            value=5
        else:
            value=int(value)
        play(self.music[:(value*1000)])
        self.ui.playbutton2.setEnabled(True)

    def audio_play2(self):
        self.ui.playbutton1.setEnabled(False)
        self.music=self.openFile()
        value=self.ui.value.text()
        db1=self.music.dBFS
        db=-(self.music.dBFS)
        db=db1+db
        if value=='0':
            value=0
        else:
            value=int(value)
        value2=self.ui.play2value.text()
        if value2=="":
            value2=5
        else:
            value2=int(value2)
        self.music=self.volume_process(self.music,db+value)
        # print("當前音量:\t",db,"\n調整後音量:\t",self.music.dBFS)
        play(self.music[:(value2*1000)])
        self.ui.playbutton1.setEnabled(True)
        return self.music
    #　修改音量大小
    def volume_process(self,file,volume):
        return file.apply_gain(volume)

    def add_function(self):
        value=int(self.ui.value.text())
        value=str(value+1)
        self.ui.value.setText(value)

    def subtract_function(self):
        value = int(self.ui.value.text())
        value = str(value -1)
        self.ui.value.setText(value)

    def saveback(self):
        self.music.export(self.filePath,format='mp3')

    def savefile(self):
        FileName,FileType=QtWidgets.QFileDialog.getSaveFileName(self,"檔案保存",r"C:\\","*.mp3")
        # print("Name:\t",FileName,"\nType:\t",FileType)
        self.ui.play2value.setText("0")
        self.audio_music=self.audio_play2()
        try:
            
            self.audio_music.export(FileName,format='mp3')
        except FileNotFoundError:
            pass

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    run=MainWindow()
    run.show()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print("錯誤是 : ",e)