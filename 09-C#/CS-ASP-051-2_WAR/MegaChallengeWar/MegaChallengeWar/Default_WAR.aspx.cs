using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace MegaChallengeWar
{
    public partial class Default_WAR : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void PlayButton_Click(object sender, EventArgs e)
        {
            Gameplay game = new Gameplay("Abraham Lincoln", "Alexander Hamilton");
            resultLabel.Text = game.Play();
            //Test
            /*
            DeckOfCards _cardsToPlayers = new DeckOfCards();
            foreach (var _currentDeck in _cardsToPlayers._currentDeck)
            {
                resultLabel.Text += ("Player 2 draws a" + (_currentDeck.cardFace + " of " + _currentDeck.cardSuit));
                
                //( of " + _currentdeck.cardSuit + "</br>");
            }
            DeckofCards playerHand = new DeckofCards();
                 foreach (var currentdeck in playerHand._currentDeck)
                 {
                     resultLabel.Text += "<br/> " + currentdeck.cardFace + " of "
                         + currentdeck.cardSuit;
                 }
            */  
        }
    }
}
