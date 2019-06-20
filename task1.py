number = int(input())
runners = list(map(int, input().split()))

runner_up = max(list(filter(lambda a: a != max(runners), runners)))

print(runner_up)
