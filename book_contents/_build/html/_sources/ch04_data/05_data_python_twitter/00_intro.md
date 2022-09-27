# Data in a Python and Twitter

Now we will look at ways data is represented in Python and what data is available from Twitter.

```{tableofcontents}
```

A function is a named section of pre-written code.

Functions can take inputs
* Inputs go in parenthese after the function name
* These inputs are called "parameters" or "arguments"
* If there are multiple inputs, they are separated by commas
* You can also specify which input you are giving within the parenthesis by putting parameter_name=value

Functions can also make outputs.
* Also called "returns" or "results"
* When the code intepreter sees the function call, it runs the code in the function wiht the inputs, and then puts the output in the place where that function call was
* The results of the function can be stored in a variable, used in a formula, or used as an argument for another function

## TODO: include in demo:

import string
import math

# TODO: Demo functions with returns (upper, isupper, sqrt, range, type)
message2 = message.upper()
message3 = message.lower()

sqrt_years = math.sqrt(years)

example_range = range(10)

print( type(message2) )

# TODO: Demo a useful trick with functions (str)
first_name = "Kyle"
last_name = "Thayer"

combined_name = first_name + " " + last_name

kyle_age = first_name + " is " + str(38) + " years old"
