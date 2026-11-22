tasks = ["done", "pending", "done", "pending", "done", "pending"]
tasks[1::2] = ["completed"] * len(tasks[1::2])
tasks[3:3] = ["audit"]
print(tasks)