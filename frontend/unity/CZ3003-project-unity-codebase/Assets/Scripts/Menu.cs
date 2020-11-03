using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Menu : MonoBehaviour
{

    public Button submitMcqButton;
    public Button submitBlankFillingButton;
    public Button leaderboardButton;

    void SubmitMcqOnClick()
    {
        SceneManager.LoadScene(sceneName: "SubmitMcq");
    }

    void SubmitBlankFillingOnClick()
    {
        SceneManager.LoadScene(sceneName: "SubmitBlankFilling");
    }

    void LeaderboardOnClick()
    {
        SceneManager.LoadScene(sceneName: "Leaderboard");
    }


    // Start is called before the first frame update
    void Start()
    {
        submitMcqButton.onClick.AddListener(SubmitMcqOnClick);
        submitBlankFillingButton.onClick.AddListener(SubmitBlankFillingOnClick);
        leaderboardButton.onClick.AddListener(LeaderboardOnClick);
    }
}
