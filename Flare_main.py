"""   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""


from PyQt5 import QtGui
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import sys


class Window(QtGui.QPushButton):
    def __init__(self):
        QtGui.QPushButton.__init__(self, 'Choose File')
        self.mediaObject = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        self.mediaObject.stateChanged.connect(self.handleStateChanged)
        self.clicked.connect(self.handleButton)

    def handleButton(self):
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.stop()
        else:
            path = QtGui.QFileDialog.getOpenFileName(self, self.text())
            if path:
                self.mediaObject.setCurrentSource(Phonon.MediaSource(path))
                self.mediaObject.play()

    def handleStateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.setText('Stop')
        elif newstate == Phonon.StoppedState:
            self.setText('Choose File')
        elif newstate == Phonon.ErrorState:
            source = self.mediaObject.currentSource().fileName()
            print 'ERROR: could not play:', source.toLocal8Bit().data()

if __name__ == '__main__':


    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Flare'
    win = Window()
    win.resize(200, 100)
    win.show()
    content= M.QMediaContent(url)
    player = M.QMediaPlayer()
    player.setMedia(content)
    player.play()                       
    player.stateChanged.connect(app.quit)
    sys.exit(app.exec_())
