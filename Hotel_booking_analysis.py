import numpy as np

booking_id = np.arange(1001, 1501)
customer_id = np.arange(501, 1001)

hotel = np.array([
"Leela","Hyatt","Oberoi","Novotel","Marriott",
"Marriott","Leela","Leela","Hyatt","Oberoi",
"Novotel","Leela","Taj","Oberoi","Novotel",
"ITC","ITC","Taj","Leela","Novotel",
"Hyatt","Taj","Leela","Leela","Hyatt",
"Taj","Marriott","Leela","ITC","Novotel",
"Marriott","Hyatt","Hyatt","Leela","Radisson",
"Taj","Taj","Leela","Radisson","Taj",
"Marriott","Radisson","Taj","ITC","Taj",
"Oberoi","Novotel","Novotel","Hyatt","Novotel",
"Oberoi","Leela","Marriott","Marriott","Taj",
"Marriott","Taj","Oberoi","Taj","Taj",
"Novotel","Leela","Radisson","Hyatt","Hyatt",
"Hyatt","Leela","Leela","ITC","Oberoi",
"Marriott","Taj","Radisson","Leela","Leela",
"Hyatt","Leela","Taj","Radisson","Hyatt",
"Marriott","Oberoi","Marriott","Marriott","Marriott",
"Oberoi","Marriott","Marriott","Hyatt","Marriott",
"Oberoi","Marriott","Novotel","Oberoi","Radisson",
"Oberoi","Radisson","Oberoi","Leela","Leela",
"ITC","Marriott","ITC","ITC","Radisson",
"Leela","Marriott","Marriott","ITC","Leela",
"Taj","Hyatt","Radisson","Marriott","Oberoi",
"Oberoi","Hyatt","Marriott","Novotel","Novotel",
"Hyatt","Hyatt","Radisson","Hyatt","Leela",
"Marriott","Marriott","Taj","Hyatt","Marriott",
"Taj","ITC","ITC","Novotel","Marriott",
"Leela","Leela","Radisson","ITC","Leela",
"Marriott","Radisson","Hyatt","Hyatt","Leela",
"Radisson","Taj","Novotel","Novotel","Radisson",
"Novotel","Radisson","Hyatt","Marriott","Leela",
"Oberoi","ITC","Leela","Radisson","Hyatt",
"Hyatt","Oberoi","Oberoi","Radisson","ITC",
"Taj","Hyatt","Novotel","Novotel","ITC",
"Hyatt","Novotel","Taj","ITC","Marriott",
"ITC","Novotel","Hyatt","Oberoi","Radisson",
"Novotel","ITC","Oberoi","Radisson","Leela",
"Oberoi","Novotel","Hyatt","Oberoi","Taj",
"Hyatt","Novotel","Leela","Radisson","Oberoi",
"Leela","Radisson","Hyatt","Marriott","Hyatt",
"Oberoi","Marriott","Novotel","Taj","Oberoi",
"Radisson","Radisson","Novotel","Marriott","Hyatt",
"Taj","Marriott","Leela","Leela","Oberoi",
"Hyatt","Hyatt","Radisson","Hyatt","Leela",
"Radisson","ITC","Oberoi","Novotel","Leela",
"Marriott","Marriott","ITC","Leela","Hyatt",
"Taj","Radisson","Marriott","Radisson","Taj",
"Radisson","Leela","Leela","Oberoi","Radisson",
"Taj","Hyatt","Marriott","Novotel","Radisson",
"Oberoi","ITC","Taj","ITC","Leela",
"Taj","Leela","Novotel","ITC","Oberoi",
"Oberoi","Radisson","Radisson","Marriott","Oberoi",
"Leela","Novotel","Taj","Taj","Oberoi",
"Oberoi","Novotel","Oberoi","Radisson","Marriott",
"Leela","ITC","Taj","Radisson","ITC",
"ITC","Novotel","Hyatt","ITC","Marriott",
"Hyatt","Taj","Leela","Oberoi","Hyatt",
"Oberoi","Hyatt","Novotel","Marriott","Novotel",
"ITC","Hyatt","Leela","Oberoi","Leela",
"Taj","ITC","Leela","Hyatt","Taj",
"Taj","Hyatt","Oberoi","Novotel","Taj",
"ITC","Taj","Leela","Marriott","Radisson",
"Radisson","Taj","Oberoi","Marriott","ITC",
"Taj","Taj","Hyatt","Radisson","Hyatt",
"Marriott","Radisson","Oberoi","Radisson","Novotel",
"ITC","Hyatt","Taj","Leela","Leela",
"Hyatt","Leela","ITC","ITC","Taj",
"Novotel","Leela","Novotel","Novotel","Radisson",
"Marriott","Oberoi","Radisson","Taj","Marriott",
"Leela","Oberoi","ITC","Taj","Oberoi",
"Marriott","Marriott","Hyatt","Novotel","Leela",
"Radisson","Marriott","Oberoi","Radisson","Novotel",
"Novotel","Hyatt","Marriott","Hyatt","Taj",
"Oberoi","ITC","ITC","Taj","Hyatt",
"Marriott","Oberoi","Taj","Hyatt","Novotel",
"Oberoi","Leela","Novotel","Taj","Radisson",
"ITC","Hyatt","Hyatt","Hyatt","Leela",
"Hyatt","Marriott","Oberoi","ITC","Taj",
"Radisson","ITC","Oberoi","Novotel","ITC",
"Radisson","Leela","Leela","Radisson","Radisson",
"Novotel","Leela","Radisson","Taj","ITC",
"Novotel","Novotel","Hyatt","Novotel","Novotel",
"Radisson","ITC","Hyatt","Novotel","Taj",
"Radisson","Marriott","Marriott","Leela","Taj",
"Novotel","Hyatt","Radisson","Taj","Radisson",
"Oberoi","Hyatt","Leela","Leela","Novotel",
"Novotel","Novotel","ITC","Radisson","Novotel",
"Oberoi","Novotel","Oberoi","Marriott","Leela",
"Hyatt","Taj","Marriott","Radisson","Novotel",
"Hyatt","Taj","Hyatt","Oberoi","Radisson",
"ITC","Marriott","Leela","Marriott","Hyatt",
"Taj","Radisson","Marriott","Radisson","Leela",
"Radisson","Leela","Radisson","Novotel","Marriott",
"Leela","Novotel","Radisson","ITC","Marriott",
"Novotel","Oberoi","Oberoi","Taj","Hyatt",
"Leela","ITC","ITC","Marriott","Marriott",
"Oberoi","ITC","Leela","Taj","Taj",
"Radisson","Taj","Hyatt","Oberoi","ITC",
"Marriott","Hyatt","Taj","ITC","Oberoi",
"Marriott","Oberoi","Radisson","Radisson","Novotel"
])

