class BrowserHistory:

    def __init__(self, homepage: str):
        # Time and Space Complexity: O(Q)

        self.urls = [homepage]
        self.length = 1
        self.ptr = 0

    def visit(self, url: str) -> None:
        self.ptr += 1

        if self.ptr  == len(self.urls):
            self.urls.append(url)
        else:
            self.urls[self.ptr] = url

        self.length = self.ptr + 1

    def back(self, steps: int) -> str:
        steps = min(steps, self.ptr)
        self.ptr -= steps

        return self.urls[self.ptr]

    def forward(self, steps: int) -> str:
        steps = min(steps, self.length - 1 - self.ptr)
        self.ptr += steps

        return self.urls[self.ptr]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
