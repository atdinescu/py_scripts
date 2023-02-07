import seaborn as sns

def label_cohort (row):
    if ((row['GP'] == 'GP_10') or (row['GP'] == 'GP_11') or (row['GP'] == 'GP_12')):
        return 5
    elif ((row['GP'] == 'GP_9') or (row['GP'] == 'GP_13') or (row['GP'] == 'GP_14') or (row['GP'] == 'GP_15')):
        return 4
    elif ((row['GP'] == 'GP_8')  or (row['GP'] == 'GP_16') or (row['GP'] == 'GP_17')):
        return 3
    else:
        return 0

def ITS_plot(ITS_param, data, x, order, hue, hue_order):
	hue_plot_params = {
		'data': data,
		'x': x,
		"order": order,
		"hue": hue,
		"hue_order": hue_order}

    ax = sns.barplot(**hue_plot_params, y=ITS_param, estimator=np.mean, ci=68, capsize=.2, errcolor='white') 
	#,fill=False)
    ax = sns.stripplot(**hue_plot_params, y=ITS_param, color='white', dodge=True)
    
    #ax = sns.barplot(**hue_plot_params, y=ITS_param, estimator=np.mean, ci=68, capsize=.2, errcolor='black') #,fill=False)
    #ax = sns.swarmplot(**hue_plot_params, y=ITS_param, color='black', dodge=True)
    
    ax.set(xlabel = 'Location')
    ax.set(ylabel = '')
    ax.set(title = ITS_param)

    ax.legend_.remove()
    #ax.legend(loc='upper center',ncol=4)
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)

    annotator = Annotator(ax, pairs, **hue_plot_params, y=ITS_param,show_non_significant=False)
    annotator.configure(test='t-test_ind', comparisons_correction='BH', correction_format="replace", text_format='star', color='white', loc='inside',pvalue_thresholds=[[1e-4, "*"], [1e-3, "*"], [1e-2, "*"], [0.05, "*"],[1, ""]])
    annotator.apply_and_annotate()
 
    img_name = str(DATA) + "/ITS_" + ITS_param + ".png"
    plt.tight_layout()

    plt.savefig(img_name, bbox_inches = "tight")
	
def ITS_subplots(ITS_param1, ITS_param2, ITS_param3):
    plt.subplot(1,3,1)
    ITS_plot(ITS_param1)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(1,3,2)
    ITS_plot(ITS_param2)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(1,3,3)
    ITS_plot(ITS_param3)
    plt.xticks(rotation=45, ha='right')
    
    img_name = str(DATA) + "/ITS_subplots.png"
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig(img_name) #, bbox_inches = "tight")	
    
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
    
    img_name = str(DATA) + "/ITS_subplots.png"
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig(img_name) #, bbox_inches = "tight")	
    
def ITS_subplots6(ITS_param1, ITS_param2, ITS_param3, ITS_param4, ITS_param5, ITS_param6):
    plt.subplot(3,2,1)
    ITS_plot(ITS_param1)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(3,2,2)
    ITS_plot(ITS_param2)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(3,2,3)
    ITS_plot(ITS_param3)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(3,2,4)
    ITS_plot(ITS_param4)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(3,2,5)
    ITS_plot(ITS_param5)
    plt.xticks(rotation=45, ha='right')
    plt.subplot(3,2,6)
    ITS_plot(ITS_param6)
    plt.xticks(rotation=45, ha='right')
    
    img_name = str(DATA) + "/ITS_subplots.png"
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig(img_name) #, bbox_inches = "tight")	