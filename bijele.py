p = [1,1,2,2,2,8]
c = list(map(int, input().split()))
r = [0,0,0,0,0,0]
i = 0
while i<len(p):
  r[i] = p[i] - c[i]
  i = i + 1

j = 0
answer = ""
while j < len(r):
  answer = answer + " " + str(r[j])
  j = j + 1
print(answer)
