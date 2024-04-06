from random import randint as rand


class roller:
    def __init__(self, count, sides, rolls):
        self._sides = sides
        self._count = count
        self._rolls = rolls
        self._hands = []
        self.hands = []

    def roll_sim(self):
        self._hands
        roll = [0] * self._count

        def hand_convert(hand_dict: dict):
            hand = ""
            for key in hand_dict.keys():
                hand += str(key) * hand_dict.get(key)

            return hand

        for i in range(self._rolls):
            for j in range(self._count):
                roll[j] = rand(1, self._sides)
            roll.sort()
            roll_count = {i: roll.count(i) for i in roll}
            roll_count_sort = list(roll_count.values())
            roll_count_sort.sort()
            self._hands.append(
                hand_convert({i: roll_count_sort.count(i) for i in roll_count_sort})
            )

        self._hands.sort()
        self._hands = {hand: self._hands.count(hand) for hand in self._hands}
        self.hands = [[hand, self._hands.get(hand)] for hand in self._hands.keys()]
        self.hands.sort(key=lambda hand: hand[1], reverse=True)
        return

    def print_hands(self):
        for hand in self.hands:
            print(
                str(hand[0])
                + ": "
                + str(hand[1])
                + " -- "
                + "{0:2.2f}%".format((hand[1] / self._rolls) * 100)
            )
        return
