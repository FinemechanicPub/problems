
def play(ratings: list[int]) -> list[int]:
    n = len(ratings)
    answer = [0] * n
    active = [1] * n

    prev_players = [i - 1 for i in range(n)]
    next_players = [i + 1 for i in range(n)]
    prev_players[0] = n - 1
    next_players[-1] = 0

    def weak(player: int) -> bool:
        return (ratings[player] < min(
            ratings[next_players[player]], ratings[prev_players[player]]
        ))

    weak_players = [i for i in range(n) if weak(i)]

    for weak_player in weak_players:
        player = weak_player
        while weak(player):
            prev_player = prev_players[player]
            next_player = next_players[player]
            if prev_player == next_player:
                break
            next_players[prev_player] = next_player
            prev_players[next_player] = prev_player
            answer[player] = active[player]
            active[next_player] = max(active[next_player], active[player] + 1)
            active[prev_player] = max(active[prev_player], active[player] + 1)
            if ratings[next_player] > ratings[prev_player]:
                player = prev_player
            else:
                player = next_player
    return answer


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n, f"Expected {n} values, got {len(a)}"
    print(*play(a), sep=" ")
