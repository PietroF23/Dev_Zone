import sys
from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QPushButton,
                             QGridLayout,
                             QVBoxLayout,
                             QComboBox,
                             QStackedLayout,
                             QLineEdit
                             )
from PyQt6.QtCore import Qt
from capsula import Capsula
from statistiche import statistiche
from download_db import *

# AGGIORNAMENTO DATABASE ALL'ACCENSIONE
x = True
if x == True:
    update_db()
    x = False

# LETTURA DATABASE GUSTI

db = read_db()
localdb = read_localdb()

#################################

# FINESTA IMPOSTAZIONI
class Impostazioni(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        grid = QGridLayout()

        # RESET DATABASE LOCALE
        reslocal = QPushButton("Reset_Local_DB")
        reslocal.clicked.connect(self.reset)
        grid.addWidget(reslocal, 2, 2)

        # INDIETRO
        back = QPushButton("BACK")
        back.setMaximumWidth(100)
        back.clicked.connect(self.backclick)
        grid.addWidget(back, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom and Qt.AlignmentFlag.AlignLeft)

        # CAMBIO GUSTO
        global layoutGusto
        layout = QVBoxLayout()
        layoutGusto = QStackedLayout()

        # SELEZIONE GUSTO
        self.pageGusto = QComboBox()

            #VALORI DA DATABASE
        for key, val in db.items():
            for v, num in val.items():
                self.pageGusto.addItem(v)

        self.pageGusto.activated.connect(self.switchGusto)
        layout.addWidget(self.pageGusto)
        grid.addLayout(layout, 1, 1)

        # SIMULAZIONE INCREMENTO GELATO LOCALE
        global line
        line = QLineEdit()
        grid.addWidget(line, 2, 1)

        add = QPushButton("AddTest")
        add.clicked.connect(self.aggiungi)
        grid.addWidget(add, 2, 0)

        self.setLayout(grid)
        self.setGeometry(400, 150, 800, 480)
        self.setWindowTitle('Impostazioni')

    def switchGusto(self):
        layoutGusto.setCurrentIndex(self.pageGusto.currentIndex())
        print(self.pageGusto.currentIndex())

    def reset(self):
        update_localdb()

    def aggiungi(self):
        global c
        localdb = read_localdb()
        sel = line.text()
        for key, value in localdb.items():
            if key == sel:
                localdb[key] += 1
        with open("localdb.json", "w") as f:
            json.dump(localdb, f)


    def backclick(self):
        global ex
        ex = Window()
        ex.show()



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        self.grid = QGridLayout()
        # CAPSULA

        caps = Capsula(
            ["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
        caps.setBarPadding(2)
        caps.setBarSolidPercent(0.9)
        caps.setBackgroundColor('gray')
        caps.sizeHint()
        caps.setFixedWidth(100)
        caps.setFixedHeight(300)
        self.grid.addWidget(caps, 0, 0)

        self.grid.addWidget(okButton, 1, 0)

        # BOTTONE IMPOSTAZIONI
        impost = QPushButton("Impostazioni")
        impost.setMaximumWidth(200)
        self.grid.addWidget(impost, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        impost.clicked.connect(self.openimpost)


        # STATISTICHE

        self.upd()

        btn = QPushButton("Aggiorna")
        self.grid.addWidget(btn, 1, 2)
        btn.clicked.connect(self.upd)


        self.setLayout(self.grid)

        self.setGeometry(400, 150, 800, 480)
        self.setWindowTitle('IceMaker v0.1.0')
        self.setStyleSheet('background-color:orange;')
        self.show()

    def upd(self):
        print("Success")
        self.c = statistiche()
        self.grid.addWidget(self.c, 0, 2)
        self.c.setMaximumHeight(400)
        ## QUI LE HO PROVATE TUTTE... MA NIENTE
        self.c.update()
        self.grid.update()
        self.update()

    def openimpost(self):
        """Apertura Impostazioni"""

        global ex
        ex = Impostazioni()
        ex.show()

def main():
    global ex
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
