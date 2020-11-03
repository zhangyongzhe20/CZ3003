using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
using Newtonsoft.Json;
using TMPro;
using System;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;
//using UnityEditor;
using System.Linq;
using System.Collections;

public class Game : MonoBehaviour
{
    // for pre-integration testing
    //string myJsonResponseForMCQ = "[{\"id\": 1, \"questionBody\": \"1 + 1 = ?\",\"questionAns\": [{\"questionText\": \"1\", \"isCorrect\": false}, {\"questionText\": \"2\",\"isCorrect\": true},{\"questionText\": \"3\",\"isCorrect\": false},{\"questionText\": \"4\",\"isCorrect\": false}]}, {\"id\": 2,\"questionBody\": \"2 + 2 = ?\",\"questionAns\": [{\"questionText\": \"2\",\"isCorrect\": false},{\"questionText\": \"4\", \"isCorrect\": true}, {\"questionText\": \"5\", \"isCorrect\": false},{\"questionText\": \"6\",\"isCorrect\": false}]}, {\"id\": 3,\"questionBody\": \"10 * 10 = ?\",\"questionAns\": [{\"questionText\": \"100\",\"isCorrect\": true},{\"questionText\": \"2\",\"isCorrect\": false},{\"questionText\": \"4\",\"isCorrect\": false},{\"questionText\": \"5\",\"isCorrect\": false}]},{\"id\": 4, \"questionBody\": \"1 + 1 = ?\",\"questionAns\": [{\"questionText\": \"1\", \"isCorrect\": false}, {\"questionText\": \"2\",\"isCorrect\": true},{\"questionText\": \"3\",\"isCorrect\": false},{\"questionText\": \"4\",\"isCorrect\": false}]}, {\"id\": 5,\"questionBody\": \"2 + 2 = ?\",\"questionAns\": [{\"questionText\": \"2\",\"isCorrect\": false},{\"questionText\": \"4\", \"isCorrect\": true}, {\"questionText\": \"5\", \"isCorrect\": false},{\"questionText\": \"6\",\"isCorrect\": false}]}]";
    //string myJsonResponseForMCQ = "";
    //string myJsonResponseForBlankFill = "[{\"id\": 1, \"questionBody\": \"1 + 1 = ?\", \"questionAns\": [{\"questionText\": \"2\", \"isCorrect\": true}]}, {\"id\": 2,\"questionBody\": \"2 + 2 = ?\",\"questionAns\": [{\"questionText\": \"4\", \"isCorrect\": true}]}, {\"id\": 3,\"questionBody\": \"10 * 10 = ?\", \"questionAns\": [{\"questionText\": \"100\", \"isCorrect\": true}]}]";

    string questionJsonResponse = "";
    int currentQuestionIndex = 0;
    bool[] userAnswers = {false, false, false, false, false};
    int sectionScore = 0;
    
    //List<MCQQuestion> questionsList;
    


    // get request to get questions
    IEnumerator GetQuestionRequest()
    {
        WWWForm formData = new WWWForm();
        formData.AddField("world", ChooseWorld.world.ToString());
        formData.AddField("section", ChooseWorld.section);
        formData.AddField("questionLevel", ChooseWorld.level);
        formData.AddField("role", ChooseCharacters.character);

        UnityWebRequest req = UnityWebRequest.Post("http://47.74.186.167:8000/api/questions", formData);
        req.SetRequestHeader("Authorization", "Token " + GlobalVars.token);

        yield return req.SendWebRequest();


        // for pre-integration testing
        //yield return 1;

        if (req.isNetworkError || req.isHttpError)
        {
            //EditorUtility.DisplayDialog("Error", "Please check your network connection", "Ok");
            
        }
        else
        {
            string response_body = req.downloadHandler.text;
            questionJsonResponse = response_body;

            // for pre-integration testing
            //questionJsonResponse = myJsonResponseForMCQ;
            var questionsList = JsonConvert.DeserializeObject<List<Question>>(questionJsonResponse);

            Debug.Log(questionsList.Count);

            if (questionsList[0].questionAns.Count == 1)
            {
                LoadingBlankFillQuestions(questionsList[0].questionBody, questionsList[0].questionAns[0].questionText, 1);
            }
            else
            {
                LoadingMCQQuestions(questionsList[0].questionBody, questionsList[0].questionAns, 1);
            }

            GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(true);

        }
    }


