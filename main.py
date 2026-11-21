from pathlib import Path

VERSES = [
    "At six I asked my mother at the door",
    "if I might cross the road alone. She weighed me,",
    "nodded — and the world widened by one yes.",
    "",
    "Now children stand at my gate and ask: May I?",
    "I hand the word out slowly, like a key —",
    "the same key, once handed to me.",
]

DESTINATION = Path("/output") / "entry.txt"


def render() -> str:
    return "\n".join(VERSES)


def emit() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    emit()
