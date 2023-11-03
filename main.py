#Team details
#Bhanu varma Domaraju (12614674)
#Gayathri Morampudi  (12611695)
#Anjali Malge  (
#Somasekhar Vavilapalli

import pandas as pd

# Function to read a CSV file and return the data as a DataFrame
def read_csv_file(file_name):
    data = pd.read_csv(file_name)
    return data

# Function to determine data types for each column
def determine_data_types(data):
    data_types = {}
    for column_name in data.columns:
        column_data = data[column_name]
        if column_data.dtype == 'int64':
            data_types[column_name] = "INT"
        elif column_data.dtype == 'datetime64[ns]':
            data_types[column_name] = "DATE"
        else:
            data_types[column_name] = "VARCHAR(255)"
    return data_types

# Function to normalize to 1NF (Identity function)
def normalize_to_1nf(data):
    decompositions = []
    for column_name in data.columns:
        decompositions.append(set([column_name]))
    return decompositions

# Function to normalize to 2NF
def normalize_to_2nf(data, functional_dependencies, mvds):
    decompositions = []

    # Initialize the decompositions with single attributes
    for column_name in data.columns:
        decompositions.append(set([column_name]))

    # Decompose based on functional dependencies
    for left, right in functional_dependencies.items():
        for attr in right:
            if attr in data.columns:
                table = set([left, attr])
                decompositions.append(table)

    # Decompose based on multi-valued dependencies
    for mvd in mvds:
        left_attr, right_attr = mvd
        if left_attr in data.columns and right_attr in data.columns:
            table = set([left_attr, right_attr])
            decompositions.append(table)

    return decompositions

# Function to normalize to 3NF
def normalize_to_3nf(data, functional_dependencies, mvds):
    decompositions = []

    # Initialize the decompositions with single attributes
    for column_name in data.columns:
        decompositions.append(set([column_name]))

    # Decompose based on functional dependencies
    for left, right in functional_dependencies.items():
        for attr in right:
            if attr in data.columns:
                table = set([left, attr])
                decompositions.append(table)

    # Decompose based on multi-valued dependencies
    for mvd in mvds:
        left_attr, right_attr = mvd
        if left_attr in data.columns and right_attr in data.columns:
            table = set([left_attr, right_attr])
            decompositions.append(table)

    # Further decompose to achieve 3NF
    new_decompositions = []
    for table in decompositions:
        primary_key = list(table)[0]
        if primary_key in functional_dependencies:
            dependents = functional_dependencies[primary_key]
            for dependent in dependents:
                if dependent in table:
                    new_table = set([primary_key, dependent])
                    new_decompositions.append(new_table)
        else:
            new_decompositions.append(table)

    return new_decompositions

# Function to find the key for 4NF
def find_key(data, functional_dependencies):
    # Start with all attributes as a potential key
    potential_key = set(data.columns)

    # Check each attribute to determine if it's part of a key
    for attr in data.columns:
        is_key = True

        for other_attr in data.columns:
            if attr != other_attr:
                closure = find_closure(attr, functional_dependencies)
                if not set(closure).issuperset(potential_key):
                    is_key = False
                    break

        if is_key:
            return attr

    return None

# Function to find the closure of an attribute set
def find_closure(X, functional_dependencies):
    closure = set(X)
    updated = True

    while updated:
        updated = False
        for dependency in functional_dependencies:
            if set(dependency).issubset(closure) and not set(functional_dependencies[dependency]).issubset(closure):
                closure.update(functional_dependencies[dependency])
                updated = True

    return list(closure)

# Function to normalize to 4NF
def normalize_to_4nf(data, functional_dependencies, mvds):
    decompositions = []

    # Find the key
    key = find_key(data, functional_dependencies)

    if key is not None:
        decompositions.append(set([key]))

    # Initialize the decompositions with single attributes
    for column_name in data.columns:
        decompositions.append(set([column_name]))

    # Decompose based on functional dependencies for 3NF
    for left, right in functional_dependencies.items():
        for attr in right:
            if attr in data.columns:
                table = set([left, attr])
                decompositions.append(table)

    # Decompose based on multi-valued dependencies
    for mvd in mvds:
        left_attr, right_attr = mvd
        if left_attr in data.columns and right_attr in data.columns:
            table = set([left_attr, right_attr])
            decompositions.append(table)

    # Further decompose to achieve 4NF
    new_decompositions = []
    for table in decompositions:
        if not table.issuperset([key]):
            primary_key = list(table)[0]
            if primary_key in functional_dependencies:
                dependents = functional_dependencies[primary_key]
                for dependent in dependents:
                    if dependent in table:
                        new_table = set([primary_key, dependent])
                        new_decompositions.append(new_table)
            else:
                new_decompositions.append(table)

    return new_decompositions

