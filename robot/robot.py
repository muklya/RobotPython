import random
import requests
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
	QComboBox, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

a = random.randint(1,3)
b = random.randint(1,3)
c = random.randint(1,3)
d = random.randint(1,3)
class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.rob = [2,2]
		self.cols=5
		self.rows=5
		self.rep=0
		self.rop=0
		self.lbl = [[QLabel(self) for j in range(self.cols)] for i in range(self.rows)]
		pixmapWall = QPixmap("wall.png").scaled(100,100)
		pixmapRobot= QPixmap("robot.jpg").scaled(100,100)
		pixmapGold = QPixmap("gold.png").scaled(100,100)
		for i in range(5):
			for j in range(5):
				if i == 0 or j==0 or j==4 or i==4:
					self.lbl[i][j].setPixmap(pixmapWall)
					self.lbl[i][j].move(100*i,100*j)
		self.lbl[3][3].setPixmap(pixmapRobot)
		self.lbl[3][3].move(self.rob[0]*100, self.rob[1]*100)
		self.lbl[2][2].setPixmap(pixmapGold)
		self.lbl[2][2].move(a*100,b*100)
		self.lbl[1][1].setPixmap(pixmapGold)
		self.lbl[1][1].move(c*100,d*100)
		self.setGeometry(300, 300, (self.rows)*100, self.cols*100)
		self.setWindowTitle('Robocop')
		self.show()
	def keyPressEvent(self, e):
		if self.rob[0]!=3 and e.key() == 16777236:
			self.rob[0]+=1
			self.lbl[3][3].move(self.rob[0]*100, self.rob[1]*100)
			self.moveSound = "move.wav"
			QSound.play(self.moveSound)
			if self.rep==0:
				if self.rob[0]==a and self.rob[1]==b:
					self.lbl[2][2].setPixmap(QPixmap("empty.png"))
					self.lbl[2][2].move(a*100,b*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rep+=1
			if self.rop==0:
				if 	self.rob[0]==c and self.rob[1]==d:
					self.lbl[1][1].setPixmap(QPixmap("empty.png"))
					self.lbl[1][1].move(c*100,d*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rop+=1
		if self.rob[0]!=1 and e.key() == 16777234:
			self.rob[0]-=1
			self.lbl[3][3].move(self.rob[0]*100, self.rob[1]*100)
			self.moveSound = "move.wav"
			QSound.play(self.moveSound)
			if self.rep==0:
				if self.rob[0]==a and self.rob[1]==b:
					self.lbl[2][2].setPixmap(QPixmap("empty.png"))
					self.lbl[2][2].move(a*100,b*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rep+=1
			if self.rop==0:
				if 	self.rob[0]==c and self.rob[1]==d:
					self.lbl[1][1].setPixmap(QPixmap("empty.png"))
					self.lbl[1][1].move(c*100,d*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rop+=1
		if self.rob[1]!=1 and e.key() == 16777235:
			self.rob[1]-=1
			self.lbl[3][3].move(self.rob[0]*100, self.rob[1]*100)	
			self.moveSound = "move.wav"
			QSound.play(self.moveSound)
			if self.rep==0:
				if self.rob[0]==a and self.rob[1]==b:
					self.lbl[2][2].setPixmap(QPixmap("empty.png"))
					self.lbl[2][2].move(a*100,b*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rep+=1
			if self.rop==0:
				if 	self.rob[0]==c and self.rob[1]==d:
					self.lbl[1][1].setPixmap(QPixmap("empty.png"))
					self.lbl[1][1].move(c*100,d*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rop+=1
		if self.rob[1]!=3 and e.key() == 16777237:
			self.rob[1]+=1
			self.lbl[3][3].move(self.rob[0]*100, self.rob[1]*100)
			self.moveSound = "move.wav"
			QSound.play(self.moveSound)
			if self.rep==0:
				if self.rob[0]==a and self.rob[1]==b:
					self.lbl[2][2].setPixmap(QPixmap("empty.png"))
					self.lbl[2][2].move(a*100,b*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rep+=1
			if self.rop==0:
				if 	self.rob[0]==c and self.rob[1]==d:
					self.lbl[1][1].setPixmap(QPixmap("empty.png"))
					self.lbl[1][1].move(c*100,d*100)
					self.moveSound = "gold.wav"
					QSound.play(self.moveSound)
					self.rop+=1
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
