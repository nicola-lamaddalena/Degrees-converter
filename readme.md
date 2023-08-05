# Degrees converter

Little library that contains functions that convert degrees from one form to another (e.g. from Celsius to Fahrenheit).

Every method of the class *Converter* return a float; in some cases the float value is rounded to the second decimal figure.

Create an instance of the class *Converter*:

```Python
conv = Converter()
```

and then call the methods of the instance with a int or float value:

```Python
print(conv.celFah(0))
# output: 32.0
```
