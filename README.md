# NFL Player Performance Analysis with Clustering and LLM Integration

## Descripción del Proyecto

Este proyecto tiene como objetivo realizar un análisis detallado del rendimiento de los jugadores de la NFL mediante el uso de técnicas de clustering y aprendizaje automático. Los usuarios pueden seleccionar la o las temporadas, el tipo de temporada y las métricas específicas para el análisis. Además, el proyecto integra un modelo de LLM a través de LangChain para ofrecer análisis adicionales basados en las entradas del usuario y los resultados del clustering.

## Funcionalidades

- **Selección de temporada y tipo de temporada**: Los usuarios pueden elegir entre Regular Season, Playoffs o una combinación de ambos.
- **Selección de métricas**: Métricas relacionadas con passing, rushing, receiving y estadísticas avanzadas.
- **Análisis con clustering**: El sistema agrupa a los jugadores en clusters basados en sus estadísticas de rendimiento.
- **Generación de análisis**: El LLM proporciona un análisis detallado sobre los clusters formados, utilizando LangChain.
  
## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

### `utils`
- `clustering.py`: Realiza el análisis de clustering sobre las estadísticas de los jugadores.
- `get_data.py`: Obtiene y limpia los datos necesarios para el análisis.
- `install_requirements.py`: Script para instalar las dependencias necesarias.
- `json_to_dict.py`: Convierte archivos JSON en diccionarios de Python para procesar configuraciones y datos.

### `assistant`
- `assistant.py`: Integra el LLM para proporcionar análisis adicionales basados en los resultados del clustering.
- `first_analysis.py`: Realiza un análisis inicial sobre los datos seleccionados.
- `init_assistant.py`: Recibe la API del usuario. La valida y retorna al agente LLM inicializado y listo para generar el análisis. En caso de recibir una API inválida, retorna `None`

### `dictionaries`
- `mapping_s_type.json`: Liga los tipos de métricas con un string. Es utilizado para generar las gráficas, el reporte y el dataframe.
- `types_of_metrics.json`: Liga los tipos de métricas con todas las características que le corresponden a cada una. Es necesario para analizar sobre las necesidades del usuario.

### `módulo principal`
- `main.py`: Módulo principal que une todos los componentes y gestiona la interacción con el usuario.
- `input_data.json`: Archivo que recibe el proyecto para su funcionamiento. Los valores `years`, `s_type` y `tom` son modificables. 

## Tipos de Temporada

El sistema permite seleccionar el tipo de temporada que se desea analizar:

- `REG`: Temporada regular
- `POS`: Playoffs
- `ALL`: Temporada regular y playoffs combinados

## Tipos de Métricas

El proyecto ofrece análisis basados en varias métricas, organizadas en las siguientes categorías:

- **Passing Metrics**: completions, passing_yards, passing_tds, etc.
- **Rushing Metrics**: carries, rushing_yards, rushing_tds, etc.
- **Receiving Metrics**: receptions, receiving_yards, receiving_tds, etc.
- **Advanced Metrics**: pacr, wopr_x, fantasy_points, dom, etc.
- **Player Info**: player_display_name, recent_team, position_group, etc. Este tipo de métricas no puede ser analizado. En un futuro se planea agregar funcionalidades de visualización y para eso son estas características.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado:

- Python 3.10+
- Las dependencias listadas en `requirements.txt`

## Ejecución del Proyecto
1. Clona el repositorio:
```bash
git clone https://github.com/aramosc09/machine_learning_with_framework.git
```

2. Ejecuta el script principal:
```bash
python main.py
```

Este script incluye la instalación de las dependencias requeridas.

## Integración con LLM
El análisis adicional es generado por un modelo de LLM a través de la integración con LangChain. El LLM utiliza las entradas del usuario y los resultados de clustering para ofrecer una visión más detallada del rendimiento de los jugadores.

## Métricas

El proyecto se basa en uso de aprendizaje no supervisado. Por lo que no cuenta con métricas explícitas. El análisis de los jugadores es realizado por el LLM y el usuario. Así mismo, este proyecto cuenta con varios módulos encargados de realizar la limpieza necesaria del dataset dependiendo de las necesidades del usuario de manera automática. Así mismo el repositorio cuenta con un par de ejemplos de ejecuciones en `machine_learning_with_framework/clustered_data`

## Ejemplo de run `gif`

![Texto alternativo](example.gif)
