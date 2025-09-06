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
        self.setGeometry(0, 0, 450, 300)
        self.setWindowTitle("ServOS Welcome")
        self.setWindowIcon(QIcon(os.path.abspath("/usr/share/ServOSWelcome/images/icon.png")))
        
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
        self.panel.setGeometry(0, 0, 165, heightPanel)
        self.panel.setStyleSheet("background-color: #000099;")
        self.resizeEvent = self.Resize

        self.firstPageLabel = QLabel(self.lang[self.syslang]["Welcome"], self)
        self.firstPageLabel.setGeometry(5, 5, 160, 20)
        self.firstPageLabel.setStyleSheet("color: white")
        self.fontfirstPageLabel = QFont()
        self.firstPageLabel.setFont(self.fontfirstPageLabel)
        
        self.secondPageLabel = QLabel(self.lang[self.syslang]["Mail"], self)
        self.secondPageLabel.setGeometry(5, 30, 160, 20)
        self.secondPageLabel.setStyleSheet("color: white")
        self.fontsecondPageLabel = QFont()
        self.secondPageLabel.setFont(self.fontsecondPageLabel)
        
        self.thirdPageLabel = QLabel(self.lang[self.syslang]["Install programs"], self)
        self.thirdPageLabel.setGeometry(5, 55, 160, 20)
        self.thirdPageLabel.setStyleSheet("color: white")
        self.fontthirdPageLabel = QFont()
        self.thirdPageLabel.setFont(self.fontthirdPageLabel)
        
        self.fourthPageLabel = QLabel(self.lang[self.syslang]["Background"], self)
        self.fourthPageLabel.setGeometry(5, 80, 160, 20)
        self.fourthPageLabel.setStyleSheet("color: white")
        self.fontfourthPageLabel = QFont()
        self.fourthPageLabel.setFont(self.fontfourthPageLabel)
        
        self.fifthPageLabel = QLabel(self.lang[self.syslang]["Weather"], self)
        self.fifthPageLabel.setGeometry(5, 105, 160, 20)
        self.fifthPageLabel.setStyleSheet("color: white")
        self.fontfifthPageLabel = QFont()
        self.fifthPageLabel.setFont(self.fontfifthPageLabel)
        
        self.sixthPageLabel = QLabel(self.lang[self.syslang]["Time Zone"], self)
        self.sixthPageLabel.setGeometry(5, 130, 160, 20)
        self.sixthPageLabel.setStyleSheet("color: white")
        self.fontsixthPageLabel = QFont()
        self.sixthPageLabel.setFont(self.fontsixthPageLabel)
        
        self.seventhPageLabel = QLabel(self.lang[self.syslang]["Choosing an User Icon"], self)
        self.seventhPageLabel.setGeometry(5, 155, 160, 20)
        self.seventhPageLabel.setStyleSheet("color: white")
        self.fontseventhPageLabel = QFont()
        self.seventhPageLabel.setFont(self.fontseventhPageLabel)
        
        self.eighthPageLabel = QLabel(self.lang[self.syslang]["Finish"], self)
        self.eighthPageLabel.setGeometry(5, 180, 160, 20)
        self.eighthPageLabel.setStyleSheet("color: white")
        self.fonteighthPageLabel = QFont()
        self.seventhPageLabel.setFont(self.fonteighthPageLabel)
        
        
        # MAIN ELEMENTS OF THE PAGES
        self.mainLabel = QLabel(self)
        self.mainLabel.setGeometry(170, 0, 300, 50)
        self.mainLabel.setStyleSheet("font-size: 20px")
        
        
        # FIRST PAGE
        welcome_text = self.lang[self.syslang]["Welcome to ServOS. For continuation installing,<br>please to click \"Next\""]
        self.welcomeLabel = QLabel(welcome_text, self)
        self.welcomeLabel.setGeometry(170, 50, 300, 50)
        self.welcomeLabel.hide()
        
        self.firstNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.firstNextButton.hide()
        self.firstNextButton.clicked.connect(self.secondPage)
        
        
        # SECOND PAGE
        mail_text = self.lang[self.syslang]["If you want to add your email to mail client,<br>please to click \"Add email\""]
        self.mailLabel = QLabel(mail_text, self)
        self.mailLabel.setGeometry(170, 50, 300, 50)
        self.mailLabel.hide()
        
        self.addMailButton = QPushButton(self.lang[self.syslang]["Add email"], self)
        self.addMailButton.setGeometry(170, 100, 80, 30)
        self.addMailButton.hide()
        self.addMailButton.clicked.connect(self.addmail)
        
        self.secondBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.secondBackButton.hide()
        self.secondBackButton.clicked.connect(self.firstPage)
        
        self.secondNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.secondNextButton.hide()
        self.secondNextButton.clicked.connect(self.thirdPage)
        
        
        # THIRD PAGE
        install_programs_text = self.lang[self.syslang]["What's programs, which you want to install?"]
        self.installProgramsLabel = QLabel(install_programs_text, self)
        self.installProgramsLabel.setGeometry(170, 50, 300, 50)
        self.installProgramsLabel.hide()
        
        self.telegramCheckBox = QCheckBox("Telegram", self)
        self.telegramCheckBox.setGeometry(170, 90, 210, 25)
        self.telegramCheckBox.hide()
        
        self.blenderCheckBox = QCheckBox("Blender", self)
        self.blenderCheckBox.setGeometry(170, 110, 210, 25)
        self.blenderCheckBox.hide()
        
        self.librecadCheckBox = QCheckBox("LibreCAD", self)
        self.librecadCheckBox.setGeometry(170, 130, 210, 25)
        self.librecadCheckBox.hide()
        
        self.sqlitebrowserCheckBox = QCheckBox("SQLiteBrowser", self)
        self.sqlitebrowserCheckBox.setGeometry(170, 150, 210, 25)
        self.sqlitebrowserCheckBox.hide()
        
        self.kritaCheckBox = QCheckBox("Krita", self)
        self.kritaCheckBox.setGeometry(170, 170, 210, 25)
        self.kritaCheckBox.hide()
        
        self.virtualboxCheckBox = QCheckBox("VirtualBox", self)
        self.virtualboxCheckBox.setGeometry(170, 190, 210, 25)
        self.virtualboxCheckBox.hide()
        
        self.kdenliveCheckBox = QCheckBox("Kdenlive", self)
        self.kdenliveCheckBox.setGeometry(170, 210, 210, 25)
        self.kdenliveCheckBox.hide()
        
        self.filezillaCheckBox = QCheckBox("FileZilla", self)
        self.filezillaCheckBox.setGeometry(170, 230, 210, 25)
        self.filezillaCheckBox.hide()
        
        self.qtcreatorCheckBox = QCheckBox("QtCreator", self)
        self.qtcreatorCheckBox.setGeometry(170, 250, 210, 25)
        self.qtcreatorCheckBox.hide()
        
        self.dbvisualizerCheckBox = QCheckBox("DbVisualizer", self)
        self.dbvisualizerCheckBox.setGeometry(170, 270, 210, 25)
        self.dbvisualizerCheckBox.hide()
        
        self.thirdBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.thirdBackButton.setGeometry(170, 260, 60, 30)
        self.thirdBackButton.hide()
        self.thirdBackButton.clicked.connect(self.secondPage)
        
        self.thirdNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.thirdNextButton.setGeometry(380, 260, 60, 30)
        self.thirdNextButton.hide()
        self.thirdNextButton.clicked.connect(self.fourthPage)
        
        
        # FOURTH PAGE
        please_choose_background_text = self.lang[self.syslang]["Please to choose your backgroud:"]
        self.chooseBackgroundLabel = QLabel(please_choose_background_text, self)
        self.chooseBackgroundLabel.setGeometry(170, 50, 300, 50)
        self.chooseBackgroundLabel.hide()
        
        self.carpatian_background_label = QPushButton(self)
        self.carpatian_background = QIcon(os.path.abspath('/usr/share/backgrounds/linuxmint/sele_ring.jpg'))
        self.carpatian_background_label.setIcon(self.carpatian_background)
        self.carpatian_background_label.setIconSize(QSize(100, 50))
        self.carpatian_background_label.setGeometry(170, 100, 100, 60)
        self.carpatian_background_label.clicked.connect(self.set_carpatian_background)
        self.carpatian_background_label.hide()

        self.autumn_background_label = QPushButton(self)
        self.autumn_background = QIcon(os.path.abspath('/usr/share/backgrounds/linuxmint/autumn.jpg'))
        self.autumn_background_label.setIcon(self.autumn_background)
        self.autumn_background_label.setIconSize(QSize(100, 50))
        self.autumn_background_label.setGeometry(275, 100, 100, 60)
        self.autumn_background_label.clicked.connect(self.set_autumn_background)
        self.autumn_background_label.hide()

        self.palanok_background_label = QPushButton(self)
        self.palanok_background = QIcon(os.path.abspath('/usr/share/backgrounds/linuxmint/palanok.jpg'))
        self.palanok_background_label.setIcon(self.palanok_background)
        self.palanok_background_label.setIconSize(QSize(100, 50))
        self.palanok_background_label.setGeometry(170, 165, 100, 60)
        self.palanok_background_label.clicked.connect(self.set_palanok_background)
        self.palanok_background_label.hide()

        self.dnipro_background_label = QPushButton(self)
        self.dnipro_background = QIcon(os.path.abspath('/usr/share/backgrounds/linuxmint/dnipro.jpg'))
        self.dnipro_background_label.setIcon(self.dnipro_background)
        self.dnipro_background_label.setIconSize(QSize(100, 50))
        self.dnipro_background_label.setGeometry(275, 165, 100, 60)
        self.dnipro_background_label.clicked.connect(self.set_dnipro_background)
        self.dnipro_background_label.hide()
        
        self.fourthBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.fourthBackButton.setGeometry(170, 260, 60, 30)
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
        self.weatherLabel.setGeometry(170, 50, 300, 50)
        self.weatherLabel.hide()
        
        self.community_input = QLineEdit(self)
        self.community_input.setPlaceholderText(self.lang[self.syslang]["Your community"])
        self.community_input.setGeometry(170, 100, 150, 30)
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
        self.weather_listbox.setGeometry(170, 130, 275, 125)
        self.weather_listbox.hide()
        
        self.fifthBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.fifthBackButton.setGeometry(170, 260, 60, 30)
        self.fifthBackButton.hide()
        self.fifthBackButton.clicked.connect(self.fourthPage)
        
        self.fifthNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.fifthNextButton.setGeometry(380, 260, 60, 30)
        self.fifthNextButton.hide()
        self.fifthNextButton.clicked.connect(self.sixthPage)
        
        
        # SIXTH PAGE        
        self.timeZoneComboBox = QComboBox(self)
        self.timeZoneComboBox.addItems(self.get_available_timezones())
        self.timeZoneComboBox.setGeometry(170, 100, 150, 30)
        self.timeZoneComboBox.hide()

        timeZone_text = self.lang[self.syslang]["Please to select your timezone:"]
        self.timeZoneLabel = QLabel(timeZone_text, self)
        self.timeZoneLabel.setGeometry(170, 50, 300, 50)
        self.timeZoneLabel.hide()
        
        self.sixthBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.sixthBackButton.setGeometry(170, 260, 60, 30)
        self.sixthBackButton.hide()
        self.sixthBackButton.clicked.connect(self.fivthPage)
        
        self.sixthNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.sixthNextButton.setGeometry(380, 260, 60, 30)
        self.sixthNextButton.hide()
        self.sixthNextButton.clicked.connect(self.seventhPage)
        
        
        # SEVENTH PAGE
        please_choose_user_icon_text = self.lang[self.syslang]["Please to choose your User Icon:"]
        self.chooseUserIconLabel = QLabel(please_choose_background_text, self)
        self.chooseUserIconLabel.setGeometry(170, 50, 300, 50)
        self.chooseUserIconLabel.hide()
        
        self.usertile1_label = QPushButton(self)
        self.usertile1 = QIcon(os.path.abspath('/usr/share/usericons/usertile1.png'))
        self.usertile1_label.setIcon(self.usertile1)
        self.usertile1_label.setIconSize(QSize(50, 50))
        self.usertile1_label.setGeometry(170, 100, 60, 60)
        self.usertile1_label.clicked.connect(self.set_usertile1)
        self.usertile1_label.hide()

        self.usertile2_label = QPushButton(self)
        self.usertile2 = QIcon(os.path.abspath('/usr/share/usericons/usertile2.png'))
        self.usertile2_label.setIcon(self.usertile2)
        self.usertile2_label.setIconSize(QSize(50, 50))
        self.usertile2_label.setGeometry(235, 100, 60, 60)
        self.usertile2_label.clicked.connect(self.set_usertile2)
        self.usertile2_label.hide()

        self.usertile3_label = QPushButton(self)
        self.usertile3 = QIcon(os.path.abspath('/usr/share/usericons/usertile3.png'))
        self.usertile3_label.setIcon(self.usertile3)
        self.usertile3_label.setIconSize(QSize(50, 50))
        self.usertile3_label.setGeometry(170, 165, 60, 60)
        self.usertile3_label.clicked.connect(self.set_usertile3)
        self.usertile3_label.hide()

        self.usertile4_label = QPushButton(self)
        self.usertile4 = QIcon(os.path.abspath('/usr/share/usericons/usertile4.png'))
        self.usertile4_label.setIcon(self.usertile4)
        self.usertile4_label.setIconSize(QSize(50, 50))
        self.usertile4_label.setGeometry(235, 165, 60, 60)
        self.usertile4_label.clicked.connect(self.set_usertile4)
        self.usertile4_label.hide()
        
        self.seventhBackButton = QPushButton(self.lang[self.syslang]["Back"], self)
        self.seventhBackButton.setGeometry(170, 260, 60, 30)
        self.seventhBackButton.hide()
        self.seventhBackButton.clicked.connect(self.sixthPage)
        
        self.seventhNextButton = QPushButton(self.lang[self.syslang]["Next"], self)
        self.seventhNextButton.setGeometry(380, 260, 60, 30)
        self.seventhNextButton.hide()
        self.seventhNextButton.clicked.connect(self.eighthPage)
        
        
        # EIGHTH PAGE
        finish_text = self.lang[self.syslang]["You complete instalation ServOS.<br>You may to click \"Exit\""]
        self.finishLabel = QLabel(finish_text, self)
        self.finishLabel.setGeometry(170, 50, 300, 50)
        self.finishLabel.hide()
        
        self.exitButton = QPushButton(self.lang[self.syslang]["Exit"], self)
        self.exitButton.setGeometry(380, 260, 60, 30)
        self.exitButton.hide()
        self.exitButton.clicked.connect(self.exit)
        
        
        self.firstPage()  
        
        self.showFullScreen()

    def get_available_timezones(self):
        try:
            result = subprocess.run(['timedatectl', 'list-timezones'], capture_output=True, text=True, check=True)
            timezones = result.stdout.splitlines()
            return timezones
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при получении часовых поясов: {e}")
            return []
    
    def Resize(self, event):
        self.panel.setGeometry(0, 0, 165, self.height())

        leftForButton = self.width() - 70
        rightForButton = self.height() - 40
        self.firstNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.secondBackButton.setGeometry(170, rightForButton, 60, 30)
        self.secondNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.thirdBackButton.setGeometry(170, rightForButton, 60, 30)
        self.thirdNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.fourthBackButton.setGeometry(170, rightForButton, 60, 30)
        self.fourthNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.fifthBackButton.setGeometry(170, rightForButton, 60, 30)
        self.fifthNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.sixthBackButton.setGeometry(170, rightForButton, 60, 30)
        self.sixthNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.seventhBackButton.setGeometry(170, rightForButton, 60, 30)
        self.seventhNextButton.setGeometry(leftForButton, rightForButton, 60, 30)
        self.exitButton.setGeometry(leftForButton, rightForButton, 60, 30)

        
        self.community_input.setGeometry(170, 100, self.width() - 285, 30)
        self.add_button.setGeometry(self.width() - 135, 100, 50, 30)
        self.remove_button.setGeometry(self.width() - 85, 100, 75, 30)
        self.weather_listbox.setGeometry(170, 130, self.width() - 160, self.height() - 175)

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
        self.kritaCheckBox.hide()
        self.virtualboxCheckBox.hide()
        self.kdenliveCheckBox.hide()
        self.filezillaCheckBox.hide()
        self.qtcreatorCheckBox.hide()
        self.dbvisualizerCheckBox.hide()
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

        self.timeZoneLabel.hide()
        self.timeZoneComboBox.hide()
        self.sixthBackButton.hide()
        self.sixthNextButton.hide()

        self.chooseUserIconLabel.hide()
        self.usertile1_label.hide()
        self.usertile2_label.hide()
        self.usertile3_label.hide()
        self.usertile4_label.hide()
        self.seventhBackButton.hide()
        self.seventhNextButton.hide()
        
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
        self.fontseventhPageLabel.setBold(False)
        self.seventhPageLabel.setFont(self.fontseventhPageLabel)
    
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
        self.kritaCheckBox.show()
        self.virtualboxCheckBox.show()
        self.kdenliveCheckBox.show()
        self.filezillaCheckBox.show()
        self.qtcreatorCheckBox.show()
        self.dbvisualizerCheckBox.show()
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
        if self.kritaCheckBox.isChecked():
            selected_programs.append("krita")
        if self.virtualboxCheckBox.isChecked():
            selected_programs.append("virtualbox")
        if self.kdenliveCheckBox.isChecked():
            selected_programs.append("kdenlive")
        if self.filezillaCheckBox.isChecked():
            selected_programs.append("filezilla")
        if self.qtcreatorCheckBox.isChecked():
            selected_programs.append("qtcreator")
        if self.dbvisualizerCheckBox.isChecked():
            command = "sudo wget https://storage.googleapis.com/dbvis-download/product_download/dbvis-24.2.2/media/dbvis_linux_24_2_2.deb && sudo at install ./dbvis_linux_24_2_2.deb && sudo rm dbvis_linux_24_2_2.deb"
            try:
                subprocess.run(['xterm', '-e', command])
            except Exception as e:
                print(f"Error executing command: {e}")
            
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
        
        self.mainLabel.setText(self.lang[self.syslang]["Time Zone"])
        self.fontsixthPageLabel.setBold(True)
        self.sixthPageLabel.setFont(self.fontsixthPageLabel)
        
        self.timeZoneLabel.show()
        self.timeZoneComboBox.show()
        self.sixthBackButton.show()
        self.sixthNextButton.show()
        
    def seventhPage(self, event):
        timezone = self.timeZoneComboBox.currentText()
        subprocess.run(['timedatectl', 'set-timezone', timezone], check=True)
        
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Choosing an User Icon"])
        self.fontseventhPageLabel.setBold(True)
        self.seventhPageLabel.setFont(self.fontseventhPageLabel)

        self.chooseUserIconLabel.show()
        self.usertile1_label.show()
        self.usertile2_label.show()
        self.usertile3_label.show()
        self.usertile4_label.show()
        self.seventhBackButton.show()
        self.seventhNextButton.show()
        
    def eighthPage(self, event):
        timezone = self.timeZoneComboBox.currentText()
        subprocess.run(['timedatectl', 'set-timezone', timezone], check=True)
        
        self.hideAll()
        
        self.mainLabel.setText(self.lang[self.syslang]["Finish"])
        self.fonteighthPageLabel.setBold(True)
        self.eighthPageLabel.setFont(self.fonteighthPageLabel)
        
        self.finishLabel.show()
        self.exitButton.show()
    
    def addmail(self):
        try:
            subprocess.Popen(['thunderbird', '--display=:0', '-AddProfile'])
        except Exception as e:
            print(f"Error opening Thunderbird: {e}")
            
    def set_carpatian_background(self):
        subprocess.run([
            "gsettings", "set", "org.mate.background", "picture-filename", '/usr/share/backgrounds/linuxmint/sele_ring.jpg'
        ])
            
    def set_autumn_background(self):
        subprocess.run([
            "gsettings", "set", "org.mate.background", "picture-filename", '/usr/share/backgrounds/linuxmint/autumn.jpg'
        ])
            
    def set_palanok_background(self):
        subprocess.run([
            "gsettings", "set", "org.mate.background", "picture-filename", '/usr/share/backgrounds/linuxmint/palanok.jpg'
        ])
            
    def set_dnipro_background(self):
        subprocess.run([
            "gsettings", "set", "org.mate.background", "picture-filename", '/usr/share/backgrounds/linuxmint/dnipro.jpg'
        ])
            
    def set_usertile1(self):
        subprocess.run([
            "cp", "/usr/share/usericons/usertile1.png", os.path.expanduser("~/.face")
        ])

    def set_usertile2(self):
        subprocess.run([
            "cp", "/usr/share/usericons/usertile2.png", os.path.expanduser("~/.face")
        ])

    def set_usertile3(self):
        subprocess.run([
            "cp", "/usr/share/usericons/usertile3.png", os.path.expanduser("~/.face")
        ])

    def set_usertile4(self):
        subprocess.run([
            "cp", "/usr/share/usericons/usertile4.png", os.path.expanduser("~/.face")
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
        autostart_file_path = os.path.join(home_dir, ".config/autostart/ServOSWelcome.desktop")
        if os.path.exists(autostart_file_path):
            os.remove(autostart_file_path)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
