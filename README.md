# UNO
This project is a simple implementation of the card game UNO using python


THE DECK: 
    108 cards
    4 colours : red, blue, green, yellow numbered 0 to 9
    3 special cards in each colour category: Skip, Draw Two, Reverse
    4 wild cards
    4 Draw Four Wild cards

THE GAMEPLAY:

    At the start of the game, each player is dealt 7 cards from the shuffled deck.

    The game begins with a starting card drawn from the deck, which is placed face up on the discard pile. The first player must match the starting card's color, number, or special ability.

    Players take turns in clockwise order. On their turn, a player must play a card that matches the color, number, or special ability of the card on the discard pile. If a player cannot play a valid card, they must draw a card from the deck.

    Special action cards have specific effects:
    - Skip: The next player in sequence is skipped, and their turn is forfeited.
    - Reverse: The direction of play is reversed, changing the order of players.
    - Draw Two: The next player in sequence must draw two cards and skip their turn.
    - Wild: The player can choose the next color to be played, without requiring a specific number.
    - Wild Draw Four: Similar to the wild card, the player also forces the next player to draw four cards and skip their turn. However, it can only be played if the player doesn't have a card of the required color.

    If a player has only one card left, they must announce "Uno" to alert other players. Failure to do so and being caught by another player results in drawing two penalty cards.

The first player to get rid of all of their cards is the winner. 

