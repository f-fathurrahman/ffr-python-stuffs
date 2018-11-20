##
angular_momenta = ['s','p','d','f','g','h','i','j','k','l']
def orbit_transform(nl,string):
    """ Transform orbitals into strings<->tuples, e.g. (2,1)<->'2p'. """
    if string==True and type(nl)==type(''):
        return nl #'2p'->'2p'
    elif string==True:
        return '%i%s' %(nl[0],angular_momenta[nl[1]]) #(2,1)->'2p'
    elif string==False and type(nl)==type((2,1)):
        return nl      #(2,1)->(2,1)
    elif string==False:
        l=angular_momenta.index(nl[1])
        n=int(nl[0])
        return (n,l)  # '2p'->(2,1)
