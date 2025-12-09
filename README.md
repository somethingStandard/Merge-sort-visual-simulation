# Merge-sort-visual-simulation

I chose merge sort because I have a good understanding of the algorithm and I think it would look the most interesting to visualize

Decomposition: Repeatedly break a list into halves then merge the sub lists into a bigger sorted list 

Pattern Recognition: Recursively splits lists in half in to two sublists until the length of the subsists are one. Then the sublists merge into bigger lists where the smaller first value of the sublists get merged then iterating to the next element in that list, this continues until one list has all of its elements merged where then the other sublist gets merged making a sorted sublist. This continues until the original two sublists get sorted then merge into the final sorted list.

Abstraction: Display elements of the list as bars with height scaled by height. Show the lists spitting into sublists. Then show the sublists merging one element at a time. Do not show how the bars are scaled. Make a minimum and maximum size for bars and set the smallest value in the list to the minimum and largest to max then every other bar would be sized based on how they compare to the min and max values eg: min 100, max 200 150 would be the average sized bar of the min and max because it is the average of 150 and 200

Algorithm Design: Take an input and verify that it is an array of integers. If the input is not valid tell the user the issue and ask for a new input. Go through the list finding the highest and lowest values, unless the list is of length one. Then go through the list giving each value a bar size by multiplying the size of the max bar by (value - min)/(max - min). If the size is zero set it to the minimum bar size. Then display all the bars with their values with an option to click sort, which plays the animation of the bars being sorted until it is sorted. 

![Uploading image.png…]()
