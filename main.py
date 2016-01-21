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
		
		self.textEdit.textChanged.connect(self.text_changes)

		menubar = self.menuBar()
		self.fileMenu = menubar.addMenu('&File')
		self.editMenu = menubar.addMenu('&Edit')

		self.initFileMenuActions()
                self.initEditMenuActions()

		self.setGeometry(100, 100, 800, 600)
		self.setWindowTitle('New file')

		self.show()

	def initFileMenuActions(self):
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

		self.fileMenu.addAction(newFile)
                self.fileMenu.addAction(openFile)
                self.fileMenu.addAction(saveFile)
                self.fileMenu.addAction(saveAsFile)
                self.fileMenu.addAction(exitFile)

	
	def initEditMenuActions(self):
		cutText = QtGui.QAction(QtGui.QIcon('cut.png'), 'Cut', self)
                cutText.setShortcut('Ctrl+X')
                cutText.setStatusTip('Cut Selected Text')
                cutText.triggered.connect(self.cut_text)

                copyText = QtGui.QAction(QtGui.QIcon('copy.png'), 'Copy', self)
                copyText.setShortcut('Ctrl+C')
                copyText.setStatusTip('Copy Selected Text')
                copyText.triggered.connect(self.copy_text)

                pasteText = QtGui.QAction(QtGui.QIcon('paste.png'),'Paste',self)
		pasteText.setShortcut('Ctrl+V')
                pasteText.setStatusTip('Paste Text')
                pasteText.triggered.connect(self.paste_text)

                selectAllText = QtGui.QAction(QtGui.QIcon('sel_all.png'),'Select All',self)
                selectAllText.setShortcut('Ctrl+A')
                selectAllText.setStatusTip('Select All Text')
                selectAllText.triggered.connect(self.sel_all_text)
		

		self.editMenu.addAction(cutText)
                self.editMenu.addAction(copyText)
                self.editMenu.addAction(pasteText)
                self.editMenu.addAction(selectAllText)

	def get_real_file_name(self, fname):
		s = ''
		for i in range(len(fname)-1,0,-1):
			if fname[i]!='/':
				s+=fname[i]
			else:	break
		return s		

		
	def text_changes(self):
		if self.cur_file:
			self.setWindowTitle(self.get_real_file_name(self.cur_file)+'*')
		else:	self.setWindowTitle('New file*')
		self.is_saved = False


	def new_file(self):
		# TODO ask for saving existing file
		self.textEdit.clear()


    	def open_file(self):
        	fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')        

       		f = open(fname, 'r')
        
        	if f:        
			self.cur_file = fname
            		data = f.read()
 	           	self.textEdit.setText(data)
			self.is_saved = True
			self.cur_file = fname
			self.setWindowTitle(self.get_real_file_name(fname))
 	
	def saveAs_file(self):
		fname = QtGui.QFileDialog.getSaveFileName(self, 'Save As file', '/home', selectedFilter='*.txt')

		text = self.textEdit.toPlainText()

		if text:
			f = open(fname,'w')
			f.write(text)
			self.is_saved = True
			self.cur_file = fname
			self.setWindowTitle(self.get_real_file_name(fname))
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
			self.setWindowTitle(self.cur_file)
			fname.close()


	def exit_file(self):
		text = self.textEdit.toPlainText()

		if self.is_saved or not text:	sys.exit()

		elif self.cur_file:
			# TODO show message for quiting or saving
			self.save_file()
		else:
			self.saveAs_file()
	
	def cut_text(self):
		print 1

	def copy_text(self):
		print 1
	
	def paste_text(self):
		print 1

	def sel_all_text(self):	
		print 1


def main():
   	app = QtGui.QApplication(sys.argv)
    	editor = Editor()
    	sys.exit(app.exec_())


if __name__ == '__main__':	main()
