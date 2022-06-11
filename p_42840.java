// https://programmers.co.kr/learn/courses/30/lessons/42840
// 모의고사

import java.util.*;

class Solution
{
    public int[] solution(int[] answers)
    {
        int[] answer;
        ArrayList<Integer> ans = new ArrayList<>();
        int[][] student = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int[] score = {0, 0, 0}; //0 0 0
        int max = -1;
        int i, j, k = 1;

        for(i = 0; i < student.length; i++)
        {
            for(j = 0; j < answers.length; j++)
            {
                if(answers[j] == student[i][j % student[i].length])
                {
                    score[i]++;
                }
            }
        }

        for(i = 0; i < score.length; i++)
        {
            if(score[i] > max)
            {
                ans.add(0, i + 1);
                max = score[i];
            }
            else if(score[i] == max)
            {
                ans.add(k++, i + 1);
            }
        }
        
        answer = new int[k];
        for(i = 0; i < answer.length; i++)
        {
            answer[i] = ans.get(i);
        }

        return answer;
    }
}