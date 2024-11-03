import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>421</width>
    <height>403</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Перемешивание</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="new_button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>111</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать новый</string>
    </property>
   </widget>
   <widget class="QPushButton" name="open_button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>160</y>
      <width>111</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Открыть файл</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="filename_edit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="text_edit">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>0</y>
      <width>281</width>
      <height>351</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="save_button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>100</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить файл</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>421</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.new_button.clicked.connect(self.new)
        self.open_button.clicked.connect(self.open)
        self.save_button.clicked.connect(self.save)

    def new(self):
        self.text_edit.setPlainText('')
        self.filename_edit.setText('')

    def open(self):
        try:
            with open(self.filename_edit.text()) as f:
                text = f.read()
            self.text_edit.setPlainText(text)
        except FileNotFoundError:
            pass

    def save(self):
        if self.filename_edit.text():
            if self.filename_edit.text()[-4:] == '.txt':
                with open(self.filename_edit.text(), 'w') as f:
                    f.write(self.text_edit.toPlainText())
            else:
                with open(self.filename_edit.text() + '.txt', 'w') as f:
                    f.write(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())
