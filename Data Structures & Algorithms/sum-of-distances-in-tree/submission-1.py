class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        # create the graph
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        
        ans = [0] * n
        count = [1] * n

        def down(node, parent): # from down to up: count, output[0]
            for child in graph[node]:
                if child != parent:
                    down(child, node)
                    count[node]  += count[child]
                    ans[node] += ans[child] + count[child]

        def reroot(node, parent):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] + n - 2*count[child]
                    reroot(child, node)


        down(0, -1)
        reroot(0, -1)
        
        return ans
