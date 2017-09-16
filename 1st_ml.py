import numpy as np

def nonlin(x, deriv=False):
	if deriv == True:
		return x*(x-1)
	return 1/(1+np.exp(-x))

#input data
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])

y = np.array([[0],[1],[1],[0]])

np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3, 4)) -1
syn1 = 2*np.random.random((4, 4)) -1	

#training set
for i in xrange(60000):
	l0 = x
	dd = np.dot(l0, syn0)
	print "dd : ", dd
	l1 = nonlin(dd)
	l2 = nonlin(np.dot(l1, syn1))

	l2_error = y - l2
	if i % 10000 == 0:
		print "Error : ", str(np.mean(np.abs(l2_error)))

	l2_delta = l2_error*nonlin(l2, deriv = True)
	l1_error = l2_delta.dot(syn1.T)

	l1_delta = l1_error*nonlin(l1, deriv=True)

	syn1 += l1.T.dot(l2_delta)
	syn1 += l0.T.dot(l1_delta)
print "output after training"
print l2
