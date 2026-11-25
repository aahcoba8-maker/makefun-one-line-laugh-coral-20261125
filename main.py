"""One Line, One Laugh — a single funny line for make.fun.

The entry is one joke: the asker begs their AI for a joke, and the AI
answers with a one-word roast of the asker. The turn is the joke.
"""

import os

TEXT = 'I asked my AI for a joke. It said: "You."'


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
