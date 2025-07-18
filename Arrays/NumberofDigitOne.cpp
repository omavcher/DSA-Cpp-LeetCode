class Solution {
public:
    int countDigitOne(int n) {
        int count = 0;
        for (long long place = 1; place <= n; place *= 10) {
            long long divider = place * 10;
            count += (n / divider) * place + 
                     min(max(n % divider - place + 1, 0LL), place);
        }
        return count;
    }
};
