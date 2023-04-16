find_max(X,Y,X) :- X => Y, !.
find_max(X,Y,X) :- X < Y.