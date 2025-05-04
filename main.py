from file_manager import file_reader, write_file

a = input("Enter num A: ")
b = input("Enter num B: ")
c = input("What do you want to do with them(*,+,-,/): ")
if c == "*":
    result = a * b
elif c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "/":
    if b == 0:
        print("0 ga bo'lish mumkin emas.")
        exit()
    result = a / b
else:
    print("Notanish amal.")
    exit()

print(f"Natija: {result}")
