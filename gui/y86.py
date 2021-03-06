# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import time, os, sys

import PyQt4, PyQt4.QtGui
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_y86 import Ui_Y86Simulator
from Ui_heijc import Ui_MainWindow

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))+os.sep+'compiler')
import assemble, start
import highlighter 

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))+os.sep+'kernel')
from Simulator import *
from Memory import CACHESIZE, MEMSIZE, VMSIZE

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class Thread(QtCore.QThread):
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self,sim, interval=0.1):
        self.sim=sim
        self.interval=interval
        self.start()

    def run(self):
        while self.sim.isTerminated == False:
            self.emit(QtCore.SIGNAL("next()"))
            time.sleep(self.interval)
        self.emit(QtCore.SIGNAL("terminate()"))
        
    
    def setslide(self,thread1,  sim, interval = 0.1):
        thread1.interval=interval

    
class Dialog(QDialog, Ui_Y86Simulator):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.simulator=Simulator()
        self.displaytext = ''
        self.thread1 = Thread()
        self.thread2 = Thread()
        self.opentxt=None
        self.savetxt=None
        self.loadyet = False
        self.terminateFlag = False
        self.connect(self.thread1, SIGNAL("next()"), self.step)
        self.connect(self.thread1, SIGNAL("terminate()"), self.terminate)
        self.connect(self.loadButton,SIGNAL("clicked()"),self.openFile)
        self.connect(self.saveButton,SIGNAL("clicked()"),self.saveFile)
        self.connect(self.runButton,SIGNAL("clicked()"),self.run)
        self.connect(self.pauseButton,SIGNAL("clicked()"),self.pause)
        #self.connect(self.begin,SIGNAL("clicked()"),self.loadFile)
        self.connect(self.stepButton,SIGNAL("clicked()"),self.step)
        self.connect(self.backButton,SIGNAL("clicked()"),self.back)
        self.connect(self.resetButton,SIGNAL("clicked()"),self.reset)
        self.frequency.setText('2.0s')
        highlighter.MyHighlighter1( self.Code, 'Classic' )
        highlighter.MemoryHighlighter( self.Memory, 'Classic' )
        highlighter.CacheHighlighter(self.Cache, 'Classic')
        
    
    def terminate(self):
        self.loadyet = False 
        self.runButton.setEnabled(True)
        self.stepButton.setEnabled(False)
        self.backButton.setEnabled(True)
        if self.terminateFlag == False:
            self.terminateFlag = True
            self.terminateShow()
            
    
    def terminateShow(self):
        reply = QtGui.QMessageBox.information(self, 'Congratulation','The program has finished,\n\
        Thank you for using our software. Special bless for you!', QMessageBox.Yes,QMessageBox.No )
        if reply == QtGui.QMessageBox.Yes:
            self.heijcwindow = QtGui.QMainWindow(self)
            self.heijcwindow.ui = Ui_MainWindow()
            self.heijcwindow.ui.setupUi(self.heijcwindow)
            self.heijcwindow.show()    
        else:
            pass
        return
        
    
    def showerror(self, string):
        reply = QtGui.QMessageBox.warning(self, 'Error',string, QMessageBox.Ok)
        if reply == QtGui.QMessageBox.Ok:
            self.openFile()
        return
        
   
    def assemblefailure(self, assemblefilename):
        reply = QtGui.QMessageBox.question(self, 'Compile failure','Do you want to modify the code in our compiler?', QMessageBox.Yes,QMessageBox.No )
        if reply == QtGui.QMessageBox.Yes:
            self.runassembleGUI(assemblefilename)
        else:
            pass
        return
    
    def runassembleGUI(self, assemblefilename):
        self.assemblewindow = QtGui.QMainWindow(self)
        self.assemblewindow.ui = start.Start(self) 
        self.assemblewindow.ui.create(assemblefilename, self)
        self.assemblewindow.ui.compile()
        self.assemblewindow.ui.show()
        
     
    def displayCode(self):
        text = self.displaytext.split('\n')
        text[:] = [line for line in text]
        
        displaytext = ''
        for line in text:
            displaytext+=line
            displaytext+='\n'
        displaytext+='hei'
        self.Code.setText(displaytext)
        self.Code.scrollToAnchor('hei') 
        return
    
    def displayMemory(self):
        current_mem = self.simulator.getMemoryChange()
        displaytext = ''
        for address in current_mem:
            add = '0x%4x'%(address)
            displaytext+='  '+add.replace(' ', '0')+': '
            displaytext+=' 0x%x'%(current_mem[address])
            displaytext+='\n' 
        self.Memory.setText(displaytext)
        return
        
    def displayCache(self):
        displaytext = '%s    isValid   isDirty      Tag         Block\n'%(' '*13)
        for SetIndex in range(0, 64):
            displaytext+='Set %2d:' %(SetIndex)
            for LineIndex in range(0, 1):
                if LineIndex != 0:
                    displaytext+='        '
                isValid, isDirty, tag, block = self.simulator.getCache(SetIndex, LineIndex)
                displaytext += 'Line%2d.%5d%10d   %10d       ['%(LineIndex, isValid, isDirty, tag)
                for byte in block:
                    displaytext+='%5d'%byte
                displaytext+='   ]\n'
        self.Cache.setText(displaytext)
        
        return
    
    def openFile(self):
        self.opentxt=QFileDialog.getOpenFileName(self,"Open file","/")  
        if self.opentxt != None and self.opentxt != '':
            try:
                self.loadAdd.setText(str(self.opentxt))
            except UnicodeEncodeError:
                self.showerror("invalid input file format")
            path = os.path.splitext(str(self.opentxt))
            try:
                prefix = path[0]
                suffix = path[1]
                if suffix not in ('.yo', '.ys', '.ybo'):
                    self.showerror("invalid input file format")
            except:
                self.showerror("invalid input file format")
            
            try:
                file=open(str(self.opentxt))
                if suffix == '.ys':
                    outputfilename = prefix+'.yo'
                    outputfile = open(outputfilename, 'w')
                    assemble.assemble(file,outputfile )
                    outputfile.close()
                    file = open(outputfilename, 'r')
                    if assemble.error != '':
                        raise Exception('Assemble Failure')
                    self.opentxt = outputfilename
                    
                self.displaytext=file.read()
                self.Code.setText(self.displaytext)
                file.close()
                
            except IOError:
                self.showerror("Cannot open file")
            except:
                self.assemblefailure(self.opentxt)
        return

    def saveFile(self):
        self.savetxt=QFileDialog.getSaveFileName(self,"Save file","/")  
        self.saveAdd.setText(str(self.savetxt))

    def loadFile(self):       
        try:
            infile=open(str(self.opentxt))
        except:
            self.showerror('You must choose a input file')
            return
        try:
            if self.savetxt != None:
                outfile = open(str(self.savetxt), 'w')
            else:
                outfile = None
        except:
            pass
        try:
            self.simulator.load(infile, outfile)
        except:
            self.showerror('Bad input file')
            
        self.loadyet = True
        return
        
        
    def run(self):
        if self.loadyet == False:
            self.loadFile()
        if self.loadyet == False:
            return
        pos = self.Slider.value()/100.0
        self.thread1.render(self.simulator, pos)
        self.runButton.setEnabled(False)
        self.stepButton.setEnabled(False)
        self.backButton.setEnabled(False)
    
    def pause(self):
        self.runButton.setEnabled(True)
        self.stepButton.setEnabled(True)
        self.backButton.setEnabled(True)
        self.thread1.terminate()


    def step(self):
        if self.loadyet == False:
            self.loadFile()
            
        if self.simulator.isTerminated == False:
            try:
                self.simulator.step()
            except:
                self.showerror()
            self.showtxt()
        else:
            self.terminate()
        

    def showtxt(self):
        if self.simulator.M_Cnd:
            self.M_bch.setText('1')
        else:
            self.M_bch.setText('0')
            
        my=[self.ZF, self.SF, self.OF, 
                self.F_stat, self.F_predPC, 
                self.D_stat,self.D_icode,self.D_ifun, self.D_rA, self.D_rB, self.D_valC, self.D_valP, 
                self.E_stat,self.E_icode, self.E_ifun,self.E_valC, self.E_valA, self.E_valB, self.E_srcA, self.E_srcB, self.E_dstE, self.E_dstM, 
                self.M_stat,self.M_icode, self.M_valE, self.M_valA, self.M_dstE, self.M_dstM, 
                self.W_stat, self.W_icode, self.W_valE, self.W_valM, self.W_dstE, self.W_dstM, 
                self.eax, self.ecx, self.edx, self.ebx, self.esp, self.ebp, self.esi, self.edi, self.cycle]
            
        his=[self.simulator.condcode['ZF'], self.simulator.condcode['SF'], self.simulator.condcode['OF'], 
                self.simulator.F_stat, self.simulator.F_predPC, 
                self.simulator.D_stat,self.simulator.D_icode,self.simulator.D_ifun, self.simulator.D_rA, self.simulator.D_rB, self.simulator.D_valC, self.simulator.D_valP, 
                self.simulator.E_stat,self.simulator.E_icode, self.simulator.E_ifun,self.simulator.E_valC, self.simulator.E_valA, self.simulator.E_valB, self.simulator.E_srcA, self.simulator.E_srcB, self.simulator.E_dstE, self.simulator.E_dstM, 
                self.simulator.M_stat,self.simulator.M_icode,self.simulator.M_valE, self.simulator.M_valA, self.simulator.M_dstE, self.simulator.M_dstM, 
                self.simulator.W_stat, self.simulator.W_icode, self.simulator.W_valE, self.simulator.W_valM, self.simulator.W_dstE, self.simulator.W_dstM, 
                self.simulator.register[0x0],  self.simulator.register[0x1],  self.simulator.register[0x2],  self.simulator.register[0x3], 
                self.simulator.register[0x4],  self.simulator.register[0x5],  self.simulator.register[0x6],  self.simulator.register[0x7], 
                self.simulator.cycle-1]
        
        for (myname, hisname) in zip(my, his):
            myname.setText(str(hisname))
            
        self.displayCode()
        self.displayMemory()
        self.displayCache()

    def on_Slider_sliderMoved(self):
        pos = self.Slider.value()/100.0
        self.frequency.setText(str(pos) + 'S')
        self.thread2.setslide(self.thread1, self.simulator, pos)
    
    def back(self):
        if self.simulator.cycle == 1:
            return
        self.simulator.back()
        self.stepButton.setEnabled(True)
        self.showtxt()
        
    def reset(self):
        self.thread1.terminate()
        self.simulator=Simulator()
        self.loadFile()
        for item in [self.ZF, self.SF, self.OF, 
                self.F_stat, self.F_predPC, 
                self.D_stat,self.D_icode,self.D_ifun, self.D_rA, self.D_rB, self.D_valC, self.D_valP, 
                self.E_stat,self.E_icode, self.E_ifun,self.E_valC, self.E_valA, self.E_valB, self.E_srcA, self.E_srcB, self.E_dstE, self.E_dstM, 
                self.M_stat,self.M_icode,self.M_bch,  self.M_valE, self.M_valA, self.M_dstE, self.M_dstM, 
                self.W_stat, self.W_icode, self.W_valE, self.W_valM, self.W_dstE, self.W_dstM, 
                self.eax, self.ecx, self.edx, self.ebx, self.esp, self.ebp, self.esi, self.edi, self.cycle]:
            item.clear()
        self.runButton.setEnabled(True)
        self.stepButton.setEnabled(True)
        self.backButton.setEnabled(True)

if __name__ == "__main__":    
    
    app = PyQt4.QtGui.QApplication(sys.argv)     
    dlg = Dialog()     
    dlg.show()     
    sys.exit(app.exec_())
