import java.util.*;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {

        int m = queries.length;
        int[] ans = new int[m];

        // Sort logs by timestamp
        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));

        // Store query indices
        Integer[] idx = new Integer[m];

        for (int i = 0; i < m; i++) {
            idx[i] = i;
        }

        // Sort queries by time
        Arrays.sort(idx, (a, b) ->
            Integer.compare(queries[a], queries[b]));

        int[] freq = new int[n + 1];

        int left = 0, right = 0;
        int active = 0;

        for (int i : idx) {

            int start = queries[i] - x;
            int end = queries[i];

            // Add logs within the right boundary
            while (right < logs.length &&
                   logs[right][1] <= end) {

                int server = logs[right][0];

                if (freq[server] == 0) {
                    active++;
                }

                freq[server]++;
                right++;
            }

            // Remove logs outside the left boundary
            while (left < right &&
                   logs[left][1] < start) {

                int server = logs[left][0];

                freq[server]--;

                if (freq[server] == 0) {
                    active--;
                }

                left++;
            }

            ans[i] = n - active;
        }

        return ans;
    }
}