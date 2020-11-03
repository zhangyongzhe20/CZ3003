using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;
using System.Collections;
using System.Collections.Generic;
//using UnityEditor;
using TMPro;
using Newtonsoft.Json;


public class Login : MonoBehaviour
{
    public GameObject Email;
    public GameObject Password;
    private string email;
    private string password;

    IEnumerator LoginPostRequest()
    {
        WWWForm formData = new WWWForm();
        formData.AddField("email", email);
        formData.AddField("password", password);

        UnityWebRequest req = UnityWebRequest.Post("http://47.74.186.167:8000/api/login/", formData);
        yield return req.SendWebRequest();

        if (req.isNetworkError || req.isHttpError)
        {
            //EditorUtility.DisplayDialog("Login Failed", "Please check your credentials", "Ok");
            Debug.Log(req.error);
        }
        else
        {
            string response_body = req.downloadHandler.text;
            LoginResponse data = JsonConvert.DeserializeObject<LoginResponse>(response_body);

            // assign global variable
            GlobalVars.token = data.token;
            GlobalVars.email = email;
            GlobalVars.id = data.user.id;

            // scene change
            SceneManager.LoadScene("MainMenu");
        }

    }

    public void LoginButton()
    {
        if (email == "" || password == "")
        {
            //EditorUtility.DisplayDialog("Alert", "Please enter your credentials", "Ok");
        }
        else
        {
            StartCoroutine(LoginPostRequest());
        }
    }


    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Tab))
        {
            if (Email.GetComponent<TMP_InputField>().isFocused)
            {
                Password.GetComponent<TMP_InputField>().Select();
            }
        }
        if (Input.GetKeyDown(KeyCode.Return))
        {
            if (password != "" && password != "")
            {
                LoginButton();
            }
        }
        email = Email.GetComponent<TMP_InputField>().text;
        password = Password.GetComponent<TMP_InputField>().text;       
    }
}
