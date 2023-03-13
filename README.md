# My approach

## in a nutshell

> - Let S be the array that collects sorted numbers
> - Let A be the original, unsorted array
> - Find smallest number in the list
> - Check if the number is already in S
>   - if so, remove it from the A
>   - otherwise put it into S
> - an extra flag is used to keep duplicate numbers

## extra slowdowns

> - when checking if a number is already in S, iteration isn't stopped when found
> - the position of the already sorted number is checked in a separate iteration
> - removal of sorted numbers is achieved by shifting required numbers to the left
>   - the original size is kept, meaning empty spaces are moved from the end of the array
>   - iteration starts at the beginning of the array and shift instructions are skipped, isntead of starting at the number that needs to be removed
> - the first empty space in S is always found by iterating through from start
> - by the nature of this approach, if duplicate numbers take an extra cycle to be sorted

## Complexity

> ~ _O(2N * 5N) = O(10N<sup>2</sup>)_
