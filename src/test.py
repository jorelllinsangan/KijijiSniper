from database import Session
from models.Client import Client
from models.Product import Product

session = Session()

cli = Client(twitter_handle = "jjorell")
cli2 = Client(twitter_handle = "test")

session.add_all([cli, cli2])


print list(session.query(Client))

