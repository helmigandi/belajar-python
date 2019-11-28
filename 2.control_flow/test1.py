# file two.py
import test

print("top-level in two.py")
test.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")