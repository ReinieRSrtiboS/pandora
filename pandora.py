

atoms = ["he", "li", "be", "ne", "na", "mg", "al", "si", "cl", "ar", "ca", "sc", "ti", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "zr", "nb"
, "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "xe", "ce", "ba", "la", "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "re", "os", "ir", "pt",
         "au", "hg", "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "np", "pu", "am", "cm", "bk", "cf", "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc"
         , "lv", "ts", "og", "b", "c", "n", "o", "f", "h", "p", "s", "k", "v", "y", "i", "w", "u"]

tekst = "once upon a time there was a doctor her name was margaret and the last name resembled " \
        "german death that day was a sunday and she didn't have to go to work so she decided to " \
        "continue writing her first yet to be published book it's title was something about " \
        "escaping and it began with such words it was a bitter december night but the paris-lyon " \
        "express was speeding gaily along in search of the flowers and the sunshine after some time " \
        "passed she decided to go out she was surprised to meet an old family friend of hers " \
        "they talked for a while and exchanged some ideas frederick had discovered something but was " \
        "unsure how to name it and margaret helped him he normally was a very stable man and did not" \
        " break down but it was visible that he really liked the name" \
        "after this encounter margaret decided to call it a day"

# tekst = "hello"
# tekst = "listen carefully"
# tekst = "so i will tell you a short story with hidden meaning"

def switch_iso(atom):
    switcher = {
        "h": 2,
        "he": 2,
        "li": 2,
        "be": 1,
               "b": 2,
               "c": 2,
               "n": 2,
               "o": 3,
                "f": 1,
               "ne": 3,
               "na": 1,
               "mg": 3,
                "al": 1,
        "si":3,
        "p":1,
        "s": 4,
        "cl":2,
        "ar":3,
               "k":2 ,
               "ca":5,
               "sc":1,
               "ti":5,
               "v":1,
               "cr":4,
               "mn":1,
               "fe":4,
               "co":1,
               "ni":5,
               "cu":2,
               "zn":5,
               "ga":2,
               "ge":4,
               "as":1,
               "se":5,
               "br":2,
               "kr":6,
               "rb":1,
               "sr":4,
               "y":1,
               "zr":4,
               "nb":1,
               "mo":6,
               "tc":0,
               "ru":7,
               "rh":1,
               "pd":6,
               "ag":2,
               "cd":6,
               "in":1,
               "sn":10,
               "sb":2,
               "te":5,
               "i":1,
               "xe":9,
               "cs":1,
               "ba":7,
               "la":1,
               "ce":4,
               "pr":1,
               "nd":5,
               "pm":0,
               "sm":5,
               "eu":2,
               "gd":6,
               "tb":1,
               "dy":7,
               "ho":1,
               "er":6,
               "tm":1,
               "yb":7,
               "lu":1,
               "hf":5,
               "ta":1,
               "w":5,
               "re":1,
               "os":6,
               "ir":2,
               "pt":5,
               "au":1,
               "hg":7,
               "tl":2,
               "pb":4,
               "bi":0,
               "po":0,
               "at":0,
               "rn":0,
               "fr":0,
               "ra":0,
               "ac":0,
               "th":1,
               "pa":0,
               "u":0,
               "np":0,
               "pu":0,
               "am":0,
               "cm":0,
               "bk":0,
               "cf":0,
               "es":0,
               "fm":0,
               "md":0,
               "no":0,
               "lr":0,
               "rf":0,
               "db":0,
               "sg":0,
               "bh":0,
               "hs":0,
               "mt":0,
               "ds":0,
               "rg":0,
               "cn":0,
               "nh":0,
               "fl":0,
               "mc":0,
               "lv":0,
               "ts":0,
               "og":0
    }
    return switcher.get(atom, "Invalid month")


def run(string):
    words = string.split(" ")
    result = []
    for word in words:
        atomslist = []
        while len(word) > 0:
            oldword = word
            for a in atoms:
                if word.startswith(a):
                    atomslist.append(a)
                    word = word[len(a):]
            if oldword == word:
                word = word[1:]
        result.append(atomslist)
    print(result)
    result2 = []
    for word in result:
        total = 0
        if len(word) == 0:
            result2.append(0)
        else:
            for a in word:
                total += switch_iso(a)
            result2.append(total)
    print(result2)
    i = 0
    totaal = 0
    while i < len(result2):
        if i % 2 == 0:
            totaal += result2[i]
        else:
            totaal += -1 * result2[i]
        i += 1
    print(totaal)
    return result

run(tekst)


