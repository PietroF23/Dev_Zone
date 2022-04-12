from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QFont

from download_db import read_db, read_localdb
import json

# POSIZIONE STATISTICHE
s_pos_x = 30
s_pos_y = 100

# DIMENSIONE COLONNA STATISTICHE
s_dim_c_x = 200
s_dim_c_y = 30

# FONT STATISTICHE
font_main = QFont("Times", 12)
font_value = QFont("Times", 12)

# VARIABILI
nacc = 0
gusti = []
valori = []


class statistiche(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        lay = QVBoxLayout(self)

        # APERTURA DATABASE GUSTI UTILIZZATI
        db = read_db()
        localdb = read_localdb()

        try:
            for key, val in db.items():
                for v, num in val.items():
                    gusti.append(v)

        except KeyError:
            print("Errore chiave!")

        try:
            for key, val in localdb.items():
                valori.append(val)

        except KeyError:
            print("Errore chiave valori!")
        n_gusti = len(gusti)



        # STATISTICHE GELATI DALL'ACCENSIONE
        """n_gelati = QLabel(f"Numero Gelati (Dall'accensione) : {nacc}")
        n_gelati.resize(s_dim_c_x, s_dim_c_y)
        n_gelati.setFont(font_main)
        lay.addWidget(n_gelati)"""


        # GENERAZIONE STATISTICHE SUI GUSTI UTILIZZATI
        for i in range(n_gusti):
            self.column_name = str(gusti[i][0]) + '_label_name'
            g_val = str("Numero gelati ") + str(gusti[i])
            self.column_name = QLabel(g_val, self)
            self.column_name.resize(s_dim_c_x, s_dim_c_y)
            self.column_name.move(s_pos_x, s_pos_y + (i - 1) * 24)
            self.column_name.setFont(font_main)

            # VALORI
            self.column_name = str(valori[i]) + '_label_name'
            g_val = str(valori[i])
            self.column_name = QLabel(g_val, self)
            self.column_name.resize(s_dim_c_x, s_dim_c_y)
            self.column_name.move((s_pos_x * 10), s_pos_y + (i - 1) * 24)
            self.column_name.setFont(font_value)

        ##########