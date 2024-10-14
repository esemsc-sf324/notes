import sys

print(f"Number of arguments: {len(sys.argv)}")
print(f"All the arguments: {sys.argv}")
print(f"Script name: {sys.argv[0]}")

try:
    print(f"First argument: {sys.argv[1]}")
except IndexError:
    print("No arguments provided")
    exit()

try:
    print(f"Second argument: {sys.argv[2]}")
except IndexError:
    print("No second argument provided")
    exit()
