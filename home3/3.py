maze = [
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0]
]

# 定義一個遞迴函數，用於深度優先搜尋
def dfs(x, y, path):
    # 判斷是否到達終點
    if x == len(maze)-1 and y == len(maze[0])-1:
        path.append((x, y))
        return path

    # 標記當前位置已被訪問
    maze[x][y] = 2

    # 嘗試向四個方向移動
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy

        # 判斷下一個位置是否越界或已訪問過
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            # 遞迴搜索下一個位置
            new_path = dfs(nx, ny, path + [(x, y)])
            if new_path is not None:
                # 如果找到了終點，返回完整路徑
                return new_path

    # 沒有找到路徑，返回空
    return None

# 執行深度優先搜尋
path = dfs(0, 0, [])

# 輸出結果
if path is None:
    print("沒有找到路徑")
else:
    print("找到了路徑：")
    for p in path:
        print(p)
