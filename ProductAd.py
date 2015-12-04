class ProductAd:

	def __init__ (self, id = None, title = None, price = None, location = None, datePosted = None):
		self.id = id
		self.title = title
		self.price = price
		self.location = location
		self.datePosted = datePosted

	def __str__(self):

		return "Title (%d): %s\nPrice: %s\nLocation: %s\nDate Posted: %s" % ( self.id, self.title, self.price, self.location, self.datePosted)




