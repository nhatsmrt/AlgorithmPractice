from typing import List


def get_key(word):
    class Key:
        def __init__(self):
            self.word = word

        def __eq__(self, other):
            return self.word + other.word == other.word + self.word

        def __lt__(self, other):
            return self.word + other.word < other.word + self.word

        def __gt__(self, other):
            return self.word + other.word > other.word + self.word

    return Key()



def smallest_concat(words: List[str]) -> str:
    # Time Complexity: O(LN log N)
    return "".join(sorted(words, key=get_key))



if __name__ == "__main__":
    with open("studious_student_input.txt", "r") as f:
        inputs = list(map(lambda line: line.split(" ")[1:], f.read().splitlines()))[1:]

    outputs = list(map(lambda pair: "Case #{}: {}".format(pair[0], pair[1]), zip(range(1, len(inputs) + 1), map(smallest_concat, inputs))))
    with open("studious_student_output.txt", "w") as f:
        f.write("\n".join(outputs))
