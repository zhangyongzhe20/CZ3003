using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class ChooseCharacters : MonoBehaviour
{
    public static string character;

    public void emptyWorld()
    {
        if (ChooseWorld.worldVisited != null)
        {
            bool[] worldVisited = { false, false, false, false, false };
            ChooseWorld.worldVisited = worldVisited;
        }
    }

    public void ChooseVirtualGuy()
    {
        character = "1";
        emptyWorld();
        SceneManager.LoadScene("ChooseWorld");
    }

    public void ChooseMaskDude()
    {
        character = "2";
        emptyWorld();
        SceneManager.LoadScene("ChooseWorld");
    }

    public void ChooseNinjaFrog()
    {
        character = "3";
        emptyWorld();
        SceneManager.LoadScene("ChooseWorld");
    }
}