city = np.array([
"Delhi","Mumbai","Hyderabad","Hyderabad","Hyderabad",
"Bangalore","Chennai","Bangalore","Jaipur","Delhi",
"Bangalore","Kolkata","Chennai","Mumbai","Jaipur",
"Delhi","Bangalore","Delhi","Kolkata","Bangalore",
"Pune","Bangalore","Kolkata","Chennai","Hyderabad",
"Mumbai","Chennai","Pune","Jaipur","Chennai",
"Pune","Kolkata","Mumbai","Mumbai","Mumbai",
"Chennai","Delhi","Chennai","Bangalore","Chennai",
"Kolkata","Pune","Hyderabad","Jaipur","Hyderabad",
"Pune","Bangalore","Kolkata","Kolkata","Kolkata",
"Chennai","Hyderabad","Bangalore","Chennai","Pune",
"Mumbai","Kolkata","Jaipur","Pune","Delhi",
"Hyderabad","Bangalore","Pune","Bangalore","Delhi",
"Mumbai","Hyderabad","Bangalore","Jaipur","Bangalore",
"Bangalore","Chennai","Hyderabad","Chennai","Delhi",
"Jaipur","Bangalore","Bangalore","Delhi","Bangalore",
"Jaipur","Delhi","Bangalore","Delhi","Pune",
"Chennai","Delhi","Chennai","Mumbai","Jaipur",
"Chennai","Chennai","Pune","Mumbai","Jaipur",
"Delhi","Mumbai","Delhi","Bangalore","Kolkata",
"Kolkata","Bangalore","Delhi","Bangalore","Chennai",
"Jaipur","Chennai","Mumbai","Bangalore","Delhi",
"Delhi","Bangalore","Hyderabad","Jaipur","Kolkata",
"Chennai","Mumbai","Hyderabad","Pune","Kolkata",
"Pune","Delhi","Chennai","Kolkata","Jaipur",
"Chennai","Hyderabad","Hyderabad","Delhi","Hyderabad",
"Pune","Kolkata","Chennai","Chennai","Bangalore",
"Pune","Jaipur","Mumbai","Kolkata","Bangalore",
"Bangalore","Delhi","Kolkata","Bangalore","Mumbai",
"Delhi","Jaipur","Kolkata","Delhi","Pune",
"Chennai","Kolkata","Kolkata","Hyderabad","Delhi",
"Jaipur","Kolkata","Chennai","Chennai","Chennai",
"Jaipur","Delhi","Delhi","Bangalore","Pune",
"Hyderabad","Jaipur","Delhi","Chennai","Jaipur",
"Hyderabad","Bangalore","Pune","Chennai","Mumbai",
"Pune","Mumbai","Chennai","Mumbai","Mumbai",
"Kolkata","Bangalore","Pune","Kolkata","Hyderabad",
"Delhi","Pune","Mumbai","Kolkata","Chennai",
"Pune","Kolkata","Delhi","Jaipur","Kolkata",
"Bangalore","Bangalore","Pune","Hyderabad","Mumbai",
"Kolkata","Jaipur","Delhi","Delhi","Chennai",
"Jaipur","Delhi","Bangalore","Mumbai","Kolkata",
"Mumbai","Bangalore","Kolkata","Kolkata","Bangalore",
"Jaipur","Delhi","Pune","Chennai","Mumbai",
"Bangalore","Jaipur","Bangalore","Chennai","Jaipur",
"Jaipur","Chennai","Chennai","Hyderabad","Mumbai",
"Jaipur","Pune","Mumbai","Delhi","Mumbai",
"Delhi","Jaipur","Bangalore","Chennai","Bangalore",
"Jaipur","Kolkata","Hyderabad","Mumbai","Chennai",
"Delhi","Jaipur","Kolkata","Hyderabad","Pune",
"Hyderabad","Hyderabad","Kolkata","Kolkata","Chennai",
"Mumbai","Pune","Pune","Jaipur","Mumbai",
"Kolkata","Kolkata","Bangalore","Chennai","Mumbai",
"Kolkata","Pune","Jaipur","Kolkata","Mumbai",
"Delhi","Hyderabad","Delhi","Kolkata","Hyderabad",
"Bangalore","Bangalore","Bangalore","Hyderabad","Pune",
"Mumbai","Chennai","Mumbai","Chennai","Mumbai",
"Pune","Hyderabad","Pune","Kolkata","Jaipur",
"Bangalore","Hyderabad","Kolkata","Pune","Pune",
"Delhi","Jaipur","Kolkata","Delhi","Bangalore",
"Chennai","Delhi","Jaipur","Chennai","Pune",
"Chennai","Chennai","Pune","Delhi","Chennai",
"Jaipur","Bangalore","Delhi","Kolkata","Hyderabad",
"Hyderabad","Mumbai","Delhi","Jaipur","Kolkata",
"Delhi","Hyderabad","Kolkata","Jaipur","Kolkata",
"Chennai","Hyderabad","Delhi","Kolkata","Bangalore",
"Kolkata","Jaipur","Mumbai","Kolkata","Hyderabad",
"Bangalore","Hyderabad","Mumbai","Jaipur","Bangalore",
"Pune","Chennai","Chennai","Bangalore","Mumbai",
"Mumbai","Pune","Chennai","Mumbai","Bangalore",
"Pune","Mumbai","Jaipur","Kolkata","Mumbai",
"Bangalore","Delhi","Kolkata","Pune","Kolkata",
"Jaipur","Pune","Kolkata","Delhi","Hyderabad",
"Bangalore","Mumbai","Pune","Pune","Delhi",
"Chennai","Hyderabad","Jaipur","Chennai","Pune",
"Chennai","Chennai","Delhi","Pune","Bangalore",
"Jaipur","Pune","Kolkata","Mumbai","Kolkata",
"Kolkata","Jaipur","Pune","Jaipur","Hyderabad",
"Chennai","Bangalore","Delhi","Hyderabad","Jaipur",
"Jaipur","Delhi","Hyderabad","Jaipur","Hyderabad",
"Jaipur","Delhi","Delhi","Kolkata","Jaipur",
"Pune","Delhi","Chennai","Bangalore","Jaipur",
"Chennai","Bangalore","Pune","Pune","Pune",
"Jaipur","Delhi","Delhi","Pune","Hyderabad",
"Hyderabad","Jaipur","Bangalore","Pune","Jaipur",
"Chennai","Pune","Kolkata","Hyderabad","Chennai",
"Delhi","Bangalore","Hyderabad","Delhi","Pune",
"Mumbai","Pune","Hyderabad","Pune","Delhi",
"Pune","Mumbai","Bangalore","Jaipur","Jaipur",
"Jaipur","Bangalore","Hyderabad","Kolkata","Chennai",
"Chennai","Delhi","Bangalore","Jaipur","Chennai",
"Pune","Jaipur","Hyderabad","Bangalore","Chennai",
"Mumbai","Hyderabad","Delhi","Bangalore","Mumbai",
"Mumbai","Chennai","Bangalore","Hyderabad","Pune",
"Kolkata","Chennai","Jaipur","Hyderabad","Jaipur",
"Delhi","Chennai","Hyderabad","Delhi","Mumbai",
"Chennai","Bangalore","Kolkata","Hyderabad","Pune",
"Delhi","Pune","Hyderabad","Delhi","Bangalore",
"Mumbai","Delhi","Mumbai","Mumbai","Hyderabad",
"Jaipur","Hyderabad","Jaipur","Chennai","Mumbai"
])

