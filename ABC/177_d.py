# https://atcoder.jp/contests/abc177/tasks/abc177_d

class UnionFind:
    # 要素数nで初期化
    def __init__(self, n):
        # 全体の大きさ
        self.n = n
        # -x: グループのサイズ(自身が根) or k(正): 根がk
        self.parent_size = [-1] * n

    # 要素の根を返す
    def leader(self, a):
        # aが根ならa自身を返す
        if self.parent_size[a] < 0:
            return a
        # aが根でないなら根に向かって木をたどる + 根の更新
        self.parent_size[a] = self.leader(self.parent_size[a])
        # 根を返す
        return self.parent_size[a]

    # aとbを結合
    def merge(self, a, b):
        # a,bの根をx,yへ
        x, y = self.leader(a), self.leader(b)
        # 根が同じなら終了
        if x == y:
            return
        # グループのサイズ=要素数 を比較。サイズの小さいほうを大きいほうに繋げるため、x < y ならば、x,yを入れ替える。
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        # サイズの更新: 小さいほうのサイズを大きいほうのサイズに足す。
        self.parent_size[x] += self.parent_size[y]
        # サイズが小さいほうの根を大きいほうの根に繋げる。
        self.parent_size[y] = x
        return

    # 同じグループか判定
    def same(self, a, b):
        # 根を比較して同じならTrue
        return self.leader(a) == self.leader(b)

    # 属するグループのサイズを返す
    def size(self, a):
        # 根の絶対値 = サイズ
        return abs(self.parent_size[self.leader(a)])

    # グループを二次元配列として返す
    def groups(self):
        # グループの格納リストを作成
        result = [[] for _ in range(self.n)]
        # リストの生成
        for i in range(self.n):
            result[self.leader(i)].append(i)
            # 空の要素を消す
        return [r for r in result if r != []]


N, M = map(int, input().split())
Uni = UnionFind(N)

for i in range(M):
    A, B = map(int, input().split())
    # AもBも0indexにする
    A -= 1
    B -= 1
    Uni.merge(A, B)

friends_group = Uni.groups()

friends_size = []
for fri in friends_group:
    friends_size.append(len(fri))

print(max(friends_size))
