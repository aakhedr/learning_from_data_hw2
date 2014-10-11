[X, y] = buildDataSet(1000);
x3 = X(:, 1) .* X(:, 2);
x4 = X(:, 1).^2;
x5 = X(:, 2).^2;
X = [ones(size(X, 1), 1) X x3 x4 x5];
data = [X y];

% simulate noise on 10% of y
data = simulateNoise(data, .1);
X = data(:, 1:end - 1); y = data(:, end);

% Nomral equation
w = pinv(X' * X) * X' * y;

a = [-1, -.05, .08, .13, 1.5, 1.5]';
b = [-1, -.05, .08, .13, 1.5, 15]'; 
c = [-1, -.05, .08, .13, 15, 1.5]';
d = [-1, -1.5, .08, .13, .05, .05]';
e = [-1, -.05, .08, 1.5, .15, .15]';

yEst = sign(X * w); Ein_w = length(yEst(yEst~=y)) / length(yEst);
disp(Ein_w);

yEst_a = sign(X * a); Ein_a = length(yEst_a(yEst_a~=y)) / length(yEst_a);
yEst_b = sign(X * b); Ein_b = length(yEst_b(yEst_b~=y)) / length(yEst_b);
yEst_c = sign(X * c); Ein_c = length(yEst_c(yEst_c~=y)) / length(yEst_c);
yEst_d = sign(X * d); Ein_d = length(yEst_d(yEst_d~=y)) / length(yEst_d);
yEst_e = sign(X * e); Ein_e = length(yEst_e(yEst_e~=y)) / length(yEst_e);
disp(Ein_a);
disp(Ein_b);
disp(Ein_c);
disp(Ein_d);
disp(Ein_e);
