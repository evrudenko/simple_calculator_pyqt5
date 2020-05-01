import sys
from PyQt5 import QtWidgets
from UI_Calculator import UI_MainWindow

class SimpleCalculator(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = UI_MainWindow(self)

		# Множество с допустимыми знаками для различных проверок введенных данных
		self.signs = {'-', '+'}

		# Определение слотов для клавиш приложения
		self.ui.pushButton_num0.clicked.connect(lambda: self.addCharacter('0'))
		self.ui.pushButton_num1.clicked.connect(lambda: self.addCharacter('1'))
		self.ui.pushButton_num2.clicked.connect(lambda: self.addCharacter('2'))
		self.ui.pushButton_num3.clicked.connect(lambda: self.addCharacter('3'))
		self.ui.pushButton_num4.clicked.connect(lambda: self.addCharacter('4'))
		self.ui.pushButton_num5.clicked.connect(lambda: self.addCharacter('5'))
		self.ui.pushButton_num6.clicked.connect(lambda: self.addCharacter('6'))
		self.ui.pushButton_num7.clicked.connect(lambda: self.addCharacter('7'))
		self.ui.pushButton_num8.clicked.connect(lambda: self.addCharacter('8'))
		self.ui.pushButton_num9.clicked.connect(lambda: self.addCharacter('9'))
		self.ui.pushButton_butSub.clicked.connect(lambda: self.addCharacter('-'))
		self.ui.pushButton_butAdd.clicked.connect(lambda: self.addCharacter('+'))
		self.ui.pushButton_butBackspace.clicked.connect(self.deleteCharacter)
		self.ui.pushButton_butClr.clicked.connect(self.clearDisplay)
		self.ui.pushButton_butEq.clicked.connect(self.calculate)

	# Функция добавления символа нажатой клавиши
	def addCharacter(self, char):
		current_main_text = self.__removeZeros(self.ui.mainDisplayPanel.text())
		current_secondary_text = self.__removeZeros(self.ui.secondaryDisplayPanel.text())

		main_text = current_main_text
		secondary_text = current_secondary_text

		if char in self.signs:
			# Искусственное ограничение суммы символов главного и вторичного полей
			if len(current_main_text) + len(current_secondary_text) < 31:
				if len(current_main_text):
					secondary_text = current_secondary_text + current_main_text + char
					main_text = ''
				elif len(current_secondary_text):
					secondary_text = current_secondary_text[:-1] + char
		# Искусственное ограничение длины главного поля
		elif len(current_main_text) < 13:
			main_text = current_main_text + char
			secondary_text = current_secondary_text

		self.ui.mainDisplayPanel.setText(main_text)
		self.ui.secondaryDisplayPanel.setText(secondary_text)
		if secondary_text:
			self.__calculateSecondaryExpression()

	# Функция удаления последнего символа выражения
	def deleteCharacter(self):
		main_text = self.ui.mainDisplayPanel.text()
		secondary_text = self.ui.secondaryDisplayPanel.text()
		if len(main_text):
			self.ui.mainDisplayPanel.setText(main_text[:-1])
		elif len(secondary_text):
			self.ui.mainDisplayPanel.setText(secondary_text[:-1])
			self.ui.secondaryDisplayPanel.setText('')

	# Функция очистки дисплея
	def clearDisplay(self):
		self.ui.mainDisplayPanel.setText('')
		self.ui.secondaryDisplayPanel.setText('')

	# Функция, выполняющая вычисления
	def calculate(self):
		main_text = self.__removeZeros(self.ui.mainDisplayPanel.text())
		secondary_text = self.ui.secondaryDisplayPanel.text()
		if main_text and secondary_text:
			if main_text[-1] in self.signs:
				return
			elif (not main_text) and secondary_text[-1] in self.signs:
				return
			result = eval(secondary_text + main_text)
			self.ui.secondaryDisplayPanel.setText('')
			self.ui.mainDisplayPanel.setText(str(result))
		elif (not main_text) and secondary_text:
			self.ui.secondaryDisplayPanel.setText('')
			self.ui.mainDisplayPanel.setText(secondary_text[:-1])

	# Функция удаления незначащих нулей из начала числа
	def __removeZeros(self, text):
		if text:
			while text[0] == '0' and len(text) > 1:
				text = text[1:]
		return text

	# Функция вычисления выражения дополнительного дисплея
	def __calculateSecondaryExpression(self):
		current_secondary_text = self.ui.secondaryDisplayPanel.text()
		secondary_text = str(eval(current_secondary_text[:-1])) + current_secondary_text[-1]
		self.ui.secondaryDisplayPanel.setText(secondary_text)

def main():
	app = QtWidgets.QApplication([])
	win = SimpleCalculator()

	win.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()