room_type = np.array([
"Deluxe","Deluxe","Suite","Suite","Deluxe",
"Executive","Suite","Deluxe","Deluxe","Deluxe",
"Suite","Executive","Deluxe","Deluxe","Executive",
"Executive","Suite","Executive","Suite","Suite",
"Suite","Standard","Deluxe","Suite","Standard",
"Standard","Deluxe","Deluxe","Executive","Standard",
"Standard","Standard","Suite","Suite","Standard",
"Suite","Deluxe","Executive","Executive","Standard",
"Standard","Deluxe","Suite","Suite","Standard",
"Deluxe","Standard","Executive","Executive","Executive",
"Suite","Executive","Suite","Standard","Suite",
"Deluxe","Standard","Deluxe","Standard","Deluxe",
"Deluxe","Standard","Suite","Executive","Standard",
"Suite","Executive","Suite","Suite","Standard",
"Executive","Suite","Executive","Deluxe","Standard",
"Executive","Deluxe","Standard","Standard","Standard",
"Executive","Standard","Suite","Deluxe","Suite",
"Executive","Suite","Executive","Executive","Deluxe",
"Standard","Suite","Suite","Deluxe","Standard",
"Deluxe","Suite","Suite","Suite","Executive",
"Suite","Deluxe","Executive","Standard","Standard",
"Deluxe","Standard","Standard","Suite","Standard",
"Deluxe","Standard","Executive","Deluxe","Deluxe",
"Suite","Standard","Executive","Suite","Executive",
"Deluxe","Executive","Executive","Executive","Deluxe",
"Deluxe","Suite","Standard","Suite","Standard",
"Standard","Suite","Deluxe","Executive","Standard",
"Suite","Standard","Deluxe","Standard","Suite",
"Executive","Suite","Standard","Standard","Suite",
"Executive","Executive","Executive","Deluxe","Executive",
"Deluxe","Deluxe","Suite","Deluxe","Standard",
"Suite","Standard","Deluxe","Executive","Executive",
"Suite","Deluxe","Executive","Deluxe","Deluxe",
"Executive","Suite","Standard","Suite","Deluxe",
"Suite","Standard","Executive","Executive","Standard",
"Executive","Standard","Executive","Suite","Executive",
"Executive","Suite","Standard","Standard","Standard",
"Executive","Standard","Suite","Suite","Suite",
"Suite","Standard","Deluxe","Deluxe","Deluxe",
"Suite","Standard","Standard","Deluxe","Suite",
"Executive","Standard","Deluxe","Executive","Suite",
"Suite","Executive","Executive","Suite","Standard",
"Deluxe","Executive","Deluxe","Executive","Suite",
"Executive","Standard","Standard","Deluxe","Deluxe",
"Suite","Deluxe","Deluxe","Deluxe","Standard",
"Standard","Deluxe","Deluxe","Standard","Standard",
"Executive","Suite","Suite","Suite","Deluxe",
"Executive","Suite","Executive","Deluxe","Deluxe",
"Suite","Standard","Standard","Suite","Executive",
"Executive","Suite","Executive","Standard","Deluxe",
"Executive","Executive","Deluxe","Suite","Suite",
"Executive","Executive","Suite","Suite","Suite",
"Deluxe","Suite","Suite","Suite","Deluxe",
"Suite","Deluxe","Suite","Suite","Executive",
"Executive","Deluxe","Suite","Suite","Deluxe",
"Standard","Standard","Standard","Standard","Standard",
"Deluxe","Executive","Deluxe","Suite","Standard",
"Suite","Deluxe","Executive","Executive","Suite",
"Deluxe","Suite","Executive","Suite","Standard",
"Executive","Standard","Deluxe","Deluxe","Executive",
"Standard","Suite","Executive","Standard","Deluxe",
"Standard","Executive","Executive","Standard","Standard",
"Suite","Standard","Deluxe","Executive","Suite",
"Standard","Standard","Executive","Executive","Standard",
"Suite","Deluxe","Deluxe","Deluxe","Standard",
"Deluxe","Suite","Standard","Deluxe","Standard",
"Executive","Standard","Suite","Deluxe","Deluxe",
"Executive","Standard","Deluxe","Standard","Suite",
"Deluxe","Executive","Executive","Suite","Executive",
"Deluxe","Suite","Suite","Deluxe","Executive",
"Suite","Executive","Deluxe","Deluxe","Deluxe",
"Executive","Suite","Standard","Deluxe","Standard",
"Standard","Executive","Executive","Standard","Executive",
"Suite","Standard","Executive","Standard","Standard",
"Suite","Executive","Deluxe","Deluxe","Standard",
"Suite","Deluxe","Deluxe","Executive","Suite",
"Executive","Suite","Deluxe","Standard","Deluxe",
"Suite","Executive","Executive","Standard","Executive",
"Deluxe","Suite","Executive","Suite","Executive",
"Executive","Suite","Deluxe","Suite","Standard",
"Suite","Executive","Suite","Standard","Deluxe",
"Executive","Standard","Standard","Executive","Standard",
"Deluxe","Deluxe","Suite","Deluxe","Deluxe",
"Standard","Suite","Deluxe","Standard","Deluxe",
"Deluxe","Executive","Standard","Standard","Standard",
"Suite","Suite","Suite","Executive","Standard",
"Executive","Suite","Suite","Deluxe","Deluxe",
"Standard","Suite","Standard","Suite","Standard",
"Suite","Suite","Suite","Standard","Standard",
"Executive","Suite","Executive","Standard","Suite",
"Executive","Executive","Executive","Suite","Standard",
"Executive","Standard","Deluxe","Suite","Suite",
"Standard","Deluxe","Standard","Suite","Executive",
"Executive","Deluxe","Suite","Standard","Standard",
"Executive","Suite","Executive","Executive","Standard",
"Executive","Deluxe","Standard","Deluxe","Standard",
"Suite","Standard","Executive","Deluxe","Deluxe",
"Suite","Suite","Suite","Standard","Executive",
"Deluxe","Deluxe","Executive","Standard","Suite",
"Executive","Executive","Suite","Deluxe","Suite"
])

