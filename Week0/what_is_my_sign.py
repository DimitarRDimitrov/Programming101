def what_is_my_sign(date, month):
    if month == 1:
        if date > 20:
            return "Aquarius"
        else:
            return "Capricorn"
    elif month == 2:
        if date > 19:
            return "Pisces"
        else:
            return "Aquarius"
    elif month == 3:
        if date > 20:
            return "Aries"
        else:
            return "Pisces"
    elif month == 4:
        if date > 20:
            return "Taurus"
        else:
            return "Aries" 
    elif month == 5:
        if date > 21:
            return "Gemini"
        else:
            return "Taurus"
    elif month == 6:
        if date > 22:
            return "Cancer"
        else:
            return "Gemini"
    elif month == 7:
        if date > 22:
            return "Leo"
        else:
            return "Cancer"
    elif month == 8:
        if date > 22:
            return "Virgo"
        else:
            return "Leo"
    elif month == 9:
        if date > 23:
            return "Libra"
        else:
            return "Virgo"
    elif month == 10:
        if date > 23:
            return "Scorpio"
        else:
            return "Libra"
    elif month == 11:
        if date > 22:
            return "Sagittarius"
        else:
            return "Scorpio"
    elif month == 12:
        if date > 21:
            return "Capricorn"
        else:
            return "Sagittarius"

print(what_is_my_sign(28, 1))
print(what_is_my_sign(8, 5))
