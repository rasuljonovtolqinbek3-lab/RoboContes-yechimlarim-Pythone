a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
k,s=a*3600+b*60+c,x*3600+y*60+z
print(max(k,s)-min(k,s))