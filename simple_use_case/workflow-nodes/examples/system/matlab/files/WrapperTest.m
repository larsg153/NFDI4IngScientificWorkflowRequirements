a=[1 2 3 4 5];
mean_a=mean(a);

a_cell=num2cell(a);
save("Mean.mat","mean_a");
fprintf("Executed matlab script to calculate the mean of an array:\n");
fprintf("The mean of the array [");
for i=1:length(a)-1
    fprintf(sprintf("%d ",a(i)));
end
fprintf(sprintf("%d] is %d\n",a(end),mean_a));
