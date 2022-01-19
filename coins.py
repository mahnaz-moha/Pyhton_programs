def ways():
	t = 200
	r_ways = [1] + [0] * t
	for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
		for i in range(len(r_ways) - coin):
			r_ways[i + coin] += r_ways[i]
	return str(r_ways[-1])

print(ways())