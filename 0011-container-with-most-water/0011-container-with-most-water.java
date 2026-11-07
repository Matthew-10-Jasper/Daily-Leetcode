class Solution {
    public int maxArea(int[] height) {
        int f=0;
        int l=height.length-1;
        int ma = 0;
        while(f<l){
            int v = (l-f)*Math.min(height[f],height[l]);
            if(ma < v){
                ma = v;
            }
            if(height[f]>height[l]){
                l--;
            }
            else{
                f++;
            }
        }
        return ma;
    }
}