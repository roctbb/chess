import os
import sys

from tkgame import TkGame

__path__ = os.path.dirname(os.path.abspath(__file__))
# Запихиваем ногами "имя-проекта/src" в путь поиска:
sys.path.append(__path__)

TkGame().run()
