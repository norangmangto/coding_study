int reverse(int x) {
    char *max = "2147483647";
    char *min = "2147483648";

    char s[12] = "";
    sprintf(s, "%d", x);

    char negative = 0;
    int len = strlen(s);
    if (s[0] == '-') {
        negative = 1;
        for (int i = 0; i<len; i++)
            s[i] = s[i+1];
        len--;
    }

    for (int i=0; i<len/2; i++) {
        char tmp = s[i];
        s[i] = s[len-1-i];
        s[len-1-i] = tmp;
    }

    // overflow check
    if (len > 10) {
        strcpy(s, "0");
        len = 1;
    } else if (len == 10) {
        if (negative) {
            for (int i=0; i<len; i++) {
                if (s[i] > min[i]) {
                    strcpy(s, "0");
                    len = 1;
                    break;
                } else if (s[i] < min[i])
                    break;
            }
        } else {
            for (int i=0; i<len; i++) {
                if (s[i] > max[i]) {
                    strcpy(s, "0");
                    len = 1;
                    break;
                } else if (s[i] < max[i])
                    break;
            }
        }
    }

    if (negative) {
        for (int i=len+1; i>0; i--) {
            s[i] = s[i-1];
        }
        s[0] = '-';
    }

    return atoi(s);
}
