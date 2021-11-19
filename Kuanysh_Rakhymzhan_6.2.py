res = []
d = dict()
with open('ngins_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        ip = ln[0]
        res.append((ip, ln[5].strip('"'), ln[6]))
        if ip not in d:
            d[ip] = 1
        else:
            d[ip] += 1
print(res)

m = 0
k = ''
for key, value in d.items():
    if value > m:
        m = value
        k = key
print(k, m)