    // post request to submit question answer
    IEnumerator SubmitAnswerRequest(int questionID, string studentAnswer, bool isAnswerCorrect)
    {
        WWWForm formData = new WWWForm();
        formData.AddField("world", ChooseWorld.world.ToString());
        formData.AddField("section", ChooseWorld.section);
        formData.AddField("questionID", questionID);
        formData.AddField("studentID", GlobalVars.id);
        formData.AddField("studentAnswer", studentAnswer);
        formData.AddField("isAnsweredCorrect", isAnswerCorrect.ToString());

        if (isAnswerCorrect)
        {
            formData.AddField("pointGain", 1);
        }
        else
        {
            formData.AddField("pointGain", 0);
        }

        UnityWebRequest req = UnityWebRequest.Post("http://47.74.186.167:8000/api/questions/submit", formData);
        req.SetRequestHeader("Authorization", "Token " + GlobalVars.token);

        yield return req.SendWebRequest();

        if (req.isNetworkError || req.isHttpError)
        {
            //Debug.Log("API call error");
            //EditorUtility.DisplayDialog("Error", "Please check your network connection", "Ok");
        }
        else
        {
            Debug.Log("API call success");
        }
    }




    // Start is called before the first frame update
    void Start()
    {
        SpriteRenderer[] sprites = GetComponentsInChildren<SpriteRenderer>();

        // Render the character according to user's choice
        LoadingCharacter(sprites);

        // call API
        StartCoroutine(GetQuestionRequest());
        
    }

    void Update()
    {
        
    }


    void LoadingCharacter(SpriteRenderer[] sprites)
    {
        if (ChooseCharacters.character == "1")
        {
            sprites[0].enabled = true;
        }
        else if (ChooseCharacters.character == "2")
        {
            sprites[1].enabled = true;
        }
        else if (ChooseCharacters.character == "3")
        {
            sprites[2].enabled = true;
        }
    }

    void LoadingMCQQuestions(string questionBody, List<QuestionAn> answers, int questionNum)
    {
        GameObject.Find("Canvas").transform.GetChild(1).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(2).gameObject.SetActive(false);

        var questionTitle = String.Format("Question {0}", questionNum);
        //GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(1).gameObject.GetComponent<TextMeshProUGUI>().SetText(questionTitle);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(2).gameObject.GetComponent<TextMeshProUGUI>().SetText(questionBody);

        GameObject.Find("Canvas").transform.GetChild(0).GetChild(7).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(8).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(9).gameObject.SetActive(false);

        GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText(answers[0].questionText);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText(answers[1].questionText);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText(answers[2].questionText);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText(answers[3].questionText);
        
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.GetComponent<Button>().onClick.AddListener(delegate {AnswerMCQQuestions(answers, 0);});
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.GetComponent<Button>().onClick.AddListener(delegate { AnswerMCQQuestions(answers, 1); });
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.GetComponent<Button>().onClick.AddListener(delegate { AnswerMCQQuestions(answers, 2); });
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.GetComponent<Button>().onClick.AddListener(delegate { AnswerMCQQuestions(answers, 3); });

    }

