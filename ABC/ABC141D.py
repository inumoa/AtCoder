import heapq

N, M = map(int, input().split())
a_list = list(map(int, input().split()))

minus_a_list = [-a for a in a_list]
heapq.heapify(minus_a_list)

for _ in range(M):
    value = -(heapq.heappop(minus_a_list))
    heapq.heappush(minus_a_list, -(value//2))

print(-sum(minus_a_list))