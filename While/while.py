Packages = 0
Customers = 0
while(Packages <= 3):
    Packages = Packages + 1
else:
    # как только значение Packages станет равным 3, мы отобрази это в окне вывода
    print("На складе 3 коробки ")

while True:
    Customers = Customers + 1
    if Customers == 5:
        print("В зале 5 покупателей ")
        break
