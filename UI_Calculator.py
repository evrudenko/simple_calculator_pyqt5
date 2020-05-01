from PyQt5 import QtCore, QtGui, QtWidgets

# Графическая оболочка калькулятора
class UI_MainWindow(object):
	def __init__(self, MainWindow):
		# MainWindow.resize(320, 460)
		MainWindow.setWindowTitle('Calculator')

		# Определение шрифтов для повторного использования
		self.mainFont = QtGui.QFont('SansSerif', 20)
		self.mainFont.setBold(True)

		self.secondaryFont = QtGui.QFont('SansSerif', 14)
		self.secondaryFont.setBold(True)

		# Инициализация менюбара
		self.menubar = MainWindow.menuBar()
		self.fileMenu = self.menubar.addMenu('File')

		self.exitAction = QtWidgets.QAction('Exit')
		self.exitAction.setShortcut('Esc')
		self.exitAction.triggered.connect(QtWidgets.qApp.quit)
		self.fileMenu.addAction(self.exitAction)

		# Инициализация основных компонентов приложения
		self.gridLayout = QtWidgets.QGridLayout()
		self.centralWidget = QtWidgets.QWidget()
		self.centralWidget.setStyleSheet('background-color: white;')
		self.centralWidget.setLayout(self.gridLayout)

		self.secondaryDisplayPanel = QtWidgets.QLabel('')
		self.secondaryDisplayPanel.setMinimumSize(QtCore.QSize(280, 25))
		self.secondaryDisplayPanel.setFont(self.secondaryFont)
		self.secondaryDisplayPanel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
		self.gridLayout.addWidget(self.secondaryDisplayPanel, 0, 0, 1, 4)

		self.mainDisplayPanel = QtWidgets.QLabel('')
		self.mainDisplayPanel.setMinimumSize(QtCore.QSize(280, 100))
		self.mainDisplayPanel.setFont(self.mainFont)
		self.mainDisplayPanel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
		self.mainDisplayPanel.setFrameShape(QtWidgets.QFrame.Panel)
		self.gridLayout.addWidget(self.mainDisplayPanel, 1, 0, 1, 4)

		self.pushButton_butBackspace = QtWidgets.QPushButton()
		self.pushButton_butBackspace.setMinimumSize(QtCore.QSize(50, 50))
		self.pushButton_butBackspace.setStyleSheet('background-color: white;')
		self.pushButton_butBackspace.setIcon(QtGui.QIcon('backspace.png'))
		self.pushButton_butBackspace.setIconSize(QtCore.QSize(30, 30))
		self.gridLayout.addWidget(self.pushButton_butBackspace, 2, 3)
		
		self.pushButton_num7 = QtWidgets.QPushButton('7')
		self.pushButton_num7.setFont(self.mainFont)
		self.pushButton_num7.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num7.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num7, 3, 0)

		self.pushButton_num8 = QtWidgets.QPushButton('8')
		self.pushButton_num8.setFont(self.mainFont)
		self.pushButton_num8.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num8.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num8, 3, 1)

		self.pushButton_num9 = QtWidgets.QPushButton('9')
		self.pushButton_num9.setFont(self.mainFont)
		self.pushButton_num9.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num9.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num9, 3, 2)

		self.pushButton_num4 = QtWidgets.QPushButton('4')
		self.pushButton_num4.setFont(self.mainFont)
		self.pushButton_num4.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num4.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num4, 4, 0)

		self.pushButton_num5 = QtWidgets.QPushButton('5')
		self.pushButton_num5.setFont(self.mainFont)
		self.pushButton_num5.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num5.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num5, 4, 1)

		self.pushButton_num6 = QtWidgets.QPushButton('6')
		self.pushButton_num6.setFont(self.mainFont)
		self.pushButton_num6.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num6.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num6, 4, 2)

		self.pushButton_num1 = QtWidgets.QPushButton('1')
		self.pushButton_num1.setFont(self.mainFont)
		self.pushButton_num1.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num1.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num1, 5, 0)

		self.pushButton_num2 = QtWidgets.QPushButton('2')
		self.pushButton_num2.setFont(self.mainFont)
		self.pushButton_num2.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num2.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num2, 5, 1)

		self.pushButton_num3 = QtWidgets.QPushButton('3')
		self.pushButton_num3.setFont(self.mainFont)
		self.pushButton_num3.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num3.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num3, 5, 2)

		self.pushButton_butClr = QtWidgets.QPushButton('C')
		self.pushButton_butClr.setFont(self.mainFont)
		self.pushButton_butClr.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_butClr.setStyleSheet('background-color: white; color: red;')
		self.gridLayout.addWidget(self.pushButton_butClr, 6, 0)

		self.pushButton_num0 = QtWidgets.QPushButton('0')
		self.pushButton_num0.setFont(self.mainFont)
		self.pushButton_num0.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_num0.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_num0, 6, 1)

		self.pushButton_butEq = QtWidgets.QPushButton('=')
		self.pushButton_butEq.setFont(self.mainFont)
		self.pushButton_butEq.setMinimumSize(QtCore.QSize(70, 70))
		self.pushButton_butEq.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_butEq, 6, 2)

		self.pushButton_butSub = QtWidgets.QPushButton('-')
		self.pushButton_butSub.setFont(self.mainFont)
		self.pushButton_butSub.setMinimumSize(QtCore.QSize(70, 140))
		self.pushButton_butSub.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_butSub, 3, 3, 2, 1)

		self.pushButton_butAdd = QtWidgets.QPushButton('+')
		self.pushButton_butAdd.setFont(self.mainFont)
		self.pushButton_butAdd.setMinimumSize(QtCore.QSize(70, 140))
		self.pushButton_butAdd.setStyleSheet('background-color: white;')
		self.gridLayout.addWidget(self.pushButton_butAdd, 5, 3, 2, 1)

		MainWindow.setCentralWidget(self.centralWidget)