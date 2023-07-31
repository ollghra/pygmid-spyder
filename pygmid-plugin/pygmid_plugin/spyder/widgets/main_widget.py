# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2023, Tiarnach Ó Riada
#
# Licensed under the terms of the Apache Software License 2.0
# ----------------------------------------------------------------------------
"""
PyGMID Plugin Main Widget.
"""


# Third party imports
from qtpy.QtWidgets import QHBoxLayout, QLabel


# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.shellconnect.main_widget import ShellConnectMainWidget
from spyder.api.translations import get_translation

from spyder.api.widgets.main_widget import PluginMainWidget

from .controller import ControllerTabs

# Localization
_ = get_translation("pygmid_plugin.spyder")


class PyGMIDPluginActions:
    ExampleAction = "example_action"


class PyGMIDPluginToolBarSections:
    ExampleSection = "example_section"


class PyGMIDPluginOptionsMenuSections:
    ExampleSection = "example_section"

class PyGMIDPluginWidget(ShellConnectMainWidget):

    # PluginMainWidget class constants

    # Signals

    def __init__(self, name=None, plugin=None, parent=None):
        super().__init__(name, plugin, parent)


    # --- PluginMainWidget API
    # ------------------------------------------------------------------------
    def get_title(self):
        return _("PyGMID Plugin")

    def get_focus_widget(self):
        pass

    def setup(self):
        # Create an example action
        example_action = self.create_action(
            name=PyGMIDPluginActions.ExampleAction,
            text="Example action",
            tip="Example hover hint",
            icon=self.create_icon("spyder"),
            triggered=lambda: print("Example action triggered!"),
        )

        # Add an example action to the plugin options menu
        menu = self.get_options_menu()
        self.add_item_to_menu(
            example_action,
            menu,
            PyGMIDPluginOptionsMenuSections.ExampleSection,
        )

        # Add an example action to the plugin toolbar
        toolbar = self.get_main_toolbar()
        self.add_item_to_toolbar(
            example_action,
            toolbar,
            PyGMIDPluginOptionsMenuSections.ExampleSection,
        )

    def update_actions(self):
        pass

    @on_conf_change
    def on_section_conf_change(self, section):
        pass

    # ShellConnectMainWidget API
    def create_new_widget(self, shellwidget):
        #shellwidget.execute("name = 9; print(9)")
        controller = ControllerTabs(parent=self, shellwidget=shellwidget)
        controller.set_shellwidget(shellwidget)
        return controller

    def close_widget(self, widget):
        widget.close()

    def switch_widget(self, widget, old_widget):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
