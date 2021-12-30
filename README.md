# Codewars

[Codewars](https://www.codewars.com) is a coding practice site for all programmers where you can learn various programming languages.
Here are some programming challenges that I completed on [Codewars](https://www.codewars.com)<br>
Click [here](https://www.codewars.com/users/Stolexx_) to see my profile!

## Explore the repository

`1.` [Python](https://github.com/Stolexx/Codewars/tree/main/python)<br>
`2.` [Java](https://github.com/Stolexx/Codewars/tree/main/java)

## A few examples
### Python

<i>Some examples of challenges I have done in Python for Codewars</i><br>
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

<i>Coming soon...</i>