    void AnswerMCQQuestions(List<QuestionAn> answers, int choice)
    {
        string userAnswer = GameObject.Find("Canvas").transform.GetChild(0).GetChild(3+choice).gameObject.GetComponent<Button>().transform.GetChild(0).GetComponent<TextMeshProUGUI>().text;

        for (int i = 0; i < 4; i++)
        {
            if(answers[i].isCorrect == true)
            {
                if (userAnswer == answers[i].questionText)
                {
                    Debug.Log("correct");
                    sectionScore += 1;
                    userAnswers[currentQuestionIndex] = true;
                }
                else
                {
                    Debug.Log("wrong");
                    userAnswers[currentQuestionIndex] = false;
                }
            }
        }

        var questionsList = JsonConvert.DeserializeObject<List<Question>>(questionJsonResponse);
        int questionID = questionsList[currentQuestionIndex].id;

        StartCoroutine(SubmitAnswerRequest(questionID, userAnswer, userAnswers[currentQuestionIndex]));

        if (currentQuestionIndex <= 3)
        {
            currentQuestionIndex = currentQuestionIndex + 1;

            GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();

            LoadingMCQQuestions(questionsList[currentQuestionIndex].questionBody, questionsList[currentQuestionIndex].questionAns, currentQuestionIndex + 1);
        }
        else
        {
            GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(false);
            GameObject.Find("Canvas").transform.GetChild(1).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(1).GetChild(2).gameObject.GetComponent<TextMeshProUGUI>().SetText(sectionScore.ToString());
            ChooseWorld.totalScore += sectionScore;
            GameObject.Find("Canvas").transform.GetChild(1).GetChild(4).gameObject.GetComponent<TextMeshProUGUI>().SetText(ChooseWorld.totalScore.ToString());

            if (sectionScore >= 3)
            {
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(5).gameObject.GetComponent<TextMeshProUGUI>().SetText("Good Job!");
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(6).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText(String.Format("Go to Level {0}", ChooseWorld.level + 1));
            }
            else
            {
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(5).gameObject.GetComponent<TextMeshProUGUI>().SetText("You Failed!");
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(6).gameObject.SetActive(false);
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(7).gameObject.SetActive(false);
                GameObject.Find("Canvas").transform.GetChild(2).gameObject.SetActive(true);
            }

            // add score to the record
            AddScoreRecord();

            // display change world if it is section 3
            if (ChooseWorld.section == 3)
            {
                if (!ChooseWorld.worldVisited.Contains(false))
                {
                    SceneManager.LoadScene("Victory");
                }
                else
                {
                    GameObject.Find("Canvas").transform.GetChild(1).GetChild(7).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText("Next World");
                }
                
            }
            sectionScore = 0;
        }
    }

    void AddScoreRecord()
    {
        var questionsList = JsonConvert.DeserializeObject<List<Question>>(questionJsonResponse);
        var num_question = questionsList.Count;

        // add section score to the score record
        string currentWorld = ChooseWorld.world.ToString();
        string currentSection = ChooseWorld.section.ToString();
        string currentLevel = ChooseWorld.level.ToString();
        Debug.Log("adding score to record for world: " + currentWorld + ", section: " + currentSection + ", level: " + currentLevel);

        WorldScoreRecord scoreRecord = ChooseWorld.scoreRecord;

        // get WorldScore object
        if (!scoreRecord.worldScores.ContainsKey(currentWorld))
        {
            scoreRecord.worldScores.Add(currentWorld, new WorldScore());
        }

        WorldScore worldScoreRecord = scoreRecord.worldScores[currentWorld];

        // get sectionScore object
        if (!worldScoreRecord.sectionScores.ContainsKey(currentSection))
        {
            worldScoreRecord.sectionScores.Add(currentSection, new SectionScore());
        }

        SectionScore sectionScoreRecord = worldScoreRecord.sectionScores[currentSection];

        // add the level score
        sectionScoreRecord.levelScores.Add(currentLevel, new LevelScore(num_question, sectionScore));
    }

