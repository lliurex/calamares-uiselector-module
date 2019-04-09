#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2019, Enrique Medina Gremaldos <quiqueiii@gmail.com>
#
#   GPLv3

from PythonQt.QtGui import *
from PythonQt.QtCore import *
from PythonQt.QtSvg import QSvgWidget
import PythonQt.calamares as calamares

import gettext
import inspect
import os
_filename = inspect.getframeinfo(inspect.currentframe()).filename
_path = os.path.dirname(os.path.abspath(_filename))

_ = gettext.gettext

@calamares_module
class UISelectorViewStep:
    def __init__(self):
        self.main_widget=None

    def prettyName(self):
        return _("User interface selector")

    def isNextEnabled(self):
        return True

    def isBackEnabled(self):
        return True

    def isAtBeginning(self):
        return True

    def isAtEnd(self):
        return True

    def jobs(self):
        return [Job("")]

    def widget(self):
        return self.main_widget

    def retranslate(self, locale_name):
        calamares.utils.debug("PythonQt retranslation event "
                              "for locale name: {}".format(locale_name))

        # First we load the catalog file for the new language...
        try:
            global _
            _t = gettext.translation('calamares-uiselector',
                                     localedir=os.path.join(_path, 'lang'),
                                     languages=[locale_name])
            _ = _t.gettext
        except OSError as e:
            calamares.utils.debug(e)
            pass
        

class UIJob:
    def __init__(self, my_msg):
        self.my_msg = my_msg

    def pretty_name(self):
        return _("User interface selector job")

    def pretty_description(self):
        return _("Plasma desktop layout selector")

    def pretty_status_message(self):
        return _("Nothing to show")

    def exec(self):
        #rmp = calamares.global_storage['rootMountPoint']
        calamares.utils.debug("UI job executed")
        return {'ok': True}

