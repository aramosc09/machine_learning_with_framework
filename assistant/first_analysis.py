def first_analysis(tom,s_types,years,summary_as_json,players_analyzed,metrics_analyzed,assistant):
    prompt = """
    I need you to analyze as deeply as possible the next data summary divided by clusters:
    {tom} from {s_types} at {years}.
    {players_analyzed} players were analyzed with {metrics_analyzed} metrics.

    {summary_as_json}""".format(tom=tom, s_types=s_types, years=years, players_analyzed=players_analyzed, metrics_analyzed=metrics_analyzed, summary_as_json=summary_as_json)
    assistant.chat(prompt)