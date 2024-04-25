% Asegura que las coordenadas de la cabeza de la serpiente estén disponibles para comparar con la fruta
safe_direction([pos(X, Y)|_], pos(FX, FY), Direction) :-
    % Calcula nueva posición basada en la dirección y verifica que no sea parte del cuerpo de la serpiente
    (
        (Direction = left, X2 is X - 1, not(member(pos(X2, Y), [pos(X, Y)|_])));
        (Direction = right, X2 is X + 1, not(member(pos(X2, Y), [pos(X, Y)|_])));
        (Direction = up, Y2 is Y - 1, not(member(pos(X, Y2), [pos(X, Y)|_])));
        (Direction = down, Y2 is Y + 1, not(member(pos(X, Y2), [pos(X, Y)|_])))
    ).

% Ajusta la definición de closest_fruit para recibir la posición de la cabeza
closest_fruit(pos(X, Y), pos(FX, FY), Direction) :-
    (
        (FX < X, Direction = left);
        (FX > X, Direction = right);
        (FY < Y, Direction = up);
        (FY > Y, Direction = down)
    ).

% Ajusta move para incluir la posición de la cabeza en la llamada a closest_fruit
move(Snake, Fruit, Direction) :-
    Snake = [Head|_],
    safe_direction(Snake, Fruit, Direction),
    closest_fruit(Head, Fruit, Direction).

% Define estas cláusulas adecuadamente para que hagan algo significativo
safe_direction(Snake, pos(FX, FY), Direction) :-
    % Implementar lógica para evitar colisiones
    true.

closest_fruit(pos(FX, FY), Direction) :-
    % Implementar lógica para encontrar el camino más corto a la fruta
    true.

