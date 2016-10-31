%Magenetic Field Model
%A program that maps z distance to magnetic field B
%Author:  Geoffrey Siow
%Last Edit:  October 30, 2016

%the minimum and maximum distances from the rail
min_z = 0.006;
max_z = 0.015;

z_steps = linspace (min_z, max_z, 1000);
B = zeros (1,length (z_steps));
%Br = 1.42-1.47 tesla
Br = 1.47;
L = 0.0254;
W = 0.0254;
D = 0.0254;
for n = 1:length(z_steps)
    B(n) = Br / pi * (atan (L*W/(2*z_steps(n)*(4*z_steps(n)^2 + L^2 + W^2)^0.5)) - atan(L*W/(2*(D+z_steps(n))*(4*(D+z_steps(n))^2+L^2+W^2)^0.5)));
end

plot (B, z_steps);
A = polyfit (B, z_steps, 999);


B_append = zeros(1, length(z_steps));
for j = 1: length(z_steps)
    for i = 1: length(A)
        B_append (j) = B_append (j) + A(i) * z_steps(j)^(length(A)-i);
    end
end

