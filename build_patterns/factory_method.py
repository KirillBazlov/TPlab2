from abc import ABC, abstractmethod

# Абстрактный класс документа - как основа
class Document(ABC):
    @abstractmethod
    def create(self):
        pass
# Конкретный документ pdf
class PDFDocument(Document):
    def create(self):
        return "PDF created"
# Конкретный документ word
class WordDocument(Document):
    def create(self):
        return "Word created"
    
# Создатель (Фабрика) - основа
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def new_document(self):
        doc = self.create_document()
        print(doc.create())

# Конкретный создатель: Фабрика для pdf 
class PDFDocumentFactory(DocumentFactory):
    def create_document(self):
        return PDFDocument()