    void LoadingBlankFillQuestions(string questionBody, string answer, int questionNum)
    {
        GameObject.Find("Canvas").transform.GetChild(1).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(2).gameObject.SetActive(false);

        var questionTitle = String.Format("Question {0}", questionNum);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(1).gameObject.GetComponent<TextMeshProUGUI>().SetText(questionTitle);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(2).gameObject.GetComponent<TextMeshProUGUI>().SetText(questionBody);

        GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.SetActive(false);
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.SetActive(false);

        GameObject.Find("Canvas").transform.GetChild(0).GetChild(7).gameObject.GetComponent<TMP_InputField>().text = "";
        GameObject.Find("Canvas").transform.GetChild(0).GetChild(8).gameObject.GetComponent<Button>().onClick.AddListener(delegate { AnswerBlankFillQuestions(answer);});

    }

    void AnswerBlankFillQuestions(string answer)
    {

        if(GameObject.Find("Canvas").transform.GetChild(0).GetChild(7).gameObject.GetComponent<TMP_InputField>().text == answer)
        {
            Debug.Log("correct");
            sectionScore += 1;
            userAnswers[currentQuestionIndex] = true;
        }
        else
        {
            Debug.Log("false");
            userAnswers[currentQuestionIndex] = false;
        }

        if (currentQuestionIndex <= 1)
        {
            currentQuestionIndex = currentQuestionIndex + 1;

            var questionsList = JsonConvert.DeserializeObject<List<Question>>(questionJsonResponse);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(8).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            LoadingBlankFillQuestions(questionsList[currentQuestionIndex].questionBody, questionsList[currentQuestionIndex].questionAns[0].questionText, currentQuestionIndex + 1);
        }
        else
        {
            if (!ChooseWorld.worldVisited.Contains(false))
            {
                SceneManager.LoadScene("Victory");
            }
            GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(false);
            GameObject.Find("Canvas").transform.GetChild(1).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(1).GetChild(2).gameObject.GetComponent<TextMeshProUGUI>().SetText(sectionScore.ToString());
            ChooseWorld.totalScore += sectionScore;
            GameObject.Find("Canvas").transform.GetChild(1).GetChild(4).gameObject.GetComponent<TextMeshProUGUI>().SetText(ChooseWorld.totalScore.ToString());
            GameObject.Find("Canvas").transform.GetChild(1).GetChild(5).gameObject.GetComponent<TextMeshProUGUI>().SetText("Nice Try!");

            if(ChooseWorld.level == 3)
            {
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(6).gameObject.GetComponent<Button>().interactable = false;
            }
            else
            {            
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(6).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText(String.Format("Go to Level {0}", ChooseWorld.level + 1));
            }

            // add score to record
            AddScoreRecord();

            if (ChooseWorld.section == 3)
            {
                GameObject.Find("Canvas").transform.GetChild(1).GetChild(7).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText("Next World");
            }
            sectionScore = 0;
        }
    }

    // get request to get level
    IEnumerator GetNextLevelRequest()
    {
        WWWForm formData = new WWWForm();
        formData.AddField("world", ChooseWorld.world.ToString());
        formData.AddField("section", ChooseWorld.section);
        formData.AddField("questionLevel", ChooseWorld.level);
        formData.AddField("role", ChooseCharacters.character);

        UnityWebRequest req = UnityWebRequest.Post("http://47.74.186.167:8000/api/questions", formData);
        req.SetRequestHeader("Authorization", "Token " + GlobalVars.token);

        yield return req.SendWebRequest();

        // for pre-integration testing
        //yield return 1;

        // for pre-integration testing
        if (req.isNetworkError || req.isHttpError)
            //if (false)
        {
            //EditorUtility.DisplayDialog("Error", "Please check your network connection", "Ok");
        }
        else
        {

            string response_body = req.downloadHandler.text;
            questionJsonResponse = response_body;

            // for pre-integration testing
            //questionJsonResponse = myJsonResponseForBlankFill;

            var questionsList = JsonConvert.DeserializeObject<List<Question>>(questionJsonResponse);
            currentQuestionIndex = 0;
            GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(7).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(8).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(9).gameObject.SetActive(true);

            GameObject.Find("Canvas").transform.GetChild(0).GetChild(8).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();


            if (questionsList[0].questionAns.Count == 1)
            {
                LoadingBlankFillQuestions(questionsList[0].questionBody, questionsList[0].questionAns[0].questionText, 1);
            }
            else
            {
                LoadingMCQQuestions(questionsList[0].questionBody, questionsList[0].questionAns, 1);
            }

        }
    }

