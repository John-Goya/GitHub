using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;

namespace MegaChallengeWar
{
    public class DeckOfCards
    {
        //public List<Card> _currentDeck; //test
        private List<Card> _currentDeck;
        private Random _random;
        private StringBuilder _handOutput;


        
        public DeckOfCards()
        {
            _currentDeck = new List<Card>(); //currentDeck is List instance of class Card
            _random = new Random();
            _handOutput = new StringBuilder();

            string[] suits = new string[] { "Clubs", "Diamonds", "Hearts", "Spades" };
            string[] faces = new string[] { "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "Jack", "Queen", "King", "Ace"};

            foreach (var suit in suits)//go through each item in array and put each faces in array into a new face variable
            {
                foreach (var face in faces)//go through each item in array and put each suits in array into new suit variable
                {
                    _currentDeck.Add(new Card() { cardFace = face, cardSuit = suit});
                    // to assign all face/suit variables to cardFace/cardSuit into a new card instance and add it to the _currentDeck list
                    

                }

            }      
            /*
            foreach (var Card in currentDeck)
            {
                currentDeck.Add(new Card(suit, face));
            }
            */

        }
        public string DealToPlayers(Player player1, Player player2) // method to assign 2 instances of "Player" class to player 1 & player 2
        {
            while (_currentDeck.Count > 0) //checks to see if cards are available in current deck
            {
                //player1._playersHand.Add(_currentDeck.ElementAt(_random.Next(_currentDeck.Count)));
                //player2._playersHand.Add(_currentDeck.ElementAt(_random.Next(_currentDeck.Count)));
                DealCards(player1);
                DealCards(player2);
                //_handOutput.Append("<br/>");
            }
            //_handOutput.Append("<br/>");
            _handOutput.Append("<br/>*********Let the fighting begin!*********<br/>");
            return _handOutput.ToString();
        }

        private void DealCards(Player player) // deals random cards to player
        {
            Card cardsToPlayers = _currentDeck.ElementAt(_random.Next(_currentDeck.Count)); //gets random card from currentDeck
            player.PlayersHand.Add(cardsToPlayers); //adds card to player
            _currentDeck.Remove(cardsToPlayers); //removes card from currentDeck

            _handOutput.Append("<br/>");
            _handOutput.Append(player.PlayerName); 
            _handOutput.Append(" is dealt the ");
            _handOutput.Append(cardsToPlayers.cardFace);
            _handOutput.Append(" of ");
            _handOutput.Append(cardsToPlayers.cardSuit);
        }
    }
}