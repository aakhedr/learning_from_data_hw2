function [x, y] = buildDataSet(N)

    %% Prepare and plot artificial dataset %%
    % ===================================== %
    
%     hold off;
    
    % generate random flaots uniformly from the interval [-1, 1]
    a = -1; b = 1;
    x1 = a + (b - a) .* rand(N, 1);		x2 = a + (b - a) .* rand(N, 1);
%     scatter(x1, x2); hold on;
%     xlabel('X1'); 	ylabel('X2');

    % pick at random two points uniformly from the interval [-1, 1]
    xAxis = a + (b - a) .* rand(2, 1); 	yAxis = a + (b - a) .* rand(2, 1);

    % linear function of form y = slope * x + y_intercept
    slope = (yAxis(2) - yAxis(1))/ (xAxis(2) - xAxis(1)); 
    intercept = yAxis(1) - (slope * xAxis(1));

    % draw line passing thru points (xAsix and yAxis)
    y1 = slope * -1 + intercept; y2 = slope * 1 + intercept;
%     scatter(xAxis, yAxis, 'filled', 'go'); 
%     line([-1 1], [y1 y2], 'Color', 'Green'); 	axis([-1 1 -1 1]);

    % complete the dataset of x and y
    x = [x1 x2]; 	y = zeros(N, 1);
    for i = 1:size(x, 1)
        if x(i, 2) > slope * x(i, 1) + intercept
            y(i) = 1; 		
%             scatter(x(i, 1), x(i, 2), 'filled', 'bo');
        elseif x(i, 2) < slope * x(i, 1) + intercept
            y(i) = -1; 		
%             scatter(x(i, 1), x(i, 2), 'filled', 'ro');
        else
            y(i) = 0;            				% Just in case :D
        end
    end
    % make sure there are no points on the line!
    assert(size(y(y == 0), 1) == 0);
end

