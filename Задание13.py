tic_num = 1

while True:
    ticket = input()

    if len(ticket) % 2 == 0:
        half = len(ticket) // 2
        first_half = ticket[:half]
        second_half = ticket[half:]

        first_sum = 0
        for number in first_half:
            first_sum += int(number)

        second_sum = 0
        for number in second_half:
            second_sum += int(number)

        if first_sum == second_sum:
            print(tic_num)
            break

    tic_num += 1
