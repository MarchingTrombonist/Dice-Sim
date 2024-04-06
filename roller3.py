from random import randint
from collections import Counter


class roller3:
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

            straight = 0
            for i in range(1, self._sides + 1):
                if roll_counter[i]:
                    straight += 1

                    # poker hands
                    if straight >= 5:
                        straight = True
                        break
                else:
                    straight = False

            hand_counts = Counter(roll_counter.values())

            hand = ""

            hand += "".join(
                f"{k}" * v for k, v in sorted(hand_counts.items(), reverse=True)
            )

            # poker hands
            if hand[0] >= 5:
                hand = "5"

            elif "4" in hand:
                hand = "4"

            elif "32" in hand:
                hand = "32"

            elif straight:
                hand = "Straight"

            elif "3" in hand:
                hand = "3"

            elif "22" in hand:
                hand = "22"

            elif "2" in hand:
                hand = "2"

            else:
                hand = "High"

            self._hands[hand] += 1

        self.hands = [[hand, count] for hand, count in self._hands.most_common()]
