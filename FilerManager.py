import csv
import sys
import traceback

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QCursor
from PyQt5.QtCore import Qt, QSize, QTimer

from os import startfile, getcwd
from webbrowser import open as openweb
from keyboard import add_hotkey

cwd = getcwd()  # Place of this program
with open('Description.txt', mode='r', encoding='utf-8') as man:
    DESCRIPTION = [i.replace('\n', '') for i in man.readlines()]  # Import description of this program


def restart():  # Restart this program
    try:
        startfile(sys.argv[0])
        sys.exit(-23)
    except Exception:
        traceback.print_exc()
        erw = QErrorMessage()
        erw.showMessage(str(error))
        erw.exec_()


class MainWindow(QWidget):
    """This is a main program window"""

    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.settings_window = SettingsWindow()  # add a settings window
        self.descr_window = DescrWindow()  # add a description window
        self.add_window = AddWindow()  # add an add window
        self.initUI()

    def initUI(self):
        try:
            self.setMaximumSize(700, 700)
            self.setMinimumSize(700, 700)
            self.setWindowTitle('Filer Manager')
            self.setWindowIcon(QIcon('icon.png'))
            self.setStyleSheet('''QWidget {
                background-color: rgb(10, 10, 20); 
            }''')

            self.menuf = QGroupBox('Tools', self)  # Group of tools buttons
            self.menuf.setStyleSheet('''QGroupBox {
                margin-top: 2ex;
            }
            QGroupBox:enabled {
                border: 1px solid rgb(180, 1, 1);
                border-radius: 8px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                left: 3ex;
                color: rgb(180, 1, 1);
            }''')

            self.menufg = QVBoxLayout()  # Box of tools buttons

            self.settings = QPushButton('Settings', self)  # Opens a settings window
            self.settings.setStyleSheet('''QPushButton {
                background-color: rgb(60, 60, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 10px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 100); 
                border-color: rgb(80, 80, 100); 
                border-style: inset;
            }''')
            self.settings.clicked.connect(lambda: self.settings_window.shower())
            self.settings.setCursor(QCursor(Qt.PointingHandCursor))
            self.menufg.addWidget(self.settings, alignment=Qt.Alignment())

            self.add = QPushButton('Addfile', self)  # Opens an add window
            self.add.setStyleSheet('''QPushButton {
                background-color: rgb(60, 60, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 10px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 100); 
                border-color: rgb(80, 80, 100); 
                border-style: inset;
            }''')
            self.add.clicked.connect(self.add_window.shower)
            self.add.setCursor(QCursor(Qt.PointingHandCursor))
            self.menufg.addWidget(self.add, alignment=Qt.Alignment())

            self.descr = QPushButton('Program', self)  # Opens a description window
            self.descr.setStyleSheet('''QPushButton {
                background-color: rgb(60, 60, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 10px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 100); 
                border-color: rgb(80, 80, 100); 
                border-style: inset;
            }''')
            self.descr.clicked.connect(lambda: self.descr_window.shower())
            self.descr.setCursor(QCursor(Qt.PointingHandCursor))
            self.menufg.addWidget(self.descr, alignment=Qt.Alignment())

            self.exitting = QPushButton('Exit', self)  # Closes a program
            self.exitting.setStyleSheet('''QPushButton {
                background-color: rgb(60, 60, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 10px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(160, 40, 40); 
                border-color: rgb(240, 60, 60); 
                border-style: inset;
            }''')
            self.exitting.clicked.connect(lambda: sys.exit())
            self.exitting.setCursor(QCursor(Qt.PointingHandCursor))
            self.menufg.addWidget(self.exitting, alignment=Qt.Alignment())

            self.menuf.setLayout(self.menufg)
            self.menuf.move(20, 20)

            self.packsf = QGroupBox('Packs', self)  # Group of pack buttons
            self.packsf.setStyleSheet('''QGroupBox {
                margin-top: 2ex;
            }
            QGroupBox:enabled {
                border: 1px solid rgb(180, 1, 1);
                border-radius: 8px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                left: 3ex;
                color: rgb(180, 1, 1);
            }''')

            self.pack1 = QPushButton('Pack 1', self)  # Button opens all programs in "Pack 1" directory
            self.pack1.setStyleSheet('''QPushButton {
                background-color: rgb(70, 70, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 8px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 100); 
                border-color: rgb(100, 100, 100); 
                border-style: inset;
            }''')
            self.pack1.clicked.connect(self.open1)
            self.pack1.setCursor(QCursor(Qt.PointingHandCursor))

            self.pack2 = QPushButton('Pack 2', self)  # Button opens all programs in "Pack 2" directory
            self.pack2.setStyleSheet('''QPushButton {
                background-color: rgb(70, 70, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 8px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 100); 
                border-color: rgb(100, 100, 100); 
                border-style: inset;
            }''')
            self.pack2.clicked.connect(self.open2)
            self.pack2.setCursor(QCursor(Qt.PointingHandCursor))

            self.pack3 = QPushButton('Pack 3', self)  # Button opens all programs in "Pack 3" directory
            self.pack3.setStyleSheet('''QPushButton {
                background-color: rgb(70, 70, 120); 
                border-style: outset; 
                border-width: 2px; 
                border-radius: 8px; 
                border-color: black; 
                color: white; 
                font: bold 24px; 
                padding: 4px;
                width: 6em;
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 100); 
                border-color: rgb(100, 100, 100); 
                border-style: inset;
            }''')
            self.pack3.clicked.connect(self.open3)
            self.pack3.setCursor(QCursor(Qt.PointingHandCursor))

            self.packsfg = QVBoxLayout()  # Box of pack buttons
            self.packsfg.addWidget(self.pack1, alignment=Qt.Alignment())
            self.packsfg.addWidget(self.pack2, alignment=Qt.Alignment())
            self.packsfg.addWidget(self.pack3, alignment=Qt.Alignment())

            self.packsf.setLayout(self.packsfg)
            self.packsf.move(20, 250)

            self.fr = QScrollArea(self)  # Group of programs in "Main" directory
            self.fr.setStyleSheet('''QScrollArea {
                border: 2px solid rgb(180, 1, 1);
                border-radius: 4px;
            }''')
            self.fr.verticalScrollBar().setStyleSheet('''QScrollBar {
                background-color: rgb(60, 60, 60); 
            }''')
            self.fr.setGeometry(0, 0, 430, 660)
            self.fr.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.fr.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

            self.frw = QWidget(flags=Qt.WindowFlags())  # Box of buttons
            self.frg = QVBoxLayout()
            self.data = {}
            with open('Main.csv', mode='r', encoding="utf8") as csvfile:
                readerpath = csv.DictReader(csvfile, delimiter='|', quotechar='"')
                for pathname in sorted(readerpath, key=lambda p: str(p['Name']).lower()):  # List of programs
                    if pathname['Type'] == 'Main':
                        btn = QPushButton(pathname['Name'], self)
                        btn.setStyleSheet('''QPushButton {
                            background-color: rgb(90, 90, 150); 
                            border-style: outset; 
                            border-width: 1px; 
                            border-radius: 5px; 
                            border-color: rgb(80, 80, 100); 
                            color: white; 
                            font: bold 20px; 
                            padding: 5px;
                            width: 16em;
                        }
                        QPushButton:hover {
                            background-color: rgb(80, 80, 140); 
                            border-style: inset;
                        }''')
                        btn.setCursor(QCursor(Qt.PointingHandCursor))
                        btn.clicked.connect(self.opener)
                        self.data[pathname['Name']] = pathname['Path']
                        self.frg.addWidget(btn, alignment=Qt.Alignment())

            if len(self.data) == 0:  # If "Main" is empty
                none_label = QLabel('EMPTY')
                none_label.setStyleSheet('''QLabel {
                    color: white;
                    font: bold 32px;
                }''')
                self.frg.addWidget(none_label, alignment=Qt.AlignCenter)
                self.add.setStyleSheet('''QPushButton {
                    background-color: rgb(80, 60, 60); 
                    border-style: outset; 
                    border-width: 2px; 
                    border-radius: 10px; 
                    border-color: red; 
                    color: red; 
                    font: bold 24px; 
                    padding: 4px;
                    width: 6em;
                }
                QPushButton:hover {
                    border-color: rgb(200, 20, 20); 
                    color: rgb(200, 20, 20); 
                    border-style: inset;
                }''')
            self.frw.setLayout(self.frg)
            self.fr.setWidget(self.frw)
            self.fr.move(250, 20)

            self.adf = QGroupBox('Advertising', self)  # Group of advertising
            self.adf.setCursor(QCursor(Qt.OpenHandCursor))
            self.adf.setStyleSheet('''QGroupBox {
                background-color: rgb(30, 30, 45); 
                margin-top: 2ex;
            }
            QGroupBox:enabled {
                border: 1px solid rgb(180, 1, 1);
                border-radius: 8px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                left: 3ex;
                color: rgb(180, 1, 1);
            }''')
            self.adfg = QVBoxLayout()
            self.adyp = QIcon('Yandex_logo_2021_Russian.png')
            self.ady = QPushButton(self)
            self.ady.setIcon(self.adyp)
            self.ady.setIconSize(QSize(175, 60))
            self.ady.setStyleSheet('''QPushButton,
            QPushButton:default,
            QPushButton:hover,
            QPushButton:selected,
            QPushButton:disabled,
            QPushButton:pressed {
                background-color: transparent;
                border-color: transparent;
                color: transparent;
            }''')
            self.ady.clicked.connect(self.adshow)
            self.adfg.addWidget(self.ady, alignment=Qt.Alignment())
            self.adf.setLayout(self.adfg)
            self.adf.move(20, 430)

            self.logo = QPushButton(f'{chr(169)} Varenik Vladimir', self)  # Copyright
            self.logo.move(20, 620)
            self.logo.resize(200, 60)
            self.logo.setFont(QFont('Arial', 15))
            self.logo.setStyleSheet('''QPushButton,
            QPushButton:default,
            QPushButton:hover,
            QPushButton:selected,
            QPushButton:disabled,
            QPushButton:pressed {
                background-color: transparent;
                border-color: transparent;
                color: rgb(30, 30, 30);
            }''')
            self.logo.clicked.connect(self.authorwindow)

        except Exception as error:  # Print a error
            traceback.print_exc()
            erw = QErrorMessage()
            erw.showMessage(str(error))
            erw.exec_()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def opener(self):  # Opens a link
        openweb(self.data[self.sender().text()])

    def open1(self):  # for "Pack 1" button
        with open('Main.csv', mode='r', encoding="utf8") as csvfile:
            readerp = csv.DictReader(csvfile, delimiter='|', quotechar='"')
            for path in readerp:
                if path['Type'] == 'Pack 1':
                    openweb(path['Path'])

    def open2(self):  # for "Pack 2" button
        with open('Main.csv', mode='r', encoding="utf8") as csvfile:
            readerp = csv.DictReader(csvfile, delimiter='|', quotechar='"')
            for path in readerp:
                if path['Type'] == 'Pack 2':
                    openweb(path['Path'])

    def open3(self):  # for "Pack 3" button
        with open('Main.csv', mode='r', encoding="utf8") as csvfile:
            readerp = csv.DictReader(csvfile, delimiter='|', quotechar='"')
            for path in readerp:
                if path['Type'] == 'Pack 3':
                    openweb(path['Path'])

    def adshow(self):  # Go to Yandex site (not always)
        openweb('https://rroll.to/chyj2Q')
        self.hide()
        self.settings_window.hide()
        self.add_window.hide()
        self.descr_window.hide()
        QTimer().singleShot(30000, lambda: self.show())

    def authorwindow(self):
        self.aw = QDialog(flags=Qt.WindowStaysOnTopHint)
        self.aw.setWindowTitle('Contacts')
        self.secr = QLabel('Contacts\nTelegram/WhatsApp:\n+79047613727', self.aw)
        self.secr.setAlignment(Qt.AlignCenter)
        self.secr.resize(120, 60)
        self.aw.show()


