def collatzchain_len(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return collatzchain_len(y) + 1

# for i in range(2,1000000):
#     liste = []
#     liste.append(collatzchain_len(i))

# print(max(liste))

ans = max(range(1, 1000000), key=collatzchain_len)
print(ans)