using System.Collections.Generic;
using System;

public class QuestionSubmission
{
    public string Proposer;
    public string questionBody;
    public List<QuestionAnswer> questionAns;

    public QuestionSubmission(string user, string qnBody, List<QuestionAnswer> answers)
    {
        Proposer = user;
        questionBody = qnBody;
        questionAns = answers;
    }

}

public class QuestionAnswer
{
    public string questionText;
    public bool isCorrect;

    public QuestionAnswer(string txt, bool correct)
    {
        questionText = txt;
        isCorrect = correct;
    }
}
