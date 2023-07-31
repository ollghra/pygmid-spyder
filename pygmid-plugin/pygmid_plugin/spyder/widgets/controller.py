from pygmid import sweep

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
        self.config_file_path = "sweep.cfg"

        self._tabWidget = QTabWidget(parent=self)
        self._tabWidget.addTab(SweepTab(parent=self), _("Sweep"))
        self._tabWidget.addTab(LookupTab(parent=self), _("Lookup"))
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
        self.config_file_path = self.parent().config_file_path

        layout = QHBoxLayout()

        formLayout = QFormLayout()
        
        hlayout = QHBoxLayout()
        
        self._model_file = QLineEdit(self)
        self._model_file.setReadOnly(True)
        hlayout.addWidget(self._model_file)

        self._select_model_file = QPushButton(_("Select"), self)
        self._select_model_file.clicked.connect(self._on_select_model_file)
        hlayout.addWidget(self._select_model_file)
 
        formLayout.addRow(_("Model file"), hlayout)
      
        self._model_info = QLineEdit(self)
        formLayout.addRow(_("Model info"), self._model_info)
        self._corner = QLineEdit("NOM", self)
        formLayout.addRow(_("Corner"), self._corner)
        self._temperature = QLineEdit("300", self)
        formLayout.addRow(_("Temperature"), self._temperature)
        self._model_n = QLineEdit(self)
        formLayout.addRow(_("Model N"), self._model_n)
        self._model_p = QLineEdit(self)
        formLayout.addRow(_("Model P"), self._model_p)
        self._save_file_n = QLineEdit("nch",self)
        formLayout.addRow(_("Save File N"), self._save_file_n)
        self._save_file_p = QLineEdit("pch", self)
        formLayout.addRow(_("Save File P"), self._save_file_p)
        self._mn = QTextEdit(self)
        formLayout.addRow(_("MN"), self._mn)
        self._mp = QTextEdit(self)
        formLayout.addRow(_("MP"), self._mp)
      
        sweepFormLayout = QFormLayout()
        label = QLabel(_("Sweep Parameters"))
        sweepFormLayout.addRow(label)

        self._vgs = QLineEdit(_("(start, stop, step)"))
        sweepFormLayout.addRow(_("VGS"), self._vgs)
        self._vds = QLineEdit(_("(start, stop, step)"))
        sweepFormLayout.addRow(_("VDS"), self._vds)
        self._vsb = QLineEdit(_("(start, stop, step)"))
        sweepFormLayout.addRow(_("VSB"), self._vsb)
        self._length = QLineEdit(_("[(start, stop, step), ...]"))
        sweepFormLayout.addRow(_("Length"), self._length)
        self._width = QLineEdit("1")
        sweepFormLayout.addRow(_("Width"), self._width)
        self._nfing = QLineEdit("1")
        sweepFormLayout.addRow(_("Number of fingers"), self._nfing)

        formLayout.addRow(sweepFormLayout)

        self._generate_config = QPushButton(_("Generate"), parent=self)
        self._generate_config.clicked.connect(self._on_generate_config)
        formLayout.addRow(self._generate_config)

        layout.addLayout(formLayout)

        vlayout = QVBoxLayout()
        self._config_label = QLabel(_("Config File") + f": {self.config_file_path}")
        self._config = QTextEdit(self)
        vlayout.addWidget(self._config_label)
        vlayout.addWidget(self._config)

        self._save_config = QPushButton(_("Save Config"))
        self._save_config.clicked.connect(self._on_save_config)
        vlayout.addWidget(self._save_config)

        layout.addLayout(vlayout)
 
        self.setLayout(layout)

        # Generate a blank config on the right
        self._on_generate_config()

    def _on_select_model_file(self):
        file_name = QFileDialog.getOpenFileName(self, _("Select Model File"), "/", _("Model files (*.scs);;All files (*)"))
        print(file_name)
        if (len(file_name[0]) > 0):
            self._model_file.setText(file_name[0])

    def _on_generate_config(self):
        self._config.setText(self._to_config())
    def _on_save_config(self):
        with open(self.config_file_path, "w+") as f:
            print(f"WRITE CONFIG to {self.config_file_path}: {self._to_config()}")
            f.write(self._config.text())



    def _to_config(self) -> str:
        return "\n".join([
            "[MODEL]",
            "file = " + self._model_file.text(),
            "info = " + self._model_info.text(),
            "corner = " + self._corner.text(),
            "temp = " + self._temperature.text(),
            "modeln = " + self._model_n.text(),
            "modelp = " + self._model_p.text(),
            "savefilen = " +self._save_file_n.text(),
            "savefilep = " + self._save_file_p.text(),
            "paramfile = params.scs",
            "[SWEEP]",
            "VGS = " + self._vgs.text(),
            "VGS = " + self._vds.text(),
            "VGS = " + self._vsb.text(),
            "VGS = " + self._length.text(),
            "VGS = " + self._width.text(),
            "VGS = " + self._nfing.text(),
            ])

def run_sweep(config_file="sweep.cfg"):
    mfn, mfp = sweep.run(config_file, skip_sweep=False)

class LookupTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._label = QLabel("Lookup")

        layout = QVBoxLayout()
        layout.addWidget(self._label)
        self.setLayout(layout)
