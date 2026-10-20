from pathlib import Path
def analyze_text(path):
    lines = words = characters = longest = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
            longest = max(longest, len(line.rstrip("\r\n")))
    return {"lines": lines, "words": words, "characters": characters, "longest": longest}


base = Path(__file__).resolve().parent
print(analyze_text(base / "data.txt"))
