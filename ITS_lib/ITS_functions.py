import seaborn as sns
import matplotlib.pyplot as plt
from statannotations.Annotator import Annotator

def label_cohort (row):
    if ((row['GP'] == 'GP_10') or (row['GP'] == 'GP_11') or (row['GP'] == 'GP_12')):
        return 5
    elif ((row['GP'] == 'GP_9') or (row['GP'] == 'GP_13') or (row['GP'] == 'GP_14') or (row['GP'] == 'GP_15')):
        return 4
    elif ((row['GP'] == 'GP_8')  or (row['GP'] == 'GP_16') or (row['GP'] == 'GP_17')):
        return 3
    else:
        return 0

def ITS_plot(ITS_param, ITS_param_units,hue_plot_params,pairs):
    #ax = sns.barplot(**hue_plot_params, y=ITS_param, estimator=np.mean, ci=68, capsize=.2, errcolor='white') 
    #ax = sns.stripplot(**hue_plot_params, y=ITS_param, color='white', dodge=True)
    
    ax = sns.barplot(**hue_plot_params, y=ITS_param, estimator=np.mean, ci=68, capsize=.15, errcolor='black') #,fill=False)
    ax = sns.stripplot(**hue_plot_params, y=ITS_param, color='black', size = 14, dodge=True)
    
    ax.set(xlabel = 'Location')
    ax.set(ylabel = ITS_param_units)
    #ax.set(title = ITS_param) #, fontweight=bold)

    ax.legend_.remove()
    #ax.legend(loc='upper center',ncol=4)
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)

    annotator = Annotator(ax, pairs, **hue_plot_params, y=ITS_param,show_non_significant=False)
    annotator.configure(test='t-test_ind', comparisons_correction='BH', correction_format="replace", text_format='star', color='black', loc='inside',pvalue_thresholds=[[1e-4, "*"], [1e-3, "*"], [1e-2, "*"], [0.05, "*"],[1, ""]])
    annotator.apply_and_annotate()
 
    img_name = str(DATA) + "/ITS_" + ITS_param + ".png"
    plt.tight_layout()

    plt.savefig(img_name, bbox_inches = "tight")
		
    
def ITS_subplots3(ITS_param1, ITS_param2, ITS_param3):
    plt.subplot(1,3,1)
    ITS_plot(ITS_param1)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(1,3,2)
    ITS_plot(ITS_param2)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(1,3,3)
    ITS_plot(ITS_param3)
    plt.xticks(rotation=45, ha='right')
    
    img_name = str(DATA) + "/ITS_subplots3.png"
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig(img_name) #, bbox_inches = "tight")		
    
def ITS_subplots6(ITS_param1, ITS_param_units1, ITS_param2, ITS_param_units2, ITS_param3, ITS_param_units3, ITS_param4, ITS_param_units4, ITS_param5, ITS_param_units5, ITS_param6, ITS_param_units6,):
    plt.subplot(3,2,1)
    ITS_plot(ITS_param1, ITS_param_units1)
    plt.xticks(ha='center')
    plt.subplot(3,2,2)
    ITS_plot(ITS_param2, ITS_param_units2)
    plt.xticks(ha='center')
    plt.subplot(3,2,3)
    ITS_plot(ITS_param3, ITS_param_units3)
    plt.xticks(ha='center')
    plt.subplot(3,2,4)
    ITS_plot(ITS_param4, ITS_param_units4)
    plt.xticks(ha='center')
    plt.subplot(3,2,5)
    ITS_plot(ITS_param5, ITS_param_units5)
    plt.xticks(ha='center')
    plt.subplot(3,2,6)
    ITS_plot(ITS_param6, ITS_param_units6)
    plt.xticks(ha='center')
    
    img_name = str(DATA) + "/ITS_subplots6.png"
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig(img_name) #, bbox_inches = "tight")	

def ITS_subplots9(ITS_param1, ITS_param_units1, ITS_param2, ITS_param_units2, ITS_param3, ITS_param_units3, ITS_param4, ITS_param_units4, ITS_param5, ITS_param_units5, ITS_param6, ITS_param_units6,
                 ITS_param7, ITS_param_units7, ITS_param8, ITS_param_units8, ITS_param9, ITS_param_units9):
    plt.subplot(3,3,1)
    ITS_plot(ITS_param1, ITS_param_units1)
    plt.xticks(ha='center')
    plt.subplot(3,3,2)
    ITS_plot(ITS_param2, ITS_param_units2)
    plt.xticks(ha='center')
    plt.subplot(3,3,3)
    ITS_plot(ITS_param3, ITS_param_units3)
    plt.xticks(ha='center')
    plt.subplot(3,3,4)
    ITS_plot(ITS_param4, ITS_param_units4)
    plt.xticks(ha='center')
    plt.subplot(3,3,5)
    ITS_plot(ITS_param5, ITS_param_units5)
    plt.xticks(ha='center')
    plt.subplot(3,3,6)
    ITS_plot(ITS_param6, ITS_param_units6)
    plt.xticks(ha='center')
    plt.subplot(3,3,7)
    ITS_plot(ITS_param7, ITS_param_units7)
    plt.xticks(ha='center')
    plt.subplot(3,3,8)
    ITS_plot(ITS_param7, ITS_param_units8)
    plt.xticks(ha='center')
    plt.subplot(3,3,9)
    ITS_plot(ITS_param9, ITS_param_units9)
    plt.xticks(ha='center')
    
    
    img_name = str(DATA) + "/ITS_subplots9.png"
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig(img_name) #, bbox_inches = "tight")		