room_price = np.array([
4993,5438,8278,7885,5357,6522,8399,4962,5359,5394,
8074,6279,5408,5264,6818,6599,8195,6747,8456,8105,
7960,3752,5362,8323,3257,3775,5366,4916,6629,3249,
3445,3262,8364,7891,3221,8493,4922,6686,6503,3608,
3191,4903,8005,8385,3626,5489,3556,6686,6668,6358,
8415,6476,8032,3436,8145,5095,3569,5033,3283,5125,
5036,3321,8039,6694,3404,7839,6435,8104,7902,3641,
6425,8324,6769,5580,3732,6265,5497,3319,3141,3320,
6809,3485,8068,5034,8155,6323,8194,6766,6353,5367,
3309,7848,8478,5082,3321,5279,8408,8382,7924,6408,
7984,5233,6713,3130,3309,4959,3727,3548,7883,3718,
5568,3361,6348,4940,5457,8135,3153,6281,8089,6833,
5450,6456,6676,6336,5025,5290,8168,3704,8009,3325,
3747,7932,5481,6516,3659,8118,3642,5205,3577,8311,
6582,8272,3161,3612,8351,6536,6768,6532,4967,6284,
5032,5418,8477,5546,3491,7806,3152,5317,6886,6480,
8310,4948,6322,5409,5555,6821,8035,3691,8045,5221,
8281,3605,6357,6483,3402,6892,3562,6331,7955,6856,
6446,7987,3180,3427,3340,6277,3350,8330,8065,7926,
8065,3742,5480,5158,5378,8122,3252,3353,5116,8486,
6892,3222,5373,6399,8207,8331,6326,6842,8001,3393,
5081,6375,5548,6871,8083,6522,3697,3167,5466,4922,
8097,5575,5309,5434,3603,3426,5071,5073,3270,3360,
6450,8392,8442,8381,5075,6255,7893,6583,5564,5204,
8138,3434,3673,7923,6800,6781,8417,6268,3248,5059,
6632,6564,5138,7832,8405,6698,6831,8463,8137,7885,
5066,8064,8322,8187,5442,7855,5222,7928,8105,6877,
6812,5061,8399,8416,5158,3382,3361,3239,3161,3147,
5450,6297,5586,8332,3487,8496,5480,6773,6863,7976,
4993,8476,6847,7847,3586,6821,3591,5026,5481,6824,
3673,8085,6507,3342,5070,3584,6569,6710,3282,3701,
7920,3558,4922,6664,8388,3551,3355,6506,6738,3576,
8245,5144,5577,5373,3583,5093,8471,3653,5458,3514,
6452,3360,7976,4991,5256,6377,3318,5037,3126,8162,
5303,6268,6548,8422,6736,5185,7801,8242,5431,6552,
8297,6282,5316,4988,5145,6683,8496,3307,5180,3454,
3226,6402,6746,3376,6764,8123,3464,6469,3190,3115,
8035,6649,5316,5285,3741,8013,5389,5128,6854,7808,
6292,8331,5543,3173,5246,8463,6883,6777,3123,6438,
5276,7859,6359,7884,6380,6239,7890,5466,8237,3587,
8430,6591,8338,3671,5202,6416,3319,3629,6613,3175,
5126,5467,8103,5485,5532,3366,8389,5210,3354,5221,
5575,6845,3232,3239,3150,7848,8074,8449,6332,3127,
6389,7953,7930,5428,5215,3677,8102,3394,7867,3798,
7961,8498,7863,3478,3725,6698,8454,6636,3388,8043,
6393,6364,6519,8208,3509,6476,3600,4921,8269,8429,
3605,5018,3448,8365,6584,6711,5589,7865,3748,3525,
6314,8411,6801,6786,3188,6296,5358,3360,5348,3566,
8170,3636,6705,5015,5405,7902,8184,8120,3673,6225,
4973,5012,6493,3528,8119,6775,6701,8203,5144,8093
])

