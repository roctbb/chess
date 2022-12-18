import sys
import os
__path__ = os.path.dirname(os.path.abspath(__file__))
# Запихиваем ногами "имя-проекта/src" в путь поиска:
sys.path.append(__path__)

print(__path__)

from interface.tkgame import TkGame

TkGame().run()