def count_glass (s: str) -> int:
    glass = set("аеиоуыэюяАЕИОУЫЭЮЯ")
    count = 0
    for book in s:
        if book in glass:
            count += 1
    return count