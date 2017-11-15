using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace MegaChallengeWar
{
    public class Player
    {
        public String PlayerName { get; set; }
        public List<Card> PlayersHand { get; set; }

        public Player()
        {
            PlayersHand = new List<Card>();
        }
    }
}