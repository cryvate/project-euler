import os

numbers = []

for filename in os.listdir(os.path.split(__file__)[0]):
    if filename.endswith(".py") and filename.startswith("problem_"):
        problem_number = int(filename[8:-3])
        numbers.append(problem_number)

numbers = sorted(numbers)
slow_numbers = {
    '1': 0.03
    # due to Travis being slower than most machines.
    # will give warnings if more time used, but won't fail
}
