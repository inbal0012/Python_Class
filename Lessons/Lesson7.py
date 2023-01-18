class Lesson7:
    # Loops
    @staticmethod
    def string_match(a, b):
        count = 0
        length = min(len(a), len(b))-1
        for i in range(length):
            if a[i] == b[i] and a[i+1] == b[i+1]:
                count += 1
        return count

    @staticmethod
    def test_string_match():
        print(f"'xxcaazz', 'xxbaaz' -> exp: 3, result: {Lesson7.string_match('xxcaazz', 'xxbaaz')}")
        print(f"'abc', 'abc' -> exp: 2, result: {Lesson7.string_match('abc', 'abc')}")
        print(f"'abc', 'axc' -> exp: 0, result: {Lesson7.string_match('abc', 'axc')}")

