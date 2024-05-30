import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib.request
import json

class PlotDrawer:
    def __init__(self, plots_folder):
        self.plots_folder = plots_folder
        os.makedirs(self.plots_folder, exist_ok=True)
    
    def draw_plots(self, data):
        df = pd.DataFrame(data)
        
        for column in df.columns:
            if column not in ['name', 'gt_corners', 'rb_corners']:
                plt.figure(figsize=(10, 6))
                plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
                plt.title(f'Histogram of {column}')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.grid(True)
                plt.tight_layout()
                
                plot_path = os.path.join(self.plots_folder, f'{column}_histogram.png')
                plt.savefig(plot_path)
                plt.close()
                
                print(f'Plot saved: {plot_path}')
        
        return [os.path.join(self.plots_folder, file) for file in os.listdir(self.plots_folder)]

if __name__ == "__main__":
    with urllib.request.urlopen("https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json") as url:
        data = json.loads(url.read().decode())

    plots_folder = 'plots'

    drawer = PlotDrawer(plots_folder)

    plot_paths = drawer.draw_plots(data)
    
    print("Paths to saved plots:")
    for plot in plot_paths:
        print(plot)
