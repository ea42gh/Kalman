import matplotlib.pyplot as plt

def show_predictor_corrector():
    plt.figure(figsize=(11, 3.), facecolor='w')
    est_y = ((164.2-158)*.8 + 158)
    ax = plt.axes(xticks=[], yticks=[], frameon=False)

    # --------------------------------------------- Arrows
    ax.annotate('', xy=[1,159], xytext=[0,158],
                arrowprops=dict(arrowstyle='->',
                                ec='darkgreen', lw=3, shrinkA=6, shrinkB=5))

    ax.annotate('', xy=[1,159], xytext=[1,164.2],
                arrowprops=dict(arrowstyle='<-',
                                ec='k', lw=3, shrinkA=8, shrinkB=8))

    ax.annotate('', xy=(1., est_y), xytext=(0.9, est_y),
                arrowprops=dict(arrowstyle='<-', ec='#004080',
                                lw=2,
                                shrinkA=3, shrinkB=4))

    # --------------------------------------------- Target points for Arrows
    plt.scatter ([0,1], [158.0,est_y], c='k',s=128)
    plt.scatter ([1], [164.2], c='darkred',s=128)
    plt.scatter ([1], [159], c='darkgreen', s=128)
    
    # --------------------------------------------- Text Annotations
    plt.text (0, 157.8,        r"prior ($x_{t-1}$)", ha='center', va='top',fontsize=18)
    plt.text (0.5, 159.6,      r"prediction", ha='center',va='top',fontsize=18,color='darkgreen')
    plt.text (1.05, 158.8,     r"predicted prior $(\bar{x}_t)$", ha='center',va='top',fontsize=18,color='darkgreen')

    plt.text (1.02, est_y-1.5, r"residual ($y_t = z_t - \bar{x}_t$)", ha='left', va='center',fontsize=18)
    plt.text (0.9, est_y,      r"new estimate ($x_t$)", ha='right', va='center',fontsize=18)
    plt.text (0.8, est_y-0.8,  r"(posterior)", ha='right', va='center',fontsize=18)
    plt.text (1.0, 164.4,      r"measurement ($z_t$)",ha='center',va='bottom',fontsize=18,color='darkred')

    # --------------------------------------------- Finalize
    plt.xlabel('time')
    ax.yaxis.set_label_position("right")
    plt.ylabel('state')
    plt.xlim(-0.1, 1.5)

def show_pb_predictor_corrector():
    plt.figure(figsize=(11, 3.), facecolor='w')
    est_y = ((164.2-158)*.8 + 158)

    ax = plt.axes(xticks=[], yticks=[], frameon=False)
    
    # --------------------------------------------- Arrows
    ax.annotate('', xy=[1,159], xytext=[0,158],
                arrowprops=dict(arrowstyle='->',
                                ec='darkgreen', lw=3, shrinkA=6, shrinkB=5))

    ax.annotate('', xy=[1,159], xytext=[1,164.2],
                arrowprops=dict(arrowstyle='<-',
                                ec='k', lw=3, shrinkA=8, shrinkB=8))

    ax.annotate('', xy=(1., est_y), xytext=(0.9, est_y),
                arrowprops=dict(arrowstyle='<-', ec='#004080',
                                lw=2,
                                shrinkA=3, shrinkB=4))


    # --------------------------------------------- Target points for Arrows
    plt.scatter ([0,1], [158.0,est_y], c='k',s=128)
    plt.scatter ([1], [164.2], c='darkred',s=128)
    plt.scatter ([1], [159],   c='darkgreen', s=128)
    
    # --------------------------------------------- Text Annotations
    plt.text (0, 157.8,        r"prior ($x_{t-1}$)",  ha='center', va='top',fontsize=18)
    plt.text (0, 157.8-0.8,    r"$\mathscr{N}(x,P)$", ha='center', va='top',fontsize=18)

    plt.text (0.3, 160.4,      r"prediction", ha='center',va='top',fontsize=18,color='darkgreen')
    plt.text (0.3, 160.4-0.8,  r"$\mathscr{N}(dx,Q)$", ha='center',va='top',fontsize=18,color='darkgreen')

    plt.text (1.05, 158.8,     r"predicted prior $(\bar{x}_t)$", ha='center',va='top',fontsize=18,color='darkgreen')
    plt.text (1.05, 158.8-0.8, r"$\mathscr{N}(x,P) * \mathscr{N}(dx,Q)$", ha='center',va='top',fontsize=18,color='darkgreen')

    plt.text (1.0, 164.4,      r"measurement $\mathscr{N}(z,R)$",ha='center',va='bottom',fontsize=18,color='darkred')

    plt.text (1.02, est_y-1.5, r"Bayesian update", ha='left', va='center',fontsize=18)

    plt.text (0.9, est_y,      r"posterior", ha='right', va='center',fontsize=18)
    plt.text (0.8, est_y-0.8,  r"$x_t$", ha='right', va='center',fontsize=18)

    # --------------------------------------------- Finalize
    plt.xlabel('time')
    ax.yaxis.set_label_position("right")
    plt.ylabel('state')
    plt.xlim(-0.1, 1.5)
