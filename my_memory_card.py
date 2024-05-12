from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox
from random import shuffle, randint

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Гос. язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французский'))
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет в флаге России?', 'Зелёный', 'Белый', 'Красный', 'Синий'))

app = QApplication([])

R_question = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

lans1 = QHBoxLayout()
lans2 = QVBoxLayout()
lans3 = QVBoxLayout()
lans2.addWidget(rbtn1)
lans2.addWidget(rbtn2)
lans3.addWidget(rbtn3)
lans3.addWidget(rbtn4)

lans1.addLayout(lans2)
lans1.addLayout(lans3)

RadioGroupBox.setLayout(lans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_result = QLabel("Прав ты или нет")
lb_correct = QLabel("Ответ тут")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(R_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addWidget(btn_OK, stretch=2)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=5)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_correct.setText(q.right_answer)
    R_question.setText(q.quest)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Правильных ответов:', window.score)
        print('Всего вопросов:', window.total)
        print('Рейтинг:', (window.score/window.total)*100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно!")
            print('Правильных ответов:', window.score)
            print('Всего вопросов:', window.total)
            print('Рейтинг:', (window.score/window.total)*100)

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    
def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Не забывай про скобки')

btn_OK.clicked.connect(click_ok)

window.score = 0 
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec_()