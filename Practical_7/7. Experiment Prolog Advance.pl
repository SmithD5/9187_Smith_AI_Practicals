%Define the cities to be visited
city(a,0,0).
city(b,1,1).
city(c,2,2).
city(d,3,3).
city(e,4,4).

%define the distance betwwen two cities
distance(X,Y,D):-
    city(X,X1,Y1),
    city(Y,X2,Y2),
    D is sqrt((X2 -X1)**2 +(Y2-Y1)**2).
%Define the path as a list of cities
path([],0).
path([X], 0).
path([X,Y|T], Dist) :-
    path([Y|T],Dist1),
    distance(X,Y,D),
    Dist is Dist1 + D.
%find the shortest path that visits every city exactly once
tsp(Path,Dist):-
    findall(D, (perm([a,b,c,d,e],Path), path(Path, D)), DList),
    min_list(DList, Dist).
%Permute the elements of a list
perm([], []).
perm(List, [H|Perm]):-
    select(H, List, Rest),
    perm(Rest, Perm).