# Function to normalize to 5NF
def normalize_to_5nf(data, functional_dependencies, mvds):
    decompositions = []

    # Find the key
    key = find_key(data, functional_dependencies)

    if key is not None:
        decompositions.append(set([key]))

    # Initialize the decompositions with single attributes
    for column_name in data.columns:
        decompositions.append(set([column_name]))

    # Decompose based on functional dependencies for 3NF
    for left, right in functional_dependencies.items():
        for attr in right:
            if attr in data.columns:
                table = set([left, attr])
                decompositions.append(table)

    # Decompose based on multi-valued dependencies
    for mvd in mvds:
        left_attr, right_attr = mvd
        if left_attr in data.columns and right_attr in data.columns:
            table = set([left_attr, right_attr])
            decompositions.append(table)

    # Further decompose to achieve 5NF
    new_decompositions = []
    for table in decompositions:
        if not table.issuperset([key]):
            primary_key = list(table)[0]
            if primary_key in functional_dependencies:
                dependents = functional_dependencies[primary_key]
                for dependent in dependents:
                    if dependent in table:
                        new_table = set([primary_key, dependent])
                        new_decompositions.append(new_table)
            else:
                new_decompositions.append(table)

    return new_decompositions

# Function to normalize to BCNF
def normalize_to_bcnf(data, functional_dependencies, mvds):
    decompositions = [data]

    for dependency in functional_dependencies:
        X, Y = dependency, functional_dependencies[dependency]
        closure_X = find_closure(X, functional_dependencies)

        # If X is a superkey, no further decomposition is needed
        if set(closure_X) == set(data.columns):
            continue

        # If not in BCNF, decompose the relation
        super_key = False
        for column in data.columns:
            if column not in X and column in closure_X:
                super_key = True
                break

        if super_key:
            decompositions = decompose(data, X, Y, decompositions)

    return decompositions

# Function to decompose a relation into multiple tables
def decompose(data, X, Y, decompositions):
    # Create a new relation with X and Y
    new_relation = data[list(X) + list(Y)]
    decompositions.append(new_relation)

    # Update the original relation without Y
    data.drop(Y, axis=1, inplace=True)

    return decompositions

# Function to generate SQL queries for the decompositions
def generate_sql(decompositions, data_types):
    queries = []
    for table in decompositions:
        table_name = "_".join(table)
        columns = []
        primary_keys = []
        foreign_keys = []

        for column_name in table:
            data_type = data_types[column_name]
            columns.append(f"{column_name} {data_type}")

            # If the column is a primary key
            if column_name.endswith("ID"):
                primary_keys.append(column_name)

            # If the column is a foreign key
            if column_name != table_name and column_name.endswith("ID"):
                foreign_keys.append(f"FOREIGN KEY ({column_name}) REFERENCES {column_name[:-2]} ({column_name})")

        # Define the primary key constraint
        if primary_keys:
            columns.append(f"PRIMARY KEY ({', '.join(primary_keys)})")

        # Define foreign key constraints
        if foreign_keys:
            columns.extend(foreign_keys)

        column_defs = columns
        query = f"CREATE TABLE {table_name} ({', '.join(column_defs)});"
        queries.append(query)

    return queries

# Main function to drive the normalization process
def main():
    # Input the CSV file name
    csv_file_name = input("Enter the CSV file name: ")

    # Reading CSV
    data = read_csv_file(csv_file_name)

    # Determine data types
    data_types = determine_data_types(data)

    # Input functional dependencies
    functional_dependencies = {}
    print("Enter functional dependencies (e.g., A -> B, C):")
    while True:
        dependency = input()
        if dependency.lower() == 'exit':
            break
        left, right = map(str.strip, dependency.split('->'))
        left_attributes = [attr.strip() for attr in left.split(',')]
        right_attributes = [attr.strip() for attr in right.split(',')]
        for left_attr in left_attributes:
            if left_attr not in functional_dependencies:
                functional_dependencies[left_attr] = []
            functional_dependencies[left_attr].extend(right_attributes)

    # Input multi-valued dependencies
    mvds = []
    print("Enter multi-valued dependencies (e.g., A ->> B):")
    while True:
        mvd_input = input()
        if mvd_input.lower() == 'exit':
            break
        left_attr, right_attr = map(str.strip, mvd_input.split('->>'))
        mvds.append((left_attr, right_attr))

    # Choose the desired normal form
    print("Choose the highest normal form to reach:")
    print("1: 1NF, 2: 2NF, 3: 3NF, 4: 4NF, 5: 5NF, b: BCNF")
    target_normal_form = input("Enter the desired normal form (1/2/3/4/5/b): ")

    # Normalize the data to the specified normal form
    if target_normal_form == '1':
        decompositions = normalize_to_1nf(data)
    elif target_normal_form == '2':
        decompositions = normalize_to_2nf(data, functional_dependencies, mvds)
    elif target_normal_form == '3':
        decompositions = normalize_to_3nf(data, functional_dependencies, mvds)
    elif target_normal_form == '4':
        decompositions = normalize_to_4nf(data, functional_dependencies, mvds)
    elif target_normal_form == '5':
        decompositions = normalize_to_5nf(data, functional_dependencies, mvds)
    elif target_normal_form == 'b':
        # Normalize the data to BCNF
        tables = normalize_to_bcnf(data, functional_dependencies, mvds)
    else:
        print("Invalid choice of normal form. Please choose 1, 2, 3, 4, 5, or b.")
        return

    # Generate SQL queries
    if target_normal_form == 'b':  # Generate SQL queries for BCNF
        sql_queries = generate_sql(tables, data_types)
    else:
        sql_queries = generate_sql(decompositions, data_types)

    # Writing to file
    output_file_name = "output.txt"
    with open(output_file_name, 'w') as f:
        f.write("Generated SQL Queries:\n")
        for query in sql_queries:
            f.write(query + '\n')

    print(f"Output written to '{output_file_name}'")

if __name__ == "__main__":
    main()

