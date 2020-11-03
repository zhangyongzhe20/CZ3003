using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;
using UnityEditor;
using Newtonsoft.Json;

public class SubmitMcq : MonoBehaviour
{
    public Dropdown worldDropdown;
    public Dropdown sceneDropdown;
    public Dropdown roleDropdown;
    public InputField questionBodyInput;
    public InputField choiceAInput;
    public InputField choiceBInput;
    public InputField choiceCInput;
    public InputField choiceDInput;
    public Dropdown answerDropdown;
    public Button backButton;
    public Button submitButton;
    public string questionBody;


    void SubmitOnClick()
    {
        StartCoroutine(SubmitMCQRequest());
    }

    IEnumerator SubmitMCQRequest()
    {
        // create answer list
        List<QuestionAnswer> answers = new List<QuestionAnswer>();
        answers.Add(new QuestionAnswer(choiceAInput.text, GetDropdownValue(answerDropdown) == "A"));
        answers.Add(new QuestionAnswer(choiceBInput.text, GetDropdownValue(answerDropdown) == "B"));
        answers.Add(new QuestionAnswer(choiceCInput.text, GetDropdownValue(answerDropdown) == "C"));
        answers.Add(new QuestionAnswer(choiceDInput.text, GetDropdownValue(answerDropdown) == "D"));


        QuestionSubmission submission = new QuestionSubmission(GlobalVars.email, questionBodyInput.text, answers);
        string jsonToSend = JsonConvert.SerializeObject(submission);
        UnityWebRequest req = UnityWebRequest.Post("http://47.74.186.167:8000/api/questions/create", "");
        req.uploadHandler = new UploadHandlerRaw(System.Text.Encoding.UTF8.GetBytes(jsonToSend));
        req.SetRequestHeader("Content-Type", "application/json");
        req.SetRequestHeader("Authorization", "Token " + GlobalVars.token);
        yield return req.SendWebRequest();

        if (req.isNetworkError || req.isHttpError)
        {
            Debug.Log(req.error);
            //EditorUtility.DisplayDialog("Netowrk Error", "Please try again later", "Ok");
        }
        else
        {
            //EditorUtility.DisplayDialog("Success", "Your question has been posted!", "Ok");
            SceneManager.LoadScene("MainMenu");
        }
    }

    string GetDropdownValue(Dropdown dropdown)
    {
        int index = dropdown.value;
        string choiceString = dropdown.options[index].text;
        return choiceString;
    }

    void BackOnClick()
    {
        SceneManager.LoadScene(sceneName: "MainMenu");
    }

    // Start is called before the first frame update
    void Start()
    {
        submitButton.onClick.AddListener(SubmitOnClick);
        backButton.onClick.AddListener(BackOnClick);
    }
}
