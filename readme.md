**Team Members**
  `  `  `Bhanu Varma Dommaraju (12614674)  `  `  `
  `  `  `Gayathri Morampudi ()  `  `  ` 
  `  `  `Somasekhar Vavilapalli (12598347)  `  `  `  
**Code description and Logic**
->Import Libraries: Import the pandas library for DataFrame handling.

->read_csv_file Function: Read a CSV file and return the data as a DataFrame.

->determine_data_types Function: Determine data types for each column (INT, DATE, or VARCHAR(255)).
    

->Normalization Functions:
normalize_to_1nf, normalize_to_2nf, normalize_to_3nf, normalize_to_4nf, normalize_to_5nf, normalize_to_bcnf functions perform normalization to the specified normal forms.
They decompose the data based on functional dependencies and multi-valued dependencies.

->find_key Function: Find a candidate key for the data based on superkey test.

->find_closure Function: Calculate the closure of an attribute set using functional dependencies.

->decompose Function: Create new relations based on functional dependencies.

->generate_sql Function: Generate SQL queries to create tables for the decomposed data.

->main Function: The main driver function that:
Reads the CSV file.
Determines data types.
Accepts user input for functional dependencies and multi-valued dependencies.
Prompts the user to choose a target normal form.
Invokes the appropriate normalization function.
Generates SQL queries for the decomposed tables and writes them to an output file.

**Sample input**
Enter the CSV file name: C:\Users\satis\Downloads\exampleInputTable (2).csv   **(Give the csv file path without double quotes("").)**
Enter functional dependencies (e.g., A -> B, C):             **(After completion of entering functional dependencies, make sure to enter 'exit')**
StudentID -> FirstName, LastName
Course, Professor -> classroom
Course -> CourseStart, CourseEnd
Professor -> ProfessorEmail
exit  
Enter multi-valued dependencies (e.g., A ->> B):             **(After completion of entering multi-valued dependencies, make sure to enter 'exit')**
Course ->> Professor
Course ->> classroom
StudentID ->> Course
StudentID ->> Professor
exit  
Choose the highest normal form to reach:
1: 1NF, 2: 2NF, 3: 3NF, 4: 4NF, 5: 5NF, b: BCNF
Enter the desired normal form (1/2/3/4/5/b): 3
Output written to 'output.txt'
