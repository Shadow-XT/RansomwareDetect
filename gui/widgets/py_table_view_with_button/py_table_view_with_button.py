# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT STYLE\
# ///////////////////////////////////////////////////////////////
from .style import *


class PyTableViewWithButton(QTableView):
    def __init__(self, btn_column,
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
        super(PyTableViewWithButton, self).__init__()

        # self.setAlternatingRowColors(True)
        self.setItemDelegateForColumn(btn_column, PyTableViewWithButton.TableButtonDelegate(self))
        self._model: QStandardItemModel = None
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
        # self.setColumnWidth(btn_column, 600)
        # header = QHeaderView()
        # self.setHorizontalHeader(['年份', '上报情况', '上报时间', '附件上传', '操作'])

    class TableButtonDelegate(QItemDelegate):
        def __init__(self, parent=None):
            super(PyTableViewWithButton.TableButtonDelegate, self).__init__(parent)

        def paint(self, painter, option, index):
            if not self.parent().indexWidget(index):
                # button_modify = QPushButton(text="修改")
                # button_modify.setStyleSheet(
                #     ''' text-align : center;
                #         background-color : NavajoWhite;
                #         height : 25px;
                #         width : 50px;
                #         border-style: solid;
                #         border-radius: 5px;
                #         font : 13px  '''
                # )
                # button_modify.clicked.connect(self.parent().buttonUpdate)
                # button_modify.index = [index.row(), index.column()]
                button_delete = QPushButton(text="删除")
                button_delete.setStyleSheet(
                    ''' text-align : center;
                        background-color : LightCoral;
                        height : 25px;
                        width : 50px;
                        border-style: solid;
                        border-radius: 5px;
                        font : 13px  '''
                )
                button_delete.clicked.connect(self.parent().buttonDelete)
                button_delete.index = [index.row(), index.column()]
                h_box_layout = QHBoxLayout()
                # h_box_layout.addWidget(button_modify)
                h_box_layout.addWidget(button_delete)
                h_box_layout.setContentsMargins(0, 0, 0, 0)
                h_box_layout.setAlignment(Qt.AlignCenter)
                widget = QWidget()
                widget.setLayout(h_box_layout)
                self.parent().setIndexWidget(
                    index,
                    widget
                )

    def setModel(self, model: QStandardItemModel):
        super(PyTableViewWithButton, self).setModel(model)
        self._model = model

    # @property
    def model(self):
        return self._model

    # def buttonUpdate(self):
    #     button = self.sender()
    #     if button:
    #         # 确定位置的时候这里是关键
    #         row = self.indexAt(button.parent().pos()).row()
    #         print(f"Delete {row}")

    def buttonDelete(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            row = self.indexAt(button.parent().pos()).row()
            if self._model is not None:
                self._model.removeRow(row)
                print("Deleted row: ", row)

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
        style_format = style.format(
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
        self.setStyleSheet(style_format)