nights = np.array([
1,4,4,4,4,4,5,2,3,4,
2,5,5,5,3,5,1,4,5,1,
3,3,1,3,3,1,4,3,2,5,
3,2,2,5,2,2,4,4,1,3,
3,3,4,5,3,5,2,1,1,2,
3,2,5,5,2,3,2,3,3,3,
4,1,3,3,5,1,4,1,1,3,
1,5,1,2,1,4,3,5,5,4,
4,4,2,4,2,4,2,5,5,1,
1,3,3,4,2,5,2,5,3,1,
3,2,2,1,2,4,2,2,3,2,
1,1,4,2,3,3,2,3,1,3,
3,4,4,5,1,1,3,1,1,3,
5,3,4,4,3,2,2,4,5,5,
1,2,2,3,2,1,2,4,5,5,
4,4,5,1,2,4,3,4,2,2,
3,5,1,3,3,1,4,5,5,4,
2,3,4,5,1,4,2,4,5,4,
4,3,2,2,5,1,3,1,5,3,
4,2,4,5,4,1,3,3,5,2,
3,3,1,1,4,3,1,5,2,1,
1,2,1,1,3,1,3,2,3,4,
1,1,5,3,1,2,3,1,2,2,
5,4,2,5,1,4,2,1,5,5,
2,3,1,3,3,2,2,5,3,4,
4,5,3,3,3,5,4,4,4,3,
1,1,3,4,1,1,2,5,4,2,
1,1,3,2,5,2,2,2,5,1,
3,1,3,4,3,2,4,1,2,2,
5,4,3,1,4,1,1,5,2,2,
5,1,2,5,4,3,1,1,2,5,
3,3,3,2,4,3,4,5,2,2,
4,4,2,5,1,1,3,4,3,3,
1,4,5,4,1,1,2,3,3,5,
2,4,4,2,4,2,4,2,3,2,
3,2,5,3,1,3,2,1,5,5,
1,2,4,2,3,1,2,3,3,2,
2,3,1,1,3,4,4,5,2,2,
4,2,5,3,5,2,1,1,2,1,
4,3,3,1,1,3,2,3,5,5,
2,2,1,4,2,1,2,5,5,5,
3,1,1,5,2,3,3,5,1,5,
3,5,4,3,4,1,5,3,4,4,
5,2,4,1,3,2,4,4,1,3,
4,3,3,3,5,5,2,2,1,4,
5,5,2,4,5,4,4,4,1,4,
1,5,4,3,4,5,1,4,4,1,
4,5,3,2,2,4,3,5,4,5,
2,1,5,1,1,2,3,3,4,4,
5,5,5,5,4,5,4,5,2,5
])

discount = np.array([
12,10,15,10,10,5,8,10,15,6,
12,8,8,6,8,5,6,6,12,6,
6,15,12,8,12,5,15,15,12,12,
12,6,6,8,10,15,5,15,6,12,
6,10,5,15,15,10,6,8,5,5,
10,5,12,6,10,6,5,6,10,10,
6,12,10,15,8,10,15,5,15,5,
5,6,6,5,15,10,8,10,6,8,
6,8,8,12,15,15,12,15,5,6,
10,10,6,15,10,15,6,5,10,6,
12,8,5,15,12,8,12,6,12,12,
8,5,10,10,6,12,5,6,15,5,
5,12,6,10,10,6,6,10,10,5,
15,5,12,15,12,6,10,10,8,15,
5,6,15,5,8,5,10,15,8,8,
10,5,8,5,10,5,10,10,8,5,
15,10,6,5,10,6,12,15,10,6,
8,5,8,15,12,6,12,8,8,8,
10,8,5,15,6,15,12,5,6,12,
10,5,5,8,8,15,12,12,12,12,
6,10,8,12,5,12,12,15,15,10,
10,5,15,15,5,6,8,15,6,6,
8,6,12,15,15,15,6,12,6,15,
15,15,5,5,15,15,5,10,6,15,
8,6,6,6,5,5,8,6,6,5,
12,6,15,5,15,6,12,6,5,8,
10,10,6,12,5,10,12,12,8,6,
6,15,5,12,10,15,5,5,5,10,
5,15,8,10,12,10,6,6,12,12,
6,5,10,10,8,5,6,5,15,5,
8,12,8,12,12,6,15,12,10,15,
5,15,10,12,8,8,8,5,12,6,
6,8,10,8,10,5,6,15,5,10,
8,15,15,12,12,6,15,12,5,12,
8,12,6,5,8,15,12,5,6,10,
15,10,6,6,10,8,8,15,15,15,
5,5,5,8,8,15,10,10,8,12,
5,12,8,8,5,12,15,6,12,10,
12,5,15,5,6,15,10,6,8,8,
8,15,5,8,6,6,10,5,15,5,
12,8,12,15,5,6,6,10,5,6,
10,8,12,8,12,15,15,6,10,8,
15,8,6,10,12,10,5,15,15,8,
6,6,6,5,10,8,8,15,5,5,
6,10,5,10,8,8,8,12,6,5,
6,5,12,12,12,15,10,15,12,5,
12,10,15,10,12,6,15,15,6,12,
15,15,15,5,8,12,6,8,6,6,
12,5,15,6,5,8,10,8,6,15,
6,15,5,15,12,8,5,8,6,6
])

