using System;
using System.Collections.Generic;

//[Serializable]
//public class GetQuestionResponse
//{
//    public List<Question> questions;
//}


[Serializable]
public class GetQuestionResponse
{
    public string id;
    public string questionBody;
    public List<Answer> questionAns;
}

[Serializable]
public class Answer
{
    public string questiontext;
    public bool isCorrect;
}
