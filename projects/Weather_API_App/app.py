from dotenv import load_dotenv
load_dotenv()

import os
import requests
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # UI Elements
        self.city_label = QLabel("🌆 Enter City Name")
        self.city_input = QLineEdit()
        self.get_weather = QPushButton("🔍 Get Weather")
        self.temperature_label = QLabel("")
        self.emoji_label = QLabel("")
        self.desc_label = QLabel("")

        self.initUI("🌤️ Weather App")

        # Button connection
        self.get_weather.clicked.connect(self.get_weather_data)

    def initUI(self, name):
        self.setWindowTitle(name)
        self.setFixedSize(360, 400)

        # Fonts
        font_label = QFont("Segoe UI", 14)
        font_result = QFont("Segoe UI", 16, QFont.Bold)

        self.city_label.setFont(font_label)
        self.city_input.setFont(font_label)
        self.get_weather.setFont(font_label)
        self.temperature_label.setFont(font_result)
        self.emoji_label.setFont(QFont("Segoe UI Emoji", 48))
        self.desc_label.setFont(font_label)

        # Layout
        vbox = QVBoxLayout()
        vbox.setSpacing(15)
        vbox.addWidget(self.city_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.city_input, alignment=Qt.AlignCenter)
        vbox.addWidget(self.get_weather, alignment=Qt.AlignCenter)
        vbox.addWidget(self.temperature_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.emoji_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.desc_label, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        # Styling
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                              stop:0 #2c3e50, stop:1 #3498db);
                color: #ecf0f1;
                font-family: 'Segoe UI';
            }

            QLabel {
                font-size: 16px;
            }

            QLineEdit {
                padding: 10px;
                font-size: 16px;
                border: 2px solid #16a085;
                border-radius: 15px;
                background-color: #ecf0f1;
                color: #2c3e50;
            }

            QPushButton {
                font-size: 16px;
                padding: 12px;
                border-radius: 20px;
                background-color: #1abc9c;
                color: white;
                border: 2px solid transparent;
                transition: all 0.3s ease-in-out;
            }

            QPushButton:hover {
                background-color: #16a085;
                border: 2px solid #ecf0f1;
            }
        """)

    def get_weather_data(self):
        city = self.city_input.text().strip().lower()
        print(f"User entered {city} as city")
        api_key = os.getenv("WEATHER_API_KEY")

        if not city:
            self.display_error("⚠️ Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print(f"Received data: {data}")
                temp = data['main']['temp']
                weather_desc = data['weather'][0]['description'].capitalize()
                icon = data['weather'][0]['icon']

                # Map weather condition to emoji (optional)
                emoji = self.map_weather_to_emoji(icon)
                self.display_weather(temp, weather_desc, emoji)
            else:
                self.display_error(f"❌ City not found: {city}")
        except Exception as e:
            self.display_error(f"💥 Error: {str(e)}")

    def display_weather(self, temp, description, emoji):
        self.temperature_label.setText(f"{temp:.1f}°C")
        self.desc_label.setText(description)
        self.emoji_label.setText(emoji)

    def display_error(self, message):
        self.temperature_label.setText("")
        self.desc_label.setText(message)
        self.emoji_label.setText("❌")

    def map_weather_to_emoji(self, icon_code):
        if icon_code.startswith('01'):
            return "☀️"
        elif icon_code.startswith('02') or icon_code.startswith('03'):
            return "⛅"
        elif icon_code.startswith('04'):
            return "☁️"
        elif icon_code.startswith('09') or icon_code.startswith('10'):
            return "🌧️"
        elif icon_code.startswith('11'):
            return "⛈️"
        elif icon_code.startswith('13'):
            return "❄️"
        elif icon_code.startswith('50'):
            return "🌫️"
        else:
            return "🌡️"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
