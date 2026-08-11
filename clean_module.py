"""A clean module used to verify that ruff and bandit checks pass."""

import hashlib
import json


def load_config(path: str) -> dict:
    """Load a JSON config file from disk."""
    with open(path, encoding="utf-8") as config_file:
        return json.load(config_file)


def hash_value(value: str) -> str:
    """Return a SHA-256 hash of the given string."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    result = add(2, 3)
    print(f"2 + 3 = {result}")
    print(f"Hash of 'hello' = {hash_value('hello')}")


if __name__ == "__main__":
    main()
