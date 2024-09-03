from utils.get_data import get_data, filter_data
from utils.clustering import clustering
from utils.json_to_dict import json_to_dict
from assistant.init_assistant import init_assistant
from assistant.first_analysis import first_analysis
from utils.install_requirements import install_requirements
import os

def main():
    # Get input data from user
    input_data = json_to_dict('input_data.json')
    years = input_data['years']
    s_type = input_data['s_type']
    tom = input_data['tom']
    mapping = json_to_dict('dictionaries/mapping_s_type.json')
    s_types = mapping[s_type]

    # Install required libraries
    base_dir = os.getcwd()
    requirements_file = os.path.join(base_dir, "requirements.txt")
    install_requirements(requirements_file)
    print('Requirements are successfully installed!')

    # Get API from user in case assistant is needed
    api = input('Please insert your OpenAI API to use the assistant. (Enter to proceed without API):     ')

    try:
        assistant = init_assistant(api) # Init assistant (None if no API provided or if API is invalid)
        raw_data = get_data(years,s_type) # Get raw data
        data_to_analyze = filter_data(raw_data,tom) # Clean data 
        players_analyzed, metrics_analyzed, summary_path, analyzed_data_path = clustering(data_to_analyze.copy(),tom,years) # Apply clustering to data, return data for assistant
        
        # Get data from json
        summary_as_json = json_to_dict(summary_path)
        data_as_json = json_to_dict(analyzed_data_path)

        if assistant:
            first_analysis(
                tom,
                s_types,
                years,
                summary_as_json,
                players_analyzed,
                metrics_analyzed,
                assistant
            )

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()