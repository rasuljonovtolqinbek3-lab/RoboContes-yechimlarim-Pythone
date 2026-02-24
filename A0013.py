n=int(input())
s=n//3600
m=(n%3600)//60
sk=n%60
print(f"{s%24}:{m:02}:{sk:02}")