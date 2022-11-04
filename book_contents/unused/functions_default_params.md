# Demo: Only positive news

What goes here? Unrelated concept? I can move this lecture around as needed


Functions with named params and default values

https://www.w3schools.com/python/python_functions.asp
```
def function_name(arg_1 = "default"):
  # do various actions, like this:
  print("arg 1 will be default if not sent:" + arg_1)

# call function
    function_name()
    function_name(arg_1 = "a different value")
```


Function returns

- Functions can “return” a value, that is, a value comes back when the function is done, that can be used (e.g., stored in a variable). E.g.

```
message = "this is a test message"

how_long_message =      len(message)
```   
             <- Output (return)    <- Inputs (arguments, parameters)


- When writing a function, to return a value, use the word “return” followed by a value

```
def mult(num1, num2):
  return num1 * num2

# call function
    number_var = mult(3, 4)
```
