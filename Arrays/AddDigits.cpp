class Solution {
public:
    int addDigits(int num) {
        bool flag = true;
        int sum =0;
        if(num<10){
            return num;
        }

        while(flag){
            sum+=num%10;
            num=num/10;
            if(num == 0 && sum>9){
                swap(num , sum);
            }

            if(sum<10 && num==0){
                flag=false;
            }
        }

        return sum;
    }
};