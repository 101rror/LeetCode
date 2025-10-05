// ---------- CP Trie Functions ----------
class CPTemplate {
    static int MAX_BITS = 19;

    static class TrieNode {
        TrieNode[] children;
        int count;

        TrieNode() {
            children = new TrieNode[2];
            count = 0;
        }
    }

    static TrieNode root = new TrieNode();

    static void insert(int num) {
        TrieNode cn = root;
        for (int i = MAX_BITS - 1; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (cn.children[bit] == null) {
                cn.children[bit] = new TrieNode();
            }
            cn = cn.children[bit];
            cn.count++;
        }
    }

    static int bm(int num) {
        TrieNode cn = root;
        int result = 0;
        for (int i = MAX_BITS - 1; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int opb = 1 - bit;

            if (cn.children[opb] != null && cn.children[opb].count > 0) {
                result = (result << 1) | opb;
                cn = cn.children[opb];
            } else {
                result = (result << 1) | bit;
                cn = cn.children[bit];
            }
        }
        return result;
    }

    static void remove(int num) {
        TrieNode cn = root;
        for (int i = MAX_BITS - 1; i >= 0; i--) {
            int bit = (num >> i) & 1;
            cn = cn.children[bit];
            cn.count--;
        }
    }
}

public class Solution {
    public String removeSubstring(String s, int k) {
        StringBuilder ans = new StringBuilder(s);
        StringBuilder patternBuilder = new StringBuilder();

        for (int i = 0; i < k; i++){
            patternBuilder.append('(');
        }
        for (int i = 0; i < k; i++){
            patternBuilder.append(')');
        }
        String pattern = patternBuilder.toString();

        if (pattern.length() == 0){
            return s;
        }

        int i = 0;
        while (i <= ans.length() - 2 * k) {
            if (ans.substring(i, i + 2 * k).equals(pattern)) {
                ans.delete(i, i + 2 * k);
                i = Math.max(0, i - 2 * k);
            }
             else {
                i++;
            }
        }

        return ans.toString();
    }
}
