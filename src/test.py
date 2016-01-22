from sqlalchemy import create_engine
from Client import Client
from Base import Base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


session = Session()
cli = Client(twitter_handle = "jjorell")
cli2 = Client(twitter_handle ="TwijijiBot")

session.add_all([cli, cli2])


clients = session.query(Client)


print list(clients)

