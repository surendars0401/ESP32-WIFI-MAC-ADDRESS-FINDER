import sys
import subprocess
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QPushButton, QWidget, QHBoxLayout, QLineEdit, QProgressBar
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class MACAddressFinder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ESP32 MAC Address Finder")
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        com_port_layout = QHBoxLayout()
        self.com_port_label = QLabel("Select COM Port:")
        com_port_layout.addWidget(self.com_port_label)

        self.com_port_dropdown = QComboBox()
        self.update_com_ports()
        com_port_layout.addWidget(self.com_port_dropdown)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_com_ports)
        com_port_layout.addWidget(self.refresh_button)

        self.layout.addLayout(com_port_layout)

        self.status_layout = QHBoxLayout()
        self.status_label = QLabel("Status: Not Connected")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(0)
        self.progress_bar.setTextVisible(False)
        self.status_layout.addWidget(self.progress_bar)

        self.layout.addLayout(self.status_layout)

        self.get_mac_button = QPushButton("Get MAC Address")
        self.get_mac_button.clicked.connect(self.get_mac_address)
        self.layout.addWidget(self.get_mac_button)

        self.mac_address_label = QLineEdit()
        self.mac_address_label.setReadOnly(True)
        self.mac_address_label.setAlignment(Qt.AlignCenter)
        self.mac_address_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.layout.addWidget(self.mac_address_label)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_com_ports)

    def update_com_ports(self):
        self.com_port_dropdown.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.com_port_dropdown.addItem(port.device)

    def refresh_com_ports(self):
        self.update_com_ports()
        self.mac_address_label.clear()

    def get_mac_address(self):
        selected_port = self.com_port_dropdown.currentText()
        if not selected_port:
            self.status_label.setText("Status: No COM port selected")
            return

        self.status_label.setText("Status: Connecting...")
        self.progress_bar.setVisible(True)
        QApplication.processEvents()

        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "esptool",
                    "--port",
                    selected_port,
                    "read_mac"
                ],
                capture_output=True,
                text=True,
                timeout=30
            )
            self.handle_subprocess_output(result)

        except subprocess.TimeoutExpired:
            self.status_label.setText("Status: Connection timed out")
        except FileNotFoundError:
            self.status_label.setText("Status: esptool executable not found")
        except Exception as e:
            self.status_label.setText(f"Status: Failed to connect ({str(e)})")
        finally:
            self.progress_bar.setVisible(False)

    def handle_subprocess_output(self, result):
        for line in result.stdout.splitlines():
            if line.startswith("MAC:"):
                mac = line.split("MAC:")[1].strip().replace(":", "")
                self.mac_address_label.setText(mac)
                self.status_label.setText("Status: Connected")
                return

        self.status_label.setText("Status: Failed to retrieve MAC address")


def main():
    app = QApplication(sys.argv)
    window = MACAddressFinder()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
