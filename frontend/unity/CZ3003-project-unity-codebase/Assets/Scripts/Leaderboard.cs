using System.Collections.Generic;
using System.Net;
using System;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Newtonsoft.Json;

public class Leaderboard : MonoBehaviour
{
    public Transform entryContainer;
    public Transform entryTemplate;
    private List<LeaderboardEntry> leaderboardEntryList;
    private List<Transform> leaderboardTransformList;
    public Button backButton;
    private float templateHeight = 25f;

    public void Start()
    {
        // set back button
        backButton.onClick.AddListener(BackOnClick);

        // set data on the leaderboard
        entryTemplate.gameObject.SetActive(false);

        // call API to get leaderboard entry
        leaderboardEntryList = FetchLeaderboard();
        leaderboardTransformList = new List<Transform>();

        int index = 0;

        foreach (LeaderboardEntry leaderboardEntry in leaderboardEntryList)
        {
            if (index == 10)
            {
                break;
            }
            CreateLeaderboardEntryTransform(leaderboardEntry, entryContainer, leaderboardTransformList);
            index++;
        }
    }

    public void CreateLeaderboardEntryTransform(LeaderboardEntry entry, Transform container, List<Transform> transformList)
    {
        Transform entryTransform = Instantiate(entryTemplate, container);
        RectTransform entryRectTransform = entryTransform.GetComponent<RectTransform>();
        entryRectTransform.anchoredPosition = new Vector2(0, -15 - templateHeight * transformList.Count);
        entryTransform.gameObject.SetActive(true);

        int rank = transformList.Count + 1;

        entryTransform.Find("RankText").GetComponent<Text>().text = rank.ToString();
        entryTransform.Find("NameText").GetComponent<Text>().text = entry.name;
        entryTransform.Find("ScoreText").GetComponent<Text>().text = entry.overallScore.ToString();

        transformList.Add(entryTransform);
    }

    private List<LeaderboardEntry> FetchLeaderboard()
    {
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(String.Format("http://47.74.186.167:8000/api/students/leaderboard"));
        request.Headers["authorization"] = "Token " + GlobalVars.token;
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        StreamReader reader = new StreamReader(response.GetResponseStream());
        string jsonResponse = reader.ReadToEnd();

        List<LeaderboardEntry> entryList = JsonConvert.DeserializeObject<List<LeaderboardEntry>> (jsonResponse);
        return entryList;
    }

    void BackOnClick()
    {
        SceneManager.LoadScene(sceneName: "MainMenu");
    }
}


