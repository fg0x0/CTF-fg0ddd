#!/usr/bin/env python


from md5 import md5

i = 0 
while ( True ):
	plaintext = '0e%d' % i
	m = md5()
	m.update(plaintext)
	h = m.hexdigest()

	if h.startswith('0e'):
		if h[2:].isdigit():
			print plaintext, h
			break

	print plaintext, h

	i += 1

	#866437cb7a794bce2b727acc0362ee27 
