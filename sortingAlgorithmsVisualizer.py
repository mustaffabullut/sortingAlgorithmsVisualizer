import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SortingVisualization(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sorting Visualization")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.animation_speed = 200  
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_step)

        self.create_input_panel()
        self.create_algorithm_panel()
        self.create_graph_panel()
        self.create_button_panel()

    def create_input_panel(self):
        self.input_panel = QHBoxLayout()

        self.size_label = QLabel("List Size:")
        self.size_input = QLineEdit()
        self.size_input.setValidator(QIntValidator())

        self.input_panel.addWidget(self.size_label)
        self.input_panel.addWidget(self.size_input)

        self.layout.addLayout(self.input_panel)

    def create_algorithm_panel(self):
        self.algorithm_panel = QHBoxLayout()

        self.algorithm_label = QLabel("Sorting Algorithm:")
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItem("Selection Sort")
        self.algorithm_combo.addItem("Bubble Sort")
        self.algorithm_combo.addItem("Insertion Sort")
        self.algorithm_combo.addItem("Merge Sort")
        self.algorithm_combo.addItem("Quick Sort")

        self.algorithm_panel.addWidget(self.algorithm_label)
        self.algorithm_panel.addWidget(self.algorithm_combo)

        self.layout.addLayout(self.algorithm_panel)

    def create_graph_panel(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.canvas)

    def create_button_panel(self):
        self.button_panel = QHBoxLayout()

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_list)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_animation)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_animation)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset)

        self.button_panel.addWidget(self.create_button)
        self.button_panel.addWidget(self.start_button)
        self.button_panel.addWidget(self.stop_button)
        self.button_panel.addWidget(self.reset_button)

        self.layout.addLayout(self.button_panel)

       
        self.speed_label = QLabel("Animation Speed:")
        self.speed_scale = QSlider(Qt.Horizontal)
        self.speed_scale.setMinimum(1)
        self.speed_scale.setMaximum(1000)
        self.speed_scale.setValue(self.animation_speed)
        self.speed_scale.setTickPosition(QSlider.TicksBelow)
        self.speed_scale.setTickInterval(1000)
        self.speed_scale.valueChanged.connect(self.update_animation_speed)

        self.layout.addWidget(self.speed_label)
        self.layout.addWidget(self.speed_scale)

    def update_animation_speed(self, value):
        self.animation_speed = value
        self.timer.setInterval(self.animation_speed)

    def create_list(self):
        size = int(self.size_input.text())

        
        self.list = random.sample(range(1, 100), size)
        self.colors = ['blue'] * size 

        self.show_graph()

    def show_graph(self):
        self.figure.clear()

        
        ax = self.figure.add_subplot(111)
        ax.bar(range(len(self.list)), self.list, color=self.colors)  

        self.canvas.draw()

    def start_animation(self):
        algorithm = self.algorithm_combo.currentText()

        if algorithm == "Bubble Sort":
            self.bubble_sort_animation()
        elif algorithm == "Insertion Sort":
            self.insertion_sort_animation()
        elif algorithm == "Selection Sort":
            self.selection_sort_animation()
        elif algorithm == "Merge Sort":
            self.merge_sort_animation()
        elif algorithm == "Quick Sort":
            self.quick_sort_animation()
        else:
            print("Invalid sorting algorithm selected.")

    def bubble_sort_animation(self):
        
        self.animation_step = 0
        self.timer.start(self.animation_speed)

    def insertion_sort_animation(self):
        
        self.animation_step = 1
        self.timer.start(self.animation_speed)

    def selection_sort_animation(self):
        
        self.animation_step = 0
        self.timer.start(self.animation_speed)

    def merge_sort_animation(self):
        
        self.animation_step = 0
        self.timer.start(self.animation_speed)

    def quick_sort_animation(self):
        
        self.animation_step = 0
        self.timer.start(self.animation_speed)

    def animate_step(self):
        algorithm = self.algorithm_combo.currentText()

        if algorithm == "Bubble Sort":
            self.bubble_sort_step()
        elif algorithm == "Insertion Sort":
            self.insertion_sort_step()
        elif algorithm == "Selection Sort":
            self.selection_sort_step()
        elif algorithm == "Merge Sort":
            self.merge_sort_step()
        elif algorithm == "Quick Sort":
            self.quick_sort_step()
        else:
            print("Invalid sorting algorithm selected.")

    def bubble_sort_step(self):
        if self.animation_step >= len(self.list) - 1:
            self.timer.stop()
            return

        for j in range(len(self.list) - self.animation_step - 1):
            if self.list[j] > self.list[j + 1]:
                self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
                self.colors[j], self.colors[j + 1] = 'red', 'red'  
            else:
                self.colors[j], self.colors[j + 1] = 'green', 'green'  

        self.show_graph()
        QApplication.processEvents()

        self.colors[len(self.list) - self.animation_step - 1] = 'yellow'  
        self.animation_step += 1

    def insertion_sort_step(self):
        if self.animation_step >= len(self.list):
            self.timer.stop()
            return

        key = self.list[self.animation_step]
        j = self.animation_step - 1
        while j >= 0 and self.list[j] > key:
            self.list[j + 1] = self.list[j]
            j -= 1

        self.list[j + 1] = key

        self.show_graph()
        QApplication.processEvents()

        self.colors = ['pink'] * (self.animation_step + 1) + ['black'] * (len(self.list) - self.animation_step - 1)  
        self.animation_step += 1

    def selection_sort_step(self):
        if self.animation_step >= len(self.list) - 1:
            self.timer.stop()
            return

        min_index = self.animation_step
        for j in range(self.animation_step + 1, len(self.list)):
            if self.list[j] < self.list[min_index]:
                min_index = j

        if min_index != self.animation_step:
            self.list[self.animation_step], self.list[min_index] = self.list[min_index], self.list[self.animation_step]
            self.colors[self.animation_step], self.colors[min_index] = 'purple', 'purple'  

        self.show_graph()
        QApplication.processEvents()

        self.colors[self.animation_step] = 'cyan'  
        self.animation_step += 1

    def merge_sort_step(self):
        if self.animation_step >= len(self.list):
            self.timer.stop()
            return

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            return merge(merge_sort(left), merge_sort(right))

        sorted_list = merge_sort(self.list[:self.animation_step + 1])
        self.list[:self.animation_step + 1] = sorted_list

        self.show_graph()
        QApplication.processEvents()

        self.colors = ['gold'] * (self.animation_step + 1) + ['black'] * (len(self.list) - self.animation_step - 1)  
        self.animation_step += 1

    def quick_sort_step(self):
        if self.animation_step >= len(self.list):
            self.timer.stop()
            return

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quick_sort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)

        quick_sort(self.list, 0, len(self.list) - 1)

        self.show_graph()
        QApplication.processEvents()

        self.colors = ['green'] * len(self.list)  
        self.animation_step = len(self.list)



    def stop_animation(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.animation_step = 0
        self.list = []
        self.colors = []  
        self.size_input.clear()
        self.show_graph()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualization()
    window.show()
    sys.exit(app.exec_())