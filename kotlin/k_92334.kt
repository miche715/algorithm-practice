// https://programmers.co.kr/learn/courses/30/lessons/92334?language=kotlin
// 신고 결과 받기

class k_92334
{
    fun solution(id: Array<String>, report: Array<String>, k: Int): Array<Int>
    {
        var answer = Array<Int>(id.size){0}
        val user_reporting = mutableMapOf<String, ArrayList<String>>()  // {유저: [그 유저가 신고한 유저들]}
        val user_reported = mutableMapOf<String, Int>()  // {유저: 그 유저가 신고 당한 횟수}
        var arr: List<String>

        for(i in id)
        {
            user_reporting[i] = arrayListOf()
            user_reported[i] = 0
        }

        for(r in report)
        {
            arr = r.split(" ")
            if(!user_reporting[arr[0]]!!.contains(arr[1]))
            {
                user_reporting[arr[0]]!!.add(arr[1])
                user_reported[arr[1]] = user_reported[arr[1]]!!.plus(1)
            }
        }

        for(i in id)
        {
            if(user_reported[i]!! >= k)
            {
                for(j in answer.indices)
                {
                    if(user_reporting[id[j]]!!.contains(i))
                    {
                        answer[j] = answer[j] + 1
                    }
                }
            }
        }

        return answer
    }
}

fun main(): Unit
{
    val p = k_92334()

    println(p.solution(arrayOf("muzi", "frodo", "apeach", "neo"), arrayOf("muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"), 2))
}

/*
{muzi=1, frodo=2, apeach=0, neo=2}

*/