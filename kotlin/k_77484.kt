// https://programmers.co.kr/learn/courses/30/lessons/77484?language=kotlin
// 로또의 최고 순위와 최저 순위

class k_77484
{
    fun solution(lottos: IntArray, win_nums: IntArray): Array<Int>
    {
        var answer = Array<Int>(2){0}
        val lotto = lottos.toMutableList()
        val win = win_nums.toMutableList()
        var same = 0
        var luck = 0

        for(l in lotto)
        {
            if(l == 0)
            {
                luck = luck + 1

                continue
            }
            else
            {
                if(l in win)
                {
                    win.remove(l)
                    same = same + 1
                }
            }
        }
        
        answer[0] = 7 - (luck + same)
        answer[1] = 7 - same
        if(answer[0] == 7)
        {
            answer[0] = 6
        }
        if(answer[1] == 7)
        {
            answer[1] = 6
        }

        return answer
    }
}

fun main()
{
    val s = k_77484()

    println(s.solution(intArrayOf(44, 1, 0, 0, 31, 25), intArrayOf(31, 10, 45, 1, 6, 19)))
}