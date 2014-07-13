m = 134456
n = 8121
k = 28411
idum = 1000
nums = dict(zip(range(m),[0 for x in range(m)]) )

counter = 0
for iteration in range(int(2e5)):
	idum = (idum*n + k)%m
	ran = idum / float(m)
	nums[idum] += 1
	if counter < m:
		print idum, ran, iteration
		counter = m
	if counter == m and nums[idum] > 1:
		print 'Sequence repeat?'
		print idum, ran, iteration
		counter += m


