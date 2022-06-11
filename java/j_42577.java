// https://programmers.co.kr/learn/courses/30/lessons/42577
// 전화번호 목록

import java.util.*;

class Solution
{
    public boolean solution(String[] phone_book)
    {
        boolean answer = true;
        int i;

        Arrays.sort(phone_book);
        for(i = 0; i < phone_book.length - 1; i++)
        {
            if(phone_book[i].length() <= phone_book[i + 1].length())
            {
                if (phone_book[i].equals(phone_book[i + 1].substring(0, phone_book[i].length())))
                {
                    answer = false;

                    break;
                }
            }
        }

        return answer;
    }
}