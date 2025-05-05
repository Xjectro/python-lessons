# | is or operator


def day_of_week(day):
    match day:
        case 1 | "sunday":
            return "It is sunday"
        case 2 | "monday":
            return "It is monday"
        case 3 | "tuesday":
            return "It is tuesday"
        case 4 | "wednesday":
            return "It is wednesday"
        case 5 | "thursday":
            return "It is thursday"
        case 6 | "friday":
            return "It is friday"
        case 7 | "saturday":
            return "It is saturday"
        case _:
            return "Invalid day"


print(day_of_week(1))
