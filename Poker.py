def isFlush(hand):
    for card in range(1, 5):
        if hand[card][-1] != hand[0][-1]:
            return False
    return True

def straight(hand):
    cards = hand
    nextcard = 0
    if cards[0][0:2] == '14' and cards[1][0:2] == '05':
        cards[0] = '01' + cards[0][2:3]#Aces can be low
        cards.sort()
        cards.reverse()
    for card in cards:
        if nextcard != 0 and nextcard != int(card[0:2]):
            return 0
        nextcard = int(card[0:2]) - 1
    return cards[0][0:2]

def ofAKind(hand):
    count = 1
    kind = 0
    list = []
    singles = []
    for card in hand:
        if card[0:2] == kind:
            count += 1
        elif count > 1:
            list.append([count,kind])
            count = 1
        elif kind != 0:
            singles.append(kind)
        kind = card[0:2]
    if count > 1:
        list.append([count,kind])
    elif kind != 0:
        singles.append(kind)
    return list, singles

def score(hand):
    S = straight(hand)
    F = isFlush(hand)
    K, NK = ofAKind(hand)
    LK = len(K)
    C = ''
    for card in hand:
        C += card[0:2]
    if S != 0:
        if F:
            return int('8' + S + '00000000')
        else:
            return int('4' + S + '00000000')
    elif LK == 1 and K[0][0] == 4:
        return int('7' + K[0][1] + NK[0] + '000000')
    elif LK == 2 and K[0][0] + K[1][0] == 5:
        if K[0][0] == 3:
            K3 = K[0][1]
            K2 = K[1][1]
        else:
            K2 = K[0][1]
            K3 = K[1][1]
        return int('6' + K3 + K2 + '000000')
    elif F:
        return int('5' + C)
    elif LK == 1 and K[0][0] == 3:
        return int('3' + K[0][1] + NK[0] + NK[1] + '0000')
    elif LK == 2:
        return int('2' + K[0][1] + K[1][1] + NK[0] + '0000')
    elif LK == 1:
        return int('1' + K[0][1] + NK[0] + NK[1] + NK[2] + '00')
    else:
        return int(C)

value = {
    '2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08',
    '9':'09','T':'10','J':'11','Q':'12','K':'13','A':'14'
}

def format(card):
    formatted = value[card[0]]
    formatted += card[-1]
    return formatted

file = open("poker.txt")
text = file.read()
file.close()
rounds = text.split("\n")
rounds.pop()

wins = 0

for hands in rounds:
    h1 = []
    h2 = []
    for i in range(5):
        h1.append(format(hands[3*i:3*i+2]))
    for i in range(5,10):
        h2.append(format(hands[3*i:3*i+2]))
    h1.sort()
    h1.reverse()
    h2.sort()
    h2.reverse()
    if score(h1) > score(h2):
        wins +=1
print(wins)
