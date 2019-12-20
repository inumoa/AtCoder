# coding:utf-8


def bellman_ford(V, E, s):
    """ 始点sから残りのノードへの最短経路を求めるベルマンフォード法
    :param V: 頂点数
    :param E: (ノード1, ノード2, コスト)のタプルのリスト
    :param s: 始点とするノード
    :return : (距離リスト, 最短経路, 負の辺によるループが存在するか)a
    """
    ##### 前処理 #####
    from collections import defaultdict
    # INFの定義
    INF = 2**63 - 1
    # 最短経路情報を格納する辞書
    dist = defaultdict(lambda: INF) # 始点から始点への移動コスト
    dist[s] = 0
    # 移動経路の履歴
    pre = {}

    ##### 最短経路算出 #####
    # 高々|V|-1回の探索でいい(|V|回以上更新がある場合は負の閉路が存在)
    for i in range(V-1):
        for n1, n2, w in E:
            # 始点からi回の探索でたどり着けない頂点は考慮しない
            # 始点 -> n2 までの最短距離 > 始点 -> n1 までの最短距離 + n1 -> n2 への移動コスト
            # の場合より短い経路が発見できたと言うことなので情報を更新
            if dist[n1] != INF and dist[n2] > dist[n1] + w:
                dist[n2] = dist[n1] + w
                pre[n2] = n1

    ##### 負の閉路検出 #####
    is_cycle = False
    for n1, n2, w in E:
        # 正しい最短距離が求まったと仮定(重要)
        # 始点 -> n1 までの最短距離 + n1 -> n2 への移動コスト < 始点 -> n2 までの最短経路
        if dist[n1] + w < dist[n2]:
            is_cycle = True

    return dist, pre, is_cycle


N, M = map(int, input().split())
abc_list = [list(map(int, input().split())) for _ in range(M)]
abc_list = [[abc[0], abc[1], -abc[2]]for abc in abc_list]

dist, pre, is_cycle = bellman_ford(N, abc_list, 1)

path_list = [N]
if is_cycle:
    while True:
        next_path = pre[N]
        if next_path in path_list:
            break
        path_list.append(next_path)

if not is_cycle or 1 not in path_list:
    print(-dist[N])
else:
    print('inf')