rating = np.array([
5,5,5,5,4,3,5,5,4,5,
5,4,4,5,4,3,5,5,2,4,
5,5,5,4,5,5,3,3,4,5,
4,5,5,3,3,4,5,5,3,3,
3,5,4,5,5,5,4,4,4,5,
5,4,4,5,4,4,4,4,4,5,
5,5,5,4,3,4,5,5,3,4,
5,5,5,5,4,5,3,5,4,4,
4,5,4,4,4,5,3,3,3,5,
3,4,4,4,4,4,3,4,4,3,
4,4,3,3,4,5,5,4,2,5,
5,3,4,2,4,3,5,4,5,4,
4,2,5,4,4,4,3,4,4,5,
5,4,5,2,4,5,4,3,5,5,
5,3,3,3,4,2,5,3,4,4,
3,5,5,4,4,4,5,5,5,4,
4,2,3,5,4,4,3,5,2,5,
4,5,5,5,4,4,5,3,4,5,
5,5,2,5,5,4,4,4,5,3,
3,5,4,4,4,2,3,3,5,5,
5,5,3,2,5,4,5,4,4,4,
4,4,3,5,5,5,5,5,5,5,
4,2,4,4,5,5,5,3,3,5,
5,4,3,3,3,5,4,4,5,4,
4,4,4,3,4,3,4,4,3,5,
5,5,5,4,3,5,4,5,5,4,
4,4,4,2,4,4,5,4,5,4,
4,4,4,5,4,4,5,3,5,4,
3,5,5,3,4,4,5,3,4,5,
2,5,4,4,4,4,4,5,5,5,
5,4,5,5,3,5,4,3,5,5,
5,2,5,4,5,3,5,3,4,5,
4,5,4,3,2,3,4,5,4,5,
5,5,5,4,5,4,5,2,3,3,
5,3,4,4,4,4,5,4,3,4,
3,5,3,5,3,4,4,4,4,4,
4,5,4,4,4,3,5,5,5,5,
3,5,3,5,5,4,5,4,4,4,
5,4,4,4,5,3,5,3,4,2,
4,5,4,3,4,2,4,4,3,5,
4,4,3,5,3,4,3,3,3,4,
3,4,4,3,5,3,4,5,5,2,
3,2,3,4,5,4,5,4,5,4,
3,3,3,3,5,5,3,5,4,3,
5,4,4,4,4,5,5,4,5,4,
4,4,4,5,4,3,5,3,5,5,
5,5,4,4,5,3,5,5,5,4,
4,3,3,4,2,5,3,5,3,4,
5,5,4,5,4,3,5,5,5,4,
4,3,2,5,4,4,5,4,5,3
])

status = np.array([
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Cancelled","Completed","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Completed","Cancelled","Cancelled",
"Completed","Cancelled","Cancelled","Cancelled","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Cancelled","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Cancelled","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Cancelled","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Cancelled","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Cancelled","Cancelled","Completed","Cancelled","Completed",
"Cancelled","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Completed","Cancelled","Cancelled",
"Completed","Completed","Cancelled","Completed","Completed",
"Cancelled","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Cancelled","Completed",
"Cancelled","Completed","Completed","Completed","Cancelled",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Completed",
"Cancelled","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Cancelled","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Completed",
"Completed","Completed","Cancelled","Completed","Cancelled",
"Cancelled","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Cancelled","Cancelled",
"Cancelled","Completed","Completed","Completed","Completed",
"Completed","Completed","Cancelled","Cancelled","Completed",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Cancelled","Cancelled","Completed","Cancelled",
"Completed","Completed","Completed","Completed","Cancelled",
"Completed","Cancelled","Completed","Completed","Completed",
"Completed","Completed","Completed","Completed","Cancelled"
])
# print("\n" + "=" * 60)
# print("BOOKING ANALYSIS")
# print("=" * 60)
# Total_booking = len(np.unique(booking_id))
# print("Total bookings:",Total_booking)
# Total_completed_bookings = np.sum(status=="Completed")
# print("Total Completed Bookings:",Total_completed_bookings)
# Total_cancelled_bookings = np.sum(status=="Cancelled")
# print("Total Cancelled Bookings:",Total_cancelled_bookings)
# Booking_Completion_Rate = (Total_completed_bookings/Total_booking)*100
# print("Booking Completion Rate:",np.round(Booking_Completion_Rate,2),"%")
# Cancellation_rate = (Total_cancelled_bookings/Total_booking)*100
# print("Cancellation Rate:",np.round(Cancellation_rate,2),"%")



# print("\n" + "=" * 60)
# print("REVENUE ANALYSIS")
# print("=" * 60)

# Gross_revenue = (room_price[status=="Completed"])
# total_Completed_gross_revenue=np.sum(Gross_revenue)
# # print("Completed Bookings Gross Revenue:",total_Completed_gross_revenue)
# Net_revenue = Gross_revenue*(1-discount[status=="Completed"]/100)
# # Total_net_revenue = np.sum(Net_revenue)
# # print("Total Completed Bookings Net Revenue:",Total_net_revenue)
# Revenue_loss = room_price[status=="Cancelled"] * (1 - discount[status=="Cancelled"]/100)
# # Total_revenue_loss = np.sum(Revenue_loss)
# # print("Total Revenue Loss Due To Cancelled Bookings:",np.round(Total_revenue_loss,2))

# Discount_Amount = room_price[status=="Completed"]*discount[status=="Completed"]/100
# # Total_discount_amount = np.sum(Discount_Amount)
# # print("Total Discount Amount:",np.round(Total_discount_amount,2))
# Avg_revenue_per_booking = np.mean(Net_revenue)
# # print(" Avg Revenue Per Booking:",np.round(Avg_revenue_per_booking,2))
# net_revenue = room_price * (1 - discount / 100)

# completed_mask = (status == "Completed")

# completed_booking_ids = booking_id[completed_mask]
# completed_revenue = net_revenue[completed_mask]

# # Highest revenue booking
# highest_index = np.argmax(completed_revenue)

# print("Highest Revenue Booking ID:", completed_booking_ids[highest_index])
# print("Highest Revenue:", np.round(completed_revenue[highest_index], 2))

# net_revenue = room_price * (1 - discount / 100)

# completed_mask = (status == "Completed")

# completed_booking_ids = booking_id[completed_mask]
# completed_revenue = net_revenue[completed_mask]

# # Lowest revenue booking
# lowest_index = np.argmin(completed_revenue)

# print("Lowest Revenue Booking ID:", completed_booking_ids[lowest_index])
# print("Lowest Revenue:", np.round(completed_revenue[lowest_index], 2))





# # print("\n" + "=" * 60)
# # print("HOTEL ANALYSIS")
# # print("=" * 60)

# # print("Total Bookings by Hotels:")
# # for h1 in np.unique(hotel):
# #     total_bookings_by_hotels = np.sum(hotel==h1)
# #     print(h1,total_bookings_by_hotels)

# # print("Completed Bookings by Hotels:")
# # for h2 in np.unique(hotel):
# #     mask2 = (hotel==h2) & (status=="Completed")
# #     Total_completed_bookings_by_hotels = np.sum(mask2)
# #     print(h2,Total_completed_bookings_by_hotels)

