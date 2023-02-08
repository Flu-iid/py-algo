from itertools import chain, combinations

t = int(input())
for i in range(t):
    input_string = input().split(" ")
    n_tracks, m_capacity = int(input_string[0]), int(input_string[1])
    track_list = []
    for track_length in range(n_tracks):
        track_length = int(input())
        track_list.append(track_length)
    power_sets = list(chain.from_iterable(combinations(
        track_list, r) for r in range(len(track_list)+1)))
    chosen_list = []
    for s in power_sets:
        if sum(s) <= m_capacity:
            if len(s) > len(chosen_list):
                chosen_list = list(s)
    print(len(chosen_list))


# i/o format probably
