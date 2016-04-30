# pyComplexity

A small Python script that leverages the [GNU Complexity](http://www.gnu.org/software/complexity) project to create a set of score reports for student code. The script expects to be placed run in the root of a project turnin directory, as shown below, and to have Complexity installed. 

## Default Score Report Example
```
Nick Gonella
Complexity results for Project2
   Total Complexity:   248, target was 350, 100%
   Average Complexity: 13, target was 27, 100%
   Maximum Complexity: 31, target was 60, 100%
   Top Quartile Ratio: 0.45, target was 0.60, 100%

Score: 100%
```
The report as well as the references are defined in the [config.py](config.py) file.

## Expected Structure
```
Main Project Folder
|-- < score traunch 1 >
|   |-- < student name >
|   |   |-- < Zipped Project file >
|   |-- < student name >
|   ...
|-- < score traunch 2 >
...
```
A score trauch folder designates a modifier on the raw score computed for each student