    public void LoadNextLevel()
    {
        ChooseWorld.level += 1;
        StartCoroutine(GetNextLevelRequest());
    }


    // get request to get level
    IEnumerator GetNextSectionRequest()
    {
        WWWForm formData = new WWWForm();
        formData.AddField("world", ChooseWorld.world.ToString());
        formData.AddField("section", ChooseWorld.section);
        formData.AddField("questionLevel", ChooseWorld.level);
        formData.AddField("role", ChooseCharacters.character);

        UnityWebRequest req = UnityWebRequest.Post("http://47.74.186.167:8000/api/questions", formData);
        req.SetRequestHeader("Authorization", "Token " + GlobalVars.token);

        yield return req.SendWebRequest();

        // for pre-integration testing
        //yield return 1;

        // for pre-integration testing
        //if (false)
        if (req.isNetworkError || req.isHttpError)
        {
            //EditorUtility.DisplayDialog("Error", "Please check your network connection", "Ok");
        }
        else
        {

            string response_body = req.downloadHandler.text;
            questionJsonResponse = response_body;

            // for pre-integration testing
            //questionJsonResponse = myJsonResponseForMCQ;

            var questionsList = JsonConvert.DeserializeObject<List<Question>>(questionJsonResponse);
            currentQuestionIndex = 0;
            GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.SetActive(true);
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.SetActive(true);

            GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();



            if (questionsList[0].questionAns.Count == 1)
            {
                LoadingBlankFillQuestions(questionsList[0].questionBody, questionsList[0].questionAns[0].questionText, 1);
            }
            else
            {
                LoadingMCQQuestions(questionsList[0].questionBody, questionsList[0].questionAns, 1);
            }

        }
    }

    public void LoadNextSection()
    {
        ChooseWorld.level = 1;
        if (ChooseWorld.section == 3)
        {
            ChooseWorld.section = 1;
            SceneManager.LoadScene("ChooseWorld");
            GameObject.Find("Canvas").transform.GetChild(1).GetChild(7).GetChild(0).gameObject.GetComponent<TextMeshProUGUI>().SetText("Next Section");
        }
        else
        {
            ChooseWorld.section += 1;
            // Call backend API here!
            StartCoroutine(GetNextSectionRequest());

            //var questionsList = JsonConvert.DeserializeObject<List<Question>>(myJsonResponseForMCQ);
            //currentQuestionIndex = 0;
            //GameObject.Find("Canvas").transform.GetChild(0).gameObject.SetActive(true);
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.SetActive(true);
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.SetActive(true);
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.SetActive(true);
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.SetActive(true);

            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(3).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(4).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(5).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();
            //GameObject.Find("Canvas").transform.GetChild(0).GetChild(6).gameObject.GetComponent<Button>().onClick.RemoveAllListeners();

            //LoadingMCQQuestions(questionsList[0].questionBody, questionsList[0].questionAns, 1);
        }

    }

    public void ReturnToMenu()
    {
        ChooseWorld.worldVisited = new bool[5];
        ChooseWorld.scoreRecord = new WorldScoreRecord();
        SceneManager.LoadScene("MainMenu");
    }

    public void GoToFailureSummary()
    {
        SceneManager.LoadScene("Failure");
    }
}


public class QuestionAn
{
    public string questionText { get; set; }
    public bool isCorrect { get; set; }
}

public class Question
{
    public int id { get; set; }
    public string questionBody { get; set; }
    public List<QuestionAn> questionAns { get; set; }
}

//public class BlankFillQuestion
//{
//    public int id { get; set; }
//    public string questionBody { get; set; }
//    public string questionAns { get; set; }
//}