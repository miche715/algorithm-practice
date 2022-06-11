// https://programmers.co.kr/learn/courses/30/lessons/49993
// 스킬트리

import java.util.*;

class Solution
{    
    public int solution(String skill, String[] skill_trees)
    {
        int answer = 0;
        int slen = skill.length();
        int tlen = skill_trees.length;
        String nt;
        Boolean flag1 = true;
        Boolean flag2 = false;
        int range;
        int i;
        int j;
        int t;
        
        for(i = 0; i < tlen; i++)
        {
        	flag2 = false;
        	
        	nt = skill_trees[i];
        	
        	range = nt.length();
        	for(j = 0; j < slen; j++)
        	{
    			flag1 = false;
        		for(t = 0; t < range; t++)
        		{
        			if(nt.charAt(t) == skill.charAt(slen - j - 1))
        			{
        				flag1 = true;
        				range = t;
        				
        				break;
        			}
        		}
        		if(flag1)
        		{
        			flag2 = true;
        		}
        		if(!flag1 && flag2)
        		{
        			break;
        		}
        	}
        	
        	if(flag1 == flag2)
        	{
        		answer++;
        	}
        }
        	
        return answer;
    }
}