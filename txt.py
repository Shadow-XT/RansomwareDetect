# from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QSizePolicy, QHBoxLayout, QWidget
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QStandardItemModel, QStandardItem
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # 创建一个QTableView对象
#         self.table_view = QTableView(self)
#         # 设置水平滚动条策略为Qt.ScrollBarAlwaysOff
#         self.table_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#
#         # 创建一个QStandardItemModel对象
#         model = QStandardItemModel()
#         # 设置表格的行数和列数
#         model.setRowCount(5)
#         model.setColumnCount(4)
#         # 将模型设置为QTableView的模型
#         self.table_view.setModel(model)
#
#         # 设置每一列的最小宽度和固定宽度
#         self.table_view.setColumnWidth(0, 150)  # 第一列最小宽度为150，固定宽度为150
#         self.table_view.setColumnWidth(1, 100)  # 第二列最小宽度为100，固定宽度为100
#         self.table_view.setColumnWidth(2, 200)  # 第三列最小宽度为200，固定宽度为200
#         self.table_view.setColumnWidth(3, 150)  # 第四列最小宽度为150，固定宽度为150
#
#         # 设置QTableView的大小策略为Expanding
#         self.table_view.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
#
#         # 创建一个水平布局，并将QTableView添加到水平布局中
#         layout = QHBoxLayout()
#         # 可是上面的列还是不能随着窗口的大小而变化，因为QTableView的大小策略为Expanding，所以我们需要将QTableView的大小策略设置为Preferred
#         layout.addWidget(self.table_view)
#         # 创建一个QWidget对象，并将水平布局设置为QWidget的布局
#         widget = QWidget()
#         widget.setLayout(layout)
#         widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         # 将QWidget设置为主窗口的中央窗口
#         self.setCentralWidget(widget)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QVBoxLayout, QWidget, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个QTableView对象
        self.table_view = QTableView(self)
        # 设置水平滚动条策略为Qt.ScrollBarAlwaysOff
        self.table_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 创建一个QStandardItemModel对象
        model = QStandardItemModel()
        # 设置表格的行数和列数
        model.setRowCount(5)
        model.setColumnCount(4)
        # 设置每一列的数据
        for row in range(5):
            for col in range(4):
                item = QStandardItem(f"Row{row}, Col{col}")
                model.setItem(row, col, item)
        # 将模型设置为QTableView的模型
        self.table_view.setModel(model)

        # 设置每一列的最小宽度和固定宽度
        self.table_view.setColumnWidth(0, 150)  # 第一列最小宽度为150，固定宽度为150
        self.table_view.setColumnWidth(1, 100)  # 第二列最小宽度为100，固定宽度为100
        self.table_view.setColumnWidth(2, 200)  # 第三列最小宽度为200，固定宽度为200
        self.table_view.setColumnWidth(3, 150)  # 第四列最小宽度为150，固定宽度为150

        # 设置QTableView的大小策略为Expanding
        self.table_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 设置QHeaderView的SectionResizeMode为Custom
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Custom)

        # 定义一个回调函数，用于调整表头的大小
        def resize_header(section, old_size, new_size):
            # 设置当前列的最小宽度和固定宽度为新的大小
            self.table_view.setColumnWidth(section, new_size)
            # 如果当前列是最后一列，那么将整个表格的宽度设置为自适应窗口大小
            if section == self.table_view.model().columnCount() - 1:
                self.table_view.horizontalHeader().setStretchLastSection(True)

        # 将回调函数绑定到QHeaderView的sectionResized信号
        header.sectionResized.connect(resize_header)

        # 创建一个QWidget对象，并将QTableView设置为QWidget的布局
        widget = QWidget()
        widget.setLayout(QVBoxLayout())
        widget.layout().addWidget(self.table_view)
        # 将QWidget设置为主窗口的中央窗口
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
