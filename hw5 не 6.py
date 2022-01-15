while True:
    from time import sleep
    def dislike_6(a):
        if a == 6:
            print("О нееееет, только не 6")
        elif type(a)==float or type(a) is int:
            return True
    a = int(input("Введите число: "))  
    print(dislike_6(a))
    sleep(10)
