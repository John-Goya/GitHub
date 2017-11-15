using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;

namespace MegaChallengeWar
{
    public class Battle
    {
        private List<Card> _bounty;
        private StringBuilder _handOutput;

        public Battle()
        {
            _bounty = new List<Card>();
            _handOutput = new StringBuilder();
        }

        public string PeformBattle(Player player1, Player player2)
        {
            Card player1card = GetCard(player1);//_player1._playersHand.ElementAt(0); (old code)
            Card player2card = GetCard(player2);//_player2._playersHand.ElementAt(0); (olc code)         

            displayBattleCards(player1, player2, player1card, player2card);
            //displayBattleCards(player1card, player2card);
            PerformEval(player1, player2, player1card, player2card);
            return _handOutput.ToString();
        }

        private Card GetCard(Player player)
        {
            Card card = player.PlayersHand.ElementAt(0);
            player.PlayersHand.Remove(card);
            _bounty.Add(card);
            return card;
        }

        private void PerformEval(Player player1, Player player2, Card player1card, Card player2card)
        {
            if (player1card.CardValue() == player2card.CardValue())
                war(player1, player2);
            //displayBattleCards(player1card, player2card);
            if (player1card.CardValue() > player2card.CardValue())
                //_handOutput.Append("</br>");
                awardBounty(player1);
            else //(player2card.CardValue() > player1card.CardValue())
                 //_player2.PlayersHand.AddRange(_bounty);
                //_handOutput.Append("</br>");
                awardBounty(player2);
        }

        private void awardBounty(Player player)
        {
            if (_bounty.Count == 0) return;
            displayBountyCards();
            player.PlayersHand.AddRange(_bounty);//add cards in bounty to winner's DeckOfCards();
            _bounty.Clear();

            _handOutput.Append(player.PlayerName);
            _handOutput.Append(" wins the bounty!<br/>");
        }

        private void displayBountyCards()
        {
            _handOutput.Append("<br/>Bounty");

            foreach (var card in _bounty)
            {
                _handOutput.Append("<br/>&nbsp;&nbsp;&nbsp;&nbsp;");
                _handOutput.Append(card.cardFace);
                _handOutput.Append(" of ");
                _handOutput.Append(card.cardSuit);
            }
            _handOutput.Append("<br/>");
        }

        private void war(Player player1, Player player2)
        {
            _handOutput.Append("</br>");
            _handOutput.Append("*********WAR*********<br/>");
            GetCard(player1);
            Card warCardPlayer1 = GetCard(player1);
            GetCard(player1);
            GetCard(player2);
            Card warCardPlayer2 = GetCard(player2);
            GetCard(player2);

            
            _handOutput.Append("</br> War Cards: ");
            _handOutput.Append("</br>&nbsp&nbsp&nbsp&nbsp");
            _handOutput.Append(player1.PlayerName);
            _handOutput.Append("'s ");
            _handOutput.Append(warCardPlayer1.cardFace);
            _handOutput.Append(" of ");
            _handOutput.Append(warCardPlayer1.cardSuit);
            _handOutput.Append(" vs ");
            _handOutput.Append(player2.PlayerName);
            _handOutput.Append("'s ");
            _handOutput.Append(warCardPlayer2.cardFace);
            _handOutput.Append(" of ");
            _handOutput.Append(warCardPlayer2.cardSuit);

            PerformEval(player1, player2, warCardPlayer1, warCardPlayer2);
        }

        private void displayBattleCards(Player player1, Player player2, Card card1, Card card2)
        {
            _handOutput.Append("</br>Battle Cards: ");
            _handOutput.Append("</br>&nbsp&nbsp&nbsp&nbsp");
            _handOutput.Append(player1.PlayerName);
            _handOutput.Append("'s ");
            _handOutput.Append(card1.cardFace);
            _handOutput.Append(" of ");
            _handOutput.Append(card1.cardSuit);
            _handOutput.Append(" vs ");
            _handOutput.Append(player2.PlayerName);
            _handOutput.Append("'s ");
            //_handOutput.Append(" VS Player's 2: ");
            _handOutput.Append(card2.cardFace);
            _handOutput.Append(" of ");
            _handOutput.Append(card2.cardSuit);
        }
    }
}