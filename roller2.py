from random import randint
from collections import Counter


class roller2:
    def __init__(self, count, sides, rolls):
        self._sides = sides
        self._count = count
        self._rolls = rolls
        self._hands = Counter()
        self.hands = []

    def roll_sim(self):
        for _ in range(self._rolls):
            roll = [randint(1, self._sides) for _ in range(self._count)]
            roll_counter = Counter(roll)

            straight_length = 0
            max_straight_length = 0
            for i in range(1, self._sides + 1):
                if roll_counter[i]:
                    straight_length += 1

                    if straight_length >= 4:
                        max_straight_length = straight_length
                else:
                    straight_length = 0

            hand_counts = Counter(roll_counter.values())
            # if 1 in hand_counts:
            #     del hand_counts[1]

            hand = ""

            hand += " ".join(
                f"{k}" * v for k, v in sorted(hand_counts.items(), reverse=True)
            )

            # if max_straight_length == 0:
            #     hand = "".join(char for char in hand if char != "1")
            # elif max_straight_length >= 4:
            #     hand = "".join(
            #         char for char in hand if char >= str(max_straight_length - 1)
            #     )

            if max_straight_length >= 4:
                hand = f"{max_straight_length}-Straight " + hand

            self._hands[hand] += 1

        self.hands = [[hand, count] for hand, count in self._hands.most_common()]
