# calories

def daily_calories(weight: float, height: int, age: int) -> int:
    return int(10 * weight + 6.25 * height + 5 * age - 161)
