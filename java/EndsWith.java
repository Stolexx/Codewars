public class EndsWith {

    // Vérification avancée de la fin d'un string

    public static boolean solution(String str, String ending) {
        if(str.endsWith(ending)) {
            Boolean result = true;
            String[] s = str.split("");
            String[] e = ending.split("");
            for (int i = 0; i < ending.length(); i++) {
                if(!(s[s.length - i] == e[i])) {
                    result = false;
                }
            }
            return result;
        }
        return false;
    }

}
