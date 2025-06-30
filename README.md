# 🏈 NFL Player Performance Analysis with Clustering and LLM Integration

## Project Overview

This project aims to provide a detailed analysis of NFL player performance using clustering and machine learning techniques. Users can select one or multiple seasons, specify the type of season, and choose relevant performance metrics. Additionally, the project integrates a Large Language Model (LLM) via LangChain to generate enriched insights based on the user’s input and the clustering results.

---

## Features

- **Season and Type Selection**: Choose between Regular Season, Playoffs, or both.
- **Metric Selection**: Analyze performance based on passing, rushing, receiving, and advanced statistics.
- **Clustering Analysis**: Players are grouped into clusters according to their performance metrics.
- **LLM-Based Analysis**: An integrated LLM provides a narrative summary and interpretation of the clustering results using LangChain.

---

## Project Structure

The project is organized into the following modules:

### `utils`
- `clustering.py`: Performs clustering analysis on player statistics.
- `get_data.py`: Retrieves and cleans the necessary data.
- `install_requirements.py`: Installs all required dependencies.
- `json_to_dict.py`: Converts JSON files to Python dictionaries for configuration and data parsing.

### `assistant`
- `assistant.py`: Uses an LLM to generate additional analysis based on clustering results.
- `first_analysis.py`: Performs an initial statistical analysis of the selected dataset.
- `init_assistant.py`: Validates and initializes the LLM agent using the user’s API key. Returns `None` if the key is invalid.

### `dictionaries`
- `mapping_s_type.json`: Maps metric types to readable strings for charting, reporting, and DataFrame generation.
- `types_of_metrics.json`: Maps each metric category to its corresponding attributes, used to tailor the analysis.

### Main Module
- `main.py`: The main script that connects all components and handles user interaction.
- `input_data.json`: Input file where the user can modify values such as `years`, `s_type`, and `tom` to define the analysis scope.

---

## Season Types

The tool supports different season types:

- `REG`: Regular Season
- `POS`: Playoffs
- `ALL`: Combination of Regular Season and Playoffs

---

## Metric Categories

The analysis supports the following metric categories:

- **Passing Metrics**: completions, passing_yards, passing_tds, etc.
- **Rushing Metrics**: carries, rushing_yards, rushing_tds, etc.
- **Receiving Metrics**: receptions, receiving_yards, receiving_tds, etc.
- **Advanced Metrics**: pacr, wopr_x, fantasy_points, dom, etc.
- **Player Info**: player_display_name, recent_team, position_group, etc.  
  These are not used in the analysis but are reserved for future visualization features.

---

## Requirements

- Python 3.10+
- All packages listed in `requirements.txt`

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/aramosc09/machine_learning_with_framework.git
```
2. Run the main script:

```bash
python main.py
```

The script will automatically install required dependencies.

## LLM Integration

This project includes an LLM-powered assistant, integrated via LangChain. The model provides insightful commentary based on clustering outputs and the user’s selected metrics. This enables more nuanced interpretation of player performance.


## Evaluation

As the project relies on unsupervised learning, there are no predefined performance metrics. The interpretation of results is handled by both the user and the LLM assistant. The system includes automated data cleaning routines based on user inputs, streamlining the analysis process.

Several example runs are available in the `machine_learning_with_framework/clustered_data` folder.

## Example Run (GIF)

![Full Example](example.gif)