class SettingsWindow(QWidget):
    """This is a settings window"""

    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.move(200, 200)
        self.setMaximumSize(200, 130)
        self.setMinimumSize(200, 130)
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon('icon.png'))

        self.clear = QPushButton('Clear data', self)
        self.clear.move(10, 10)
        self.clear.resize(180, 50)
        self.clear.setStyleSheet('''QPushButton {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 10px; 
            border-color: black; 
            color: rgb(215, 215, 215); 
            font: 24px; 
            padding: 4px;
            width: 6em;
        }
        QPushButton:hover {
            border-color: rgb(200, 20, 20); 
            color: rgb(200, 20, 20); 
            border-style: inset;
        }''')
        self.clear.clicked.connect(cleardata)

        self.over = QPushButton('Files overview', self)
        self.over.move(10, 70)
        self.over.resize(180, 50)
        self.over.setStyleSheet('''QPushButton {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 10px; 
            border-color: black; 
            color: rgb(215, 215, 215); 
            font: 24px; 
            padding: 4px;
            width: 6em;
        }
        QPushButton:hover {
            border-color: rgb(40, 40, 40); 
            color: rgb(165, 165, 165); 
            border-style: inset;
        }''')
        self.over.clicked.connect(lambda: startfile(cwd))

    def shower(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()


class AddWindow(QWidget):
    """This window add a new links or programs"""

    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add...')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(200, 400, 300, 240)
        self.setStyleSheet('''QWidget {
            background-color: rgb(80, 80, 80); 
        }''')

        self.getpath = QLineEdit('path', self)  # Get a full path
        self.getpath.move(10, 10)
        self.getpath.resize(280, 35)
        self.getpath.setStyleSheet('''QLineEdit {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 8px; 
            border-color: black; 
            color: rgb(240, 240, 240); 
            font: 18px; 
            padding: 4px;
            width: 6em;
        }
        QLineEdit:hover {
            color: rgb(215, 215, 215); 
            border-style: inset;
        }''')

        self.getname = QLineEdit('name', self)  # Get a name
        self.getname.move(10, 70)
        self.getname.resize(280, 35)
        self.getname.setStyleSheet('''QLineEdit {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 8px; 
            border-color: black; 
            color: rgb(240, 240, 240); 
            font: 18px; 
            padding: 4px;
            width: 6em;
        }
        QLineEdit:hover {
            color: rgb(215, 215, 215); 
            border-style: inset;
        }''')

        self.getpl = QComboBox(self)  # Get a pack
        self.getpl.addItems(['Main', 'Pack 1', 'Pack 2', 'Pack 3'])
        self.getpl.move(10, 130)
        self.getpl.resize(280, 35)
        self.getpl.setStyleSheet('''QComboBox {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 8px; 
            border-color: black; 
            color: rgb(215, 215, 215); 
            font: 18px; 
            padding: 4px;
            width: 6em;
        }
        QComboBox:hover {
            border-color: rgb(40, 40, 40); 
            color: rgb(165, 165, 165); 
            border-style: inset;
        }
        QComboBox::drop-down {
            background-color: rgb(80, 80, 80); 
            border-radius: 8px; 
        }''')

        self.go = QPushButton('Save', self)  # Save
        self.go.move(10, 190)
        self.go.resize(135, 40)
        self.go.clicked.connect(self.enter)
        self.go.setStyleSheet('''QPushButton {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 10px; 
            border-color: black; 
            color: rgb(215, 215, 215); 
            font: 24px; 
            padding: 4px;
            width: 6em;
        }
        QPushButton:hover {
            border-color: rgb(40, 40, 40); 
            color: rgb(165, 165, 165); 
            border-style: inset;
        }''')

        self.overb = QPushButton('Overview', self)  # Choose in explorer
        self.overb.move(155, 190)
        self.overb.resize(135, 40)
        self.overb.clicked.connect(self.filedial)
        self.overb.setStyleSheet('''QPushButton {
            background-color: rgb(65, 65, 65); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 10px; 
            border-color: black; 
            color: rgb(215, 215, 215); 
            font: 24px; 
            padding: 4px;
            width: 6em;
        }
        QPushButton:hover {
            border-color: rgb(40, 40, 40); 
            color: rgb(165, 165, 165); 
            border-style: inset;
        }''')

    def enter(self):  # Save
        with open('Main.csv', mode='a', newline='', encoding="utf8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Type', 'Path', 'Name'], delimiter='|',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            new = {'Type': self.getpl.currentText(),
                   'Path': self.getpath.text(),
                   'Name': self.getname.text()}
            writer.writerow(new)
        restart()

    def filedial(self):  # Get path in explorer
        path = QFileDialog().getOpenFileUrl()[0].path()[1:]
        if path:
            self.getpath.setText(path)

    def shower(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()


class DescrWindow(QWidget):
    """This window is a description"""

    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.setGeometry(1350, 200, 400, 400)
        self.setWindowTitle('Description')
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyleSheet('''QWidget {
            background-color: rgb(80, 80, 80); 
        }''')

        self.lay = QVBoxLayout()
        self.descr = QPlainTextEdit(self)  # Text
        self.descr.appendPlainText('\n'.join(DESCRIPTION))
        self.descr.setReadOnly(True)
        self.descr.setStyleSheet('''QPlainTextEdit {
            background-color: rgb(25, 25, 25); 
            border-style: outset; 
            border-width: 2px; 
            border-radius: 6px; 
            border-color: black; 
            color: white; 
            font: 12px; 
            padding: 4px;
            width: 6em;
        }''')
        self.lay.addWidget(self.descr, alignment=Qt.Alignment())
        self.setLayout(self.lay)

    def shower(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()


def cleardata():
    """Clear a data"""
    with open('Main.csv', mode='w', newline='', encoding="utf8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Type', 'Path', 'Name'], delimiter='|',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
    restart()


def hotkey():
    """This is a hotkey work (secret function of this program)"""
    if form.isHidden():
        form.show()
    else:
        form.hide()


if __name__ == '__main__':  # Launch of program
    try:
        add_hotkey('ctrl + shift + f', hotkey)  # Secret hotkey
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # For big displays
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
        app = QApplication(sys.argv)  # Application
        app.setWindowIcon(QIcon('icon.png'))
        form = MainWindow()  # Main window
        form.show()
        sys.exit(app.exec())  # Exit
    except Exception as error:  # Send a error
        traceback.print_exc()
        erw = QErrorMessage()
        erw.showMessage(str(error))
        erw.exec_()
