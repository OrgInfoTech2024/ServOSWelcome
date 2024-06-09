from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from language import langDict
import sys
import shutil
import subprocess
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 300)
        self.setWindowTitle("ServOS Welcome")
        self.setWindowIcon(QIcon(os.path.abspath("/usr/share/ServOSWelcome/images/icon.png")))
        
        # CHECKING LIVE CD
        username = os.getlogin()
        livecdusername = ""
        with open(os.path.abspath("/usr/share/ServOSWelcome/datas/livecdusername.txt"), 'r') as file:
            livecdusername = file.read()
        if username == livecdusername:
            self.close

        # SOUND
        self.media_player = QMediaPlayer()
        sound_path = os.path.abspath("/usr/share/ServOSWelcome/sounds/title.mp3")
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))
        self.media_player.play()
        
        # LANGUAGE
        self.lang = langDict
        self.syslang = QLocale.system().name()
        if self.syslang not in self.lang:
            self.syslang = "en_US"
        

        # BACK PANEL
        self.panel = QWidget(self)
        heightPanel = int(self.geometry().height())
        self.panel.setGeometry(0, 0, 145, heightPanel)
        self.panel.setStyleSheet("background-color: #000099;")
        self.resizeEvent = self.panelHeight
        
        self.firstPageLabel = QLabel(self.lang[self.syslang]["Welcome"], self)
        self.firstPageLabel.setGeometry(5, 5, 140, 20)
        self.firstPageLabel.setStyleSheet("color: white")
        self.fontfirstPageLabel = QFont()
        self.firstPageLabel.setFont(self.fontfirstPageLabel)
        
        self.secondPageLabel = QLabel(self.lang[self.syslang]["Mail"], self)
        self.secondPageLabel.setGeometry(5, 30, 140, 20)
        self.secondPageLabel.setStyleSheet("color: white")
        self.fontsecondPageLabel = QFont()
        self.secondPageLabel.setFont(self.fontsecondPageLabel)
        
        self.thirdPageLabel = QLabel(self.lang[self.syslang]["Install programs"], self)
        self.thirdPageLabel.setGeometry(5, 55, 140, 20)
        self.thirdPageLabel.setStyleSheet("color: white")
        self.fontthirdPageLabel = QFont()
        self.thirdPageLabel.setFont(self.fontthirdPageLabel)
        
        self.fourthPageLabel = QLabel(self.lang[self.syslang]["Background"], self)
        self.fourthPageLabel.setGeometry(5, 80, 140, 20)
        self.fourthPageLabel.setStyleSheet("color: white")
        self.fontfourthPageLabel = QFont()
        self.fourthPageLabel.setFont(self.fontfourthPageLabel)
        
        self.fifthPageLabel = QLabel(self.lang[self.syslang]["Weather"], self)
        self.fifthPageLabel.setGeometry(5, 105, 140, 20)
        self.fifthPageLabel.setStyleSheet("color: white")
        self.fontfifthPageLabel = QFont()
        self.fifthPageLabel.setFont(self.fontfifthPageLabel)
        
        self.sixthPageLabel = QLabel(self.lang[self.syslang]["Finish"], self)
        self.sixthPageLabel.setGeometry(5, 130, 140, 20)
        self.sixthPageLabel.setStyleSheet("color: white")
        self.fontsixthPageLabel = QFont()
        self.sixthPageLabel.setFont(self.fontsixthPageLabel)
        
        
        # MAIN ELEMENTS OF THE PAGES
        self.mainLabel = QLabel(self)
        self.mainLabel.setGeometry(150, 0, 300, 50)
        self.mainLabel.setStyleSheet("font-size: 20px")
        
        
        # FIRST PAGE
        welcome_text = self.lang[self.syslang]["Welcome to ServOS. For continuation installing,<br>please to click \"Next\""]
        self.welcomeLabel = QLabel(welcome_text, self)
        self.welcomeLabel.setGeometry(150, 50, 300, 50)
        self.welcomeLabel.hide()
        
        self.firstNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.firstNextButton.setGeometry(380, 260, 60, 30)
        self.firstNextButton.hide()
        self.firstNextButton.clicked.connect(self.secondPage)
        
        
        # SECOND PAGE
        mail_text = self.lang[self.syslang]["If you want to add your email to mail client,<br>please to click \"Add email\""]
        self.mailLabel = QLabel(mail_text, self)
        self.mailLabel.setGeometry(150, 50, 300, 50)
        self.mailLabel.hide()
        
        self.addMailButton = QPushButton(self.lang[self.syslang]["Add email"], self)
        self.addMailButton.setGeometry(150, 100, 80, 30)
        self.addMailButton.hide()
        self.addMailButton.clicked.connect(self.addmail)
        
        self.secondBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.secondBackButton.setGeometry(150, 260, 60, 30)
        self.secondBackButton.hide()
        self.secondBackButton.clicked.connect(self.firstPage)
        
        self.secondNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.secondNextButton.setGeometry(380, 260, 60, 30)
        self.secondNextButton.hide()
        self.secondNextButton.clicked.connect(self.thirdPage)
        
        
        # THIRD PAGE
        install_programs_text = self.lang[self.syslang]["What's programs, which you want to install?"]
        self.installProgramsLabel = QLabel(install_programs_text, self)
        self.installProgramsLabel.setGeometry(150, 50, 300, 50)
        self.installProgramsLabel.hide()
        
        self.telegramCheckBox = QCheckBox("Telegram", self)
        self.telegramCheckBox.setGeometry(150, 100, 210, 25)
        self.telegramCheckBox.hide()
        
        self.blenderCheckBox = QCheckBox("Blender", self)
        self.blenderCheckBox.setGeometry(150, 130, 210, 25)
        self.blenderCheckBox.hide()
        
        self.librecadCheckBox = QCheckBox("LibreCAD", self)
        self.librecadCheckBox.setGeometry(150, 160, 210, 25)
        self.librecadCheckBox.hide()
        
        self.sqlitebrowserCheckBox = QCheckBox("DB Browser (SQLiteBrowser)", self)
        self.sqlitebrowserCheckBox.setGeometry(150, 190, 210, 25)
        self.sqlitebrowserCheckBox.hide()
        
        self.thirdBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.thirdBackButton.setGeometry(150, 260, 60, 30)
        self.thirdBackButton.hide()
        self.thirdBackButton.clicked.connect(self.secondPage)
        
        self.thirdNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.thirdNextButton.setGeometry(380, 260, 60, 30)
        self.thirdNextButton.hide()
        self.thirdNextButton.clicked.connect(self.fourthPage)
        
        
        # FOURTH PAGE
        please_choose_background_text = self.lang[self.syslang]["Please to choose your backgroud:"]
        self.chooseBackgroundLabel = QLabel(please_choose_background_text, self)
        self.chooseBackgroundLabel.setGeometry(150, 50, 300, 50)
        self.chooseBackgroundLabel.hide()
        
        self.carpatian_background_label = QPushButton(self)
        self.carpatian_background = QIcon(os.path.abspath('/usr/share/backgrounds/ServOS/carpatian.jpg'))
        self.carpatian_background_label.setIcon(self.carpatian_background)
        self.carpatian_background_label.setIconSize(QSize(126, 96))
        self.carpatian_background_label.setGeometry(150, 100, 120, 60)
        self.carpatian_background_label.clicked.connect(self.set_carpatian_background)
        self.carpatian_background_label.hide()

        self.autumn_background_label = QPushButton(self)
        self.autumn_background = QIcon(os.path.abspath('/usr/share/backgrounds/ServOS/autumn.jpg'))
        self.autumn_background_label.setIcon(self.autumn_background)
        self.autumn_background_label.setIconSize(QSize(126, 96))
        self.autumn_background_label.setGeometry(275, 100, 120, 60)
        self.autumn_background_label.clicked.connect(self.set_autumn_background)
        self.autumn_background_label.hide()

        self.palanok_background_label = QPushButton(self)
        self.palanok_background = QIcon(os.path.abspath('/usr/share/backgrounds/ServOS/palanok.jpg'))
        self.palanok_background_label.setIcon(self.palanok_background)
        self.palanok_background_label.setIconSize(QSize(126, 96))
        self.palanok_background_label.setGeometry(150, 165, 120, 60)
        self.palanok_background_label.clicked.connect(self.set_palanok_background)
        self.palanok_background_label.hide()

        self.dnipro_background_label = QPushButton(self)
        self.dnipro_background = QIcon(os.path.abspath('/usr/share/backgrounds/ServOS/dnipro.jpg'))
        self.dnipro_background_label.setIcon(self.dnipro_background)
        self.dnipro_background_label.setIconSize(QSize(126, 96))
        self.dnipro_background_label.setGeometry(275, 165, 120, 60)
        self.dnipro_background_label.clicked.connect(self.set_dnipro_background)
        self.dnipro_background_label.hide()
        
        self.fourthBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.fourthBackButton.setGeometry(150, 260, 60, 30)
        self.fourthBackButton.hide()
        self.fourthBackButton.clicked.connect(self.thirdPage)
        
        self.fourthNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.fourthNextButton.setGeometry(380, 260, 60, 30)
        self.fourthNextButton.hide()
        self.fourthNextButton.clicked.connect(self.fivthPage)
        
        
        # FIVTH PAGE
        self.weather_list = []
        
        weather_text = self.lang[self.syslang]["Please to add you community region:"]
        self.weatherLabel = QLabel(weather_text, self)
        self.weatherLabel.setGeometry(150, 50, 300, 50)
        self.weatherLabel.hide()
        
        self.community_input = QLineEdit(self)
        self.community_input.setPlaceholderText(self.lang[self.syslang]["Your community"])
        self.community_input.setGeometry(150, 100, 150, 30)
        self.community_input.hide()
        
        self.add_button = QPushButton(self.lang[self.syslang]["Add"], self)
        self.add_button.setGeometry(300, 100, 50, 30)
        self.add_button.clicked.connect(self.add)
        self.add_button.hide()
        
        self.remove_button = QPushButton(self.lang[self.syslang]["Remove"], self)
        self.remove_button.setGeometry(350, 100, 75, 30)
        self.remove_button.clicked.connect(self.remove)
        self.remove_button.hide()
        
        self.weather_listbox = QListWidget(self)
        self.weather_listbox.setGeometry(150, 130, 275, 125)
        self.weather_listbox.hide()
        
        self.fifthBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.fifthBackButton.setGeometry(150, 260, 60, 30)
        self.fifthBackButton.hide()
        self.fifthBackButton.clicked.connect(self.fourthPage)
        
        self.fifthNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.fifthNextButton.setGeometry(380, 260, 60, 30)
        self.fifthNextButton.hide()
        self.fifthNextButton.clicked.connect(self.sixthPage)
        
        
        # SIXTH PAGE
        finish_text = self.lang[self.syslang]["You complete instalation ServOS.<br>You may to click \"Exit\""]
        self.finishLabel = QLabel(finish_text, self)
        self.finishLabel.setGeometry(150, 50, 300, 50)
        self.finishLabel.hide()
        
        self.exitButton = QPushButton(self.lang[self.syslang]["Exit"], self)
        self.exitButton.setGeometry(380, 260, 60, 30)
        self.exitButton.hide()
        self.exitButton.clicked.connect(self.exit)
        
        
        self.firstPage()    
    
    def panelHeight(self, event):
        self.panel.setGeometry(0, 0, 145, self.height())   
    
    def hideAll(self):
        self.welcomeLabel.hide()
        self.firstNextButton.hide()
        
        self.mailLabel.hide()
        self.addMailButton.hide()
        self.secondBackButton.hide()
        self.secondNextButton.hide()
        
        self.installProgramsLabel.hide()
        self.telegramCheckBox.hide()
        self.blenderCheckBox.hide()
        self.librecadCheckBox.hide()
        self.sqlitebrowserCheckBox.hide()
        self.thirdBackButton.hide()
        self.thirdNextButton.hide()
        
        self.chooseBackgroundLabel.hide()
        self.carpatian_background_label.hide()
        self.autumn_background_label.hide()
        self.palanok_background_label.hide()
        self.dnipro_background_label.hide()
        self.fourthBackButton.hide()
        self.fourthNextButton.hide()
        
        self.weatherLabel.hide()
        self.community_input.hide()
        self.add_button.hide()
        self.remove_button.hide()
        self.weather_listbox.hide()
        self.fifthBackButton.hide()
        self.fifthNextButton.hide()
        
        self.finishLabel.hide()
        self.exitButton.hide()
        
        self.fontfirstPageLabel.setBold(False)
        self.firstPageLabel.setFont(self.fontfirstPageLabel)
        self.fontsecondPageLabel.setBold(False)
        self.secondPageLabel.setFont(self.fontsecondPageLabel)
        self.fontthirdPageLabel.setBold(False)
        self.thirdPageLabel.setFont(self.fontthirdPageLabel)
        self.fontfourthPageLabel.setBold(False)
        self.fourthPageLabel.setFont(self.fontfourthPageLabel)
        self.fontfifthPageLabel.setBold(False)
        self.fifthPageLabel.setFont(self.fontfifthPageLabel)
        self.fontsixthPageLabel.setBold(False)
        self.sixthPageLabel.setFont(self.fontsixthPageLabel)
    
    def firstPage(self):
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Welcome"])
        self.fontfirstPageLabel.setBold(True)
        self.firstPageLabel.setFont(self.fontfirstPageLabel)
        
        self.welcomeLabel.show()
        self.firstNextButton.show()
    
    def secondPage(self):
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Mail"])
        self.fontsecondPageLabel.setBold(True)
        self.secondPageLabel.setFont(self.fontsecondPageLabel)
        
        self.mailLabel.show()
        self.addMailButton.show()
        self.secondBackButton.show()
        self.secondNextButton.show()
    
    def thirdPage(self):
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Install programs"])
        self.fontthirdPageLabel.setBold(True)
        self.thirdPageLabel.setFont(self.fontthirdPageLabel)
        
        self.installProgramsLabel.show()
        self.telegramCheckBox.show()
        self.blenderCheckBox.show()
        self.librecadCheckBox.show()
        self.sqlitebrowserCheckBox.show()
        self.thirdBackButton.show()
        self.thirdNextButton.show()
    
    def fourthPage(self):
        selected_programs = []

        if self.telegramCheckBox.isChecked():
            selected_programs.append("telegram-desktop")
        if self.blenderCheckBox.isChecked():
            selected_programs.append("blender")
        if self.librecadCheckBox.isChecked():
            selected_programs.append("librecad")
        if self.sqlitebrowserCheckBox.isChecked():
            selected_programs.append("sqlitebrowser")
            
        if selected_programs:
            programs_to_install = ' '.join(selected_programs)
            command = f'sudo apt-get install {programs_to_install} -y'
            try:
                subprocess.run(['xterm', '-e', command])
            except Exception as e:
                print(f"Error executing command: {e}")
            
            
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Background"])
        self.fontfourthPageLabel.setBold(True)
        self.fourthPageLabel.setFont(self.fontfourthPageLabel)
        
        self.chooseBackgroundLabel.show()
        self.carpatian_background_label.show()
        self.autumn_background_label.show()
        self.palanok_background_label.show()
        self.dnipro_background_label.show()
        self.fourthBackButton.show()
        self.fourthNextButton.show()
    
    def fivthPage(self):
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Weather"])
        self.fontfifthPageLabel.setBold(True)
        self.fifthPageLabel.setFont(self.fontfifthPageLabel)
    
        self.weatherLabel.show()
        self.community_input.show()
        self.add_button.show()
        self.remove_button.show()
        self.weather_listbox.show()
        self.fifthBackButton.show()
        self.fifthNextButton.show()
        
    def sixthPage(self, event):
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, '.programdates', 'weather.txt')
        try:
            with open(file_path, 'w') as f:
                for item in self.weather_list:
                    f.write(f'{item}\n')
        except:
            print('Error')
        
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Finish"])
        self.fontsixthPageLabel.setBold(True)
        self.sixthPageLabel.setFont(self.fontsixthPageLabel)
        
        self.finishLabel.show()
        self.exitButton.show()
    
    def addmail(self):
        try:
            subprocess.Popen(['thunderbird', '--display=:0', '-AddProfile'])
        except Exception as e:
            print(f"Error opening Thunderbird: {e}")
            
    def set_carpatian_background(self):
        subprocess.run([
            "qdbus",
            "org.kde.plasmashell",
            "/PlasmaShell",
            "org.kde.PlasmaShell.evaluateScript",
            "string:var allDesktops = desktops(); for (i = 0; i < allDesktops.length; i++) { d = allDesktops[i]; d.wallpaperPlugin = 'org.kde.image'; d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); d.writeConfig('Image', '/usr/share/backgrounds/ServOS/carpatian.jpg'); }"
        ])
            
    def set_autumn_background(self):
        subprocess.run([
            "qdbus",
            "org.kde.plasmashell",
            "/PlasmaShell",
            "org.kde.PlasmaShell.evaluateScript",
            "string:var allDesktops = desktops(); for (i = 0; i < allDesktops.length; i++) { d = allDesktops[i]; d.wallpaperPlugin = 'org.kde.image'; d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); d.writeConfig('Image', '/usr/share/backgrounds/ServOS/autumn.jpg'); }"
        ])
            
    def set_palanok_background(self):
        subprocess.run([
            "qdbus",
            "org.kde.plasmashell",
            "/PlasmaShell",
            "org.kde.PlasmaShell.evaluateScript",
            "string:var allDesktops = desktops(); for (i = 0; i < allDesktops.length; i++) { d = allDesktops[i]; d.wallpaperPlugin = 'org.kde.image'; d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); d.writeConfig('Image', '/usr/share/backgrounds/ServOS/palanok.jpg'); }"
        ])
            
    def set_dnipro_background(self):
        subprocess.run([
            "qdbus",
            "org.kde.plasmashell",
            "/PlasmaShell",
            "org.kde.PlasmaShell.evaluateScript",
            "string:var allDesktops = desktops(); for (i = 0; i < allDesktops.length; i++) { d = allDesktops[i]; d.wallpaperPlugin = 'org.kde.image'; d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); d.writeConfig('Image', '/usr/share/backgrounds/ServOS/dnipro.jpg'); }"
        ])
        
    def add(self):
        text = self.community_input.text()
        self.weather_list.append(str(text))
        self.weather_listbox.clear()
        self.weather_listbox.addItems(self.weather_list)

    def remove(self):
        selected_item = self.weather_listbox.currentItem()
        if selected_item:
            text = selected_item.text()
            self.weather_list.remove(text)
            self.weather_listbox.clear()
            self.weather_listbox.addItems(self.weather_list)
    
    def exit(self):
        home_dir = os.path.expanduser("~")
        autostart_file_path = os.path.join(home_dir, ".config/autostart/python.desktop")
        if os.path.exists(autostart_file_path):
            os.remove(autostart_file_path)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())