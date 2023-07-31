from qtpy import PYQT5
from qtpy.QtWidgets import *
from spyder.api.translations import get_translation
from spyder.api.widgets.mixins import SpyderWidgetMixin
_ = get_translation("pygmid_plugin.spyder")

class ControllerTabs(QWidget, SpyderWidgetMixin):
    def __init__(self, parent, shellwidget):
        if PYQT5:
            super().__init__(parent=parent, class_parent=parent)
        else:
            QWidget.__init__(self, parent)
            SpyderWidgetMixin.__init__(self, class_parent=parent)
        self.shellwidget = shellwidget

        self._tabWidget = QTabWidget(parent=self)
        self._tabWidget.addTab(SweepTab(), _("Sweep"))
        self._tabWidget.addTab(LookupTab(), _("Lookup"))
        layout = QVBoxLayout()
        layout.addWidget(self._tabWidget)
        self.setLayout(layout)

    def set_shellwidget(self, shellwidget):
        self.shellwidget = shellwidget
        self._refresh()

    def _refresh(self) -> None:
        if self.shellwidget.kernel_client is None:
            return
        self.shellwidget.call_kernel(interrupt=True)

class SweepTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._label = QLabel("SWEEP")

        layout = QVBoxLayout()
        layout.addWidget(self._label)
        self.setLayout(layout)

class LookupTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._label = QLabel("Lookup")

        layout = QVBoxLayout()
        layout.addWidget(self._label)
        self.setLayout(layout)
