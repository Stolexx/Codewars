public class DigPow {

    // Instructions : https://www.codewars.com/kata/5552101f47fc5178b1000050

    public static long digPow(int n, int p) {
        int sum = 0;
        for (int i = p; i < String.valueOf(n).length() + p; i++) {
            sum += Math.pow(Integer.parseInt(String.valueOf(Integer.toString(n).toCharArray()[i-p])), i);
        }
        return ((float)sum / n == (int)sum / n ? sum / n : -1);
    }

}
