using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace MegaChallengeWar
{
    public class Gameplay
    {
        private Player _player1;
        private Player _player2;
        public Gameplay(string player1Name, string player2Name)
        {
            _player1 = new Player() { PlayerName = player1Name };
            _player2 = new Player() { PlayerName = player2Name };
        }
        public string Play()
        {
            DeckOfCards game = new DeckOfCards();

            string result = "Dealing cards ...";
            result += game.DealToPlayers(_player1, _player2);

            int round = 0;
            while (_player1.PlayersHand.Count !=0 && _player2.PlayersHand.Count !=0)
            {
                Battle battleround = new Battle();
                result += battleround.PeformBattle(_player1, _player2);

                round++;
                if (round > 20)
                    break;
                //return _sb.ToString();
                /*
                displayBattleCards(card1, card2);
                if (card1.CardValue() > card2.CardValue())
                    awardWinner(player1);
                if (card2.CardValue() > card1.CardValue())
                    awardWinner(player2);
                else
                   War(player1, player2);
                */
            }
            result += DetermineWinner(_player1, _player2);
            return result;
        }


        private string DetermineWinner(Player player1, Player player2)
        {
            string result = "";
            result += ("</br>" + _player1.PlayerName + " has " + _player1.PlayersHand.Count + " cards.");
            result += ("</br>" + _player2.PlayerName + " has " + _player2.PlayersHand.Count + " cards." + "<br/>");

            if (_player1.PlayersHand.Count > _player2.PlayersHand.Count)
                result += (_player1.PlayerName + " is the winner!");
            //result += "<br/>Player 1 wins";
            //if (_player1.PlayersHand.Count == _player2.PlayersHand.Count)
                    //result += (_player1.PlayerName + " and " + _player2.PlayerName + " proclaim a truce!");
            else
                result += (_player2.PlayerName + " is the winner!");
            //result += "<br/>Player 2 wins";

            return result;
        }
    }
}