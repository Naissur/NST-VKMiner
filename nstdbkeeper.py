#!/usr/bin/python -t

class NSTDBKeeper:

	""" Creates database.
		To be used in connection with NSTVKFetcher.
		Written by NST team.
	"""
	
	def __init__(self):
		print "NSTDBKeeper: NSTDBKeeper initialized"

	def insert(self, personId, friendList):
		print "NSTDBKeeper: Insetring {} width friends {}".format(personId, ' '.join(friendList))
