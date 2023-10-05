from client import MyOPAClient
from database import Database
from models import Clearance, Document, User


def main():
    db = Database()
    user = User(
        name="tsuser",
        clearance=Clearance.GOLD,
        attributes=["sci=sci1", "sci=sci2"],
    )
    print(user.to_dict())

    document = Document(
        name="ts-sci1-doc",
        clearance=Clearance.GOLD,
        attributes=["sci=sci1", "sci=sci3"],
    )
    print(document.to_dict())

    opa = MyOPAClient()
    opa.request_access(user, document)


if __name__ == "__main__":
    main()
