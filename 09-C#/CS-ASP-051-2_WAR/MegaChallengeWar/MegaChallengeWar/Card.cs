using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace MegaChallengeWar
{
    public class Card 
    {
        /*
        public string suit { get; internal set; } // Suit of card ("Hearts", "Diamonds", etc)
        public string face { get; internal set; } // Face of card ("Deuce", "Ace", etc) 

        public static implicit operator string(Card v)
        {
            throw new NotImplementedException();
        }

        public Card(string cardSuit, string cardFace)//instance constructor of card face & suit
        {
            suit = cardSuit; //initialize suit of card
            face = cardFace; //initialize face of card
        }
        public override string ToString() //return string of Card
        {
            return face + " of " + suit;
        }
        */
        public string cardSuit { get; set; }
        public string cardFace { get; set; }

        public int CardValue()
        {
            int value = 0;

            switch (this.cardFace)
            {
                case "Jack":
                    value = 11;
                    break;
                case "Queen":
                    value = 12;
                    break;
                case "King":
                    value = 13;
                    break;
                case "Ace":
                    value = 14;
                    break;
                default:
                    //Convert.ToInt32(cardFace);
                    value = int.Parse(this.cardFace);
                    
                    //value = int.Parse(this.cardFace);
                    //value = 0;
                    break;
            }
            return value;
        }
    }
}