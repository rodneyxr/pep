import unittest

from pep.client import MyOPAClient
from pep.models import Clearance, Document, User


class TestOPA(unittest.TestCase):
    def setUp(self) -> None:
        self.opa = MyOPAClient()
        return super().setUp()

    def create_user(self, clearance, attributes=None, name="testuser"):
        return User(name=name, clearance=clearance, attributes=attributes)

    def create_document(self, clearance, attributes=None, name="testdoc"):
        return Document(name=name, clearance=clearance, attributes=attributes)

    def assertAllow(self, user, document):
        self.assertTrue(
            self.opa.request_access(user, document),
            msg=f"User {user} should be allowed to access {document}",
        )

    def assertDeny(self, user, document):
        self.assertFalse(
            self.opa.request_access(user, document),
            msg=f"User {user} should not be allowed to access {document}",
        )

    def test_public_user_can_access_public_document_with_no_attributes(self):
        user = self.create_user(Clearance.PUBLIC)
        doc = self.create_document(Clearance.PUBLIC)
        self.assertAllow(user, doc)

    def test_public_user_with_attributes_can_access_public_document_with_no_attributes(
        self,
    ):
        user = self.create_user(Clearance.PUBLIC, attributes=["nat=usa"])
        doc = self.create_document(Clearance.PUBLIC)
        self.assertAllow(user, doc)

    def test_public_user_with_attributes_can_access_public_document_with_attributes(
        self,
    ):
        user = self.create_user(Clearance.PUBLIC, attributes=["nat=usa"])
        doc = self.create_document(Clearance.PUBLIC, attributes=["nat=usa"])
        self.assertAllow(user, doc)

    def test_public_user_with_attributes_can_access_public_document_with_attributes2(
        self,
    ):
        user = self.create_user(
            Clearance.PUBLIC, attributes=["nat=usa", "project=financial"]
        )
        doc = self.create_document(Clearance.PUBLIC, attributes=["nat=usa"])
        self.assertAllow(user, doc)

    def test_public_user_with_no_attributes_cannot_access_bronze_document_without_attributes(
        self,
    ):
        user = self.create_user(Clearance.PUBLIC)
        doc = self.create_document(Clearance.BRONZE)
        self.assertDeny(user, doc)

    def test_gold_user_no_attributes_cannot_access_public_document_with_attributes(
        self,
    ):
        user = self.create_user(Clearance.GOLD)
        doc = self.create_document(Clearance.PUBLIC, attributes=["nat=usa"])
        self.assertDeny(user, doc)

    def test_gold_user_with_attributes_cannot_access_public_document_with_different_attributes(
        self,
    ):
        user = self.create_user(Clearance.GOLD, attributes=["nat=uk"])
        doc = self.create_document(Clearance.PUBLIC, attributes=["nat=usa"])
        self.assertDeny(user, doc)
