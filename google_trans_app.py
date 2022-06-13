import sys

#궁금) 왜 from PyQt5 import *를 하지 않고 이렇게 야금야금 import하냐? (PyQt5 전체 용량이 어마어마하게 커서 그래.)
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans

form_class = uic.loadUiType('ui/googleUi.ui')[0] #왜 인덱스[0]을 붙여요? 그냥 구문이 그렇다. 같은 이름의 ui들이 있을 수 있어서 인덱스로 구분해야 한대..

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__() # 엄 앱의 초기화자(부모의 초기화자) 호출
        self.setupUi(self) # 미리 제작해 놓은 googleUi.ui 연결띠
        self.setWindowTitle('보기만 해도 지려버리는 한줄 번역기') #아버지 창문 제목 (앱 윈도우 타이틀) 설정
        self.setWindowIcon(QIcon('icons/google.png')) # 윈도우 아이콘 불러오기
        self.statusBar().showMessage('Google Translator App(아버지) Version 1.0') #이놈이 setStatusbar도 아니고 StatusBar도 아니고... 소문자로 시작하는 statusBar였다! 킹받네~~

        #시그널 만들 때, 디자이너로 만들었던 UI 요소 이름들은 틀리면 않돼!!! ~디버깅 너무 어려워~
        self.btn_trans.clicked.connect(self.trans_operation)
        self.btn_reset.clicked.connect(self.reset_operation)

    def trans_operation(self):
        trans = googletrans.Translator() #일단 Translator() 객체 하나 만들어 주고...
        trans_str = self.input_ko.text() #오 그냥 이렇게 self.인풋창이름.text()만 해도 되는구나! (근데 아래 append() 안에서는 text() 하면 안 되고 text다. 킹받네)

        trans_result_en = trans.translate(trans_str, dest='en')
        trans_result_ja = trans.translate(trans_str, dest='ja')
        trans_result_zh_cn = trans.translate(trans_str, dest='zh-cn')

        self.output_en.append(trans_result_en.text) #어 디자이너 계속 보면서 버튼 이름들 틀리지 말고~~~ 중요하니까 2번 말하는 거임, ㅋ~~~
        self.output_ja.append(trans_result_ja.text)
        self.output_zh_cn.append(trans_result_zh_cn.text)

    def reset_operation(self):
        self.input_ko.clear()
        self.output_en.clear()
        self.output_ja.clear()
        self.output_zh_cn.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())


