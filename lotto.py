from random import shuffle
from time import sleep

gamenum = input( 'input lotto game number : ' )
for i in range( int( gamenum ) ):
    balls = [ x + 1 for x in range( 45 ) ]
    ret = []
    for j in range( 6 ):
        shuffle( balls )
        number = balls.pop()
        ret.append( number )
    ret.sort()

    print( f'lotto number {i + 1:2} : ', end = '' )
    print( ret )
    sleep( 1 )
