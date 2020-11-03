using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using Unity.PerformanceTesting;
using UnityEngine;
using UnityEngine.TestTools;
using Unity.PerformanceTesting;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine.Profiling;
using System;
using System.Runtime.InteropServices;
using TMPro;

namespace Tests
{
    public class PerfTest
    {
        // Testing for Login
        [UnityTest, Performance]
        public IEnumerator Login()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("Login");
            }
            yield return null;


            yield return new WaitForSeconds(.001f);

            TMP_InputField Email = GameObject.Find("Email").GetComponent<TMP_InputField>();
            Email.text = "C170166@e.ntu.edu.sg";


            TMP_InputField Password = GameObject.Find("Password").GetComponent<TMP_InputField>();

            Password.text = "password";

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button LoginButton = GameObject.Find("Button").GetComponent<UnityEngine.UI.Button>();
            LoginButton.onClick.Invoke();

            yield return Measure.Frames().Run();




        }
        //Custom measurement to capture total allocated and reserved memory
        [Test, Performance, Version("1")]
        public void Measure_Empty()
        {
            var allocated = new SampleGroupDefinition("TotalAllocatedMemory", SampleUnit.Megabyte);
            var reserved = new SampleGroupDefinition("TotalReservedMemory", SampleUnit.Megabyte);
            Measure.Custom(allocated, Profiler.GetTotalAllocatedMemoryLong() / 1048576f);
            Measure.Custom(reserved, Profiler.GetTotalReservedMemoryLong() / 1048576f);
        }

        // Scene Measurement
        [UnityTest, Performance]
        public IEnumerator Rendering_Scene()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("MainMenu");
            }
            yield return null;

            yield return Measure.Frames().Run();
        }

        // From MainMenu to Forum with tweet shared 
        [UnityTest, Performance]
        public IEnumerator MainMenu_to_Forum_Share_Tweet()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("MainMenu");
            }
            yield return null;

            UnityEngine.UI.Button forumButton = GameObject.Find("TheForum").GetComponent<UnityEngine.UI.Button>();
            forumButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.InputField TwitterText = GameObject.Find("TwitterText").GetComponent<UnityEngine.UI.InputField>();

            TwitterText.text = "Hi!";

            UnityEngine.UI.Button TwitterBtn = GameObject.Find("TwitterBtn").GetComponent<UnityEngine.UI.Button>();
            TwitterBtn.onClick.Invoke();

            yield return null;

            yield return Measure.Frames().Run();
        }

        // From MainMenu to Forum with FB shared 
        [UnityTest, Performance]
        public IEnumerator MainMenu_to_Forum_Share_FB()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("MainMenu");
            }
            yield return null;

            UnityEngine.UI.Button forumButton = GameObject.Find("TheForum").GetComponent<UnityEngine.UI.Button>();
            forumButton.onClick.Invoke();

            yield return new WaitForSeconds(.5f);

            UnityEngine.UI.Button TwitterBtn = GameObject.Find("FBBtn").GetComponent<UnityEngine.UI.Button>();
            TwitterBtn.onClick.Invoke();

            yield return null;

            yield return Measure.Frames().Run();
        }

        // Submit MCQ questions
        [UnityTest, Performance]
        public IEnumerator Submit_MCQ_Questions()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("MainMenu");
            }
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


            yield return null;

            yield return Measure.Frames().Run();
        }

        // Submit blank questions
        [UnityTest, Performance]
        public IEnumerator Submit_Blank_Questions()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("MainMenu");
            }
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

            yield return null;

            yield return Measure.Frames().Run();
        }

        //Start Game test for all Level 1
        [UnityTest, Performance]
        public IEnumerator Start_Game_test()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("MainMenu");
            }
            yield return null;

            Boolean loop = true;

            UnityEngine.UI.Button forumButton = GameObject.Find("StartGame").GetComponent<UnityEngine.UI.Button>();
            forumButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);


            UnityEngine.UI.Button characterButton = GameObject.Find("VirtualGuyButton").GetComponent<UnityEngine.UI.Button>();
            characterButton.onClick.Invoke();

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button worldButton = GameObject.Find("World1").transform.GetChild(0).GetComponent<UnityEngine.UI.Button>();
            worldButton.onClick.Invoke();

            yield return new WaitForSeconds(0.1f);

            // Button A B C D
            UnityEngine.UI.Button AnswerA = GameObject.Find("A").gameObject.GetComponent<Button>();
            AnswerA.onClick.Invoke();

            yield return Measure.Frames().Run();
        }

        //Leaderboard test
        [UnityTest, Performance]
        public IEnumerator Leaderboard_Test()
        {
            using (Measure.Scope(new SampleGroupDefinition("Setup.LoadScene")))
            {
                SceneManager.LoadScene("Login");
            }
            yield return null;

            yield return new WaitForSeconds(.001f);

            TMP_InputField Email = GameObject.Find("Email").GetComponent<TMP_InputField>();

            Email.text = "C170166@e.ntu.edu.sg";

            TMP_InputField Password = GameObject.Find("Password").GetComponent<TMP_InputField>();

            Password.text = "password";

            yield return new WaitForSeconds(.001f);

            UnityEngine.UI.Button LoginButton = GameObject.Find("Button").GetComponent<UnityEngine.UI.Button>();
            LoginButton.onClick.Invoke();

            yield return new WaitForSeconds(1);

            UnityEngine.UI.Button leaderBoardButton = GameObject.Find("Leaderboard").GetComponent<UnityEngine.UI.Button>();
            leaderBoardButton.onClick.Invoke();

            yield return new WaitForSeconds(2);

            GameObject container = GameObject.Find("LeaderboardContainer");

            int tenthRank = container.transform.childCount - 1;

            Transform lastChild = container.transform.GetChild(tenthRank);

            UnityEngine.UI.Text lastRank = lastChild.Find("RankText").GetComponent<UnityEngine.UI.Text>();

            Debug.Log(lastRank.text);

            // UnityEngine.UI.Text ranktext = GameObject.Find("Rank Text").GetComponent<UnityEngine.UI.Text>();

            yield return Measure.Frames().Run();
        }
    }
}
