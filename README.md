Methods
Overview
The goal of this lab was to implement the Quicksort algorithm to sort a list of cities based on various criteria, including alphabetical order, population, and latitude. The project also required the creation of a City class, accurate reading of input files, and the generation of multiple output files. Additionally, a dynamic visualization of the 50 most populous cities was to be included. Emphasis was placed on both the correctness of the algorithm implementations and the clarity and organization of the code.

![Screenshot (78)](https://github.com/user-attachments/assets/d3383214-d0ef-4253-8ed5-c61b68f367e7)


Process
Partition Function:

The partition function was implemented as the core component of the Quicksort algorithm. It was responsible for selecting a pivot element and rearranging the elements of the list such that those less than the pivot appeared before it, and those greater appeared after. The correctness of this function was critical, as it directly influenced the efficiency and accuracy of the Quicksort process.
Quicksort and Sort Functions:

Building on the partition function, the Quicksort algorithm was implemented. This recursive function repeatedly applied the partition function to subarrays, ensuring that the entire list was sorted. Additionally, a sort function was created to handle the initial invocation of Quicksort and to sort the list based on different criteria, such as alphabetical order, population, and latitude.
Comparison Functions:

Comparison functions were developed to facilitate sorting based on different criteria. These functions were passed to the Quicksort algorithm to determine the order of elements. For example, one function compared city names alphabetically, while another compared cities based on their population or latitude.
City Class:

A City class was created to represent each city in the list. This class included attributes such as the city's name, population, and latitude, along with methods to access and modify these attributes. The correctness of the City class was essential, as it ensured that each city was accurately represented and manipulated during the sorting process.
Reading Input and Writing Output Files:

The program included methods to read input data from a file containing a list of cities and their attributes. This data was then processed and sorted using the Quicksort algorithm. The results were written to output files, with one file for each sorting criterion: alphabetical order, population, and latitude.
Sorting by Alphabetical Order, Population, and Latitude:

The list of cities was sorted three times: once alphabetically, once by population, and once by latitude. The results of each sort were saved in separate output files, demonstrating the versatility and correctness of the Quicksort implementation.
Dynamic Visualization of 50 Most Populous Cities:

A dynamic visualization was created to display the 50 most populous cities. This visualization provided an interactive way to view the data, allowing users to see how the cities were distributed in terms of population. The implementation focused on creating a clear and informative display that enhanced the understanding of the data.
Code Design and Style:

Throughout the project, careful attention was paid to the design and organization of the code. Functions were modular, with clear responsibilities, and the overall structure of the code was designed to be easy to follow. Variable and function names were chosen to be descriptive, and comments were included to explain the purpose and functionality of different sections of the code. Instance variables were used correctly to manage the state of objects, particularly within the City class.
Conclusion
This lab successfully implemented the Quicksort algorithm to sort cities based on multiple criteria, ensuring both correctness and efficiency. The project also demonstrated strong code design and organization, with a clear structure and well-documented code. The inclusion of a dynamic visualization added an interactive element, making the data more accessible and engaging.
