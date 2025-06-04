pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = int(pool/quantity)
except :
    print('Divide by zero completed!')
    chunk = 1

print(f'Each mailing will have {chunk} items.')