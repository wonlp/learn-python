# See PyCharm help at https://www.jetbrains.com/help/pycharm/
x=100
def func():
    x=1000
    def func2():
        global x
        x=2000
    func2()
    print(x)
print(x)




