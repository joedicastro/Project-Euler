#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Poker hands
Problem 54
http://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    * High Card: Highest value card.
    * One Pair: Two cards of the same value.
    * Two Pairs: Two different pairs.
    * Three of a Kind: Three cards of the same value.
    * Straight: All cards are consecutive values.
    * Flush: All cards of the same suit.
    * Full House: Three of a kind and a pair.
    * Four of a Kind: Four cards of the same value.
    * Straight Flush: All cards are consecutive values of same suit.
    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:

    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

    Hand    Player 1                Player 2                    Winner

    1       5H 5C 6S 7S KD          2C 3S 8S 8D TD              Player 2
            Pair of Fives           Pair of Eights 

    2       5D 8C 9S JS AC          2C 5C 7D 8S QH              Player 1
            Highest card Ace        Highest card Queen 

    3       2D 9C AS AH AC          3D 6D 7D TD QD              Player 2
            Three Aces              Flush  with Diamonds         

    4       4D 6S 9H QH QC          3D 6D 7H QD QS              Player 1
            Pair of Queens          Pair of Queens
            Highest card Nine       Highest card Seven 

    5       2H 2D 4C 4D 4S          3C 3D 3S 9S 9D              Player 1
            Full House              Full House
            With Three Fours        with Three Threes 

The file, <poker.txt>, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?

"""


from collections import Counter


def get_hand(cards):
    """Translate a hand in a number where the different combinations are
    arranged by rank value, from the most significant digit (left) to the less,
    e.g. the first digit is 1 if the hand is a royal flush else a 0 and so
    on. The greatest number is the winner.

    """

    hand = {}
    # cards valued
    hand['cards'] = sorted(['23456789TJQKA'.index(c[0]) + 2 for c in cards])
    # check royal flush
    hand['rf'] = 1 if hand['cards'] == [10, 11, 12, 13, 14] else 0
    # check flush
    hand['fl'] = 1 if len(set([f[1] for f in cards])) == 1 else 0
    # check straigh
    hand['st'] = int(all(1 if hand['cards'][i + 1] - hand['cards'][i] == 1
                         else 0 for i in xrange(4)))
    hand['stc'] = max(hand['cards']) if hand['st'] else 0
    # check straight flush (straight and flush)
    hand['sf'] = hand['st'] and hand['fl']
    hand['sfc'] = hand['stc'] if hand['sf'] else 0

    # get the numbers of cards by card
    count = Counter(hand['cards'])

    # check one pair
    hand['op'] = 1 if 2 in count.values() else 0
    hand['opc'] = max(f for f in count if count[f] == 2) if hand['op'] else 0
    # check two pairs
    hand['tp'] = 1 if sum(1 for p in count if count[p] == 2) == 2 else 0
    hand['tpc'] = ''.join(sorted(['{0:02}'.format(f) for f in count if
                                  count[f] == 2],
                                 reverse=True)) if hand['tp'] else '0000'
    # check three of a kind
    hand['tk'] = 1 if 3 in count.values() else 0
    hand['tkc'] = [f for f in count if count[f] == 3][0] if hand['tk'] else 0
    # check four of a kind
    hand['fk'] = 1 if 4 in count.values() else 0
    hand['fkc'] = [f for f in count if count[f] == 4][0] if hand['fk'] else 0
    # check full house
    hand['fh'] = hand['tk'] and hand['op']
    hand['fhc'] = '{0:02}{1:02}'.format(hand['tkc'],
                                        hand['opc']) if hand['fh'] else '0000'

    # the cards sorted from the highest to the lowest
    hand['hc'] = ''.join(['{0:02}'.format(c) for c in hand['cards'][::-1]])

    score = int('{rf}{sf}{sfc:02}{fk}{fkc:02}{fh}{fhc}{fl}{st}{stc:02}{tk}'
                '{tkc:02}{tp}{tpc}{op}{opc:02}{hc}'.
                format(rf=hand['rf'], sf=hand['sf'], sfc=hand['sfc'],
                       fk=hand['fk'], fkc=hand['fkc'], fh=hand['fh'],
                       fhc=hand['fhc'], fl=hand['fl'], st=hand['st'],
                       stc=hand['stc'], tk=hand['tk'], tkc=hand['tkc'],
                       tp=hand['tp'], tpc=hand['tpc'], op=hand['op'],
                       opc=hand['opc'], hc=hand['hc']))

    return score


all_hands = open('poker.txt').read().splitlines()

hands_by_player = [(line.split()[:5], line.split()[-5:]) for line in all_hands]
player_one_win = 0

for player_one_hand, player_two_hand in hands_by_player:
    if get_hand(player_one_hand) > get_hand(player_two_hand):
        player_one_win += 1

print 'Player 1 win {0} hands'.format(player_one_win)
