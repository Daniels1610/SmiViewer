import re, json

#
# Helpers Data Cleaning
#

def _clean_model_steps(input_str: str) -> list:
    # Use regex to find all tuples in the format ('name', model(...))
    pattern = re.compile(r"\('(\w+)',\s*([^\)]+\))")
    matches = pattern.findall(input_str)

    # Convert the matches into the desired format
    processed_list = [f'{name.capitalize()}: {model.strip()}' for name, model in matches]
    return processed_list

def _clean_stringified_dict(stringified_json: str) -> dict:
    if not stringified_json:
        return None
    # Replace single quotes with double quotes
    corrected_json_str = stringified_json.replace("'", '"')

    # Convert to JSON object
    return json.loads(corrected_json_str)