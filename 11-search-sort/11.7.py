from functools import cache


def largestPossibleNumber(people):

    @cache
    def largestPossibleNumberFrom(person):
        eligible = [p for p in people if (p[0]<person[0]) and (p[1]<person[1])]
        if not eligible:
            return 1
        return 1 + max(largestPossibleNumberFrom(p) for p in eligible)

    return max(largestPossibleNumberFrom(p) for p in people)


