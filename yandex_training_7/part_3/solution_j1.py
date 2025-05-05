"""LZW Yandex Training style"""

LETTER_WIDTH = 5


class OutBitStream:
    WORD = 8
    WORD_MASK = (1 << WORD) - 1

    def __init__(self):
        self.bytes = []
        self.cache = 0
        self.cached = 0

    def push(self, value: int, width: int):
        self.cache |= value << self.cached
        self.cached += width
        self.flush(False)

    def flush(self, total=True):
        while self.cached >= self.WORD:
            self.bytes.append(self.cache & self.WORD_MASK)
            self.cache >>= self.WORD
            self.cached -= self.WORD
        if self.cached and total:
            self.bytes.append(self.cache)
            self.cache = 0
            self.cached = 0


class InBitStream:
    WORD = 8

    def __init__(self, data: list[int]):
        self.bytes = data
        self.pointer = 0
        self.cache = 0
        self.cached = 0

    def pull(self, width) -> int | None:
        while self.cached < width and self.pointer < len(self.bytes):
            self.cache |= self.bytes[self.pointer] << self.cached
            self.cached += self.WORD
            self.pointer += 1
        if self.cached < width:
            return None
        value = self.cache & ((1 << width) - 1)
        self.cache >>= width
        self.cached -= width
        return value


def pack(text: str) -> list[int]:
    buffer = OutBitStream()

    vocab: dict[str, int] = {"": 0}
    first = 0
    for last in range(len(text)):
        key = text[first:last + 1]
        if key in vocab:
            continue
        prev_index = vocab[key[:-1]]
        letter = ord(text[last]) - ord('a')
        buffer.push(letter, LETTER_WIDTH)
        buffer.push(prev_index, len(vocab).bit_length())
        vocab[key] = len(vocab)
        first = last + 1
    if first < len(text):
        buffer.push(ord(text[-1]) - ord('a'), LETTER_WIDTH)
        buffer.push(vocab[text[first:-1]], len(vocab).bit_length())
    buffer.flush()
    return buffer.bytes


def unpack(bytes: list[int]) -> str:
    buffer = InBitStream(bytes)

    text: list[str] = []
    vocab: list[str] = [""]

    while (letter := buffer.pull(LETTER_WIDTH)) is not None:
        prev_index = buffer.pull(len(vocab).bit_length())
        if prev_index is None:
            break
        fragment = f"{vocab[prev_index]}{chr(letter + ord('a'))}"
        text.append(fragment)
        vocab.append(fragment)

    return "".join(text)


if __name__ == "__main__":
    mode = input()
    if mode == "pack":
        text = input()
        bytes = pack(text)
        print(len(bytes))
        print(" ".join(map(str, bytes)), flush=True)
    elif mode == "unpack":
        n = int(input())
        bytes = list(map(int, input().split()))
        print(unpack(bytes), flush=True)
