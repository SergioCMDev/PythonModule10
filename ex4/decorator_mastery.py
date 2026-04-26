from collections.abc import Callable
from functools import wraps
import time
from typing import Any
import random


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def execute_function() -> Callable:
        start: float = time.time()
        print(f"Casting {func.__name__}...")
        result = func()
        end: float = time.time()
        length: float = end - start
        print(f"Spell completed in {length:.3f} seconds")
        return result

    return execute_function


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(
                spell_name: str,
                power: int,
                *args: Any,
                **kwargs: Any) -> str | Any:
            if (power >= min_power):
                return func(spell_name, power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    attempt: int = 0

    def decorator(func: Callable) -> str | Any:
        nonlocal attempt
        if (attempt < max_attempts):
            try:
                return func()
            except Exception:
                attempt += 1
                print(f"Spell failed, retrying...("
                      f"attempt {attempt}/{max_attempts})")
                return decorator(func)
        else:
            return "Spell casting failed after max_attempts attempts"
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        size: int = len(name)
        letter_spaces: bool = all(letter == ' ' or letter.isalpha()
                                  for letter in name)
        return letter_spaces and size >= 3

    def cast_spell(self, spell_name: str, power: int) -> str:
        validator = power_validator(10)
        created_spell_funct = validator(spell_casted_right)
        res = created_spell_funct(spell_name, power)
        return res


def hello() -> str:
    print("We are executing Hello")
    time.sleep(0.59876)
    return ("Hello")


def hello_2(spell_name: str, power: int) -> str:
    print(f"We are executing {spell_name} with {power}")
    return ("Hello")


def raiserExcept() -> str:
    seed: int = random.randint(1, 100)
    if (seed < 30):
        return "Everything OK"
    else:
        raise Exception


def spell_casted_right(spell_name: str, power: int) -> str:
    return f"Successfully cast '{spell_name}' with '{power}' power"


def main() -> None:
    print("Testing spell timer")
    timed_hello = spell_timer(hello)
    res = timed_hello()
    print(f"Result: {res}")
    print()
    print("Testing power_validator")
    validator = power_validator(20)
    right_spell = validator(hello_2)
    res = right_spell("Hello", 30)
    print(res)
    res = right_spell("Hello", 10)
    print(res)

    print()

    print("Testing retry spell")
    retrier = retry_spell(3)
    res = retrier(raiserExcept)
    print(res)
    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name(" a "))
    print(MageGuild.validate_mage_name(" a"))

    mageGuild = MageGuild()
    print(mageGuild.cast_spell("pepito", 10))
    print(mageGuild.cast_spell("fire", 5))


if __name__ == "__main__":
    main()
