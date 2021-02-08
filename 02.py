def compute():
	ans = 0
	x = 1
	y = 2
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)
