players = [("Aria", 88, True), ("Kael", 95, False), ("Zane", 91, True), ("Mira", 76, True), ("Lyra", 99, True), ("Dax", 84, True)]
top3 = sorted([p for p in players if p[2]], key=lambda p: p[1], reverse=True)[:3]
result = [f"Rank {i + 1}: {name} ({score})" for i, (name, score, _) in enumerate(top3)]
print(result)