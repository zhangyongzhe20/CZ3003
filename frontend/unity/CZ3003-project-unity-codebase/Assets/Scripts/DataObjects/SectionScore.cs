using System;
using System.Collections.Generic;

public class SectionScore
{
    public Dictionary<string, LevelScore> levelScores;

    public SectionScore()
    {
        levelScores = new Dictionary<string, LevelScore>();
    }
}
