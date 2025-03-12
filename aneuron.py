j = [1, 2, 3] # input
w = [2, 3, 4] # weight
b = 1

def cni(j, w, b): # cni stands for compute_neuron_input
	j_with_bias = [1] + j.copy()
	w_with_bias = [b] + w.copy()

	jblen = len(j_with_bias)
	wblen = len(w_with_bias)

	acc = 0

	if (jblen != wblen):
		return "Vector j and w should have same length"

	for i in range(jblen):
		acc = acc + (j_with_bias[i] * w_with_bias[i])

	return acc

print(cni(j, w, b))
