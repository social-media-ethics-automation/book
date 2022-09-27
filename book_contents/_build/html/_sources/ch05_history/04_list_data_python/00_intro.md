# Lists in Python


```{tableofcontents}
```


TODO: Add these to the demos:
## for loops
For loops allow you to repeat an action multiple times.

```
for loop_value in thing_to_loop_over:
    # Put actions to repeat here
```

For loops have to have something to loop over, which goes after "in".
* You can use it with the function range to repeat an action a given number of times.
* You can use it on a list, though we'll cover that more later.

As the loop goes, it saves the current thing it is looking at in the temporary variable you list before the in.

The commands you want to repeat need to be tabbed in one more level than the for statement to indicate they go inside the for loop.


# TODO: Demo some for loops, including the one below

for x in range(10):
    print("<<<<< " + str(x*4 + 1) + "/40")
    print("^^^^^ " + str(x*4 + 2) + "/40")
    print(">>>>> " + str(x*4 + 3) + "/40")
    print("vvvvv " + str(x*4 + 4) + "/40")

for loop: are we there yet
