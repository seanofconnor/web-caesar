def encrypt(text, rot):
    l = len(text)
    i = 0
    newText = ''
    # cycle through chars in text
    while i < l:
        c = text[i]
        newText = newText + rotate_character(c, rot)
        i = i + 1
    return(newText)

def alphabet_position(letter):
    bet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    x = bet.index(letter)
    if x > 25:
        x = x - 25
        return x
    else:
        x = x + 1
        return x

def rotate_character(char, rot):
    bet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # check if alpha
    if char in bet:
        # calculate new letter
        x = alphabet_position(char)
        newChar = (x + rot) % 26 - 1
        # check for uppercase
        isupper = bet.index(char)
        # uppercase
        if isupper > 25:
            return(bet[newChar].upper())
        else:
            return(bet[newChar])
    else:
        return(char)
