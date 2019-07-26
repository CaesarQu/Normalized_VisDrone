% Graphs by Jeromy Yu
x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
%x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18];
y1 = [79, 122, 173, 231, 298, 449, 509, 612, 659, 721, 764, 806, 856, 959, 1030, 1071, 1121, 1200, 1238, 1279];
y2 = [846, 846, 846, 846, 866, 866, 866, 916, 916, 916, 916, 916, 916, 916, 916, 916, 916, 916, 916, 916];
y3 = [538, 504, 508, 542, 516, 599, 694, 565, 720, 575, 665, 698, 580, 566, 761, 685, 764, 744, 718, 686];
y4 = [69, 107, 150, 199, 253, 348, 398, 481, 520, 575, 612, 650, 692, 789, 852, 889, 929, 998, 1028, 1089];
[f1, a1] = fit(transpose(x),transpose(y1),'poly5');
[f2, a2] = fit(transpose(x),transpose(y2),'poly5');
[f3, a3] = fit(transpose(x),transpose(y3),'poly5');
[f4, a4] = fit(transpose(x),transpose(y4),'poly5');
diff1 = abs([f1(1)-y1(1),f1(2)-y1(2),f1(3)-y1(3),f1(4)-y1(4),f1(5)-y1(5),f1(6)-y1(6),f1(7)-y1(7),f1(8)-y1(8),f1(9)-y1(9),f1(10)-y1(10),f1(11)-y1(11),f1(12)-y1(12),f1(13)-y1(13),f1(14)-y1(14),f1(15)-y1(15),f1(16)-y1(16),f1(17)-y1(17),f1(18)-y1(18),f1(19)-y1(19),f1(20)-y1(20)]);
diff2 = abs([f2(1)-y2(1),f2(2)-y2(2),f2(3)-y2(3),f2(4)-y2(4),f2(5)-y2(5),f2(6)-y2(6),f2(7)-y2(7),f2(8)-y2(8),f2(9)-y2(9),f2(10)-y2(10),f2(11)-y2(11),f2(12)-y2(12),f2(13)-y2(13),f2(14)-y2(14),f2(15)-y2(15),f2(16)-y2(16),f2(17)-y2(17),f2(18)-y2(18),f2(19)-y2(19),f2(20)-y2(20)]);
diff3 = abs([f3(1)-y3(1),f3(2)-y3(2),f3(3)-y3(3),f3(4)-y3(4),f3(5)-y3(5),f3(6)-y3(6),f3(7)-y3(7),f3(8)-y3(8),f3(9)-y3(9),f3(10)-y3(10),f3(11)-y3(11),f3(12)-y3(12),f3(13)-y3(13),f3(14)-y3(14),f3(15)-y3(15),f3(16)-y3(16),f3(17)-y3(17),f3(18)-y3(18),f3(19)-y3(19),f3(20)-y3(20)]);
diff4 = abs([f4(1)-y4(1),f4(2)-y4(2),f4(3)-y4(3),f4(4)-y4(4),f4(5)-y4(5),f4(6)-y4(6),f4(7)-y4(7),f4(8)-y4(8),f4(9)-y4(9),f4(10)-y4(10),f4(11)-y4(11),f4(12)-y4(12),f4(13)-y4(13),f4(14)-y4(14),f4(15)-y4(15),f4(16)-y4(16),f4(17)-y4(17),f4(18)-y4(18),f4(19)-y4(19),f4(20)-y4(20)]);
figure(1)
hold on
%rectangle('Position',[4.75,y3(5)-diff3(5),0.5,diff3(5)*2]);
plot(x, y1,'ro-')
plot(x, y2,'bs-')
plot(x, y3,'m^-')
plot(x, y4,'k*-')
xline(17)
e1 = errorbar(x, y1, diff1)
e1.Color = 'red'
e2 = errorbar(x, y2, diff2)
e2.Color = 'blue'
e3 = errorbar(x, y3, diff3)
e3.Color = 'magenta'
e4 = errorbar(x, y4, diff4)
e4.Color = 'black'
xlabel('Air to Ground Sever Ratio')
ylabel('Optimal Schedule Time (s)')
h = zeros(4, 1);
h(1) = plot(NaN,NaN, 'ro-');
h(2) = plot(NaN,NaN, 'bs-');
h(3) = plot(NaN,NaN, 'm^-');
h(4) = plot(NaN,NaN, 'kx-');
legend(h,'Offload Only', 'Local Only', 'Random', 'Our Approach', 'Location', 'northwest')
set(gca, 'FontName', 'Times');
grid on
hold off
%legend({'Offload Only', 'Local Only', 'Random'},'Location', 'northwest')

