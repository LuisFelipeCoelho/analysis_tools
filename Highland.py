import numpy as np

def highlandMagicConstant(x, sigma):
	h = (sigma*13.6*np.sqrt(x)*(1+0.038*np.log(x)))**2
	print(str((13.6*(1+0.038*np.log(x)))**2) + ' * ' + str(x) + ' * ' + str(sigma**2))
	print(str(x*13.6**2) + ' * ' + str((1+0.038*np.log(x))**2) + ' * ' + str(sigma**2))
	print(str((13.6*sigma)**2) + ' * ' + str(x) + ' * ' + str((1+0.038*np.log(x))**2))
	print(h)
	print(134*0.05*9)
	return h


x = 0.025
sigma = 3
highlandMagicConstant(x, sigma)

# x = 0.09804522341059585 -> sigma**2 = (2)**2 = 4
# x = 0.04643000000000014 -> sigma**2 = (3)**2 = 9
