public class DnaStrand {

    // Trouver la molécule correspondante à chaque molécule qui compose une séquence ADN 

    public static String makeComplement(String dna) {
        String result = "";
        for (String c : dna.split("")) {
            if(c.equals("A")) {
                result += "T";
            }else if(c.equals("T")) {
                result += "A";
            }else if(c.equals("C")) {
                result += "G";
            }else if(c.equals("G")) {
                result += "C";
            }
        }
        return result;
    }

}