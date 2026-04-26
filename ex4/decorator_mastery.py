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
        def wrapper(power: int,  *args: Any, **kwargs: Any) -> Callable:
            if (power >= min_power):
                print("OK")
                return func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    attempt: int = 0

    def decorator(func: Callable) -> Callable:
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
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def hello() -> str:
    print("We are executing Hello")
    return ("Hello")


def hello_2(power: int) -> str:
    print(f"We are executing Hello with {power}")
    return ("Hello")


def raiserExcept() -> str:
    seed: int = random.randint(1, 100)
    if (seed < 30):
        return "Everything OK"
    else:
        raise Exception


def main() -> None:
    print("Testing spell timer")
    timed_hello = spell_timer(hello)
    res = timed_hello()
    print(res)
    print()
    print("Testing power_validator")
    validator = power_validator(20)
    right_spell = validator(hello_2)
    right_spell(30)
    print("Testing retry spell")
    retrier = retry_spell(3)
    res = retrier(raiserExcept)
    print(res)


if __name__ == "__main__":
    main()
