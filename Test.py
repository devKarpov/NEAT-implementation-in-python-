class lmao():
    def __init__(self, state) -> None:
        self.state = state


xd = { }
xd[1] = lmao(True)
xd[2] = lmao(True)
xd[3] = lmao(True)
xd[4] = lmao(True)

xd = {key:val for key, val in xd.items() if not val.state}

print(xd)