# Codewars

<b>[Codewars](https://www.codewars.com)</b> is a <b>coding practice site</b> for all programmers where you can <b>learn and practice</b> various programming languages.
Here are some <b>programming challenges</b> that I completed on [Codewars](https://www.codewars.com).<br>
- Click [here](https://www.codewars.com/users/Stolexx_) to see my <b>profile</b>!

## Explore the repository

`1.` [Python](https://github.com/Stolexx/Codewars/tree/main/python)<br>
`2.` [Java](https://github.com/Stolexx/Codewars/tree/main/java)<br>
`3.` [OCaml](https://github.com/Stolexx/Codewars/tree/main/ocaml)

## A few examples
### Python

<i>Some examples of challenges I have done in Python for [Codewars](https://www.codewars.com)</i><br>
<br>

`1.` [MaxAndMin.py](https://github.com/Stolexx/Codewars/blob/main/python/MaxAndMin.py)

```python
# Trouver le maximum et le minimum parmis une string qui contient des nombres

def high_and_low(numbers):
    list = [e for e in numbers.split()]
    return max(list) + " " + min(list)
```

`2.` [ListFormat.py](https://github.com/Stolexx/Codewars/blob/main/python/ListFormat.py)

```python
# Formatter une liste avec des virgules et des & pour la rendre lisible

def namelist(names):
    list = [e.get("name") for e in names]
    result = ", ".join(list)
    if len(list) > 1: result = result[:result.rfind(",")] + " &" + result[result.rfind(",")+1:]
    return result
```

`3.` [DuplicateChecker.py](https://github.com/Stolexx/Codewars/blob/main/python/DuplicateChecker.py)

```python
# Formatter une liste avec des virgules et des & pour la rendre lisible

def namelist(names):
    list = [e.get("name") for e in names]
    result = ", ".join(list)
    if len(list) > 1: result = result[:result.rfind(",")] + " &" + result[result.rfind(",")+1:]
    return result
```

### Java

<i>Some examples of challenges I have done in Java for [Codewars](https://www.codewars.com)</i><br>
<br>

`1.` [DRoot.java](https://github.com/Stolexx/Codewars/blob/main/java/DRoot.java)

```java
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
```

`2.` [BinaryArrayToNumber.java](https://github.com/Stolexx/Codewars/blob/main/java/BinaryArrayToNumber.java)

```java
// Conversion d'une liste de nombres binaires en un entier

public static int ConvertBinaryArrayToInt(List<Integer> binary) {
    String result = "";
    for (Integer b : binary) {
        result += b;
    }
    return Integer.parseInt(result, 2);
}
```

`3.` [DigPow.java](https://github.com/Stolexx/Codewars/blob/main/java/DigPow.java)

```java
// Instructions : https://www.codewars.com/kata/5552101f47fc5178b1000050

public static long digPow(int n, int p) {
    int sum = 0;
    for (int i = p; i < String.valueOf(n).length() + p; i++) {
        sum += Math.pow(Integer.parseInt(String.valueOf(Integer.toString(n).toCharArray()[i-p])), i);
    }
    return ((float)sum / n == (int)sum / n ? sum / n : -1);
}
```
