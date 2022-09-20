import main
main.add(20, 40)
main.sub(10, 5)
print(main.it)
#############

from main import add, sub, it

add(10, 100)
sub(10, 1)
print(it)

######################

from main import *

add(10, 40)
print(it)
sub(10, 20)
students("Sardor", "Kurmanbek", "Adilet")