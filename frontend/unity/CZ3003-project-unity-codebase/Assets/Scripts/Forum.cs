using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Forum : MonoBehaviour
{
    public static string forumContent;
    public GameObject inputField;
    public GameObject textDisplay;
    public share share;

    void Start()
    {
        share = new share();
    }

    public void forumCreate()
    {
        forumContent = inputField.GetComponent<Text>().text;
        textDisplay.GetComponent<TextMeshProUGUI>().text = "Ready to share!";
        share.shareScoreOnTwitter();
    }

    public void BackToMenu()
    {
        SceneManager.LoadScene("MainMenu");
    }

}


public class share
{
    /* TWITTER VARIABLES*/
    //Twitter Share Link
    string TWITTER_ADDRESS = "http://twitter.com/intent/tweet";

    //Language
    string TWEET_LANGUAGE = "en";

    //This is the text which you want to show
    //string textToDisplay = Forum.forumContent;

    /*END OF TWITTER VARIABLES*/

    // Use this for initialization
    public void shareScoreOnTwitter()
    {
        Application.OpenURL(TWITTER_ADDRESS + "?text=" + WWW.EscapeURL(Forum.forumContent) + "&amp;lang=" + WWW.EscapeURL(TWEET_LANGUAGE));
    }

}