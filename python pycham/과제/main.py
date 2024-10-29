# main.py
from animals import Dog, Eagle

def main():
    dog = Dog("Buddy", "Golden Retriever")
    eagle = Eagle("Eagle Eye", 2.3)

    print(dog.info())
    print(eagle.info())

if __name__ == "__main__":
    main()
