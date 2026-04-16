import matplotlib.pyplot as plt
import seaborn as sns

def show_plot(reset_theme, small_text, data, x, y, title, x_axis=None, y_axis=None, hue=None, despine=None, plot_type=None):
    sns.set_theme(style="whitegrid")
    
    if reset_theme:
        plt.rcdefaults()
        sns.set_theme(style="whitegrid")

    if small_text:
        sns.set_theme(style='whitegrid', font_scale=0.7)

    if plot_type == 'bar':
        plot = sns.barplot(data=data, x=x, y=y, hue=hue)
        # adding labels to each bar, more info found here: https://www.geeksforgeeks.org/python/how-to-show-values-on-seaborn-barplot/
        for container in plot.containers:
            plot.bar_label(container, padding=2)
    else:
        plot = sns.lineplot(data=data, x=x, y=y, hue=hue)
    
    if x_axis is not None:
        plot.set_xlabel(x_axis)
    
    if y_axis is not None:
        plot.set_ylabel(y_axis)
    
    plot.set_title(label=title)

    if despine == 'bottom':
        sns.despine(bottom = True)
    elif despine == 'left':
        sns.despine(left=True)
    else:
        None
        
    plt.show()