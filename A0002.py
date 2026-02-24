yil = int(input())
if (yil % 400 == 0) or (yil % 4 == 0 and yil % 100 != 0):
    print(f"12.09.{yil}")
else:
    print(f"13.09.{yil}")