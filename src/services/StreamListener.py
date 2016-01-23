import tweepy
from models.Client import Client


class StreamListener(tweepy.StreamListener):

	def __init__(self, Session, api  = None):
		self.Session = Session
		self.api = api
		

	def on_status(self, tweet):
		print(tweet.text)

		#Check if tweet is from existing Client
		if self.is_client(tweet.user.screen_name):
			print "%s is already a client" % tweet.user.screen_name
		else:
			#add client to database
			self.add_client(tweet.user)

		#We now want to parse the message
		if self.valid_tweet(tweet.text):
			self.confirm_request(tweet.user.screen_name)
		else:
			self.error_response(tweet.user.screen_name)


	def on_error(self, status_code):

		if status_code == 420:
			return False


	def is_client(self, twitter_handle):
		
		client = False
		session = self.Session()
	
		if session.query(Client).filter_by(twitter_handle=twitter_handle).count():
			client = True

		return client

	def valid_tweet(self, message):

		if len(message.split(":")) == 2:
			return True

		return False

	def confirm_request(self, client):
		self.api.update_status(status="I will notify you if anything comes up, @%s" % client)
		
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





