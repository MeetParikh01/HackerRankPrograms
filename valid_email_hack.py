import re 

def fun(s):
	valid_email = re.match(r'[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}',s)
	return True if valid_email else False

def filter_mail(emails):
	return list(filter(fun,emails))

if __name__ == '__main__':
	num_emails = int(input('Enter total Num of emails  to enter(int):'))
	emails=[input('Enter email address:') for email in range(0,num_emails)]
	print(sorted(filter_mail(emails)))
