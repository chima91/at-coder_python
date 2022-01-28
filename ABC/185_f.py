# https://atcoder.jp/contests/abc185/tasks/abc185_f

def segfunc(x, y):
    return x ^ y


class SegTree:
    def __init__(self, x_list, init, segfunc):
        self.init = init
        self.segfunc = segfunc
        self.Height = len(x_list).bit_length()+1
        self.Tree = [init]*(2**self.Height)
        self.num = 2**(self.Height-1)
        for i in range(len(x_list)):
            self.Tree[2**(self.Height-1)+i] = x_list[i]
        for i in range(2**(self.Height-1)-1, 0, -1):
            self.Tree[i] = segfunc(self.Tree[2*i], self.Tree[2*i+1])

    def select(self, k):
        return self.Tree[k+self.num]

    def update(self, k, x):
        i = k+self.num
        self.Tree[i] = x
        while i > 1:
            if i % 2 == 0:
                self.Tree[i//2] = self.segfunc(self.Tree[i], self.Tree[i+1])
            else:
                self.Tree[i//2] = self.segfunc(self.Tree[i-1], self.Tree[i])
            i //= 2

    def query(self, l, r):
        result = self.init
        l += self.num
        r += self.num+1

        while l < r:
            if l % 2 == 1:
                result = self.segfunc(result, self.Tree[l])
                l += 1
            if r % 2 == 1:
                result = self.segfunc(result, self.Tree[r-1])
            l //= 2
            r //= 2
        return result


N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(A, 0, segfunc)
for i in range(Q):
    T, X, Y = map(int, input().split())
    if T == 1:
        X -= 1
        seg.update(X, seg.select(X) ^ Y)
    else:
        X -= 1
        Y -= 1
        print(seg.query(X, Y))


# 区間和のためのセグメントツリー

# 演算（x+yをx|yにすればorになるし、min(x,y)にすれば最小値を取ってくる）
def segfunc(x, y):
    return x + y


class SegTree:
    # 初期化(元のリスト, 単位元, 演算)
    def __init__(self, x_list, init, segfunc):
        self.init = init
        self.segfunc = segfunc
        # 高さ = 元の数列の長さのビット長+1
        self.Height = len(x_list).bit_length()+1
        # 木
        self.Tree = [init] * (2 ** self.Height)
        # Tree最下段左端のインデックス
        self.num = 2 ** (self.Height - 1)
        # 最下段に要素をセット
        for i in range(len(x_list)):
            self.Tree[2**(self.Height-1)+i] = x_list[i]
        # Treeを上に向かって構築していく
        for i in range(2**(self.Height-1)-1, 0, -1):
            self.Tree[i] = segfunc(self.Tree[2*i], self.Tree[2*i]+1)

    # 要素の参照: 計算量はO(1)
    def select(self, k):
        return self.Tree[k+self.num]

    # 要素の更新: 計算量はO(logN)
    def update(self, k, x):
        # 最下段のインデックス番号に合わせる
        i = k+self.num
        # 最下段の要素を更新
        self.Tree[i] = x
        # 上に向かって更新
        while i > 0:
            if i % 2 == 0:
                self.Tree[i//2] = self.segfunc(self.Tree[i], self.Tree[i+1])
            else:
                self.Tree[i//2] = self.segfunc(self.Tree[i-1], self.Tree[i])
            i //= 2

    # 区間の処理
    def query(self, l, r):
        # 下から処理
        # 計算結果(初期値は単位元)
        result = self.init
        # 左端(最下段のインデックスに合わせる)
        l += self.num
        # 右端(最下段のインデックスに合わせる, 後の処理を楽にするため+1しておく。)
        r += self.num + 1

        while l < r:
            if l % 2 == 1:
                result = self.segfunc(result, self.Tree[l])
                # 1個右に移動
                l += 1
            if r % 2 == 1:
                result = self.segfunc(result, self.Tree[r-1])
            l //= 2
            r //= 2
            return result
