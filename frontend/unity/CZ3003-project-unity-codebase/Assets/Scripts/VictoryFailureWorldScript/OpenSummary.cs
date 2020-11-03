using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

public class OpenSummary : MonoBehaviour
{
    // Use this for initialization
    void Start()
    {
        int score = 0;
        int maxScore = 0;

        WorldScoreRecord scoreRecord = ChooseWorld.scoreRecord;

        // add up score
        foreach (KeyValuePair<string, WorldScore> worldItem in scoreRecord.worldScores)
        {
            WorldScore worldScore = worldItem.Value;
            foreach (KeyValuePair<string, SectionScore> sectionItem in worldScore.sectionScores)
            {
                SectionScore sectionScore = sectionItem.Value;

                foreach (KeyValuePair<string, LevelScore> levelItem in sectionScore.levelScores)
                {
                    score = score + levelItem.Value.score;
                    maxScore = maxScore + levelItem.Value.maxScore;
                }
            }
        }

        GameObject.Find("Canvas").transform
            .GetChild(0).gameObject.transform
            .GetChild(0)
            .GetComponent<Text>().text = "Total Score: " + score.ToString() + "/" + maxScore.ToString();
    }
}
