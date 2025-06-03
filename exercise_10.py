fruit_count = {}

while True:
    fruit = input("Enter a fruit (type 'exit' to stop): ").lower()
    if fruit == 'exit':
        break
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

print("\nFinal counts:")
for fruit, count in fruit_count.items():
    print(f"{fruit} is {count}")