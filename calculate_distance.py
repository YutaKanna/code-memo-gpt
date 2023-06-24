import itertools

def calculate_distance(city1, city2):
    # 2つの都市の距離を計算する関数（適宜実装してください）
    # ここではユークリッド距離を使用します
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def traveling_salesman(cities):
    # 全ての都市の組み合わせを生成
    permutations = list(itertools.permutations(cities))
    
    # 最短経路とその距離を初期化
    shortest_distance = float('inf')
    shortest_path = []
    
    # 全ての組み合わせについて最短経路を探索
    for path in permutations:
        total_distance = 0
        
        # 経路の距離を計算
        for i in range(len(path)-1):
            total_distance += calculate_distance(path[i], path[i+1])
        
        # 最短経路かどうかを判定
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path
    
    return shortest_path, shortest_distance

# 都市の座標データ（例）
cities = [(0, 0), (1, 5), (2, 3), (5, 2)]

# 近似解を求める
shortest_path, shortest_distance = traveling_salesman(cities)

# 結果の出力
print("最短経路:", shortest_path)
print("最短距離:", shortest_distance)
