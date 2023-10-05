from typing import List

from pep.models import Document, User


class Database(object):
    def __init__(self):
        self._users = []
        self._documents = []

    @property
    def users(self) -> List[User]:
        return self._users

    @property
    def documents(self) -> List[Document]:
        return self._documents

    def add_user(self, user: User):
        if not isinstance(user, User):
            raise ValueError("User must be an instance of the 'User' class")
        self._users.append(user)

    def remove_user(self, user: User):
        try:
            self._users.remove(user)
        except ValueError:
            pass

    def add_document(self, document: Document):
        if not isinstance(document, Document):
            raise ValueError("Document must be an instance of the 'Document' class")
        self._documents.append(document)

    def remove_document(self, document: Document):
        try:
            self._documents.remove(document)
        except ValueError:
            pass
