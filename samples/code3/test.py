def mystery(N):
        s = []
        while N > 0:
                s.append(N % 3)
                N = N / 3

#       print("s = ", s)

        buf = ""
        while len(s) > 0:
                buf += str(s.pop())

#       print("buf = ", buf)
        return buf

print(mystery(50))
