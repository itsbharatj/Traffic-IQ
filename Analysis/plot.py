import matplotlib.pyplot as plt
import json

from scipy.interpolate import make_interp_spline
import numpy as np


with open('./lights_data.json', 'r') as f_obj :
    data = json.load(f_obj)

data = [
    data_point for data_point in data if data_point["way"] != "SH12A"
]

# print(data)

# data = {
#     0: 0, 103: 13, 155: 19, 263: 31, 334: 38, 345: 42, 362: 49,
#     381: 53, 416: 60, 508: 73, 564: 80, 732: 103, 935: 134,
#     1089: 171, 1106: 176, 1119: 193, 1255: 222, 1420: 240,
#     1494: 247, 1613: 257, 1632: 259, 1759: 270, 1788: 272,
#     1897: 283, 1947: 288, 1985: 291, 2019: 294, 2254: 315,
#     2315: 321, 2375: 329, 2535: 358, 2577: 369, 2670: 395,
#     2741: 414, 2752: 417, 2853: 434, 3075: 462, 3171: 479,
#     3184: 481, 3449: 513, 3599: 524, 3687: 531, 3950: 553,
#     4065: 575, 4076: 580, 4140: 593, 4190: 602, 4277: 614,
#     4388: 626, 4555: 641, 4593: 645, 4753: 671, 4792: 679,
#     4814: 683, 4902: 696, 4928: 701, 5086: 724, 5176: 736,
#     5237: 747, 5250: 754, 5347: 774, 5439: 791, 5476: 796,
#     5545: 804, 5617: 813, 5625: 814, 5679: 820, 5704: 823,
#     5747: 827, 5806: 834, 5829: 836, 5908: 845, 5990: 854,
#     6075: 863, 6233: 878, 6276: 883, 6347: 894, 6414: 908,
#     6464: 921, 6503: 930, 6550: 939, 6574: 944, 6614: 951,
#     6711: 963, 6751: 967, 6789: 971, 6822: 975, 6901: 982,
#     6942: 986, 6966: 989, 7083: 1000, 7137: 1006, 7280: 1025,
#     7355: 1034, 7393: 1039, 7493: 1051, 7537: 1058, 7541: 1059,
#     7586: 1074, 7600: 1076, 7639: 1081, 7649: 1083, 7688: 1088,
#     7698: 1090, 7737: 1096, 7746: 1099, 8156: 1138, 8464: 1160,
#     8612: 1176, 8642: 1181, 8673: 1186, 8692: 1191, 9114: 1233,
#     9131: 1235, 9223: 1246, 9376: 1269, 9460: 1282, 9473: 1284,
#     9488: 1287, 9607: 1304, 9666: 1312, 9735: 1321, 9804: 1330,
#     9894: 1339, 9916: 1342, 10332: 1380, 10463: 1395, 10594: 1413,
#     10631: 1419, 10694: 1429, 10729: 1434, 10829: 1450
# }

intersections = [1100, 2700, 3200, 4000, 4820, 5650, 6450, 7450, 8080, 9500, ]

# # Extract keys and values
# x_values = list(data.keys())
# y_values = list(data.values())

# Plot the data
plt.figure(figsize=(10, 5))

splines = []

for data_point in data[:] : 

    x_values = [int(x) for x in data_point["road_distance_timing(meters:seconds)"].keys()]
    y_values = list(data_point["road_distance_timing(meters:seconds)"].values())

    X_Y_Spline = make_interp_spline(x_values, y_values)
    splines.append(X_Y_Spline)

    X_ = np.linspace(min(x_values), max(x_values), 15000)
    Y_ = X_Y_Spline(X_)

    plt.plot(X_, Y_, color='b', alpha=0.1)

    # plt.plot(x_values, y_values, linestyle='-', color='b', alpha=0.1)

# Add vertical lines with thin width and less opacity
for xc in intersections:
    plt.axvline(x=xc, color='k', linestyle='--', linewidth=2, alpha=0.4)

plt.xlabel('Distance, d (in m)')
plt.ylabel('Time to Travel d, t (in sec)')
plt.title('Travel Plot')
# plt.legend()
plt.grid()
plt.show()

