from PyQt5.QtWidgets import QApplication, QWidget

class Gui(QWidget):
    
    def __init__(self, n, world):
        super().__init__()
        
        self.n = n
        self.interface()
        self.grid = True
        
    def interface(self):
        
        self.resize(1024, 768)
        self.setWindowTitle("Cops and Robbers")
        self.show()
        
    #def createGrid():
        #grid = [[for x in range()]]
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    okno = Gui()
    sys.exit(app.exec_())