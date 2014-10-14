def what_is_my_sign(day, month):
    if not correct_date(day, month):
        return "There isn't such an animal!"
    else:
        sign = {1: ("Capricorn", "Aquarius", 21),
                2: ("Aquarius", "Pisces", 20),
                3: ("Pisces", "Aries", 21),
                4: ("Aries", "Taurus", 21),
                5: ("Taurus", "Gemini", 22),
                6: ("Gemini", "Cancer", 22),
                7: ("Cancer", "Leo", 23),
                8: ("Leo", "Virgo", 23),
                9: ("Virgo", "Libra", 24),
                10: ("Libra", "Scorpio", 24),
                11: ("Scorpio", "Sagittarius", 23),
                12: ("Sagittarius", "Capricorn", 22)}
        if day < sign[month][2]:
            return sign[month][0]
        else:
            return sign[month][1]


def correct_date(day, month):
    if (month == 1 and day > 0 and day < 32 or
        month == 2 and day > 0 and day < 30 or
        month == 3 and day > 0 and day < 32 or
        month == 4 and day > 0 and day < 31 or
        month == 5 and day > 0 and day < 32 or
        month == 6 and day > 0 and day < 31 or
        month == 7 and day > 0 and day < 32 or
        month == 8 and day > 0 and day < 32 or
        month == 9 and day > 0 and day < 31 or
        month == 10 and day > 0 and day < 32 or
        month == 11 and day > 0 and day < 31 or
            month == 12 and day > 0 and day < 32):
        return True
    return False


def main():
    print("should be \"Leo\": %s" % what_is_my_sign(5, 8))
    print("should be \"Aquarius\": %s" % what_is_my_sign(29, 1))
    print("should be \"Cancer\": %s" % what_is_my_sign(30, 6))
    print("should be \"Gemini\": %s" % what_is_my_sign(31, 5))
    print("should be \"Aquarius\": %s" % what_is_my_sign(2, 2))
    print("should be \"Taurus\": %s" % what_is_my_sign(8, 5))
    print("should be \"Capricorn\": %s" % what_is_my_sign(9, 1))

if __name__ == '__main__':
    main()
