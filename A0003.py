sonlar = list(map(int, input().split()))
print( f"{sum(sonlar) - max(sonlar)} {sum(sonlar) - min(sonlar)}")

