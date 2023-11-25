import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.title = ['ID', 'Сорт', 'степень обжарки', 'молотый/в зернах', 'вкус', 'цена', 'объем']
        self.tableWidget.setColumnCount(len(self.title))
        self.tableWidget.setHorizontalHeaderLabels(self.title)
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect(r"C:\Users\PERSCOMP\PycharmProjects\Ecspresso\coffee")
        self.cur = con.cursor()

        sp = self.cur.execute(f"SELECT * FROM information").fetchall()
        for i, row in enumerate(sp):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())