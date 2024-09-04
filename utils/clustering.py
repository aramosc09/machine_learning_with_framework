from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import os

def clustering(data,tom,years):
    print('About to apply clustering to data...')
    print(tom, 'in', years)
    print('----------------------------------------------------------------------------------')

    type_of_metrics = tom.lower().replace(' ','_')
    years_str = str(years).replace('[','').replace(']','').replace(', ','_')
    base_path = 'clustered_data/'+type_of_metrics+'_'+years_str
    os.makedirs(base_path,exist_ok=True)

    try:
        # Preprocesamiento de datos
        features = data.drop(columns=['player_display_name', 'recent_team', 'position_group', 'headshot_url'])
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)

        print('Applying clustering...')
        # Aplicar K-means
        kmeans = KMeans(n_clusters=2, random_state=42)  # Puedes ajustar el número de clusters
        data['cluster'] = kmeans.fit_predict(scaled_features)
        print('Clustering was succesfull!')

        players_analyzed = data.shape[0]
        metrics_analyzed = data.select_dtypes(include=['number']).shape[1]
        print(players_analyzed, 'players were analyzed with', metrics_analyzed, 'metrics!')

        summary = data.select_dtypes(include=['number']).groupby('cluster').mean()
        summary_path = 'summary_'+type_of_metrics+'_'+years_str+'.json'
        summary.to_json(os.path.join(base_path,summary_path),orient="index")
        print('Summary saved as:',summary_path)

        data_path = type_of_metrics+'_'+years_str+'.json'
        data.to_json(os.path.join(base_path,data_path),orient="records")
        print('Data saved as:',data_path)
        print('----------------------------------------------------------------------------------')

        print('Generating pairplot...')
        pairplot_path = type_of_metrics+'_pairplot_'+years_str+'.png'
        plt.figure()
        sns.pairplot(data,hue='cluster')
        plt.title(tom+'Pairplot by Clusters')
        plt.savefig(os.path.join(base_path,pairplot_path))
        print('Pairplot saved as:',pairplot_path)
        print('----------------------------------------------------------------------------------')

        return players_analyzed, metrics_analyzed, os.path.join(base_path,summary_path), os.path.join(base_path,data_path), base_path

    except Exception as e:
        print(e)
