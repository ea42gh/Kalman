import matplotlib.pyplot as plt
import numpy as np

from filterpy.stats import plot_covariance_ellipse

# ---------------------------------------------------------------------------------
def show_legend():
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# ---------------------------------------------------------------------------------
def set_labels(title=None, x=None, y=None):
    """ helps make code in book shorter. Optional set title, xlabel and ylabel
    """
    if x is not None:
        plt.xlabel(x)
    if y is not None:
        plt.ylabel(y)
    if title is not None:
        plt.title(title)
# ---------------------------------------------------------------------------------
def set_limits(x, y):
    """ helper function to make code in book shorter. Set the limits for the x
    and y axis.
    """
    plt.gca().set_xlim(x)
    plt.gca().set_ylim(y)
# ---------------------------------------------------------------------------------
def show_cov4x4( Q, lbls=('$x$', '$y$', '$\dot x$', '$\dot y$') ):
    fig = plt.figure(figsize=(4, 4))
    im = plt.imshow( Q, interpolation="none", cmap=plt.get_cmap('binary'))
    plt.title('Covariance Matrix')
    ylocs, ylabels = plt.yticks()
    # set the locations of the yticks
    plt.yticks(np.arange(5))
    # set the locations and labels of the yticks
    plt.yticks(np.arange(4), lbls, fontsize=22)

    xlocs, xlabels = plt.xticks()
    # set the locations of the yticks
    plt.xticks(np.arange(5))
    # set the locations and labels of the yticks
    plt.xticks(np.arange(4), lbls, fontsize=22)

    plt.xlim([-0.5,3.5])
    plt.ylim([3.5, -0.5])

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes("right", "5%", pad="3%")
    plt.colorbar(im, cax=cax)

    plt.tight_layout()
# ---------------------------------------------------------------------------------
def show_cov6x6( Q ):
    fig = plt.figure(figsize=(4, 4))
    im = plt.imshow( Q, interpolation="none", cmap=plt.get_cmap('binary'))
    plt.title('Covariance Matrix')
    ylocs, ylabels = plt.yticks()
    # set the locations of the yticks
    plt.yticks(np.arange(7))
    # set the locations and labels of the yticks
    #plt.yticks(np.arange(4), lbls, fontsize=22)

    xlocs, xlabels = plt.xticks()
    # set the locations of the yticks
    plt.xticks(np.arange(7))
    # set the locations and labels of the yticks
    #plt.xticks(np.arange(7), lbls, fontsize=22)

    plt.xlim([-0.5,3.5])
    plt.ylim([3.5, -0.5])

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes("right", "5%", pad="3%")
    plt.colorbar(im, cax=cax)

    plt.tight_layout()
# ---------------------------------------------------------------------------------
def plot_measurements(xs, ys=None, color='k', lw=2, label='Measurements',
                       lines=False, **kwargs):
     """ Plot measurements"""

     plt.autoscale(tight=True)
     if lines:
         if ys is not None:
             return plt.plot(xs, ys, color=color, lw=lw, ls='--', label=label, **kwargs)
         else:
             return plt.plot(xs, color=color, lw=lw, ls='--', label=label, **kwargs)
     else:
         if ys is not None:
             return plt.scatter(xs, ys, edgecolor=color, facecolor='none',
                         lw=2, label=label, **kwargs),
         else:
             return plt.scatter(range(len(xs)), xs, edgecolor=color, facecolor='none',
                         lw=2, label=label, **kwargs),
 
# ---------------------------------------------------------------------------------
def plot_filter(xs, ys=None, c='#013afe', label='Filter', var=None, **kwargs):
    if ys is None:
        ys = xs
        xs = range(len(ys))

    plt.plot(xs, ys, color=c, label=label, **kwargs)

    if var is None:
        return

    var = np.asarray(var)

    std = np.sqrt(var)
    std_top = ys+std
    std_btm = ys-std

    plt.plot(xs, ys+std, linestyle=':', color='k', lw=2)
    plt.plot(xs, ys-std, linestyle=':', color='k', lw=2)
    plt.fill_between(xs, std_btm, std_top,
                     facecolor='yellow', alpha=0.2)
# ---------------------------------------------------------------------------------
def plot_track(xs, ys=None, label='Track', color='k', lw=2, **kwargs):
    if ys is not None:
        return plt.plot(xs, ys, color=color, lw=lw, ls=':', label=label, **kwargs)
    else:
        return plt.plot(xs, color=color, lw=lw, ls=':', label=label, **kwargs)
# ---------------------------------------------------------------------------------
def plot_kf_result( data, mu, cov=None, cols=(0,2), title=None, aspect_equal=True, lloc=2):
    '''
    data       - dat frame with zs in 'x','y',  track in 'x.true', 'y.true'
    x,y        - filter output positions
    '''
    plot_filter(mu[:,cols[0]], mu[:,cols[1]], c='r')
    plot_track( data['x.true'], data['y.true'], color='k' )
    plot_measurements( data['x'], data['y'], color='b' )
    
    if cov is not None:
        for i in range( len(data) ):
            loc   = (mu[i,cols[0]], mu[i,cols[1]])
            P     = cov[i]
            covar = np.array([[P[cols[0], cols[0]], P[cols[1], cols[0]]], 
                              [P[cols[0], cols[1]], P[cols[1], cols[1]]]])
            plot_covariance_ellipse(loc, cov=covar, fc='y', ec='y', std=3, alpha=0.3, axis_equal=aspect_equal)

    plt.legend(loc=lloc)
    set_labels(title=title, y='meters', x='meters')
    if aspect_equal:
        plt.gca().set_aspect('equal')
    plt.xlim((-1, mu[-1,cols[0]]))
    plt.show()
# ---------------------------------------------------------------------------------
def plot_residual_limits(Ps, stds=1.):
    """ plots standand deviation given in Ps as a yellow shaded region. One std
    by default, use stds for a different choice (e.g. stds=3 for 3 standard
    deviations.
    """

    std = np.sqrt(Ps) * stds

    plt.plot(-std, color='k', ls=':', lw=2)
    plt.plot(std, color='k', ls=':', lw=2)
    plt.fill_between(range(len(std)), -std, std,
                 facecolor='#ffff00', alpha=0.3)
# ---------------------------------------------------------------------------------
def plot_residuals( t_x, x, var, dt=1, title=None, y_label=None, stds=1 ):
    res = t_x - x
    plt.figure()
    plt.plot( [dt*i for i in range(len(x))], res, color='#af3afe')
    plot_residual_limits( var, stds)
    set_labels( title=title,y=y_label,x='time (sec)' )

