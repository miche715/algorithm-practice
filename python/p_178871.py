# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 달리기 경주

def solution(players, callings):
    player_indices = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        index = player_indices[calling]
        previous_player = players[index - 1]
        players[index - 1], players[index] = players[index], players[index - 1]
        player_indices[calling] = player_indices[calling] - 1
        player_indices[previous_player] = player_indices[previous_player] + 1
    
    return players