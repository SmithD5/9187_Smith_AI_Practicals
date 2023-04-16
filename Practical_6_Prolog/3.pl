list_member(X,[X|_]).
list_member(X,[_|T]) :- list member(X,TAIL).