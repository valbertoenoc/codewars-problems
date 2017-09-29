def tribonacci(signature, n):
	if n < len(signature):
		return signature[0:n]
	else:
		index = 0
		while len(signature) < n:

			signature.append(sum(signature[index:]))
			index += 1

		return signature


print(tribonacci([1,1,1], 10))