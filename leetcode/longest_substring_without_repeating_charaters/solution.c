int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    if (n<2)
        return n;

    int cs[255+1] = {0, };
    int max_len = 0;

    int i = 0, j = 0;
    for (j=0; j<n; j++) {
        if (cs[s[j]] == 1) {
            // compare current length with the longest length
            if (j-i > max_len)
                max_len = j-i;

            // remove previous characters until finding the character same with current character s[j]
            while (s[i] != s[j]) {
                cs[s[i]] = 0;
                i++;
            }

            // remove the character same with current character s[j]
            cs[s[i++]] = 0;
        }

        cs[s[j]] = 1;
    }

    // compare current length with the longest length one more
    if (j-i > max_len)
        max_len = j-i;

    return max_len;
}
