firist_name="hello"
last_name="worled"
n=12.5
x=True
if x==True:
    print(firist_name+" "+last_name+" age= "+str(n))
else:
    print("moheb")

print(n)  
print(int(n))
print(n)
print(n**int(n))
print(n-int(n))
print(str(max(n,int(n)))+" "+str(min(n,int(n))))
print(n//2)
print(n%2)

name=input("what is your name: ")
print("Hello "+name)

print("my name\'mahmoud",end=" ")
print("Ahmad'\t\toooooooo\noo\fooo")
print("""mmmmmmmmmmmmm
      mmmmmmmmmmmmmmmmm
      aaaaaaaaaaaaaaaaa
      aaaaaaaaaaaaaaaaa""")

p="mahmoud moheb" #space=1=char
print(len(p))
print(type(p))

print(p.upper())
print(p.capitalize())
print(p.find(" "))

name=p[0:7]
print(name)
name=p[0:]
print(name)

n=-3.6
print(abs(n))
print(round(n))
n=-3.2
print(round(n))

print(sum([1,2,3,4,5,6,7,8,9]))
num=[1, 2, 3, 6, 4 ,5, 8, 45 ,87]
print(max(num),min(num))
x=27
c=4
if x%c>0:
    print(c%x)
elif c%x>0:
    print(1)
for x in range(12,100,1):
    print(str(x)+'- '+"Hello")

name="mahmoud"
for n in name:
    print(n)

fro=["nm","bm","vn","zm"]
for z in fro:
    print(z)
x=10
while 2<x :
    x-=1
    print(x)


n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                if a[k] == a[j] + a[i]:
                    print(k + 1, j + 1, i + 1)
                    exit()

print(-1)

n = int(input("Enter +ve int: "))
sum = 0
for i in range (1, n + 1):
    sum = sum + i
print (sum)

l=['1','2','3','4','5']
print (l)
for i in range(len(l)):
    l[i]=int(l[i])

print(l)


def name (c,v):
    print(c+v)


































































































































































































































