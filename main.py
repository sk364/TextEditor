#!/usr/bin/python

import sys
from PyQt4 import QtGui


class Editor(QtGui.QMainWindow):
    
    	def __init__(self):
        	super(Editor, self).__init__()
        
        	self.initUI()
        
    	def initUI(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.open_file)

		saveFile = QtGui.QAction(QtGui.QIcon('save.png'),'Save',self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip('Save new File')
		saveFile.triggered.connect(self.save_file)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)       
		fileMenu.addAction(saveFile)    
	    
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Editor')
		self.show()
		
    	def open_file(self):
	
        	fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        
       		f = open(fname, 'r')
        
        	with f:        
            		data = f.read()
 	           	self.textEdit.setText(data) 
 	
	def save_file(self):
		fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '/home')

		text = self.textEdit.toPlainText()
		if text:
			f = open(fname,'w')	
			f.write(text)
			f.close()
	
        
def main():
    
   	app = QtGui.QApplication(sys.argv)
    	editor = Editor()
    	sys.exit(app.exec_())


if __name__ == '__main__':	main()
