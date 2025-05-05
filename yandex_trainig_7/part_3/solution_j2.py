"""LZW Wikipedia style"""

ALPHABET = "#abcdefghjiklmnopqrstuvwxyz"


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
        self.cached -=  width
        return value


def pack(text: str) -> list[int]:
    
    buffer = OutBitStream()    
    vocab = {letter: i for i, letter in enumerate(ALPHABET)}

    first = 0
    for last in range(len(text)):
        key = text[first:last + 1]
        if key in vocab:
            continue
        prev_index = vocab[key[:-1]]
        buffer.push(prev_index, len(vocab).bit_length())
        vocab[key] = len(vocab)
        first = last
    if first < len(text):
        prev_index = vocab[text[first:]]
        buffer.push(prev_index, len(vocab).bit_length())
    buffer.flush()

    return buffer.bytes


def unpack(bytes: list[int]) -> str:
    text: list[str] = []
    vocab = list(ALPHABET)

    buffer = InBitStream(bytes)
    while (key := buffer.pull((len(vocab) + 1).bit_length())) is not None:
        if key < len(vocab):
            if text:
                vocab.append(text[-1] + vocab[key][:1])
            text.append(vocab[key])
        else:
            v = text[-1] + text[-1][:1]
            vocab.append(v)
            text.append(v)

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
        assert len(bytes) == n, f"Expected {n} bytes, got {len(bytes)}"
        print(unpack(bytes), flush=True)
