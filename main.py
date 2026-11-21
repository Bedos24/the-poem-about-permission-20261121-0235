import os

POEM = """At six I asked my mother at the door
if I might cross the road alone. She weighed me,
nodded — and the world widened by one yes.

Now children stand at my gate and ask: May I?
I hand the word out slowly, like a key —
the same key, once handed to me."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
