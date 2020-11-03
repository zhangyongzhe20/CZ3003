using System;

[Serializable]
public class LoginResponse
{
    public UserInfo user;
    public string token;
}

[Serializable]
public class UserInfo
{
    public int id;
    public string email;
    public string name;
    public int distanceToNPC;
    public int overallScore;
    public bool containBonus;
    public string role;
}
