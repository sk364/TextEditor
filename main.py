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
		#self.statusBar()

		self.cur_file = ''
		self.is_saved = False

		newFile = QtGui.QAction(QtGui.QIcon('new.png'), 'New', self)
		newFile.setShortcut('Ctrl+N')
		newFile.setStatusTip('New file')
		newFile.triggered.connect(self.new_file)

		openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.open_file)

		saveAsFile = QtGui.QAction(QtGui.QIcon('saveAs.png'),'Save As',self)
		saveAsFile.setStatusTip('Save As new or existing file')
		saveAsFile.triggered.connect(self.saveAs_file)

		saveFile = QtGui.QAction(QtGui.QIcon('save.png'),'Save',self)
                saveFile.setShortcut('Ctrl+S')
                saveFile.setStatusTip('Save new File')
                saveFile.triggered.connect(self.save_file)

		exitFile = QtGui.QAction(QtGui.QIcon('exit.png'),'Exit',self)
                exitFile.setShortcut('Ctrl+W')
                exitFile.setStatusTip('Exit File')
                exitFile.triggered.connect(self.exit_file)

		self.textEdit.textChanged.connect(self.text_changes)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newFile)
		fileMenu.addAction(openFile)       
		fileMenu.addAction(saveFile)
		fileMenu.addAction(saveAsFile)
		fileMenu.addAction(exitFile)

		self.setGeometry(100, 100, 800, 600)
		self.setWindowTitle('Editor')
		self.show()

		
	def text_changes(self):
		self.setWindowTitle('Editor*')
		is_saved = False

	def new_file(self):
		self.textEdit.clear()


    	def open_file(self):
        	fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')        

       		f = open(fname, 'r')
        
        	if f:        
			self.cur_file = fname
            		data = f.read()
 	           	self.textEdit.setText(data) 
 	
	def saveAs_file(self):
		fname = QtGui.QFileDialog.getSaveFileName(self, 'Save As file', '/home', selectedFilter='*.txt')

		text = self.textEdit.toPlainText()

		if text:
			f = open(fname,'w')
			f.write(text)
			self.is_saved = True
			self.cur_file = fname
			self.setWindowTitle('Editor')
			f.close()
	
	def save_file(self):
		text = self.textEdit.toPlainText()

		if self.cur_file:	fname = open(self.cur_file, 'w')
		elif text:
			self.saveAs_file()
			return
		else:	return
		
		if fname:
			fname.write(text)
			self.is_saved = True
			self.setWindowTitle('Editor')
			fname.close()


	def exit_file(self):
		text = self.textEdit.toPlainText()

		if self.is_saved or not text:	sys.exit()

		elif self.cur_file:
			# TODO show message for quitting or saving
			self.save_file()
		else:
			self.saveAs_file()
		
			
        
def main():
    
   	app = QtGui.QApplication(sys.argv)
    	editor = Editor()
    	sys.exit(app.exec_())


if __name__ == '__main__':	main()
