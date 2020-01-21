N, U, D = [int(x) for x in input().split() ]
balls = [int(x) for x in input().split()]
spec_choice = 1
selected = balls[0]

for i in range(1, len(balls)):
    if selected == balls[i]:
        selected = balls[i]

    elif spec_choice == 1 and balls[i] < selected and abs(selected - balls[i]) >= D:
        selected = balls[i]
        spec_choice = 0

    elif balls[i] > selected and abs(balls[i] - selected) <= U and abs(balls[i] - selected) >= D:
        selected = balls[i]

print(balls.index(selected))

