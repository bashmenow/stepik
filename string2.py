s, t = [str(input()) for i in range(2)]
count = 0
while t in s:
    count += 1
    s = s[s.find(t) + 1:]
print(count)