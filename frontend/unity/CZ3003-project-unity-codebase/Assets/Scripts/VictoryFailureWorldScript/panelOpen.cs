using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class panelOpen : MonoBehaviour
{
    public GameObject Panel;

    public void OpenPanel(string world)
    {
        if(Panel != null)
        {
            Panel.SetActive(true);

            // set title
            Panel.transform.GetChild(0).gameObject.GetComponent<Text>().text = "World " + world;

            // set all values to N/A
            for (int i = 1; i < 10; i++)
            {
                Panel.transform.GetChild(i+6).gameObject.GetComponent<Text>().text = "N/A";
            }

            // set score
            WorldScoreRecord scoreRecord = ChooseWorld.scoreRecord;

            if (scoreRecord.worldScores.ContainsKey(world))
            {
                int worldIndex = int.Parse(world);
                if (scoreRecord.worldScores.ContainsKey(worldIndex.ToString()))
                {
                    WorldScore worldScore = scoreRecord.worldScores[worldIndex.ToString()];

                    for (int sectionIndex = 1; sectionIndex < 4; sectionIndex++)
                    {
                        if (worldScore.sectionScores.ContainsKey(sectionIndex.ToString()))
                        {
                            SectionScore sectionScore = worldScore.sectionScores[sectionIndex.ToString()];

                            for (int levelIndex = 1; levelIndex < 4; levelIndex++)
                            {
                                if (sectionScore.levelScores.ContainsKey(levelIndex.ToString()))
                                {
                                    LevelScore levelScore = sectionScore.levelScores[levelIndex.ToString()];
                                    // set the text on the panel
                                    int componentIndex = (sectionIndex - 1 ) * 3 + levelIndex + 6;
                                    Panel.transform.GetChild(componentIndex).gameObject.GetComponent<Text>().text = levelScore.score.ToString() + "/" + levelScore.maxScore.ToString();
                                }
                            }
                        }
                    }
                }
            }
        }
    }

}
