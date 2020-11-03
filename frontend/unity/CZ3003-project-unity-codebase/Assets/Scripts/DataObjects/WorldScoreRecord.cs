using System;
using System.Collections.Generic;

public class WorldScoreRecord
{
    public Dictionary<string, WorldScore> worldScores;

    public WorldScoreRecord()
    {
        worldScores = new Dictionary<string, WorldScore>();
    }
}