from pandas import DataFrame

from qt_core import *
from .style import *


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
                    font : 16px  '''
            )
            button_update.clicked.connect(self.parent().on_btn_update_clicked)
            button_update.index = [index.row(), index.column()]
            button_delete = QPushButton(text="删除")
            button_delete.setStyleSheet(
                ''' text-align : center;
                    background-color : LightCoral;
                    height : 25px;
                    width : 60px;
                    border-style: solid;
                    border-radius: 5px;
                    font : 16px  '''
            )
            button_delete.clicked.connect(self.parent().on_btn_delete_clicked)
            button_delete.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
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

    def on_editor_editing_finished(self):
        editor = self.sender()
        if isinstance(editor, QLineEdit):
            index = self.parent().model().index(editor.index[0], editor.index[1])
            value = editor.text()
            self.parent().model().setData(index, value, Qt.EditRole)
            self.parent().closePersistentEditor(index)


class PyTableViewPandas(QTableView):
    def __init__(self,
                 radius=8,
                 color="#FFF",
                 bg_color="#444",
                 selection_color="#FFF",
                 header_horizontal_color="#333",
                 header_vertical_color="#444",
                 bottom_line_color="#555",
                 grid_line_color="#555",
                 scroll_bar_bg_color="#FFF",
                 scroll_bar_btn_color="#3333",
                 context_color="#00ABE8"
                 ):
        super(PyTableViewPandas, self).__init__()

        # self.setAlternatingRowColors(True)
        self._style_sheet = None
        self._model = None
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

    def setModel(self, data: DataFrame):
        self._model = PandasModel(data)
        super(PyTableViewPandas, self).setModel(self._model)
        self.setItemDelegateForColumn(self.model().columnCount() - 1, ButtonDelegate(self))

    # @property
    def model(self) -> PandasModel:
        return self._model

    def on_btn_delete_clicked(self):
        btn = self.sender()
        if btn:
            # print(btn.index[0], btn.index[1],end=' ')
            # index = self.model().index(btn.index[0], btn.index[1])
            # self.model().removeRow(btn.index[0])

            row = self.indexAt(btn.parent().pos()).row()
            self.model().removeRow(row)
            print(f"delete {row}")

    def on_btn_update_clicked(self):
        btn = self.sender()
        if btn:
            index = self.indexAt(btn.pos())
            print(f"update {index}")
            # index = self.indexAt(btn.pos())
            # self.model().removeRow(index.row())
        # btn = self.sender()
        # index = self.parent().indexAt(btn.pos())
        # self.parent().model().removeRow(index.row())
        # btn = self.sender()
        # index = self.parent().indexAt(btn.pos())
        # self._editor = QLineEdit(self.parent())
        # self._editor.setText(self.parent().model().data(index))
        # self._editor.index = [index.row(), index.column()]
        # self._editor.editingFinished.connect(self.on_editor_editing_finished)
        # self.parent().setIndexWidget(index, self._editor)
        # self._editor.setFocus()

    def set_stylesheet(
            self,
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
    ):
        # APPLY STYLESHEET
        self._style_sheet = style.format(
            _radius=radius,
            _color=color,
            _bg_color=bg_color,
            _header_horizontal_color=header_horizontal_color,
            _header_vertical_color=header_vertical_color,
            _selection_color=selection_color,
            _bottom_line_color=bottom_line_color,
            _grid_line_color=grid_line_color,
            _scroll_bar_bg_color=scroll_bar_bg_color,
            _scroll_bar_btn_color=scroll_bar_btn_color,
            _context_color=context_color
        )
        self.setStyleSheet(self._style_sheet)

    def get_style_sheet(self):
        return self._style_sheet

    # def update_stylesheet(self, stylesheet):

