from urllib import urlencode
from urllib2 import urlopen
from random import choice

url = "http://rubiksolve.com/cubesolve.php"

trials = 1

colors = {
    1 : 'Y',
    2 : 'R',
    3 : 'B',
    4 : 'W',
    5 : 'G',
    6 : 'O'
}

tData = []

for tr in range( 0, trials ):
    data = {
        'cubevariablevalue': {  'U' : [ 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 
        'L' : [ 6, 6, 6, 6, 6, 6, 6, 6, 6 ], 
        'F' : [ 4, 4, 4, 4, 4, 4, 4, 4, 4 ], 
        'R' : [ 2, 2, 2, 2, 2, 2, 2, 2, 2 ], 
        'B' : [ 1, 1, 1, 1, 1, 1, 1, 1, 1 ], 
        'D' : [ 5, 5, 5, 5, 5, 5, 5, 5, 5 ] },
        'solvesubmit' : 'Solve Cube'
    }

    sideNumbers = {
        0 : 'L',
        2 : 'R'
    }

    sandwichNumbers = {
        0 : 'U',
        6 : 'D'
    }

    def turnClockwise( a ):
        c = 0
        r1 = []
        r2 = []
        r3 = []
        for i in list( reversed( a ) ):
            if c == 0:
                r3.append( i )
            elif c == 1:
                r2.append( i )
            elif c == 2:
                r1.append( i )
            c = ( c + 1 ) % 3
        return r1 + r2 + r3

    def sideForward( x ):
        currVals = []
        c = 0
        for i in data['cubevariablevalue']['U']:
            if c == x:
                currVals.append( i )
            c = ( c + 1 ) % 3
        c = 0
        for i in data['cubevariablevalue']['F']:
            if c == x:
                currVals.append( i )
            c = ( c + 1 ) % 3
        c = 0
        for i in data['cubevariablevalue']['D']:
            if c == x:
                currVals.append( i )
            c = ( c + 1 ) % 3
        c = 0
        if x == 0:
            b = 2
        else:
            b = 0
        for i in data['cubevariablevalue']['B']:
            if c == b:
                currVals.append( i )
            c = ( c + 1 ) % 3
        #Upper Layer Switch
        data['cubevariablevalue']['U'][x] = currVals[3]
        data['cubevariablevalue']['U'][x + 3] = currVals[4]
        data['cubevariablevalue']['U'][x + 6] = currVals[5]
        #Front Layer Switch
        data['cubevariablevalue']['F'][x] = currVals[6]
        data['cubevariablevalue']['F'][x + 3] = currVals[7]
        data['cubevariablevalue']['F'][x + 6] = currVals[8]
        #Down Layer Switch
        data['cubevariablevalue']['D'][x] = currVals[11]
        data['cubevariablevalue']['D'][x + 3] = currVals[10]
        data['cubevariablevalue']['D'][x + 6] = currVals[9]
        #Back Layer Switch
        if x == 0:
            b = 2
        else:
            b = 0
        data['cubevariablevalue']['B'][b] = currVals[2]
        data['cubevariablevalue']['B'][b + 3] = currVals[1]
        data['cubevariablevalue']['B'][b + 6] = currVals[0]
        #Right/Left Layer Switch
        for i in range(0, 3):
            data['cubevariablevalue'][sideNumbers[x]] = turnClockwise( data['cubevariablevalue'][sideNumbers[x]] )
            if x == 2:
                break

    def sandwichCw( x ):
        currVals = []
        c = x
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['F'][c] )
            c += 1
        c = x
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['L'][c] )
            c += 1
        c = x
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['B'][c] )
            c += 1
        c = x
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['R'][c] )
            c += 1
        #Front Layer Switch
        data['cubevariablevalue']['F'][x] = currVals[9]
        data['cubevariablevalue']['F'][x + 1] = currVals[10]
        data['cubevariablevalue']['F'][x + 2] = currVals[11]
        #Left Layer Switch
        data['cubevariablevalue']['L'][x] = currVals[0]
        data['cubevariablevalue']['L'][x + 1] = currVals[1]
        data['cubevariablevalue']['L'][x + 2] = currVals[2]
        #Back Layer Switch
        data['cubevariablevalue']['B'][x] = currVals[3]
        data['cubevariablevalue']['B'][x + 1] = currVals[4]
        data['cubevariablevalue']['B'][x + 2] = currVals[5]
        #Right Layer Switch
        data['cubevariablevalue']['R'][x] = currVals[6]
        data['cubevariablevalue']['R'][x + 1] = currVals[7]
        data['cubevariablevalue']['R'][x + 2] = currVals[8]
        #Up/Down Layer Switch
        for i in range( 0, 3 ):
            data['cubevariablevalue'][sandwichNumbers[x]] = turnClockwise( data['cubevariablevalue'][sandwichNumbers[x]] )
            if x == 0:
                break

    def frontCw():
        currVals = []
        c = 6
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['U'][c] )
            c += 1
        c = 0
        for i in data['cubevariablevalue']['L']:
            if c == 2:
                currVals.append( i )
            c = ( c + 1 ) % 3
        c = 0
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['D'][c] )
            c += 1
        c = 0
        for i in data['cubevariablevalue']['R']:
            if c == 0:
                currVals.append( i )
            c = ( c + 1 ) % 3
        #Front Layer Switch
        data['cubevariablevalue']['U'][6] = currVals[5]
        data['cubevariablevalue']['U'][7] = currVals[4]
        data['cubevariablevalue']['U'][8] = currVals[3]
        #Left Layer Switch
        data['cubevariablevalue']['L'][2] = currVals[6]
        data['cubevariablevalue']['L'][5] = currVals[7]
        data['cubevariablevalue']['L'][8] = currVals[8]
        #Down Layer Switch
        data['cubevariablevalue']['D'][0] = currVals[11]
        data['cubevariablevalue']['D'][1] = currVals[10]
        data['cubevariablevalue']['D'][2] = currVals[9]
        #Right Layer Switch
        data['cubevariablevalue']['R'][0] = currVals[0]
        data['cubevariablevalue']['R'][3] = currVals[1]
        data['cubevariablevalue']['R'][6] = currVals[2]
        #Up/Down Layer Switch
        data['cubevariablevalue']['F'] = turnClockwise( data['cubevariablevalue']['F'] )

    def backCw():
        currVals = []
        c = 0
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['U'][c] )
            c += 1
        c = 0
        for i in data['cubevariablevalue']['L']:
            if c == 0:
                currVals.append( i )
            c = ( c + 1 ) % 3
        c = 6
        for i in range( 0, 3 ):
            currVals.append( data['cubevariablevalue']['D'][c] )
            c += 1
        c = 0
        for i in data['cubevariablevalue']['R']:
            if c == 2:
                currVals.append( i )
            c = ( c + 1 ) % 3
        #Front Layer Switch
        data['cubevariablevalue']['U'][0] = currVals[5]
        data['cubevariablevalue']['U'][1] = currVals[4]
        data['cubevariablevalue']['U'][2] = currVals[3]
        #Left Layer Switch
        data['cubevariablevalue']['L'][0] = currVals[6]
        data['cubevariablevalue']['L'][3] = currVals[7]
        data['cubevariablevalue']['L'][6] = currVals[8]
        #Down Layer Switch
        data['cubevariablevalue']['D'][6] = currVals[11]
        data['cubevariablevalue']['D'][7] = currVals[10]
        data['cubevariablevalue']['D'][8] = currVals[9]
        #Right Layer Switch
        data['cubevariablevalue']['R'][2] = currVals[0]
        data['cubevariablevalue']['R'][5] = currVals[1]
        data['cubevariablevalue']['R'][8] = currVals[2]
        #Up/Down Layer Switch
        for i in range( 0, 3 ):
            data['cubevariablevalue']['B'] = turnClockwise( data['cubevariablevalue']['B'] )

    faces = {
      'R' : { 'allowed' : True, 'enables' : ['U', 'D', 'F', 'B'] },
      'L' : { 'allowed' : True, 'enables' : ['U', 'D', 'F', 'B'] },
      'U' : { 'allowed' : True, 'enables' : ['R', 'L', 'F', 'B'] },
      'D' : { 'allowed' : True, 'enables' : ['R', 'L', 'F', 'B'] },
      'F' : { 'allowed' : True, 'enables' : ['R', 'L', 'U', 'D'] },
      'B' : { 'allowed' : True, 'enables' : ['R', 'L', 'U', 'D'] }
    }

    face_index = ['R', 'L', 'U', 'D', 'F', 'B']

    scramble = []

    turns = 25

    for i in range( 0, turns ):
        face = choice( face_index )
        while not faces[face]['allowed'] :
            face = choice( face_index )
        faces[face]['allowed'] = False
        for f in range( 0, 4 ):
            faces[faces[face]['enables'][f]]['allowed'] = True
        direction = choice( [ "", '\'', '2' ] )
        scramble.append( face + direction )

    #scramble = ["R'", 'D2', 'U', 'B2', "L'", "D'", "F'", 'D2', "L'", 'B', 'D', 'R2', 'L2', 'U', 'D2', 'L2', 'F', 'B2', 'L2', 'R', "F'", "L'", 'F2', "R'", 'L']

    #print scramble

    for turn in scramble:
        temp = turn.split( '2' )
        num = len( temp )
        turn = temp[ 0 ]
        for i in range( 0, num ):
            if turn == 'R':
                sideForward( 2 )
            elif turn == 'R\'':
                sideForward( 2 )
                sideForward( 2 )
                sideForward( 2 )
            elif turn == 'L':
                sideForward( 0 )
                sideForward( 0 )
                sideForward( 0 )
            elif turn == 'L\'':
                sideForward( 0 )
            elif turn == 'U':
                sandwichCw( 0 )
            elif turn == 'U\'':
                sandwichCw( 0 )
                sandwichCw( 0 )
                sandwichCw( 0 )
            elif turn == 'D':
                sandwichCw( 6 )
                sandwichCw( 6 )
                sandwichCw( 6 )
            elif turn == 'D\'':
                sandwichCw( 6 )
            elif turn == 'F':
                frontCw()
            elif turn == 'F\'':
                frontCw()
                frontCw()
                frontCw()
            elif turn == 'B':
                backCw()
                backCw()
                backCw()
            elif turn == 'B\'':
                backCw()
            else:
                print 'false'

    newData = ' '
    t = 1
    newData += 'U:'
    for u in data['cubevariablevalue']['U']:
        newData += str( u )
    newData += ' '
    newData += 'L:'
    for u in data['cubevariablevalue']['L']:
        newData += str( u )
    newData += ' '
    newData += 'F:'
    for u in data['cubevariablevalue']['F']:
        newData += str( u )
    newData += ' '
    newData += 'R:'
    for u in data['cubevariablevalue']['R']:
        newData += str( u )
    newData += ' '
    newData += 'B:'
    for u in data['cubevariablevalue']['B']:
        newData += str( u )
    newData += ' '
    newData += 'D:'
    for u in data['cubevariablevalue']['D']:
        newData += str( u )
    data['cubevariablevalue'] = newData

    solver = urlopen( url=url, data=urlencode( data ) )
    siteData = solver.read()
    print siteData.count( '1/4' ) + ( 2 * siteData.count( '1/2' ) )
    tData.append( siteData.count( '1/4' ) + ( 2 * siteData.count( '1/2' ) ) )

