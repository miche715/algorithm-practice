// https://programmers.co.kr/learn/courses/30/lessons/76501
// 음양 더하기

class k_76501
{
    fun solution(absolutes: IntArray, signs: BooleanArray): Int
    {
        var answer = 0

        for(i in absolutes.indices)
        {
            if(signs[i])
            {
                answer = answer + absolutes[i]
            }
            else
            {
                answer = answer + (absolutes[i] * -1)
            }
        }

        return answer
    }
}

fun main()
{
    val s = k_76501()

    println(s.solution(intArrayOf(4, 7, 12), booleanArrayOf(true,false,true)))
}