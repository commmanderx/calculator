def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Amaliatni tanlang.")
print("1.Qushish")
print("2.Ajratish")
print("3.Ko'paytirish")
print("4.Divide")
while True:
    
    choice = input("Raqamni tanlang(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("raqamni kiriting: "))
        num2 = float(input("Ikkinchi raqamni kiring: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Keyingi  hisobmi qilamizmi? (haa/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
