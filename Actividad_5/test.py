import numpy as np
def test1(*args):
	try:
		assert np.abs(integral_riemann(*args)-0.746824132812427)<1e-6
		print("Resultado Correcto")
	except:
		print("Resultado Incorrecto")
def test2(*args):
	try:
		assert np.abs(integral_trapecio(*args)-0.746824132812427)<1e-6
		print("Resultado Correcto")
	except:
		print("Resultado Incorrecto")
