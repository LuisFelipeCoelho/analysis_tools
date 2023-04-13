import numpy as np

dx = 0.0000000001
ha = 134*0.05*9 # this is athena highland eq.
error = 1
x = 0.098 # initial value for x etimation
sigma2 = 4 # in acts sigma==2 so sigma2==4

while error > dx:
	h = sigma2*(13.6*np.sqrt(x)*(1+0.038*np.log(x)))**2 # this is acts highland eq.
	error = ha - h # error between athena and acts highland eq.
	print("ha: {}, h: {}, error: {}, x: {}".format(ha, h, error, x))
	x += dx
	if ha < h:
		print("ha < h")
		break
	xFinal = x

print('radLength should be = ' + str(xFinal) + ' for sigma2 = ' + str(sigma2))		
		
# x = 0.09804522341059585 -> sigma**2 = (2)**2 = 4
# x = 0.04643000000000014 -> sigma**2 = (3)**2 = 9
