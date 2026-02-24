# Principio da segregação de interfaces. Interfaces são partidas de forma mais dinâmica assim podendo utilizala de forma especifica

from abc import ABC, abstractmethod

class Documents(ABC): #classe genérica
    
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass

    #Essa classe abstrata vira: ISP


class DocumentPDF:
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentTXT:
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentExcel():
    
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass
