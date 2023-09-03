from abc import ABC, abstractmethod

class File_vacancy(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass
    @abstractmethod
    def find_vacancy(self):
        pass
    @abstractmethod
    def del_vacancy(self):
        pass

