from fastapi import APIRouter

router = APIRouter()


@router.get("/prime-numbers")
async def do_maths(from_number: int, to_number:int):
    return count_primes_in_range(from_number, to_number)


def count_primes_in_range(start, end):
    return sum(is_prime(n) for n in range(start, end))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True