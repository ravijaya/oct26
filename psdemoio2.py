"""demo for the IO"""
import sys
import traceback

try:
    name = input('enter the name :')
    city = input('enter the city :')
    zip_code = int(input('enter the postal code :'))

    print('name :', name)
    print('city :', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as error:
    print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
    print(error)

print('next statement after try except block')