# # print("Cancelled Bookings by Hotels:")
# # for h3 in np.unique(hotel):
# #     mask3 = (hotel==h3) & (status=="Cancelled")
# #     Total_cancelled_bookings_by_hotels = np.sum(mask3)
# #     print(h3,Total_cancelled_bookings_by_hotels)

# print("Completed Booking Hotel's Revenue")
# revenue1 = room_price * (1 - discount/100)
# completed_revenue2 = np.sum(revenue1[status=="Completed"])
# # for h4 in np.unique(hotel):
# #     mask4 = (hotel==h4) & (status=="Completed")
# #     Completed_booking_revenue = np.sum(revenue1[mask4])
# #     print(h4,np.round(Completed_booking_revenue,2))

# # print("Completed Booking Hotel's Revenue Contribution")
# # for h5 in np.unique(hotel):
# #     mask5 = (hotel==h5) & (status=="Completed")
# #     completed_bookings_revenue = np.sum(revenue1[mask5])
# #     completed_bookings_revenue_contribution = (completed_bookings_revenue/completed_revenue2)*100
# #     print(h5,np.round(completed_bookings_revenue_contribution,2),"%")

# # print("Completed Booking Hotels's Rating")
# # for h6 in np.unique(hotel):
# #     mask6 = (hotel==h6) & (status=="Completed")
# #     Hotels_rating = np.mean(rating[mask6])
# #     print(h6,np.round(Hotels_rating,2))

# # print("Completed Bookings Hotel's Avg Room Price:")
# # for h7 in np.unique(hotel):
# #     mask7 = (hotel==h7) & (status=="Completed")
# #     Avg_room_price = np.mean(room_price[mask7])
# #     print(h7,np.round(Avg_room_price,2))
# print("Highest Revenue Hotel:")
# print("Highest Revenue Hotel")

# net_revenue = room_price * (1 - discount / 100)

# hotel_names = np.unique(hotel)
# hotel_revenues = []

# for h in hotel_names:
#     mask = (hotel == h) & (status == "Completed")
#     revenue = np.sum(net_revenue[mask])
#     hotel_revenues.append(revenue)

# hotel_revenues = np.array(hotel_revenues)

# highest_index = np.argmax(hotel_revenues)

# print("Hotel:", hotel_names[highest_index])
# print("Revenue:", np.round(hotel_revenues[highest_index], 2))


# print("Lowest Revenue Hotel:")
# print("Lowest Revenue Hotel")

# net_revenue = room_price * (1 - discount / 100)

# hotel_names = np.unique(hotel)
# hotel_revenues = []

# for h in hotel_names:
#     mask = (hotel == h) & (status == "Completed")
#     revenue = np.sum(net_revenue[mask])
#     hotel_revenues.append(revenue)

# hotel_revenues = np.array(hotel_revenues)

# lowest_index = np.argmin(hotel_revenues)

# print("Hotel:", hotel_names[lowest_index])
# print("Revenue:", np.round(hotel_revenues[lowest_index], 2))




# print("\n" + "=" * 60)
# print("CITY ANALYSIS")
# print("=" * 60)

# print("Total Bookings by City")
# for c1 in np.unique(city):
#     total_booking_by_cities = np.sum(city==c1)
#     print(c1,total_booking_by_cities)

# print("Completed Booking by City")
# for c2 in np.unique(city):
#     mask8 = (city==c2) & (status=="Completed")
#     total_completed_booking_by_cities = np.sum(mask8)
#     print(c2,total_completed_booking_by_cities)

# print("Total Cancelled bookings by city")
# for c3 in np.unique(city):
#     mask9 = (city==c3) & (status=="Cancelled")
#     total_cancelled_booking_by_cities = np.sum(mask9)
#     print(c3,total_cancelled_booking_by_cities)

# print(" Completed Bookings Revenue by cities")
# revenue3 = room_price*(1-discount/100)
# for c4 in np.unique(city):
#     mask10 = (city==c4) & (status=="Completed")
#     revenue_by_cities = np.sum(revenue3[mask10])
#     print(c4,np.round(revenue_by_cities,2))

# print("Completed Booking Revenue Contribution")
# completed_revenue3 = np.sum(revenue3[status=="Completed"])
# for c5 in np.unique(city):
#     mask11 = (city==c5) & (status=="Completed")
#     total_revenue_by_cities = np.sum(revenue3[mask11])
#     city_revenue_contribution = (total_revenue_by_cities/completed_revenue3)*100
#     print(c5,np.round(city_revenue_contribution,2),"%")


# print("Avg rating by Cities")
# for c6 in np.unique(city):
#     mask12 = (city==c6) & (status=="Completed")
#     avg_rating_by_cities = np.mean(rating[mask12])
#     print(c6,np.round(avg_rating_by_cities,2))

# print("Avg room price by city")
# for c7 in np.unique(city):
#     mask13 = (city==c7) & (status=="Completed")
#     avg_room_price_by_cities =np.mean(room_price[mask13])
#     print(c7,np.round(avg_room_price_by_cities,2))

# print("Highest Revenue City")
# net_revenue = room_price * (1 - discount / 100)

# city_names = np.unique(city)
# city_revenues = []

# for c in city_names:
#     mask = (city == c) & (status == "Completed")
#     revenue = np.sum(net_revenue[mask])
#     city_revenues.append(revenue)

# city_revenues = np.array(city_revenues)

# highest_index = np.argmax(city_revenues)

# print("City:", city_names[highest_index])
# print("Revenue:", np.round(city_revenues[highest_index], 2))





# print("\n" + "=" * 60)
# print("ROOM TYPE ANALYSIS")
# print("=" * 60)
# print("Total Bookings by Room Type")
# for r1 in np.unique(room_type):
#     total_bookings_by_room_type = np.sum(room_type==r1)
#     print(r1,total_bookings_by_room_type)

# print("Total Completed Bookings by Room type")
# for r2 in np.unique(room_type):
#     mask14 = (room_type==r2) & (status=="Completed")
#     completed_booking_by_roomtype = np.sum(mask14)
#     print(r2,completed_booking_by_roomtype)

# print("Total Cancelled Booking by Room type")
# for r3 in np.unique(room_type):
#     mask15 = (room_type==r3) & (status=="Cancelled")
#     Cancelled_booking_by_roomtype = np.sum(mask15)
#     print(r3,Cancelled_booking_by_roomtype)

