% Graphs by Jeromy Yu
figure(1)
%time
local_t_low = [696, 744, 755, 624, 763, 572, 696, 696, 590, 658, 620, 658, 668];
remote_t_low = [272, 224, 313, 263, 321, 290, 276, 249, 291, 268, 249, 253, 250];
random_t_low = [582, 668, 793, 586, 801, 648, 734, 658, 552, 620, 658, 658, 630];
our_t_low = [250, 300, 485, 270, 550, 355, 250, 250, 270, 250, 250, 250, 300];
local_t_med = [526, 603, 758, 729, 678, 679, 565];
remote_t_med = [297, 264, 250, 262, 290, 284, 255];
random_t_med = [607, 645, 647, 655, 754, 602, 641];
our_t_med = [350, 355, 365, 415, 353, 369, 387];
local_t_high = [657, 771, 723, 685, 685, 619];
remote_t_high = [298, 268, 293, 269, 291, 325];
random_t_high = [657, 809, 723, 685, 611, 733];
our_t_high = [435, 435, 575, 519, 519, 435];
%load carsmall
%boxplot(MPG, Origin)
ranges1 = char('Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Random L', 'Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L')
low = [local_t_low, remote_t_low, random_t_low, our_t_low];
med = [local_t_med, remote_t_med, random_t_med, our_t_med];
high = [local_t_high, remote_t_high, random_t_high, our_t_high];
time = [low, med, high];
ranges2 = char('Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M', 'Remote Only M','Random M','Random M','Random M','Random M','Random M','Random M','Random M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M')
ranges3 = char('Local Only H','Local Only H','Local Only H','Local Only H','Local Only H','Local Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Random H','Random H','Random H','Random H','Random H','Random H','Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H')
ranges_total = [ranges1;ranges2;ranges3];
length(ranges2);
length(ranges1);
length(ranges3);
%subplot(3,1,1);
hold on
boxplot(time, ranges_total);
ylabel('Optimal Schedule Time (s)')
grid on
%title('0~30 Objects Detected')
h(1) = plot(NaN,NaN, 'r');
h(2) = plot(NaN,NaN, 'b');
h(3) = plot(NaN,NaN, 'g');
h(4) = plot(NaN,NaN, 'k');
legend(h,'Local Only', 'Offload Only', 'Random', 'Our Approach', 'Location', 'southeast')
set(gca, 'FontName', 'Times');
set(gca, 'XTick', []);
hold off
%subplot(3,1,2);
%boxplot(med, ranges2);
%grid on
%ylabel('Time (s)')
%title('30~60 Objects Detected')
%set(gca, 'FontName', 'Times');
%subplot(3,1,3);
%boxplot(high, ranges3);
%grid on
%ylabel('Time (s)')
%title('60~90 Objects Detected')
%set(gca, 'FontName', 'Times');

figure(2)
%energy
local_e_low = [3381,3312,3330,2867,3620,2833,3299,2722,2766,2722,2969,3134,3147];
remote_e_low = [255,244,341,286,349,316,301,272,317,292,272,276,273];
random_e_low = [2681,3147,3124,2785,3620,3080,3175,3010,2642,3052,2928,3052,2776];
our_e_low = [271,321,566,291,796,411,271,271,311,271,271,271,321];
local_e_med = [2501, 3001, 2688,3436,2998,3222,2829];
remote_e_med = [324,300,268,343,299,322,278];
random_e_med = [2789,2836,3017,3066,3492,2728,2829];
our_e_med = [371,376,391,436,374,390,408];
local_e_high = [2964,3664,3362,3055,3096,3170];
remote_e_high = [325,366,336,305,309,317];
random_e_high = [2840,3087,2951,3014,3014,3087];
our_e_high = [456,456,596,540,540,456];
%load carsmall
%boxplot(MPG, Origin)
ranges1 = char('Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Random L', 'Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L')
low = [local_e_low, remote_e_low, random_e_low, our_e_low];
med = [local_e_med, remote_e_med, random_e_med, our_e_med];
high = [local_e_high, remote_e_high, random_e_high, our_e_high];
energy = [low, med, high];
ranges2 = char('Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M', 'Remote Only M','Random M','Random M','Random M','Random M','Random M','Random M','Random M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M')
ranges3 = char('Local Only H','Local Only H','Local Only H','Local Only H','Local Only H','Local Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Random H','Random H','Random H','Random H','Random H','Random H','Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H')
ranges_total = [ranges1;ranges2;ranges3];
length(ranges2);
length(ranges1);
length(ranges3);
%subplot(3,1,1);
hold on
boxplot(energy, ranges_total);
h(1) = plot(NaN,NaN, 'r');
h(2) = plot(NaN,NaN, 'b');
h(3) = plot(NaN,NaN, 'g');
h(4) = plot(NaN,NaN, 'k');
legend(h,'Local Only', 'Offload Only', 'Random', 'Our Approach', 'Location', 'northeast')
ylabel('Avg Energy/Drone (J)')
grid on
set(gca, 'FontName', 'Times');
set(gca, 'XTick', []);
hold off

figure(3)
%energy consumption rate
local_r_low = (local_e_low .* 5) ./ local_t_low
remote_r_low = (remote_e_low .* 5) ./ remote_t_low;
random_r_low = (random_e_low .*5) ./ random_t_low;
our_r_low = (our_e_low .* 5) ./ our_t_low;
local_r_med = (local_e_med .* 5) ./ local_t_med;
remote_r_med = (remote_e_med .* 5) ./ remote_t_med;
random_r_med = (random_e_med .*5) ./ random_t_med;
our_r_med = (our_e_med .* 5) ./ our_t_med;
local_r_high = (local_e_high .* 5) ./ local_t_high;
remote_r_high = (remote_e_high .* 5) ./ remote_t_high;
random_r_high = (random_e_high .*5) ./ random_t_high;
our_r_high = (our_e_high .* 5) ./ our_t_high;
ranges1 = char('Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Local Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Remote Only L','Random L', 'Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Random L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L','Our Approach L')
low = [local_r_low, remote_r_low, random_r_low, our_r_low];
med = [local_r_med, remote_r_med, random_r_med, our_r_med];
high = [local_r_high, remote_r_high, random_r_high, our_r_high];
rate = [low, med, high];
ranges2 = char('Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Local Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M','Remote Only M', 'Remote Only M','Random M','Random M','Random M','Random M','Random M','Random M','Random M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M', 'Our Approach M')
ranges3 = char('Local Only H','Local Only H','Local Only H','Local Only H','Local Only H','Local Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Remote Only H','Random H','Random H','Random H','Random H','Random H','Random H','Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H', 'Our Approach H')
ranges_total = [ranges1;ranges2;ranges3];
length(ranges2);
length(ranges1);
length(ranges3);
%subplot(3,1,1);
hold on
boxplot(rate, ranges_total);
h(1) = plot(NaN,NaN, 'rs');
h(2) = plot(NaN,NaN, 'bs');
h(3) = plot(NaN,NaN, 'gs');
h(4) = plot(NaN,NaN, 'ks');
legend(h,'Local Only', 'Offload Only', 'Random', 'Our Approach', 'Location', 'northeast')
ylabel('Energy Consumption Rate (J/s)')
grid on
set(gca, 'FontName', 'Times');
set(gca, 'XTick', []);
hold off
