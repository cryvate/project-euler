import os

numbers = []

for filename in os.listdir(os.path.split(__file__)[0]):
    if filename.endswith(".py") and filename.startswith("problem_"):
        problem_number = int(filename[8:-3])
        numbers.append(problem_number)