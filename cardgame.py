class card():
  suit_names = ['clubs','diamonds','hearts','spades']
  rank_names = [None, 'Ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

  def __init__(self,rank=0,suit=2):
   self.rank = rank
   self.suit = suit

  def __str__(self):
   return f"the rank is {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suit]}"

ace_of_spade = card(1,3)

print(ace_of_spade)
