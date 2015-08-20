import requests
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	
	# def __init__(self):
	# 	super(MyHTMLParser, self).__init__()
	# 	self.token = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'input' and self.is_hidden_token(attrs):
			self.token = attrs[2][1]
			print('find token: ', self.token)

		print tag, attrs

	def handle_endtag(self, tag):
		pass
	def handle_data(self, data):
		pass

	def is_hidden_token(self, attrs):
		if len(attrs) > 2 and attrs[0][1] == 'hidden' and attrs[1][1] == '_token':
			return True
		return False		

if __name__ == '__main__':
	#get login page
	r_login_page = requests.get("http://r.naiveblue.com/index.php/login/index")
	parser = MyHTMLParser()
	parser.feed(r_login_page.content)

	#send login info
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	params = {'username':'13116775341', 'password':'bgscy89622', '_token':parser.token}
	r_login_res = requests.post("http://r.naiveblue.com/index.php/login/Index", headers = headers, data=params)	
	f = open('naive_blue_book_page.html', 'w')
	f.write(r_login_res.content)

	for i in xrange(5):
		print 'parsing r_login_res'

	parser.feed(r_login_res.content)
