using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using UnityEngine.SceneManagement;
using TMPro;


namespace Tests
{
    public class SysTest
    {

        [UnityTest]
        public IEnumerator Login()
        {
            SceneManager.LoadScene("Login");

            yield return new WaitForSeconds(.001f);

            TMP_InputField Email = GameObject.Find("Email").GetComponent<TMP_InputField>();

            Email.text = "C170166@e.ntu.edu.sg";

            TMP_InputField Password = GameObject.Find("Password").GetComponent<TMP_InputField>();

            Password.text = "password";

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button LoginButton = GameObject.Find("Button").GetComponent<UnityEngine.UI.Button>();
            LoginButton.onClick.Invoke();

            yield return new WaitForSeconds(.25f);

            var StartBtn = GameObject.Find("StartGame").GetComponent<UnityEngine.UI.Button>();

            Assert.AreEqual("StartGame", StartBtn.tag);

            yield return new WaitForSeconds(.001f);


        }

        [UnityTest]
        public IEnumerator MainMenu_to_Forum()
        {
            SceneManager.LoadScene("MainMenu");

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button forumButton = GameObject.Find("TheForum").GetComponent<UnityEngine.UI.Button>();
            forumButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            var twitter = GameObject.FindGameObjectWithTag("Twitter");
            Assert.AreEqual("Twitter", twitter.tag);

            yield return new WaitForSeconds(.001f);


        }
        // A Test behaves as an ordinary method
        [UnityTest]
        public IEnumerator MainMenu_to_Forum_with_Tweets()
        {
            SceneManager.LoadScene("MainMenu");

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button forumButton = GameObject.Find("TheForum").GetComponent<UnityEngine.UI.Button>();
            forumButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.InputField TwitterText = GameObject.Find("TwitterText").GetComponent<UnityEngine.UI.InputField>();

            TwitterText.text = "Hi!";

            UnityEngine.UI.Button TwitterBtn = GameObject.Find("TwitterBtn").GetComponent<UnityEngine.UI.Button>();
            TwitterBtn.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

        }

        [UnityTest]
        public IEnumerator Submit_MCQ_Questions()
        {

            SceneManager.LoadScene("MainMenu");

            yield return null;

            UnityEngine.UI.Button MCQButton = GameObject.Find("SubmitMCQ").GetComponent<UnityEngine.UI.Button>();
            MCQButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.InputField QuestionBody = GameObject.Find("QuestionBody").GetComponent<UnityEngine.UI.InputField>();

            QuestionBody.text = "This is a new question!";

            UnityEngine.UI.InputField ChoiceA = GameObject.Find("ChoiceA").GetComponent<UnityEngine.UI.InputField>();

            ChoiceA.text = "Answer A";

            UnityEngine.UI.InputField ChoiceB = GameObject.Find("ChoiceB").GetComponent<UnityEngine.UI.InputField>();

            ChoiceB.text = "Answer B";

            UnityEngine.UI.InputField ChoiceC = GameObject.Find("ChoiceC").GetComponent<UnityEngine.UI.InputField>();

            ChoiceC.text = "Answer C";

            UnityEngine.UI.InputField ChoiceD = GameObject.Find("ChoiceD").GetComponent<UnityEngine.UI.InputField>();

            ChoiceD.text = "Answer D";

            UnityEngine.UI.Button SubmitBtn = GameObject.Find("SubmitButton").GetComponent<UnityEngine.UI.Button>();
            SubmitBtn.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            yield return null;
        }

        [UnityTest]
        public IEnumerator Submit_Blank_Questions()
        {

            SceneManager.LoadScene("MainMenu");

            yield return null;

            UnityEngine.UI.Button SubmitBlankFillButton = GameObject.Find("SubmitBlankFill").GetComponent<UnityEngine.UI.Button>();
            SubmitBlankFillButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.InputField QuestionBody = GameObject.Find("QuestionBody").GetComponent<UnityEngine.UI.InputField>();

            QuestionBody.text = "This is a new question!";

            UnityEngine.UI.InputField Answer = GameObject.Find("Answer").GetComponent<UnityEngine.UI.InputField>();

            Answer.text = "This is the answer to the blank question";

            UnityEngine.UI.Button SubmitBtn = GameObject.Find("SubmitButton").GetComponent<UnityEngine.UI.Button>();
            SubmitBtn.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            yield return null;
        }

        [UnityTest]
        public IEnumerator Start_Game_test()
        {
            SceneManager.LoadScene("MainMenu");

            yield return null;

            UnityEngine.UI.Button forumButton = GameObject.Find("StartGame").GetComponent<UnityEngine.UI.Button>();
            forumButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);


            UnityEngine.UI.Button characterButton = GameObject.Find("VirtualGuyButton").GetComponent<UnityEngine.UI.Button>();
            characterButton.onClick.Invoke();

            yield return new WaitForSeconds(0.001f);

            UnityEngine.UI.Button worldButton = GameObject.Find("World1").transform.GetChild(0).GetComponent<UnityEngine.UI.Button>();
            worldButton.onClick.Invoke();

            yield return new WaitForSeconds(0.1f);

            // Button A
            UnityEngine.UI.Button AnswerA = GameObject.Find("A").gameObject.GetComponent<UnityEngine.UI.Button>();
            AnswerA.onClick.Invoke();
            yield return new WaitForSeconds(.001f);
            AnswerA.onClick.Invoke();
            yield return new WaitForSeconds(.001f);

            yield return null;

        }


        [UnityTest]
        public IEnumerator Leaderboard_ten_results_test()
        {
            SceneManager.LoadScene("Login");

            yield return new WaitForSeconds(.001f);

            TMP_InputField Email = GameObject.Find("Email").GetComponent<TMP_InputField>();

            Email.text = "C170166@e.ntu.edu.sg";

            TMP_InputField Password = GameObject.Find("Password").GetComponent<TMP_InputField>();

            Password.text = "password";

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button LoginButton = GameObject.Find("Button").GetComponent<UnityEngine.UI.Button>();
            LoginButton.onClick.Invoke();

            yield return new WaitForSeconds(.5f);

            UnityEngine.UI.Button leaderBoardButton = GameObject.Find("Leaderboard").GetComponent<UnityEngine.UI.Button>();
            leaderBoardButton.onClick.Invoke();

            yield return new WaitForSeconds(2);

            GameObject container = GameObject.Find("LeaderboardContainer");

            int tenthRank = container.transform.childCount - 1;

            Transform lastChild = container.transform.GetChild(tenthRank);

            UnityEngine.UI.Text lastRank = lastChild.Find("RankText").GetComponent<UnityEngine.UI.Text>();

            Assert.AreEqual("10", lastRank.text);

            yield return null;


        }



    }
}
