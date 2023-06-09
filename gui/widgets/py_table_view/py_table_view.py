# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT STYLE\
# ///////////////////////////////////////////////////////////////
from .style import *


class PyTableView(QTableView):
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
        super(PyTableView, self).__init__()

        # self.setAlternatingRowColors(True)
        # self.setItemDelegateForColumn(btn_column, PyTableView.TableButtonDelegate(self))
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

    def setModel(self, model: QStandardItemModel):
        super(PyTableView, self).setModel(model)
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
