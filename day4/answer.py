def result1():
    data = []
    for b in open('input.txt'):
        data.append(b)
    drawn_numbers = data[0].split(',')
    print(drawn_numbers)
    bingo_cards = []
    begin = 2
    for i in range(len(data)//6):
        cart = []
        [cart.append(data[i*6+begin+x].split()) for x in range(5)]
        cart.extend(list(map(list, zip(*cart))))
        print(cart)
        bingo_cards.append(cart)
    print(len(bingo_cards))
    for nr in drawn_numbers:
        for cart in bingo_cards:
            for row in cart:
                copy = row.copy()
                [row.remove(x) for x in copy if x==nr]
                if len(row)==0:
                    sum = 0
                    for rows in cart[:5]:
                        for nrs in rows:
                            sum += int(nrs)
                    return int(nr)*sum
    return 0


def result2():
    data = []
    for b in open('input.txt'):
        data.append(b)
    drawn_numbers = data[0].split(',')
    print(drawn_numbers)
    bingo_cards = []
    begin = 2
    for i in range(len(data) // 6):
        cart = []
        [cart.append(data[i * 6 + begin + x].split()) for x in range(5)]
        cart.extend(list(map(list, zip(*cart))))
        print(cart)
        bingo_cards.append(cart)
    print(len(bingo_cards))
    for nr in drawn_numbers:
        for i, cart in enumerate(bingo_cards):
            for row in cart:
                copy = row.copy()
                [row.remove(x) for x in copy if x == nr]
                if len(row) == 0:
                    if len(bingo_cards) == 1:
                        sum = 0
                        for rows in cart[:5]:
                            for nrs in rows:
                                sum += int(nrs)
                        return int(nr) * sum
                    del bingo_cards[i]
                    break
    return 0


def result2_golf():
    print("Nee")


if __name__ == "__main__":
    print(result2())
