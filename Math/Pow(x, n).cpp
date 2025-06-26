class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1.0; 

        long long absN = abs((long long)n); 
        double result = 1.0;
        while (absN > 0) {
            if (absN % 2 == 1) { 
                result *= x;
            }
            x *= x;         
            absN /= 2;      
        }

        return (n < 0) ? 1 / result : result;
    }
};
