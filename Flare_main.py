"""   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""


import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import sys

app=C.QCoreApplication(sys.argv)

url= C.QUrl.fromLocalFile("./some.mp3")
content= M.QMediaContent(url)
player = M.QMediaPlayer()
player.setMedia(content)
player.play()

player.stateChanged.connect(app.quit)
app.exec()
