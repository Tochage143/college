import threading


def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")


def check_prime(number):
    if number <= 1:
        print(f"{number} is Not Prime")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is Not Prime")
            return
    print(f"{number} is Prime")



number = 29


thread1 = threading.Thread(target=check_even_odd, args=(number,))
thread2 = threading.Thread(target=check_prime, args=(number,))


thread1.start()
thread2.start()


thread1.join()
thread2.join()
