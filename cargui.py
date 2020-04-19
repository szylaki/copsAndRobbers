from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout)

class Gui(QWidget):
    
    def __init__(self, n, world):
        super().__init__()
        
        self.n = n
        self.window()
        self.createGrid()
        
        
    def window(self):
        self.resize(1024, 768)
        self.setWindowTitle("Cops and Robbers")
        self.show()
        
    def createGrid():
        grid = QGridLayout()
        
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    okno = Gui()
    sys.exit(app.exec_())