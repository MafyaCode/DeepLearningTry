import sys
from PySide6.QtWidgets import QApplication
# Asumsikan Anda punya MainWindow di src/aplikasi_saya/main_window.py
from src.aplikasi_saya.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv) # Buat aplikasi Qt
    window = MainWindow()        # Buat instance window utama Anda
    window.show()                # Tampilkan window
    sys.exit(app.exec())         # Jalankan event loop Qt