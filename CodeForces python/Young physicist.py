n=int(input())
sx = sy = sz = 0
for i in range(n):
    x,y,z = [int(v) for v in input().split()]
    sx += x
    sy += y
    sz += z
    
if sx == sy == sz == 0:
    print("YES")
else:
    print('NO')
