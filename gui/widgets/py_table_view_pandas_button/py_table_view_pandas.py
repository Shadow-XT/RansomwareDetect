import os

from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QStyledItemDelegate, QPushButton, QHBoxLayout, QLineEdit, QTableView, QWidget, QFileDialog
from pandas import DataFrame

from util import calculate_entropy, PandasModel
from util.__call_function__ import __call_msgbox__
from util.file_function import get_file_info
from .style import *


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
                    height : 30px;
                    width : 60px;
                    border-style: solid;
                    border-radius: 5px;
                    font : 18px  '''
            )
            button_update.clicked.connect(self.parent().on_btn_update_clicked)
            button_update.index = [index.row(), index.column()]
            button_delete = QPushButton(text="删除")
            button_delete.setStyleSheet(
                '''QPushButton{ text-align : center;
                    background-color : LightCoral;
                    height : 30px;
                    width : 60px;
                    border-style: solid;
                    border-radius: 5px;
                    font : 18px } '''
            )
            button_delete.clicked.connect(self.parent().on_btn_delete_clicked)
            button_delete.index = [index.row(), index.column()]
            button_cal = QPushButton(text="计算")
            button_cal.setStyleSheet(
                ''' text-align : center;
                    background-color : Skyblue;
                    height : 30px;
                    width : 60px;
                    border-style: solid;
                    border-radius: 5px;
                    font : 18px  '''
            )
            button_cal.clicked.connect(self.parent().on_button_cal_clicked)
            button_cal.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(button_cal)
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


class PyTableViewPandasWithButton(QTableView):
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
                 context_color="#00ABE8",
                 ui=None
                 ):
        super(PyTableViewPandasWithButton, self).__init__()
        self._ui = ui
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
        super(PyTableViewPandasWithButton, self).setModel(self._model)
        self.setItemDelegateForColumn(self.model().columnCount() - 1, ButtonDelegate(self))

    # @property
    def model(self) -> PandasModel:
        return self._model

    def on_btn_delete_clicked(self):
        btn = self.sender()
        if btn:
            row = self.indexAt(btn.parent().pos()).row()
            self.model().removeRow(row)
            print(f"delete {row}")

    def on_btn_update_clicked(self):
        btn = self.sender()
        if btn:
            index = self.indexAt(btn.parent().pos()).row()
            # 打开文件选择弹框，文件过滤为可全部
            select_file = QFileDialog.getOpenFileName(self, "选择文件", os.path.expanduser("~"), "All Files(*.*)")[0]
            select_file_dir = os.path.dirname(select_file)
            select_file_size_k = os.path.getsize(select_file) // 1024
            if select_file:
                for i in range(self.model().rowCount()):
                    if select_file == self.model().dataX(i, 0):
                        __call_msgbox__("提示", "不可以选相同的文件", self._ui, self)
                        return
                    file = self.model().dataX(i, 0)
                    dirx = os.path.dirname(file)
                    if dirx == select_file_dir:
                        if abs(select_file_size_k - os.path.getsize(file) // 1024) < 3:
                            __call_msgbox__("提示", "同一目录下的文件大小不能相近", self._ui, self)
                            return
                info = get_file_info(select_file)
                if info is None:
                    __call_msgbox__("错误", "读取文件信息失败", self._ui, self)
                    return
                self.model().updateRow(index, (select_file, info[0] if info[0] else "未知", info[1]))
            else:
                __call_msgbox__("提示", "未选择文件", self._ui, self)

    def on_button_cal_clicked(self):
        btn = self.sender()
        if btn:
            row = self.indexAt(btn.parent().pos()).row()
            __call_msgbox__("计算结果", f"计算的信息熵值为: {os.linesep}"
                                        f"{calculate_entropy(self.model().dataX(row, 0), 0.8)}",
                            self._ui, self)

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
