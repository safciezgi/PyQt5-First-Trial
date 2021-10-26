#from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*  
import psutil
import shutil
import netifaces
import platform

class first_GUI(QWidget):
    def __init__(self):
        #super(first_GUI, self).__init__()
        #super().__init__()
        QWidget.__init__(self)
        self.setWindowOpacity(0.7)
        self.setStyleSheet("""
                           background-color: rgb(13, 61, 133);
                           """)
        
        self.label1 = QLabel("Network Interfaces Ip & Names")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("""
                                  color: white;
                                  font-weight: bold; 
                                  font-size: 16pt
                                  """)
        self.label2 = QLabel("Disk Usage")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("""
                                  color: white;
                                  font-weight: bold;
                                  font-size: 16pt
                                  """)
        self.label3 = QLabel("System Info")
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setStyleSheet("""
                                  color: white;
                                  font-weight: bold;
                                  font-size: 16pt
                                  """)                          
        self.label4 = QLabel("System Info")
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setStyleSheet("""
                                  color: white;
                                  font-weight: bold;
                                  font-size: 16pt
                                  """) 
        self.label5 = QLabel("System Info")
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setStyleSheet("""
                                  color: white;
                                  font-weight: bold;
                                  font-size: 16pt
                                  """)                          
        
        Button1_clr = QPushButton("Clear")
        Button1_clr.setMinimumHeight(40)
        Button1_clr.setStyleSheet("""
                                  background-color: white;
                                  font-weight: bold;
                                  font-size: 16pt
                                  """)
        Button1_show = QPushButton("Show")
        Button1_show.setMinimumHeight(40)
        Button1_show.setStyleSheet("""
                                   background-color: white;
                                   font-weight: bold;
                                   font-size: 16pt
                                   """)
           
        #Buttons assignment
        Button1_clr.clicked.connect(self.clear_text)
        Button1_show.clicked.connect(self.show_text)



        vertical_layout = QVBoxLayout()
        #first row widgets
        vertical_layout.addWidget(self.label1)
        
        
        #second row widgets
        vertical_layout.addWidget(self.label2)
       

        #third row widgets
        vertical_layout.addWidget(self.label3)


        #fourth row widgets
        vertical_layout.addWidget(self.label4)
        vertical_layout.addWidget(self.label5)


        #Button functions call
        vertical_layout.addWidget(Button1_clr)
        vertical_layout.addWidget(Button1_show)

        #Window settings
        self.setLayout(vertical_layout)
        self.setWindowTitle("PyQt5 OS Trial GUI")
        self.resize(600,500)


    def clear_text(self):
        self.label1.clear()
        self.label2.clear()
        self.label3.clear()
        self.label4.clear()
        self.label5.clear()
    def show_text(self):

        #Network interfaces
        addrs = psutil.net_if_addrs()
        eth = list(addrs.keys())
        self.label1.setText(str(eth[0]) + ' ' + netifaces.ifaddresses(eth[0])[netifaces.AF_INET][0]['addr'] + "\n" + str(eth[1])+ ' ' + netifaces.ifaddresses(eth[1])[netifaces.AF_INET][0]['addr'])
        
        #Disk usage
        total, used, free = shutil.disk_usage("/")
        self.label2.setText("Total: %d \n " % (total // (2**30)) + "Used: %d GiB \n" % (used // (2**30)) + "Free: %d GiB" % (free // (2**30)))
        
        #System Info
        uname = platform.uname()
        self.label3.setText(f"System: {uname.system}\nNode Name: {uname.node}\nRelease: {uname.release}\nVersion: {uname.version}\nMachine: {uname.machine}\nProcessor: {uname.processor}\n")
       
        #CPU Info
        phy_core = psutil.cpu_count(logical=False)
        total_core = psutil.cpu_count(logical=True)
        self.label4.setText("Physical cores:" + str(phy_core) + "\n" + "Total cores:" + str(total_core))
        cpufreq = psutil.cpu_freq()
        self.label5.setText(f"Max Frequency: {cpufreq.max:.2f}Mhz\nMax Frequency: {cpufreq.max:.2f}Mhz\nMin Frequency: {cpufreq.min:.2f}Mhz\nCurrent Frequency: {cpufreq.current:.2f}Mhz")
        
app = QApplication([])
widget = first_GUI()
widget.show()
app.exec_() 