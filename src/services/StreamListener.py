import tweepy
from models.KijijiWatcher import KijijiWatcher
from models.Client import Client


class StreamListener(tweepy.StreamListener):

	def __init__(self, Session, api  = None):
		self.Session = Session
		self.api = api
		
	#I need to protect from tweets from myself
	def on_status(self, tweet):
		print(tweet.text)
		new_client = False
		#Check if tweet is from existing Client
		if not self.is_client(tweet.user.screen_name):
			#add client to database
			self.add_client(tweet.user)
			new_client = True
		
		#We now want to parse the message and check if its valid or not
		parsed_message = parse_message(tweet.text)

		if self.valid_tweet(parsed_message):
			self.confirm_request(tweet.user.screen_name)
		else:
			self.error_response(tweet.user.screen_name)


		if new_client:
			client = self.get_client(tweet.user.screen_name)
			watcher = KijijiWatcher(client) 
		else:





	def on_error(self, status_code):

		if status_code == 420:
			return False


	def is_client(self, twitter_handle):
		
		client = False
		session = self.Session()
	
		if self.get_client(twitter_handle).count():
			client = True

		return client

	# @TwitterBot [product] | [price cap] | [location]
	#price cap check for $ .
	def valid_tweet(self, message):

		is_valid = False

		#len of mesage must be greater than one but less than or equal to 3
		if len(message) == 1:
			is_valid = True
		elif len(message) == 2:
			if self.is_number(message[1]):
				is_valid = True
		elif len(message) == 3:
			if message[1] != '' and self.is_number(message[1]):
				is_valid = True
			elif self.is_number(message[1]):
				is_valid = True

		return is_valid

	def parse_message(self, message):

		return message.replace('@TwitterBot', '').replace('$', '').split('|')


	def get_client(self, twitter_handle):
		return session.query(Client).filter_by(twitter_handle=twitter_handle)

	def confirm_request(self, client):
		self.api.update_status(status="I will notify you if anything comes up, @%s." % client)
		
	def error_response(self, client):
		self.api.update_status(status="Sorry, @%s, your message is formatted wrong." % client)

	def add_client(self, client):
		
		session = self.Session()

		new_client = Client()
		
		new_client.twitter_handle = client.screen_name
		new_client.location = client.location
		new_client.name = client.name
		new_client.followers_count = client.followers_count
		new_client.twitter_id = client.id_str

		session.add(new_client)
		session.commit()

		return new_client

	def is_number(self,price):
		try:
			float(price)
			return True
		except ValueError:
			return False





