function data = simulateNoise(data, noise)
    for i = 1:(size(data, 1) * noise)
        index = random('unid', size(data, 1));
        if data(index, end) == 1
            data(index, end) = -1
        else
            data(index, end) = -1
        end
    end
end