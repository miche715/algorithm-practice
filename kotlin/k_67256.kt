// https://programmers.co.kr/learn/courses/30/lessons/67256
// 키패드 누르기

import kotlin.math.*

class k_67256
{
    fun solution(numbers: IntArray, hand: String): String
    {
        var answer = ""
        var left = 11
        var right = 12
        val pos = mapOf(
            1 to arrayOf(0, 0), 2 to arrayOf(1, 0), 3 to arrayOf(2, 0), 
            4 to arrayOf(0, 1), 5 to arrayOf(1, 1), 6 to arrayOf(2, 1), 
            7 to arrayOf(0, 2), 8 to arrayOf(1, 2), 9 to arrayOf(2, 2), 
            11 to arrayOf(0, 3), 0 to arrayOf(1, 3), 12 to arrayOf(2, 3), 
        )

        for(n in numbers)
        {
            if(n == 1 || n == 4 || n == 7)
            {
                answer = answer + "L"
                left = n
            }
            else if(n == 3 || n == 6 || n == 9)
            {
                answer = answer + "R"
                right = n
            }
            else  // 2, 5, 8, 0
            {
                if(abs(pos.get(n)!![0] - pos.get(left)!![0]) + abs(pos.get(n)!![1] - pos.get(left)!![1]) < abs(pos.get(n)!![0] - pos.get(right)!![0]) + abs(pos.get(n)!![1] - pos.get(right)!![1]))
                {
                    answer = answer + "L"
                    left = n
                }
                else if(abs(pos.get(n)!![0] - pos.get(left)!![0]) + abs(pos.get(n)!![1] - pos.get(left)!![1]) > abs(pos.get(n)!![0] - pos.get(right)!![0]) + abs(pos.get(n)!![1] - pos.get(right)!![1]))
                {
                    answer = answer + "R"
                    right = n
                }
                else
                {
                    if(hand == "left")
                    {
                        answer = answer + "L"
                        left = n
                    }
                    else
                    {
                        answer = answer + "R"
                        right = n
                    }
                }
            }
        }

        return answer
    }
}

fun main()
{
    val s = k_67256()

    println(s.solution(intArrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 0), "right"))
}

/*
1 2 3
4 5 6
7 8 9
* 0 #

(0, 0) (1, 0) (2, 0)
(0, 1) (1, 1) (2, 1)
(0, 2) (1, 2) (2, 2)
       (1, 3)
       
*/