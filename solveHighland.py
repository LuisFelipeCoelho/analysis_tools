import numpy as np

dx = 0.00001
ha = 134*0.05*9
error = 1
x = 0.046000000000000006
while error > dx:
	h = 9*(13.6*np.sqrt(x)*(1+0.038*np.log(x)))**2
	error = ha - h
	print("ha: {}, h: {}, error: {}, x: {}".format(ha, h, error, x))
	x += dx
	if ha < h:
		print("ha < h")
		break
		
		
# x = 0.09804522341059585 -> sigma**2 = (2)**2 = 4
# x = 0.04643000000000014 -> sigma**2 = (3)**2 = 9
