// https://programmers.co.kr/learn/courses/30/lessons/77884
// 약수의 개수와 덧셈

class k_77884
{
    fun solution(left: Int, right: Int): Int
    {
        var answer: Int = 0
        var sum = 0

        for(n in left..right)
        {
            for(i in 1..n)
            {
                if(n % i == 0)
                {
                    sum = sum + 1
                }
            }
            if(sum % 2 == 0)
            {
                answer = answer + n
            }
            else
            {
                answer = answer - n
            }
            sum = 0
        }

        return answer
    }
}

fun main()
{
    val s = k_77884()

    println(s.solution(1, 1))
}