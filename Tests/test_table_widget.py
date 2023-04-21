# from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel
# from PySide6.QtGui import QColor, QBrush
# from PySide6.QtWidgets import QApplication, QTabWidget
#
#
# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data):
#         super().__init__()
#         self._data = data
#
#     def rowCount(self, parent=QModelIndex()):
#         return len(self._data)
#
#     def columnCount(self, parent=QModelIndex()):
#         return len(self._data[0])
#
#     def data(self, index, role=Qt.DisplayRole):
#         if not index.isValid():
#             return None
#         row, col = index.row(), index.column()
#         value = self._data[row][col]
#         if role == Qt.DisplayRole:
#             return str(value)
#         elif role == Qt.BackgroundRole:
#             if self._data[row][col] != self._original_data[row][col]:
#                 return QBrush(QColor(0, 255, 0, 128))
#         return None
#
#     def setData(self, index, value, role=Qt.EditRole):
#         if not index.isValid():
#             return False
#         row, col = index.row(), index.column()
#         if role == Qt.EditRole:
#             self._data[row][col] = value
#             self.dataChanged.emit(index, index)
#             return True
#         return False
#
#     def flags(self, index):
#         return Qt.ItemIsEnabled | Qt.ItemIsEditable
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#
#     data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     original_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
#     table_model = MyTableModel(data)
#     table_model._original_data = original_data
#
#     table_view = QTabWidget()
#     table_view.setModel(table_model)
#     table_view.show()
#
#     app.exec_()

from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel
from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import QApplication, QTableView


class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row, col = index.row(), index.column()
        value = self._data[row][col]
        if role == Qt.DisplayRole:
            return str(value)
        elif role == Qt.BackgroundRole:
            if self._data[row][col] != self._original_data[row][col]:
                return QBrush(QColor(0, 255, 0, 128))
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        row, col = index.row(), index.column()
        if role == Qt.EditRole:
            self._data[row][col] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable


if __name__ == '__main__':
    app = QApplication([])

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    original_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    table_model = MyTableModel(data)
    table_model._original_data = original_data

    table_view = QTableView()
    table_view.setModel(table_model)

    # 设置表头背景色
    table_view.verticalHeader().setStyleSheet("background-color: #D3D3D3;")
    # 设置行号单元格背景色
    table_view.verticalHeader().setDefaultSectionSize(20)
    table_view.setStyleSheet("QTableView::item:selected{color:black;background-color:lightblue;}"
                             "QTableView::item:selected:!active{color:black;background-color:lightblue;border-width: 0px;}"
                             "QTableView::item:!selected:hover{color: black;background-color:#F0E68C;border-width: 0px;}"
                             "QTableView::verticalHeader{width:60px;background-color: #D3D3D3;border: 1px solid black;}"
                             "QTableView::verticalHeader::section{background-color:white;border: 1px solid black;}"
                             "QTableView::item{border: 1px solid black;}"
                             "QTableView::item:selected:!active{background-color:lightblue;border-width: 0px;}"
                             "QTableView::item:hover{background-color:#F0E68C;border-width: 0px;}")
    table_view.show()

    app.exec_()
