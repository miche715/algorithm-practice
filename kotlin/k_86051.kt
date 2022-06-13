// https://programmers.co.kr/learn/courses/30/lessons/86051
// 없는 숫자 더하기

class k_86051
{
    fun solution(numbers: IntArray): Int
    {
        var answer = 0
        val num = mutableListOf<Int>(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

        for(n in numbers)
        {
            num.remove(n)
        }

        for(n in num)
        {
            answer = answer + n
        }

        return answer
    }
}

fun main()
{
    val s = k_86051()

    println(s.solution(intArrayOf(1,2,3,4,6,7,8,0)))
}