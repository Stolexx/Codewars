import java.util.List;

public class BinaryArrayToNumber {

    // Conversion d'une liste de nombres binaires en un entier

    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        String result = "";
        for (Integer b : binary) {
            result += b;
        }
        return Integer.parseInt(result, 2);
    }

}