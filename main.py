from pep.client import MyOPAClient
from pep.database import Database
from pep.models import Clearance, Document, User


def main():
    db = Database()
    user = User(
        name="gold_user",
        clearance=Clearance.GOLD,
        attributes=["team=backend", "team=frontend"],
    )
    print(user.to_dict())

    document = Document(
        name="gold-backend-document",
        clearance=Clearance.GOLD,
        attributes=["team=backend"],
    )
    print(document.to_dict())

    db.add_user(user)
    db.add_document(document)

    opa = MyOPAClient()
    result = opa.request_access(user, document)

    if result:
        print(f"ACCESS GRANTED: User `{user.name}` GRANTED access to `{document.name}`")
    else:
        print(f"ACCESS DENIED: User `{user.name}` DENIED access to `{document.name}`")


if __name__ == "__main__":
    main()
