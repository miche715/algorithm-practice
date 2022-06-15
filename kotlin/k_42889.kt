// https://programmers.co.kr/learn/courses/30/lessons/42889?language=kotlin
// 실패율

class k_42889
{
    fun solution(num: Int, stages: IntArray): MutableList<Int>
    {
        var answer = mutableListOf<Int>()
        var player = stages.size
        val challenger = mutableMapOf<Int, Int>()  // {스테이지 번호, 도전자 수}
        val failure = mutableMapOf<Int, Double>()  // {스테이지 번호, 실패율}
        val sortedByValue: List<Pair<Int, Double>>

        for(i in 1..num)
        {
            challenger[i] = 0
            failure[i] = 0.0
        }
        
        stages.forEach()
        {
            if(it != num + 1)
            {
                challenger[it] = challenger[it]!!.plus(1)
            }      
        }
        
        for(i in 1..num)
        {
            failure[i] = challenger[i]!! / player.toDouble()
            player = player - challenger[i]!!
            if(player == 0)
            {
                break
            }
        }

        sortedByValue = failure.toList().sortedWith(compareByDescending({it.second}))
        for(s in sortedByValue)
        {
            answer.add(s.first)
        }

        return answer
    }
}

fun main()
{
    val s = k_42889()

    println(s.solution(5, intArrayOf(3, 3, 3, 3)))
}
