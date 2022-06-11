// https://programmers.co.kr/learn/courses/30/lessons/42579
// 베스트앨범

import java.util.*;

class Solution
{
        public int[] solution(String[] genres, int[] plays)
    {
        int[] answer;
        ArrayList<Integer> aa = new ArrayList<>();
        HashMap<String, Integer> mh = new HashMap<>();
        String[] sg;
        Integer[] sp;
        int max, mid;
        int maxi, midi;
        int cnt;
        int i, j;

        for(i = 0; i < genres.length; i++)
        {
            mh.put(genres[i], mh.getOrDefault(genres[i], 0) + plays[i]);
        }
        sg = new String[mh.size()];
        sp = new Integer[mh.size()];

        i = 0;
        for(String key : mh.keySet())
        {
            sp[i++] = mh.get(key);
        }
        Arrays.sort(sp, Collections.reverseOrder());

        for(i = 0; i < sp.length; i++)
        {
            for(String key : mh.keySet())
            {
                if(mh.get(key).equals(sp[i]))
                {
                    sg[i] = key;
                }
            }
        }
        
        for(i = 0; i < sg.length; i++)
        {
            max = 0;
            mid = 0;
            maxi = -1;
            midi = -1;
            cnt = 0;

            for(j = 0; j < genres.length; j++)
            {
                if(genres[j].equals(sg[i]))
                {
                    if(plays[j] > max)
                    {
                        mid = max;
                        midi = maxi;
                        max = plays[j];
                        maxi = j;

                        cnt++;
                    }
                    else if(plays[j] > mid)
                    {
                        mid = plays[j];
                        midi = j;

                        cnt++;
                    }
                }
            }

            aa.add(maxi);
            if(cnt >= 2)
            {
                aa.add(midi);
            }
        }

        answer = new int[aa.size()];
        for(i = 0; i < aa.size(); i++)
        {
            answer[i] = aa.get(i);
        }

        return answer;
    }
}