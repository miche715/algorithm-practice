// https://programmers.co.kr/learn/courses/30/lessons/42842
// 카펫

import java.util.*;

class Solution
{
    public int[] solution(int brown, int yellow)
    {
        int[] answer = new int[2];
        ArrayList<Integer> divisor = new ArrayList<>();
        int x, y;
        int i = 1;

        for(i = 1; i <= yellow; i++)
        {
            if(yellow % i == 0)
            {
                divisor.add(i);
            }
        }

        for(i = 0; i < (divisor.size() / 2) + (divisor.size() % 2); i++)
        {
            x = (divisor.get(divisor.size() - 1 - i)) + 2;
            y = divisor.get(i);

            if((x + y) * 2 == brown)
            {
                answer[0] = x;
                answer[1] = y + 2;

                break;
            }
        }

        return answer;
    }
}