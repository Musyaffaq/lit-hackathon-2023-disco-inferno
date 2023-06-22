import pandas as pd
import ast
import PyPDF2
import re
from pathlib import Path
import os


def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            content = ''
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                content += page.extract_text()
            return content
    except FileNotFoundError:
        print("File not found.")


def append_to_db(output_string):
    dbpath = Path('Database/Database.csv')
    current_dataframe = pd.read_csv(dbpath)
    # Convert the output string to a dictionary
    print(output_string)
    output_dict = ast.literal_eval(output_string)

    # Create a new dictionary to represent the new row
    new_row = {
        'case_summary': output_dict['case_summary'],
        'corem': [judge.strip() for judge in re.split(r',|and', output_dict['corem'])],
        'court': output_dict['court'],
        'categories': [category.strip() for category in output_dict['categories'].split(',')]
    }

    # Append the new row to the existing dataframe
    new_dataframe = pd.concat([current_dataframe, pd.DataFrame([new_row])], ignore_index=True)

    new_dataframe.to_csv(dbpath)


def get_top_similar_cases(dataframe, query_item):
    # Create a new column to store the number of similar tags
    dataframe['similar_tags'] = dataframe['tags'].apply(lambda x: len(set(x) & set(query_item)))

    # Sort the dataframe based on the number of similar tags in descending order
    sorted_dataframe = dataframe.sort_values(by='similar_tags', ascending=False)

    # Get the top 3 case names with the most similar tags
    top_cases = sorted_dataframe['case_name'].head(3).tolist()

    return top_cases
