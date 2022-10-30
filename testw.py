from instr import *

class MainWin(QWidget):
    def init(self):
        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.resize(win_width, win_height)
            self.move(win_x, win_y)
            def initUI(self):
                self.hello_text = QLabel('txt_hello')
                self.instruction = QLabel('txt_instruction')
                self.button = QPushButton('txt_next')
                self.layout = QVBoxLayout()
                self.hello_text.addWidget(self.layout)
                self.instruction.addWidget(self.layout)
                self.button.addWidget(self.layout)


txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'

txt_instruction = 'Данное приложение позволит вам с помощью текста Руфье провести первичную диагностику вашего здоровья. Просьба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке. У испытуемого, находящегося в положении лежа на спине в течение 5 минут, определяют частоту пульса за 15 секунд; затем в течение 45 секунд испытуемый выполняет 30 приседаний. После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд, а потом - за последние 15 секунд первой минуты периода восстановления. Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головукружение, шум в ушах, сильная отдышка и др.), то тест необходимо прервать и обратиться к врачу.'

txt_next = 'Начать'

txt_title = 'Здоровье'
win_x, win_y = 100, 50
win_width, win_height = 1000, 600