import pandas as pd
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        data['操作'] = None
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section < self._data.shape[1]:
                    return str(self._data.columns[section])
                else:
                    return None
            elif orientation == Qt.Vertical:
                return str(section + 1)
        return None
        # if role != Qt.DisplayRole:
        #     return None
        # if orientation == Qt.Horizontal:
        #     return self._data.columns[section]
        # else:
        #     return str(section)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            row = index.row()
            col = index.column()
            return str(self._data.iloc[row, col])
        return None

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            try:
                self._data.iloc[row, col] = value
            except:
                return False
            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def removeRow(self, row, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        self._data.drop(self._data.index[row], inplace=True)
        self.endRemoveRows()


class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)
        self._editor = None

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            button_update = QPushButton(text="修改")
            button_update.setStyleSheet(
                ''' text-align : center;
                    background-color : NavajoWhite;
                    height : 25px;
                    width : 60px;
                    border-style: solid;
                    border-radius: 5px;
                    font : 13px  '''
            )
            button_update.clicked.connect(self.on_btn_update_clicked)
            button_update.index = [index.row(), index.column()]
            button_delete = QPushButton(text="删除")
            button_delete.setStyleSheet(
                ''' text-align : center;
                    background-color : LightCoral;
                    height : 25px;
                    width : 60px;
                    border-style: solid;
                    border-radius: 5px;
                    font : 13px  '''
            )
            button_delete.clicked.connect(self.on_btn_delete_clicked)
            button_delete.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            # h_box_layout.addWidget(button_modify)
            h_box_layout.addWidget(button_update)
            h_box_layout.addWidget(button_delete)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )

    def on_btn_delete_clicked(self):
        btn = self.sender()
        if btn:
            index = self.parent().indexAt(btn.parent().pos())
            self.parent().model().removeRow(index.row())

    def on_btn_update_clicked(self):
        btn = self.sender()
        index = self.parent().indexAt(btn.pos())
        self._editor = QLineEdit(self.parent())
        self._editor.setText(self.parent().model().data(index))
        self._editor.index = [index.row(), index.column()]
        self._editor.editingFinished.connect(self.on_editor_editing_finished)
        self.parent().setIndexWidget(index, self._editor)
        self._editor.setFocus()

    def on_editor_editing_finished(self):
        editor = self.sender()
        if isinstance(editor, QLineEdit):
            index = self.parent().model().index(editor.index[0], editor.index[1])
            value = editor.text()
            self.parent().model().setData(index, value, Qt.EditRole)
            self.parent().closePersistentEditor(index)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pandas Table")

        # create data
        data = pd.DataFrame([
            ['John', 30, 'New York'],
            ['Jane', 25, 'Paris'],
            ['Bob', 40, 'London'],
            ['Alice', 35, 'Tokyo'],
            ['Tom', 50, 'Beijing'],
            ['Jack', 45, 'Shanghai'],
            ['Rose', 20, 'Shenzhen']
        ], columns=['姓名', '年龄', '城市'])

        # create table view
        self.table = QTableView()
        self.model = PandasModel(data)
        self.table.setModel(self.model)

        # set delegate
        self.table.setItemDelegateForColumn(self.model.columnCount() - 1, ButtonDelegate(self.table))

        # add table view to main window
        self.setCentralWidget(self.table)
        # self.resize(500, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
