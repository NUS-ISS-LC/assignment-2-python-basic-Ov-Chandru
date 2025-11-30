def find(s, n):
# write your implementation here
    lens=len(s)
    print(lens)
    for i in range(lens):
        for j in range(lens-1-i):
            if s[i] + s[j+1+i] == n:
                a= i
                b= j+1+i
    return a, b

s=[2,7,9,15]
print(find(s,9))
