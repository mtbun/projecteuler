def compute():
	s = "".join(str(i) for i in range(1, 1000000))
	ans = 1
	for i in range(7):
		ans *= int(s[10**i - 1])
	return str(ans)
