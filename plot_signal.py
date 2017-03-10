def plt_signal(x, y, labelx, labely, direccion, mostrar, guardar)
    '''
    Plots and saves a signal.
    Input: vectors x and y, labels for each axis (str), a path to de output image in 
           direccion (str), a order for show the picture, and a order to save or not 
           the result in a png there (guardar =1 saves the file).
    Output: The function shows picture and saves it in direccion in png format.
    '''

    #plt.figure(figsize=(30,10))
    plt.plot(x,y)
    plt.plot(times, envolv, linewidth=3)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    #plt.plot(times,peaks,'.')
    plt.show()
    plt.savefig(direccion+'.png')
    plt.close()

    pass
