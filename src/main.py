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

token = {
	'consumer': 'WaRuTvxIkNngrckv3qDkzq672',
	'access': '192557797-8DaByIFaOgWcyJC1yqTcXgGmzq8iiYiP8ZFxiLgO'
}

secret = {
	'consumer': 'isKk8nxD7LLS1sRrVSWhzwanCrJOray25yrWUarr2z7oTIvj6H',
	'access': 'Uf1DCJgNbedA6HlnO3eO3IOaPYWFJOh7ltBRLRJyJIydB'
}

def main():
	initialize_database()
	session = Session()
	authenticate_bot()

	listener = StreamListener()
	myStream = tweepy.Stream(auth =twitter_api.auth, listener=listener)

	myStream.filter(track=['snow', 'hate'])


def initialize_database():
	global engine
	global Session

	engine = create_engine('sqlite:///:memory:', echo=True)
	Session = sessionmaker(bind=engine)

	Base.metadata.create_all(engine)	

def authenticate_bot():
	global twitter_api

	auth = tweepy.OAuthHandler(token['consumer'], secret['consumer'])
	auth.set_access_token(token['access'], secret['access'])

	twitter_api = tweepy.API(auth)








main()

