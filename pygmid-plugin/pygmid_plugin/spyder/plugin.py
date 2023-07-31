# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2023, Tiarnach Ó Riada
#
# Licensed under the terms of the Apache Software License 2.0
# ----------------------------------------------------------------------------
"""
PyGMID Plugin Plugin.
"""

# Third-party imports
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugins import Plugins, SpyderDockablePlugin
from spyder.api.translations import get_translation

# Local imports
from pygmid_plugin.spyder.confpage import PyGMIDPluginConfigPage
from pygmid_plugin.spyder.widgets import PyGMIDPluginWidget

_ = get_translation("pygmid_plugin.spyder")


class PyGMIDPlugin(SpyderDockablePlugin):
    """
    PyGMID Plugin plugin.
    """

    NAME = "pygmid_plugin"
    REQUIRES = []
    OPTIONAL = []
    WIDGET_CLASS = PyGMIDPluginWidget
    CONF_SECTION = NAME
    CONF_WIDGET_CLASS = PyGMIDPluginConfigPage

    # --- Signals

    # --- SpyderDockablePlugin API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("PyGMID Plugin")

    def get_description(self):
        return _("Use PyGMID sweep and lookup within spyder")

    def get_icon(self):
        return QIcon()

    def on_initialize(self):
        widget = self.get_widget()
        

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------
