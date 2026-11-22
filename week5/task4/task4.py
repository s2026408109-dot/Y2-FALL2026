raw_temps = [22.5, "ERR", 18.0, None, 30.2, "ERR", 0.0]
result = [round(t * 1.8 + 32, 1) for t in raw_temps if isinstance(t, (int, float)) and not isinstance(t, bool)]
print(result)