# print("Completed booking room type revenue")
# revenue4 = room_price * (1 - discount/100)
# for r4 in np.unique(room_type):
#     mask16 = (room_type==r4) & (status=="Completed")
#     revenue_by_room_type = np.sum(revenue4[mask16])
#     print(r4,np.round(revenue_by_room_type,2))

# print("revenue contribution by room type")
# completed_revenue4 = np.sum(revenue4[status=="Completed"])
# for r5 in np.unique(room_type):
#     mask17 = (room_type==r5) & (status=="Completed")
#     room_type_revenue = np.sum(revenue4[mask17])
#     room_type_revenue_contribution = (room_type_revenue/completed_revenue4)*100
#     print(r5,np.round(room_type_revenue_contribution,2),"%")


# print("Avg room price by room type")
# for r6 in np.unique(room_type):
#     mask18 = (room_type==r6) & (status=="Completed")
#     avg_price_by_room_type = np.mean(room_price[mask18])
#     print(r6,np.round(avg_price_by_room_type,2))


# print("Avg rating by room type")
# for r7 in np.unique(room_type):
#     mask19 = (room_type==r7) & (status=="Completed")
#     avg_rating_by_room_type = np.mean(rating[mask19])
#     print(r7,np.round(avg_rating_by_room_type,2))


# print("Highest Revenue Room Type")

# net_revenue = room_price * (1 - discount / 100)

# room_types = np.unique(room_type)
# room_type_revenues = []

# for r in room_types:
#     mask = (room_type == r) & (status == "Completed")
#     revenue = np.sum(net_revenue[mask])
#     room_type_revenues.append(revenue)

# room_type_revenues = np.array(room_type_revenues)

# highest_index = np.argmax(room_type_revenues)

# print("Room Type:", room_types[highest_index])
# print("Revenue:", np.round(room_type_revenues[highest_index], 2))


# print("\n" + "=" * 60)
# print("CUSTOMER ANALYSIS")
# print("=" * 60)

# print("Highest Spending Customer")

# net_revenue = room_price * (1 - discount / 100)

# customer_ids = np.unique(customer_id)
# customer_spending = []

# for c1 in customer_ids:
#     mask = (customer_id == c1) & (status == "Completed")
#     spending = np.sum(net_revenue[mask])
#     customer_spending.append(spending)

# customer_spending = np.array(customer_spending)

# highest_index = np.argmax(customer_spending)

# print("Customer ID:", customer_ids[highest_index])
# print("Total Spending:", np.round(customer_spending[highest_index], 2))

# print("Lowest Spending Customer")

# net_revenue = room_price * (1 - discount / 100)

# customer_ids = np.unique(customer_id)
# customer_spending = []

# for c2 in customer_ids:
#     mask = (customer_id == c2) & (status == "Completed")
#     spending = np.sum(net_revenue[mask])
#     if spending > 0:      # Ignore customers with no completed bookings
#         customer_spending.append(spending)

# customer_spending = np.array(customer_spending)

# completed_customers = customer_ids[
#     np.array([np.sum(net_revenue[(customer_id == c) & (status == "Completed")]) > 0
#               for c in customer_ids])
# ]

# lowest_index = np.argmin(customer_spending)

# print("Customer ID:", completed_customers[lowest_index])
# print("Total Spending:", np.round(customer_spending[lowest_index], 2))

# print("Average Spending Customer:")

# net_revenue = room_price * (1 - discount / 100)

# customer_ids = np.unique(customer_id)
# customer_spending = []

# for c3 in customer_ids:
#     mask = (customer_id == c3) & (status == "Completed")
#     spending = np.sum(net_revenue[mask])

#     if spending > 0:
#         customer_spending.append(spending)

# average_spending = np.mean(customer_spending)

# print("Average Customer Spending:", np.round(average_spending, 2))



print("\n" + "=" * 60)
print("STAY ANALYSIS")
print("=" * 60)

# print("Completed Bookings Avg stays")
# avg_stay = np.mean(nights[status=="Completed"])
# print("Avg Stay:",np.round(avg_stay,2),"nights")

# print("Longest stay by completed bookings:")
# highest_stay = np.max(nights[status=="Completed"])
# print("Longest Stay:",highest_stay)

# print("Shortest stay by completed bookings:")
# shortest_stay = np.min(nights[status=="Completed"])
# print("Shotest Stays:",shortest_stay)


# print("Stays by Hotels")
# for h20 in np.unique(hotel):
#     mask30 = (hotel==h20) & (status=="Completed")
#     Total_stays_by_hotels = np.sum(nights[mask30])
#     print(h20,Total_stays_by_hotels,"nights")


# print("Stays by cities")
# for c20 in np.unique(city):
#     mask31 = (city==c20) & (status=="Completed")
#     total_stays_by_city = np.sum(nights[mask31])
#     print(c20,total_stays_by_city,"nights")



# print("\n" + "=" * 60)
# print("DISCOUNT ANALYSIS")
# print("=" * 60)

# print("Completed Booking Total Discount Amount")
# discount_amount = room_price[status=="Completed"]*discount[status=="Completed"]/100
# total_discount_amount = np.sum(discount_amount)
# print("Total Discount Amount:",np.round(total_discount_amount,2))

# print("Discount By Hotel")
# discount_amount2 = room_price * discount/100
# for h40 in np.unique(hotel):
#     mask40 = (hotel==h40) & (status=="Completed")
#     discount_amount_by_hotels=np.sum(discount_amount2[mask40])
#     print(h40,np.round(discount_amount_by_hotels,2))

# print("Discount Amount By City")
# for c40 in np.unique(city):
#     mask41 = (city==c40) & (status=="Completed")
#     discount_amount_by_cities = np.sum(discount_amount2[mask41])
#     print(c40,np.round(discount_amount_by_cities,2))


# print("Discount Amount By Room Type")
# for r40 in np.unique(room_type):
#     mask42 = (room_type==r40) & (status=="Completed")
#     discount_amount_by_roomtype = np.sum(discount_amount2[mask42])
#     print(r40,np.round(discount_amount_by_roomtype,2))