figure(2)
z1 = [154, 171, 176, 171, 174, 193, 187, 199, 194, 190, 199, 198, 197, 196, 196, 195, 195, 193, 192, 190];
z2 = [6052, 4709, 4438, 4451, 4595, 5760, 5602, 5889, 5636, 5554, 5347, 5174, 5070, 5276, 5287, 5155, 5075, 5123, 5018, 4923];
z3 = [2973, 1602, 1876, 1976, 2278, 2040, 2708, 2569, 2572, 2452, 2541, 2560, 2594, 2408, 3067, 3050, 2948, 2922, 2978, 2924];
z4 = [240, 235, 241, 252, 271, 350, 344, 366, 353, 351, 340, 331, 326, 343, 345, 338, 334, 338, 332, 327];
[f1, a1] = fit(transpose(x),transpose(z1),'poly5');
[f2, a2] = fit(transpose(x),transpose(z2),'poly5');
[f3, a3] = fit(transpose(x),transpose(z3),'poly5');
[f4, a4] = fit(transpose(x),transpose(z4),'poly5');
diff1 = abs([f1(1)-z1(1),f1(2)-z1(2),f1(3)-z1(3),f1(4)-z1(4),f1(5)-z1(5),f1(6)-z1(6),f1(7)-z1(7),f1(8)-z1(8),f1(9)-z1(9),f1(10)-z1(10),f1(11)-z1(11),f1(12)-z1(12),f1(13)-z1(13),f1(14)-z1(14),f1(15)-z1(15),f1(16)-z1(16),f1(17)-z1(17),f1(18)-z1(18),f1(19)-z1(19),f1(20)-z1(20)]);
diff2 = abs([f2(1)-z2(1),f2(2)-z2(2),f2(3)-z2(3),f2(4)-z2(4),f2(5)-z2(5),f2(6)-z2(6),f2(7)-z2(7),f2(8)-z2(8),f2(9)-z2(9),f2(10)-z2(10),f2(11)-z2(11),f2(12)-z2(12),f2(13)-z2(13),f2(14)-z2(14),f2(15)-z2(15),f2(16)-z2(16),f2(17)-z2(17),f2(18)-z2(18),f2(19)-z2(19),f2(20)-z2(20)]);
diff3 = abs([f3(1)-z3(1),f3(2)-z3(2),f3(3)-z3(3),f3(4)-z3(4),f3(5)-z3(5),f3(6)-z3(6),f3(7)-z3(7),f3(8)-z3(8),f3(9)-z3(9),f3(10)-z3(10),f3(11)-z3(11),f3(12)-z3(12),f3(13)-z3(13),f3(14)-z3(14),f3(15)-z3(15),f3(16)-z3(16),f3(17)-z3(17),f3(18)-z3(18),f3(19)-z3(19),f3(20)-z3(20)]);
diff4 = abs([f4(1)-z4(1),f4(2)-z4(2),f4(3)-z4(3),f4(4)-z4(4),f4(5)-z4(5),f4(6)-z4(6),f4(7)-z4(7),f4(8)-z4(8),f4(9)-z4(9),f4(10)-z4(10),f4(11)-z4(11),f4(12)-z4(12),f4(13)-z4(13),f4(14)-z4(14),f4(15)-z4(15),f4(16)-z4(16),f4(17)-z4(17),f4(18)-z4(18),f4(19)-z4(19),f4(20)-z4(20)]);
hold on
for idx = 1:20
    plot([idx idx],[z1(idx)-diff1(idx) z1(idx)+diff1(idx)],'r')
    plot([idx idx],[z2(idx)-diff2(idx) z2(idx)+diff2(idx)],'b')
    plot([idx idx],[z3(idx)-diff3(idx) z3(idx)+diff3(idx)],'m')
    plot([idx idx],[z4(idx)-diff4(idx) z4(idx)+diff4(idx)],'k')
