import random

def play_slot_machine():
    symbols = ['🍒', '🍋', '🔔', '⭐', '7️⃣']
    result = [random.choice(symbols) for _ in range(3)]
    win = result[0] == result[1] == result[2]
    return result, win
