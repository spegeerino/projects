poker_file = open("p054_poker.txt","r")
p1_hands = []
p2_hands = []
for i in range(1000):
    two_hand_string = poker_file.readline()[:-1]
    cards = two_hand_string.split(" ")
    p1_hands.append(cards[:5])
    p2_hands.append(cards[5:])

def is_flush(hand):
    suit_set = set()
    for card in hand:
        suit_set.add(card[1])
    if len(suit_set) != 1:
        return False, 0
    return True, rank_score(hand)

def convert_rank_to_number(rank):
    if rank == 'T':
        return '10'
    if rank == 'J':
        return '11'
    if rank == 'Q':
        return '12'
    if rank == 'K':
        return '13'
    if rank == 'A':
        return '14'
    return rank

def convert_rank_to_number_for_straight(rank, rank_list):
    if rank == 'T':
        return '10'
    if rank == 'J':
        return '11'
    if rank == 'Q':
        return '12'
    if rank == 'K':
        return '13'
    if rank == 'A':
        if '5' in rank_list:
            return '1'
        else:
            return '14'
    return rank

def is_straight(hand):
    rank_list = []
    for card in hand:
        rank_list.append(card[0])
    if len(set(rank_list)) != 5:
        return False, 0
    for i in range(len(rank_list)):
        rank_list[i] = convert_rank_to_number_for_straight(rank_list[i], rank_list)
        rank_list[i] = int(rank_list[i])
    rank_list.sort()
    for i in range(len(rank_list) - 1):
        if rank_list[i+1] - rank_list[i] != 1:
            return False, 0 
    return True, rank_list[-1]

def rank_score(hand):
    rank_list = [int(convert_rank_to_number(card[0])) for card in hand]
    rank_list.sort()
    out = 0
    for i in range(len(rank_list)):
        out += rank_list[i] * (16 ** i)
    return out

def eval_hand(hand):
    '''returns a 2 entry list: first entry should be compared first, then the second entry to tiebreak'''
    straight_info = is_straight(hand)
    flush_info = is_flush(hand)
    #straight flush 9 DONE (royal flush too, it's just the highest straight flush)
    if straight_info[0] and flush_info[0]:
        return 9, straight_info[1]
    #check if len(rank_set) == 2, then we have either four of a kind or full house
    rank_list = []
    for card in hand:
        rank_list.append(int(convert_rank_to_number(card[0])))
    rank_set = set(rank_list)
    if len(rank_set) == 2:
        for rank in rank_set:
            rank_list.remove(rank)
        rank_set = set(rank_list)
        if len(rank_set) == 1:
            #four of a kind found, now need to do tiebreakers
            tiebreaker_score = 16 * rank_list[0]
            for card in hand:
                x = int(convert_rank_to_number(card[0]))
                if x != rank_list[0]:
                    tiebreaker_score += x
                    break
            return 8, tiebreaker_score
        else:
            #full house found, now need to do tiebreaker
            for rank in rank_set:
                rank_list.remove(rank)
            tiebreaker_score = 16 * rank_list[0]
            for card in hand:
                x = int(convert_rank_to_number(card[0]))
                if x != rank_list[0]:
                    tiebreaker_score += x
                    break
            return 7, tiebreaker_score
            
    #four of a kind 8 DONE
    #full house 7 DONE
    #flush 6 DONE
    if flush_info[0]:
        return 6, flush_info[1]
    #straight 5 DONE 
    if straight_info[0]:
        return 5, straight_info[1]
    if len(rank_set) == 3:
        #three of a kind or two pair
        for rank in rank_set:
            rank_list.remove(rank)
        rank_set = set(rank_list)
        if len(rank_set) == 1:
            #three of a kind, time to do tiebreaker
            tiebreaker_score = rank_list[0] * 256
            not_three_ranks = []
            for card in hand:
                x = int(convert_rank_to_number(card[0]))
                if x != rank_list[0]:
                    not_three_ranks.append(x)
            not_three_ranks.sort()
            tiebreaker_score += 16*not_three_ranks[1] + not_three_ranks[0]
            return 4, tiebreaker_score
        else:
            #two pair, time to do tiebreaker
            rank_list.sort()
            tiebreaker_score = 256 * rank_list[1] + 16* rank_list[0]
            for card in hand:
                x = int(convert_rank_to_number(card[0]))
                if x not in rank_list:
                    tiebreaker_score += x
                    break
            return 3, tiebreaker_score
    #three of a kind 4 DONE
    #two pair 3 DONE
    if len(rank_set) == 4:
        #one pair
        for rank in rank_set:
            rank_list.remove(rank)
        tiebreaker_score = 4096 * rank_list[0]
        non_pair_cards = []
        for card in hand:
            x = int(convert_rank_to_number(card[0]))
            if x != rank_list[0]:
                non_pair_cards.append(card)
        tiebreaker_score += rank_score(non_pair_cards)
        return 2, tiebreaker_score
    #one pair 2 DONE
    #high card 1 DONE
    return 1, rank_score(hand)

test = ['AC', '2D', '3C', '4H', '5S']
count = 0
for i in range(1000):
    # print(p1_hands[i])
    # print(p2_hands[i])
    p1_score1, p1_score2 = eval_hand(p1_hands[i])
    p2_score1, p2_score2 = eval_hand(p2_hands[i])
    if p1_score1 > p2_score1:
        count += 1
        # print("win")
    if p1_score1 == p2_score1:
        if p1_score2 > p2_score2:
            count += 1
            # print("tiebreak win")
    # print(p1_score1)
    # print(p1_score2)
    # print(p2_score1)
    # print(p2_score2)
    # print("-" * 30)
print(count)