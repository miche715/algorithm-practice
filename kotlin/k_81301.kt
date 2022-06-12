// https://programmers.co.kr/learn/courses/30/lessons/81301
// 숫자 문자열과 영단어

class k_81301
{
    fun solution(str: String): Int
    {
        var answer: String = ""
        val num = mutableMapOf<String, String>()
        val stack = mutableListOf<String>()
        var key: String

        num.put("zero", "0"); num.put("one", "1")
        num.put("two", "2"); num.put("three", "3")
        num.put("four", "4"); num.put("five", "5")
        num.put("six", "6"); num.put("seven", "7")
        num.put("eight", "8"); num.put("nine", "9")

        for(s in str)
        {
            if(s.isDigit())
            {
                answer = answer + s
            }
            else
            {
                stack.add(s.toString())
                key = stack.joinToString("")
                if(num.containsKey(key))
                {
                    answer = answer + num.get(key)
                    stack.clear()
                }
            }
        }
        
        return answer.toInt()
    }
}

fun main()
{
    val s = k_81301()

    println(s.solution("123"))
}