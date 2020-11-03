using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ChooseWorld : MonoBehaviour
{
    public static int world;
    public static int section = 1;
    public static int level = 1;
    public static int totalScore = 0;
    public static bool[] worldVisited = {false, false, false, false, false};
    public static WorldScoreRecord scoreRecord = new WorldScoreRecord();

    // Start is called before the first frame update
    void Start()
    {
        for(int i = 0; i < 5; i++)
        {
            GameObject.Find("Canvas").transform.GetChild(4 + i).gameObject.SetActive(false);
            if (worldVisited[i] == true)
            {
                GameObject.Find("Canvas").transform.GetChild(2).GetChild(i).GetChild(0).gameObject.SetActive(false);
                GameObject.Find("Canvas").transform.GetChild(4 + i).gameObject.SetActive(true);
            }
        }
        Debug.Log("scene ready");
    }

    // Update is called once per frame
    void Update()
    {
        
    }


    public void setVars(int worldChoice)
    {
        world = worldChoice;
        section = 1;
        level = 1;
        worldVisited[worldChoice - 1] = true;
    }

    public void ChooseWorld1()
    {
        setVars(1);
        SceneManager.LoadScene("World1");
    }

    public void ChooseWorld2()
    {
        setVars(2);
        SceneManager.LoadScene("World2");
    }

    public void ChooseWorld3()
    {
        setVars(3);
        SceneManager.LoadScene("World3");
    }

    public void ChooseWorld4()
    {
        setVars(4);
        SceneManager.LoadScene("World4");
    }

    public void ChooseWorld5()
    {
        setVars(5);
        SceneManager.LoadScene("World5");
    }
}
