if __name__ == "__main__":
    n = int(input("Число напиши: "))
    a = 1
    while a < n:
        a = a * 2
    if a == n:
        print("YES")
    else:
        print("NO")
