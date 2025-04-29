# =====================================================================================================
# ========================= Made By RyuKam1 & Ryuk_ASF(They're The Same Person) =======================
# =====================================================================================================
# ========= Please Do Not Change Any Parts Of The Code, If You Don't Know What You're Doing ===========
# =====================================================================================================


import sys
import multiprocessing
import queue
import time

from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect


class MainWindow(QMainWindow):
    def __init__(self, command_queue):
        super().__init__()
        print("MainWindow: Initializing")
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dots = []  # List of (x, y) tuples for green dots
        self.command_queue = command_queue

        # Initially set window to full screen transparent overlay
        screen_geometry = QtWidgets.qApp.desktop().screenGeometry()
        self.setGeometry(screen_geometry)

        # Timer to check for commands
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.process_commands)
        self.timer.start(100)  # check every 100 ms

    def process_commands(self):
        try:
            while True:
                command = self.command_queue.get_nowait()
                print(f"MainWindow: Received command: {command}")
                if command["action"] == "display_grid":
                    pos1 = command.get("pos1")
                    pos2 = command.get("pos2")
                    spacing = command.get("spacing", 32)
                    if pos1 and pos2:
                        self.display_grid_between_points(pos1, pos2, spacing)
                elif command["action"] == "quit":
                    print("MainWindow: Quitting application")
                    QtWidgets.qApp.quit()
        except queue.Empty:
            pass

    def display_green_dots(self, x_coords, y_coords):
        print(
            f"MainWindow: Displaying green dots at {len(x_coords)} x-coords and {len(y_coords)} y-coords")
        self.dots = []
        for x in x_coords:
            for y in y_coords:
                self.dots.append((x, y))
        self.update()

    def display_grid_between_points(self, pos1, pos2, spacing=32):
        print(
            f"MainWindow: Displaying grid between points {pos1} and {pos2} with spacing {spacing}")
        x_start, y_start = pos1
        x_end, y_end = pos2

        x_min, x_max = sorted([x_start, x_end])
        y_min, y_max = sorted([y_start, y_end])

        x_spacing = (x_max - x_min) / 31
        y_spacing = (y_max - y_min) / 31

        x_coords = [int(x_min + i * x_spacing) for i in range(32)]
        y_coords = [int(y_min + i * y_spacing) for i in range(32)]

        self.display_green_dots(x_coords, y_coords)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(0, 255, 0))  # Green color
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        dot_radius = 5

        for x, y in self.dots:
            painter.drawEllipse(QtCore.QPoint(x, y), dot_radius, dot_radius)

    def mousePressEvent(self, event):
        print("MainWindow: Mouse pressed, quitting application")
        QtWidgets.qApp.quit()


def run_app(command_queue):
    print("run_app: Starting QApplication")
    app = QApplication(sys.argv)
    window = MainWindow(command_queue)
    window.show()
    sys.exit(app.exec_())


class SplashApp:
    def __init__(self):
        print("SplashApp: Initializing")
        self.process = None
        self.command_queue = multiprocessing.Queue()

    def start(self):
        if self.process is None or not self.process.is_alive():
            print("SplashApp: Starting process")
            self.process = multiprocessing.Process(
                target=run_app, args=(self.command_queue,))
            self.process.start()
            # Wait a bit for the app to start
            time.sleep(0.5)

    def display_grid_between_points(self, pos1, pos2, spacing=32):
        if self.process and self.process.is_alive():
            print(
                f"SplashApp: Sending display_grid command with pos1={pos1}, pos2={pos2}, spacing={spacing}")
            self.command_queue.put({
                "action": "display_grid",
                "pos1": pos1,
                "pos2": pos2,
                "spacing": spacing
            })
        else:
            print("SplashApp: Process not alive, cannot send display_grid command")

    def stop(self):
        if self.process and self.process.is_alive():
            print("SplashApp: Sending quit command")
            self.command_queue.put({"action": "quit"})
            self.process.join()
            self.process = None


# Global splash instance to keep process alive
_splash_instance = None


def splashDraw(pos1, pos2, spacing=32):
    global _splash_instance
    if _splash_instance is None:
        print("splashDraw: Creating new SplashApp instance")
        _splash_instance = SplashApp()
        _splash_instance.start()
    _splash_instance.display_grid_between_points(pos1, pos2, spacing)


if __name__ == '__main__':
    splash = SplashApp()
    splash.start()
    splash.display_grid_between_points((646, 165), (1273, 793), spacing=28)
