from typing import Any, Optional, Tuple


def optionals_to_int(*bools: Tuple[Optional[Any]]) -> int:
    sum = 0
    for i in bools:
        sum += 1 if i else 0
    return sum
