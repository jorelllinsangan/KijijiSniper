from database.Base import Base
from models.Client import Client
from models.Product import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None
Session = None


def main():
	initialize_database()
	session = Session()
	cli = Client(twitter_handle = "jjorell")
	session.add(cli)

def initialize_database():
	global engine
	engine = create_engine('sqlite:///:memory:', echo=True)
	global Session
	Session = sessionmaker(bind=engine)
	Base.metadata.create_all(engine)	


main()

