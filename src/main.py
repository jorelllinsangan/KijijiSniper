from database.Base import Base
from models.Client import Client
from models.Product import Product
from services.StreamListener import StreamListener
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tweepy

engine = None
Session = None
twitter_api = None


def main():
	initialize_database()
	
	authenticate_bot()

	

	listener = StreamListener(Session, twitter_api)
	myStream = tweepy.Stream(auth =twitter_api.auth, listener=listener)

	myStream.filter(track=['@TwijijiBot'])

def initialize_database():
	global engine
	global Session

	engine = create_engine('sqlite:///database/twijiji_data.db', echo=True)
	Session = sessionmaker(bind=engine)

	Base.metadata.create_all(engine)	

def authenticate_bot():
	global twitter_api

	file_name = 'keys.txt'
	secrets = read_keys(file_name)
	print secrets
	auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
	auth.set_access_token(secrets['access_token'], secrets['access_secret'])

	twitter_api = tweepy.API(auth)

def read_keys(file_name):
	secrets = {}

	with open(file_name, 'rb') as f:
		lines = f.readlines()
		
	for line in lines:
		line = line.rstrip().split(":")
		secrets[line[0]] = line[1]

	return secrets

main()

