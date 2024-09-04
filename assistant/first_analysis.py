import os

def first_analysis(tom,s_types,years,summary_as_json,players_analyzed,metrics_analyzed,assistant,base_path):
    prompt = """
    I need you to analyze as deeply as possible the next data summary divided by clusters:
    {tom} from {s_types} at {years}.
    {players_analyzed} players were analyzed with {metrics_analyzed} metrics.

    {summary_as_json}""".format(tom=tom, s_types=s_types, years=years, players_analyzed=players_analyzed, metrics_analyzed=metrics_analyzed, summary_as_json=summary_as_json)
    answer = assistant.chat(prompt)

    # Guardar el string en un archivo .md
    type_of_metrics = tom.lower().replace(' ','_')
    years_str = str(years).replace('[','').replace(']','').replace(', ','_')
    data_path = 'report_'+type_of_metrics+'_'+years_str+'.md'
    file_name = os.path.join(base_path,data_path)
    try:
        with open(file_name, "w") as file:
            file.write(answer)
        print("Assistant's analysis was succesfully saved!")
        return file_name
    except Exception as e:
        print("Could not save the assistant's analysis.")
        print(e)
        return
