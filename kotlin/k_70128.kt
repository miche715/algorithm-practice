// https://programmers.co.kr/learn/courses/30/lessons/70128
// 내적

class k_70128
{
    fun solution(a: IntArray, b: IntArray): Int
    {
        var answer = 0

        for(i in a.indices)
        {
            answer = answer + a[i] * b[i]
        }

        return answer
    }
}

fun main()
{
    val s = k_70128()

    println(s.solution(intArrayOf(1,2,3,4), intArrayOf(-3,-1,0,2)))
}