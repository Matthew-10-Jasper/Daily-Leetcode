
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):

        # Free servers: (weight, index)
        free = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free)

        # Busy servers: (finish_time, weight, index)
        busy = []

        ans = []
        t = 0

        for i in range(len(tasks)):

            t = max(t, i)

            # If no server is free, jump to next finish time
            if not free:
                t = busy[0][0]

            # Release all servers finished by time t
            while busy and busy[0][0] <= t:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            # Select the best available server
            w, idx = heapq.heappop(free)

            ans.append(idx)

            # Assign task and calculate finish time
            heapq.heappush(busy, (t + tasks[i], w, idx))

        return ans