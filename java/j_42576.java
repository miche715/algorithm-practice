// https://programmers.co.kr/learn/courses/30/lessons/42576
// 완주하지 못한 선수

import java.util.*;

class Solution
{
    public String solution(String[] participant, String[] completion)
    {
        HashMap<String, Integer> co = new HashMap<>();
        int i;

        for(i = 0; i < completion.length; i++)
        {
            co.put(completion[i], co.getOrDefault(completion[i], 0) + 1);
        }

        for(i = 0; i < participant.length; i++)
        {
            if(co.getOrDefault(participant[i], 0) == 0)
            {
                return participant[i];
            }
            else if(co.getOrDefault(participant[i], 0) > 0)
            {
                co.put(participant[i], co.get(participant[i]) - 1);
            }
        }

        return null;
    }
}