# https://atcoder.jp/contests/abc049/tasks/arc065_a
S = input()


def solve(s):
    while True:
        for frag in ("erase", "eraser", "dream", "dreamer"):
            # 4単語のどれかでSが終わっていたら、Sの末尾からその単語を削っていく。
            if s.endswith(frag):
                s = s[:-len(frag)]
                break
        # for文で一度もbreakしなかった時
        else:
            print("NO")
            break
        # すべて削ることができたら、print("YES")
        # まだ削り終わっていなければ、for文へ戻る
        if not s:
            print("YES")
            break


solve(S)
