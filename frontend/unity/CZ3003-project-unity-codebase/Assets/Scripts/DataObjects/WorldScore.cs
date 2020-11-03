using System;
using System.Collections.Generic;

public class WorldScore
{
    public Dictionary<string, SectionScore> sectionScores;

    public WorldScore()
    {
        sectionScores = new Dictionary<string, SectionScore>();
    }
}
