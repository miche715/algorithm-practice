// https://programmers.co.kr/learn/courses/30/lessons/42578
// 위장

import java.util.*;

class Solution
{
    public int solution(String[][] clothes)
    {
        int answer = 0;
        int tmp = 1;
        HashMap<String, Integer> cloth = new HashMap<>();
        int i;

        for(i = 0; i < clothes.length; i++)
        {
            cloth.put(clothes[i][1], cloth.getOrDefault(clothes[i][1], 0) + 1);
        }
        
        for (String key : cloth.keySet())
        {
            tmp = tmp * (cloth.get(key) + 1);
        }
        answer = answer + tmp - 1;
        
        return answer;
    }
}