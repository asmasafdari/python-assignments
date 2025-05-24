class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total instances created: {cls.count}")

if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    Counter.show_count()  # Output: Total instances created: 3