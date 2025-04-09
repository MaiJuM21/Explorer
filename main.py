from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QListWidgetItem, QMenu, QInputDialog
from PyQt5.QtGui import QIcon
import os
from PyQt5.QtWidgets import QListView, QFileSystemModel
import shutil

class Ui_MainWindow(object):
    model = QtWidgets.QFileSystemModel()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 708)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #e7e9f6;;")
        self.centralwidget.setObjectName("centralwidget")

        self.ftop = QtWidgets.QFrame(self.centralwidget)
        self.ftop.setGeometry(QtCore.QRect(0, 0, 971, 41))
        self.ftop.setAutoFillBackground(False)
        self.ftop.setStyleSheet("background-color: white;\n"
                                "border-bottom-right-radius: 20px;\n"
                                "border-bottom-left-radius: 20px;")
        self.ftop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ftop.setObjectName("ftop")

        self.fftop = QtWidgets.QFrame(self.ftop)
        self.fftop.setGeometry(QtCore.QRect(860, -5, 111, 41))
        self.fftop.setAutoFillBackground(False)
        self.fftop.setStyleSheet("background-color: white;\n"
                                 "border-radius: 20px;")
        self.fftop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fftop.setObjectName("fftop")

        self.gridLayout = QtWidgets.QGridLayout(self.fftop)
        self.gridLayout.setObjectName("gridLayout")

        self.exit = QtWidgets.QPushButton(self.fftop)
        self.exit.setEnabled(True)
        self.exit.setMinimumSize(QtCore.QSize(25, 25))
        self.exit.setAutoFillBackground(False)
        self.exit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                "border-radius: 20px;")
        self.exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(lambda: QtWidgets.QApplication.instance().quit())
        self.gridLayout.addWidget(self.exit, 0, 2, 1, 1)
        self.show = QtWidgets.QPushButton(self.fftop)
        self.show.setMinimumSize(QtCore.QSize(25, 25))
        self.show.setAutoFillBackground(False)
        self.show.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.show.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show.setIcon(icon)
        self.show.setObjectName("show")
        self.show.clicked.connect(lambda: self.minimizeToTaskbar(MainWindow))
        self.gridLayout.addWidget(self.show, 0, 0, 1, 1)
        self.full = QtWidgets.QPushButton(self.fftop)
        self.full.setMinimumSize(QtCore.QSize(25, 25))
        self.full.setAutoFillBackground(False)
        self.full.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.full.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.full.setIcon(icon1)
        self.full.setIconSize(QtCore.QSize(15, 15))
        self.full.setObjectName("full")
        self.full.clicked.connect(lambda: self.openFullScreen(MainWindow))
        self.gridLayout.addWidget(self.full, 0, 1, 1, 1)
        self.flabel = QtWidgets.QLineEdit(self.centralwidget)
        self.flabel.setGeometry(QtCore.QRect(60, 50, 911, 41))
        self.flabel.setStyleSheet("background-color: white;\n"
                                  "border-radius: 20px;\n"
                                  "padding-left: 10px;")
        self.flabel.setObjectName("flabel")
        self.flabel.returnPressed.connect(self.handleFilePath)
        self.cw = QtWidgets.QWidget(self.centralwidget)
        self.cw.setGeometry(QtCore.QRect(0, 100, 971, 481))
        self.cw.setStyleSheet("background: rgba(255,255,255,0)")
        self.cw.setObjectName("cw")

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowMaximizeButtonHint)

        self.size_grip = QtWidgets.QSizeGrip(MainWindow)
        self.size_grip.setStyleSheet("background: transparent;")
        self.size_grip.setGeometry(QtCore.QRect(MainWindow.width() - 20, MainWindow.height() - 20,20,20))
        self.size_grip.setCursor(QtCore.Qt.SizeFDiagCursor)
        self.size_grip.setVisible(True)

        self.centerfile = QListView(self.cw)
        self.centerfile.setGeometry(QtCore.QRect(60, 0, 911, 481))
        self.centerfile.doubleClicked.connect(self.openFile)
        self.centerfile.setMinimumSize(QtCore.QSize(0, 0))
        self.centerfile.setStyleSheet("background: white; border-radius: 20px; padding-left: 10px; padding-top: 10px")
        self.centerfile.setObjectName("file")

        self.model.setRootPath("/")
        self.model.setResolveSymlinks(True)
        self.centerfile.setModel(self.model)
        self.centerfile.setRootIndex(self.model.index("/"))
        self.centerfile.show()

        

        self.contextMenu = QMenu(self.centralwidget)

        self.model.setRootPath("/")
        self.model.setResolveSymlinks(True)
        self.centerfile.setModel(self.model)
        self.centerfile.setRootIndex(self.model.index("/"))
        self.centerfile.show()

        self.centerfile.setContextMenuPolicy(Qt.CustomContextMenu)
        self.centerfile.customContextMenuRequested.connect(self.showContextMenu)


        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(10, 50, 41, 41))
        self.minus.setAutoFillBackground(False)
        self.minus.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                 "border-radius: 20px;")
        self.minus.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minus.setIcon(icon3)
        self.minus.setIconSize(QtCore.QSize(30, 30))
        self.minus.setObjectName("minus")
        self.minus.clicked.connect(self.navigateBack)

        
        self.listWidget_icon_only = QtWidgets.QListWidget(self.cw)
        self.listWidget_icon_only.setGeometry(QtCore.QRect(0, 0, 51, 481))
        self.listWidget_icon_only.setStyleSheet("background: white;\n"
                                                "border-top-right-radius: 20px;\n"
                                                "border-bottom-right-radius: 20px;")
        self.listWidget_icon_only.setObjectName("listWidget_icon_only")

        self.side_menu_icon_only = self.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)


        self.main_content = self.listWidget_icon_only

        

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menu_list = [
            {
                "name": "PC",
                "icon": "icons/pc.png"
            },
            {
                "name": "C:"
            },
            {
                "name": "D:"
            }
        ]


        self.init_list_widget_icon_only()

        self.onDiskSelected(self.listWidget_icon_only.item(0))



    def handleFilePath(self):
        file_path = self.flabel.text()
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                self.centerfile.setRootIndex(self.model.index(file_path))
            else:
                os.startfile(file_path)
        else:
            self.flabel.setText("Не правильно указан путь")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flabel.setText(_translate("MainWindow", "C:"))

    def navigateBack(self):
        root_index = self.centerfile.rootIndex()
        parent_index = root_index.parent()
        if parent_index.isValid():
            self.centerfile.setRootIndex(parent_index)
            model = self.centerfile.model()
            file_path = model.filePath(parent_index)
            self.flabel.setText(file_path)

    def openFullScreen(self, MainWindow):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            MainWindow.showMaximized()

    def minimizeToTaskbar(self, MainWindow):
        MainWindow.showMinimized()
        


    def events(self):
        try:
            self.file.doubleClicked.connect(self.openFile)
        except Exception as error:
            self.Errors.setText(f"Error: {error}")

    def init_list_widget_icon_only(self):
        for menu in self.menu_list:
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setText(menu.get("name"))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)
        self.side_menu_icon_only.itemClicked.connect(self.onDiskSelected)

    def onDiskSelected(self, item):
        disk_name = item.text()
        if disk_name == 'PC':
            self.model.setRootPath('/')
            self.centerfile.setRootIndex(self.model.index('PC'))
            self.flabel.setText("PC")
            self.side_menu_icon_only.setCurrentRow(0)
        else:
            self.flabel.setText(disk_name)
            if disk_name.endswith(":"):
                root_path = f"{disk_name}"
                self.model.setRootPath(root_path)
                self.centerfile.setRootIndex(self.model.index(root_path))
                for index, menu in enumerate(self.menu_list):
                    if menu.get("name") == disk_name:
                        self.listWidget_icon_only.setCurrentRow(index)
                        if disk_name == "C:":
                            self.side_menu_icon_only.setCurrentRow(1)
                        elif disk_name == "D:":
                            self.side_menu_icon_only.setCurrentRow(2)


                        

    def openFile(self, index):
        model = index.model()
        if not index.isValid():
            return
        file_path = model.filePath(index)
        if os.path.isdir(file_path):
            self.centerfile.setRootIndex(index)
        else:
            os.startfile(file_path)
        self.flabel.setText(file_path)
    
    def showContextMenu(self, position):
        self.contextMenu.clear()
        open_action = self.contextMenu.addAction("Открыть")
        create_folder_action = self.contextMenu.addAction("Создать папку")
        create_folder_action.triggered.connect(self.createFolder)
        create_file_action = self.contextMenu.addAction("Создать файл")
        create_file_action.triggered.connect(self.createFile)
        open_action.triggered.connect(self.openFileFromContextMenu)
        delete_action = self.contextMenu.addAction("Удалить")
        delete_action.triggered.connect(self.deleteFileFromContextMenu)
        self.contextMenu.exec_(self.centerfile.viewport().mapToGlobal(position))


    def openFileFromContextMenu(self):
        index = self.centerfile.currentIndex()
        model = index.model()
        if not index.isValid():
            return
        file_path = model.filePath(index)
        if os.path.isdir(file_path):
            self.centerfile.setRootIndex(index)
        else:
            os.startfile(file_path)
        self.flabel.setText(file_path)

    def createFolder(self):
        index = self.centerfile.currentIndex()
        model = index.model()
        if not index.isValid():
            return
        dir_path = model.filePath(index)
        root_index = self.centerfile.rootIndex()
        root_path = model.filePath(root_index)
        new_folder_name, ok = QtWidgets.QInputDialog.getText(None, 'Создать папку', "Введите название папки:")
        if ok and new_folder_name:
            new_folder_path = os.path.join(root_path, new_folder_name)
            print("New Folder Path:", new_folder_path)
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
                self.centerfile.setRootIndex(self.model.index(root_path))

    def createFile(self):
        index = self.centerfile.currentIndex()
        model = index.model()
        if not index.isValid():
            return
        dir_path = model.filePath(index)
        root_index = self.centerfile.rootIndex()
        root_path = model.filePath(root_index)
        new_file_name, ok = QtWidgets.QInputDialog.getText(None, 'Создать файл', "Введите название файла:")
        if ok and new_file_name:
            new_file_path = os.path.join(dir_path, new_file_name)
            print("New File Path:", new_file_path)
            if not os.path.exists(new_file_path):
                open(new_file_path, 'a').close()
                self.centerfile.setRootIndex(self.model.index(root_path))

    
    def deleteFileFromContextMenu(self):
        index = self.centerfile.currentIndex()
        model = index.model()
        if not index.isValid():
            return
        file_path = model.filePath(index)
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
            self.model.remove(index)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.pos() in self.ui.ftop.geometry():
            self.ui.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and hasattr(self.ui, 'dragPosition'):
            self.move(event.globalPos() - self.ui.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if hasattr(self.ui, 'dragPosition'):
            del self.ui.dragPosition

    def resizeEvent(self, event):
        self.resizeElements(event.size())

    def resizeElements(self, size):
        new_width = size.width()
        new_height = size.height()

        self.ui.ftop.setGeometry(QtCore.QRect(0, 0, new_width, 41))
        self.ui.fftop.setGeometry(QtCore.QRect(new_width - 111, -5, 111, 42))
        self.ui.flabel.setGeometry(QtCore.QRect(60 , 50, new_width - 120, 41))
        self.ui.cw.setGeometry(QtCore.QRect(0, 100, new_width, new_height - 100))
        self.ui.centerfile.setGeometry(QtCore.QRect(60, 0, new_width - 120, new_height - 100))
        self.ui.listWidget_icon_only.setGeometry(QtCore.QRect(0, 0, 51, new_height - 100))
        self.ui.minus.setGeometry(QtCore.QRect(10, 50, 41, 41))
        self.ui.size_grip.setGeometry(QtCore.QRect(new_width - 20, new_height - 20, 20, 20))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    with open("style.qss") as f:
        style_str = f.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
