import abc
from abc import ABC, abstractmethod

class plugin(ABC):

    @property
    @abstractmethod
    def IDENTIFIER(self):
        pass

    @abstractmethod
    def check_project(self, path):
        pass