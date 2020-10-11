import sys

params = sys.argv[1:]
if "help" in params or "Help" in params or "h" in params:
    print("Ввдите посдедовательно, наработку в часай, часовую ставку, размер премии, через запятую")
else:
    prize = float(params[2]) / 100
    salary = prize + (float(params[0]) * float(params[1]))
    print(salary)

