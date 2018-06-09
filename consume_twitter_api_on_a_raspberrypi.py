# -*- coding: utf-8 -*-
#!/usr/bin/env python 

from twython import TwythonStreamer

APP_KEY =  ' '
APP_SECRET = ' '
OAUTH_TOKEN = ' '
OAUTH_TOKEN_SECRET = ' '

class MyStreamer(TwythonStreamer):

	successes = 0

	def on_success(self, data):
		if 'text' in data:
			self.successes += 1
			if self.successes >= 3:
				print('Ian G. Harris is popular!')

if __name__ == '__main__':
	stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	stream.statuses.filter(track='Ian G. Harris')

