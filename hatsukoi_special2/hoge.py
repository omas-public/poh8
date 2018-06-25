from collections import Counter

s = 'pizzahgoehgogheo'
t = 'paizabhgoejhoge'
sdic = Counter(s)
tdic = Counter(t)
print(sum(dict((tdic - sdic)).values()))
