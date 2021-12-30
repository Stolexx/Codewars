public class DRoot {

    // "Racine digitale" d'un nombre (https://en.wikipedia.org/wiki/Digital_root)

    public static int digital_root(int n) {
        int result = n;
        while (String.valueOf(result).length() > 1) {
            int math = 0;
            for(String c : String.valueOf(result).split("(?<=.)")) {
                math += Integer.valueOf(c);
            }
            result = math;
        }
        return result;
    }

}