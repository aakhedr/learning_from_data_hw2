function randomPoints = pickRandomXrow(X, n)
    m = size(X, 1);
    randomPoints = zeros(n, size(X, 2));
    for i = 1:n
        index = random('unid', m);
        randomPoints(i, :) = X(index, :);
    end
end