min([A], A).
min([H|R], N):-
	min(R, RN),
	N is min(H, RN).