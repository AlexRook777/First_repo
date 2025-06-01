import random
message = "Hello world!"
i = random.randint(0, 10)
y = random.randint(i, len(message))
print(message)
print(f"i: {i}, y: {y}")
print(message[i:y])