end
plot(x, z1,'ro-')
plot(x, z2,'bs-')
plot(x, z3,'m^-')
plot(x, z4,'kx-')
xlabel('Air to Ground Sever Ratio')
ylabel('Avg Energy/Drone (J)')
h = zeros(4, 1);
h(1) = plot(NaN,NaN, 'ro-');
h(2) = plot(NaN,NaN, 'bs-');
h(3) = plot(NaN,NaN, 'm^-');
h(4) = plot(NaN,NaN, 'kx-');
legend(h,'Offload Only', 'Local Only', 'Random', 'Our Approach', 'Location', 'northeast')
set(gca, 'FontName', 'Times');
grid on
hold off

figure(3)
hold on
w1 = (z1.*x) ./ y1
w2 = (z2.*x) ./ y2
w3 = (z3.*x) ./ y3
w4 = (z4.*x) ./ y4
plot(x, w1, 'ro-')
plot(x, w2, 'bs-')
plot(x, w3, 'm^-')
plot(x, w4, 'kx-')
xlabel('Air to Ground Server Ratio')
ylabel('Energy Consumption Rate (J/s)')
[f1, a1] = fit(transpose(x),transpose(w1),'poly5');
[f2, a2] = fit(transpose(x),transpose(w2),'poly5');
[f3, a3] = fit(transpose(x),transpose(w3),'poly5');
[f4, a4] = fit(transpose(x),transpose(w4),'poly5');
diff1 = abs([f1(1)-w1(1),f1(2)-w1(2),f1(3)-w1(3),f1(4)-w1(4),f1(5)-w1(5),f1(6)-w1(6),f1(7)-w1(7),f1(8)-w1(8),f1(9)-w1(9),f1(10)-w1(10),f1(11)-w1(11),f1(12)-w1(12),f1(13)-w1(13),f1(14)-w1(14),f1(15)-w1(15),f1(16)-w1(16),f1(17)-w1(17),f1(18)-w1(18),f1(19)-w1(19),f1(20)-w1(20)]);
diff2 = abs([f2(1)-w2(1),f2(2)-w2(2),f2(3)-w2(3),f2(4)-w2(4),f2(5)-w2(5),f2(6)-w2(6),f2(7)-w2(7),f2(8)-w2(8),f2(9)-w2(9),f2(10)-w2(10),f2(11)-w2(11),f2(12)-w2(12),f2(13)-w2(13),f2(14)-w2(14),f2(15)-w2(15),f2(16)-w2(16),f2(17)-w2(17),f2(18)-w2(18),f2(19)-w2(19),f2(20)-w2(20)]);
diff3 = abs([f3(1)-w3(1),f3(2)-w3(2),f3(3)-w3(3),f3(4)-w3(4),f3(5)-w3(5),f3(6)-w3(6),f3(7)-w3(7),f3(8)-w3(8),f3(9)-w3(9),f3(10)-w3(10),f3(11)-w3(11),f3(12)-w3(12),f3(13)-w3(13),f3(14)-w3(14),f3(15)-w3(15),f3(16)-w3(16),f3(17)-w3(17),f3(18)-w3(18),f3(19)-w3(19),f3(20)-w3(20)]);
diff4 = abs([f4(1)-w4(1),f4(2)-w4(2),f4(3)-w4(3),f4(4)-w4(4),f4(5)-w4(5),f4(6)-w4(6),f4(7)-w4(7),f4(8)-w4(8),f4(9)-w4(9),f4(10)-w4(10),f4(11)-w4(11),f4(12)-w4(12),f4(13)-w4(13),f4(14)-w4(14),f4(15)-w4(15),f4(16)-w4(16),f4(17)-w4(17),f4(18)-w4(18),f4(19)-w4(19),f4(20)-w4(20)]);
h = zeros(4, 1);
e1 = errorbar(x, w1, diff1)
e1.Color = 'red'
e2 = errorbar(x, w2, diff2)
e2.Color = 'blue'
e3 = errorbar(x, w3, diff3)
e3.Color = 'magenta'
e4 = errorbar(x, w4, diff4)
e4.Color = 'black'
h(1) = plot(NaN,NaN, 'ro-');
h(2) = plot(NaN,NaN, 'bs-');
h(3) = plot(NaN,NaN, 'm^-');
h(4) = plot(NaN,NaN, 'kx-');
legend(h,'Offload Only', 'Local Only','Random' ,'Our Approach', 'Location', 'northwest')
set(gca, 'FontName', 'Times');
ylim([0 60])
grid on
hold off