"""
Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных
    аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов,
    причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
    Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.
"""


class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        if type(value) in (int, float) and value < 0:
            object.__setattr__(self, key, abs(value))
        else:
            object.__setattr__(self, key, value)


# INPUT DATA:

# TEST_1:
print("\nтест 1")
point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

# TEST_2:
print("\nтест 2")
point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

# TEST_3:
print("\nтест 3")
digits = [(41, -46.982, -50.885), (-31.33, 37, -15), (-64.524, -19, 72), (-95.638, -73.587, 60),
          (36.306, -62.569, 24.661), (-80.629, -58.157, 33.249), (-77, 69, -45), (-12.582, 70.973, 30), (6, -88, 93),
          (25, -13, -85.357), (19, -12.808, -10), (-77.629, 44.438, -24.381), (-99, -59.473, 79), (-74, 34, -45.838),
          (67.211, 44.514, -15.8), (-67.386, -35, -98), (64.87, 31, -26), (12.768, 5, 29), (-13, -62, -14),
          (-25.556, -21.151, 12.877), (-31, -31, 56), (3, -79, -98.841), (14, 77.955, 79), (45, -97, 86),
          (20.738, 8.901, 88), (-88.291, -93.351, 10.693), (-93, -73.704, -2), (-68.639, -16, -92.5), (-15, 78.87, 26),
          (-11.582, 22, -78), (-24, 68, -1.309), (-76.477, 0, -34.691), (30, -45.51, 62.84), (77, 5, -56.421),
          (-30.478, -93, 98), (3.342, -34.798, 40), (-53.95, 77.961, 55.11), (-18.11, 99.845, -31), (6, 10, -61.407),
          (-45.454, -6.931, 43), (66, -28, -80), (-22, 38, 90), (-32.58, 25.981, -23.347), (49.949, -85, 76.6),
          (-28, 44.367, -27), (33, 95.999, -14.2), (39.526, -53.18, -68.35), (-4, 93.902, -51.103),
          (-69.535, -1, 15.489), (0, 21.938, -51.44), (-83.872, 49.79, 51), (48, 83.347, 57.603),
          (50.694, -49, -41.915), (-99, 55, -79), (56, -31, 41.341), (47.974, 8.197, -54.329), (-30.535, -15, -7.709),
          (40.297, -68.63, 17), (8, 91.741, -93), (25, -26.69, 5.786), (10, -73.356, -99.778), (-47, -93.133, -29),
          (3, 84, -70.61), (-84, 82.758, 7), (-70, -12, 21.549), (-9.699, -20, -32.531), (41, 62.337, 29.986),
          (-61.581, -95.783, -25.223), (-93.798, 33, 89.562), (-4, -54, -35.218), (77, -16, -43),
          (-37.318, -95.341, 35.938), (3, -68, -30.802), (33.251, -73.924, -19.747), (4.9, -83, 75),
          (91.819, -83.1, 66), (-42.17, 45, -82), (49, 15.708, 71.726), (21.282, 84, -86), (-79.494, -2, -25.527),
          (-30.44, 65, 51), (-23.622, -30, -37), (34, 1.616, 57), (58, -2.4, 10), (85.188, -96, -47),
          (-69, 26, -51.598), (-92, -68, 100), (61, 19.734, 42), (-93.316, 16.108, 66.469), (53.174, 30.254, 29),
          (-16, 66.949, -52), (17.131, -30.501, 45.32), (88.56, 95, 59.82), (-5, 8.784, 89), (-8, 44, -50),
          (-21.625, 33, -14.697), (51, -11.634, 50.436), (38, -53, -25.622), (-12, -54.732, -79.28),
          (62, -8.249, -45.204)]

for x, y, z in digits:
    obj = NonNegativeObject(x=x, y=y, z=z)
    print(obj.x, obj.y, obj.z)

# TEST_4:
print("\nтест 4")
colors = [('DarkOrange', '#b10916', '49,151,220'), ('SlateBlue', '#ae7772', '120,71,214'),
          ('HoneyDew', '#2fb773', '196,79,251'), ('BlueViolet', '#b9978b', '142,137,36'),
          ('Indigo', '#28ba85', '231,69,176'), ('Black', '#4bd02f', '207,140,98'), ('Brown', '#0d49c6', '197,191,229'),
          ('Peru', '#b24644', '112,81,143'), ('MidnightBlue', '#177797', '51,149,39'),
          ('FloralWhite', '#886ea4', '214,46,34'), ('DarkBlue', '#350a99', '170,233,66'),
          ('SlateGray', '#f3a95f', '18,149,1'), ('PaleVioletRed', '#7a1996', '124,125,102'),
          ('LawnGreen', '#9358f6', '137,245,109'), ('Coral', '#2f249e', '83,134,157'),
          ('DimGray', '#944839', '124,125,62'), ('PeachPuff', '#f1e2e7', '1,111,86'),
          ('LightCoral', '#eeabc6', '29,9,139'), ('Maroon', '#a9f3c8', '81,154,188'),
          ('Tomato', '#e4be00', '172,10,168'), ('SlateBlue', '#a05d9a', '211,169,128'),
          ('DarkBlue', '#7511b7', '216,218,152'), ('Brown', '#6546c7', '59,179,70'),
          ('DeepPink', '#625fef', '57,223,157'), ('DarkGoldenRod', '#e53677', '199,196,104'),
          ('CornflowerBlue', '#4d2efd', '40,89,225'), ('WhiteSmoke', '#1172ca', '206,57,200'),
          ('HotPink', '#52bed4', '248,150,40'), ('LightCoral', '#c74821', '121,14,52'),
          ('MidnightBlue', '#30f9a1', '70,110,120'), ('DarkOrchid', '#ee1c70', '166,9,182'),
          ('LightGray', '#420bf1', '172,169,187'), ('Cyan', '#a94c78', '151,179,203'),
          ('DodgerBlue', '#379e70', '11,104,108'), ('DimGray', '#9fffd7', '251,198,219'),
          ('Thistle', '#4417b0', '16,174,138'), ('DarkTurquoise', '#b3cc88', '130,104,127'),
          ('PaleVioletRed', '#6077ab', '155,146,33'), ('MediumAquaMarine', '#f4ebf1', '218,246,43'),
          ('MistyRose', '#597c82', '91,27,56'), ('Chartreuse', '#846e03', '244,53,59'),
          ('IndianRed', '#ca78db', '122,249,206'), ('Gold', '#a37606', '183,41,74'), ('Coral', '#dfe4ab', '222,212,51'),
          ('Violet', '#3351e0', '199,243,33'), ('DarkGray', '#121e75', '82,92,254'),
          ('Orchid', '#8ec999', '122,144,112'), ('MintCream', '#ddd31a', '17,33,64'),
          ('AliceBlue', '#62ae10', '89,95,177'), ('MediumVioletRed', '#135161', '109,229,26'),
          ('LightBlue', '#2a8365', '181,80,247'), ('DarkBlue', '#1eaf30', '254,226,120'),
          ('Aquamarine', '#94c6ae', '169,160,80'), ('LightGreen', '#cf2cb1', '223,222,19'),
          ('CadetBlue', '#27b6ac', '42,192,60'), ('LavenderBlush', '#4e9e09', '135,79,139'),
          ('SteelBlue', '#f01ec2', '34,40,31'), ('Khaki', '#1f77b9', '184,128,255'),
          ('CadetBlue', '#475bd0', '241,96,192'), ('DarkGoldenRod', '#4e8dca', '208,152,181'),
          ('Purple', '#d50f13', '11,111,161'), ('Lime', '#9e634d', '108,254,243'), ('DarkBlue', '#654a0d', '58,224,70'),
          ('LemonChiffon', '#58773c', '14,18,184'), ('LimeGreen', '#36fbfe', '76,230,77'),
          ('Moccasin', '#a96e79', '126,53,178'), ('Crimson', '#d16c92', '252,115,3'),
          ('Salmon', '#f741b9', '169,228,57'), ('Magenta', '#c1a2e4', '182,101,34'),
          ('Wheat', '#4b6d47', '124,243,188'), ('Red', '#37d7dd', '17,106,108'),
          ('AntiqueWhite', '#181f23', '202,193,129'), ('MediumAquaMarine', '#0880fa', '233,44,253'),
          ('DeepSkyBlue', '#4585c4', '74,249,202'), ('Pink', '#05bed8', '241,71,40'),
          ('DarkTurquoise', '#14d1c0', '89,113,245'), ('Cornsilk', '#a340dd', '201,74,56'),
          ('GoldenRod', '#2b9a59', '23,42,242'), ('Gray', '#b41a00', '44,97,249'),
          ('PeachPuff', '#6aacbb', '159,231,251'), ('Bisque', '#2b7dcf', '196,234,78'),
          ('SlateGray', '#38a08a', '142,219,169'), ('Coral', '#22449f', '31,206,61'),
          ('Fuchsia', '#158c36', '200,188,107'), ('PaleTurquoise', '#054a9c', '178,1,189'),
          ('Aquamarine', '#6469fe', '168,53,161'), ('PaleTurquoise', '#2c3baf', '138,128,153'),
          ('OldLace', '#000489', '139,164,57'), ('DarkTurquoise', '#288895', '66,40,107'),
          ('CadetBlue', '#485065', '252,7,163'), ('Tomato', '#8f8c65', '91,220,28'),
          ('Thistle', '#1b9acf', '77,121,43'), ('Purple', '#c758fb', '13,175,93'),
          ('LightSteelBlue', '#6be86f', '217,67,4'), ('DarkOliveGreen', '#7c2cb0', '185,62,159'),
          ('DarkSalmon', '#1b978c', '24,210,58'), ('BurlyWood', '#a724b5', '166,194,47'),
          ('MediumVioletRed', '#3de76b', '249,124,4'), ('LemonChiffon', '#b0fa95', '134,79,200'),
          ('LightSeaGreen', '#c2aac1', '133,214,213')]

for color, hex_color, rgb_color in colors:
    obj = NonNegativeObject(rgb_color=rgb_color, color=color, hex_color=hex_color)
    print(obj.color, obj.hex_color, obj.rgb_color)

# TEST_5:
print("\nтест 5")
persons = [('Laura', 'Sawyer', 'elizabethmcneil@example.org', 35), ('Jason', 'Coleman', 'lisareid@example.org', 14),
           ('Joseph', 'Estrada', 'brownwendy@example.net', -13), ('Brian', 'Wood', 'jordancarpenter@example.net', -27),
           ('Michael', 'Higgins', 'masonjennifer@example.com', 12),
           ('Richard', 'Schneider', 'sharonallen@example.com', -30), ('Matthew', 'Jones', 'iterrell@example.net', 15),
           ('Andrew', 'Howard', 'dannymontgomery@example.org', -29), ('Kenneth', 'Myers', 'ftodd@example.net', -20),
           ('Rita', 'Mcdonald', 'christopher25@example.com', 4), ('Cristian', 'Bryant', 'maryjohnson@example.net', 35),
           ('Ashley', 'Dickson', 'johnsoncarly@example.org', 0), ('Mario', 'White', 'anthonynicholas@example.org', -30),
           ('Gregory', 'Curtis', 'lucas53@example.com', 23), ('Daniel', 'Mitchell', 'elizabeth13@example.org', -18),
           ('Michael', 'Chase', 'eric03@example.com', -26), ('Kimberly', 'Burch', 'kcharles@example.com', 10),
           ('Kristen', 'Rollins', 'oliviadunn@example.net', -9),
           ('Sharon', 'Gentry', 'anthonystephens@example.org', -9), ('Joseph', 'Mcmahon', 'lmayer@example.org', 15),
           ('Steven', 'Rhodes', 'christopher82@example.net', -8), ('Joshua', 'Gray', 'lmorales@example.net', 25),
           ('Stephanie', 'Green', 'andersontammie@example.com', -16), ('April', 'Cowan', 'nicolewade@example.net', -12),
           ('Erica', 'Gilmore', 'hubbardsusan@example.org', -31),
           ('Elizabeth', 'Holmes', 'codyrussell@example.com', -38), ('Joseph', 'Campbell', 'kaylee62@example.com', 14),
           ('Jeremy', 'Moore', 'dawsonsean@example.com', -15), ('Monique', 'Crosby', 'michaeljones@example.net', -26),
           ('James', 'Castaneda', 'jonesbarbara@example.org', 28), ('Ryan', 'Glass', 'stephencollins@example.com', -36),
           ('Ryan', 'Holloway', 'jason03@example.com', -10), ('Danielle', 'Allison', 'scottgarcia@example.com', 21),
           ('David', 'Rodriguez', 'edwin89@example.org', 3), ('Fernando', 'Hendrix', 'umccann@example.com', -32),
           ('Elizabeth', 'Herrera', 'christopherhawkins@example.org', -8),
           ('Pamela', 'Davis', 'mariacross@example.com', -38), ('Cynthia', 'Johnson', 'grahamjeremy@example.com', -10),
           ('Christine', 'Stanley', 'kaylafernandez@example.net', -38),
           ('Robert', 'Shelton', 'russelljennifer@example.com', 34),
           ('Brett', 'Wells', 'castrotravis@example.net', -12), ('Nichole', 'Duran', 'wrightanne@example.com', -10),
           ('Ruben', 'Stone', 'angelica95@example.org', -12), ('Daryl', 'Miller', 'hernandezkimberly@example.com', 13),
           ('Megan', 'Wilson', 'garciakathleen@example.net', 31),
           ('Alisha', 'Johnson', 'danielsanchez@example.net', -2), ('Jeffrey', 'Pierce', 'isnyder@example.com', -21),
           ('James', 'Shaffer', 'hailey46@example.net', -4), ('David', 'James', 'janetlee@example.net', 3),
           ('William', 'Kennedy', 'sarahhogan@example.com', 18), ('Kristin', 'Williams', 'marialopez@example.net', -17),
           ('Mark', 'Stevens', 'greenandrea@example.org', 13), ('Earl', 'Thompson', 'dvillanueva@example.org', -34),
           ('Steven', 'Clark', 'scannon@example.com', -22), ('Dennis', 'Schultz', 'anthonythompson@example.org', 1),
           ('Frank', 'Stewart', 'gonzalezjonathan@example.com', 8), ('Matthew', 'Shaffer', 'kevin84@example.org', 33),
           ('Dawn', 'Bradshaw', 'jamesjohnson@example.com', 7), ('Victoria', 'Thomas', 'oyang@example.com', 6),
           ('Brandy', 'Whitehead', 'allenkelly@example.com', -10), ('April', 'Kelly', 'james39@example.com', 19),
           ('Sandra', 'White', 'nicholas66@example.net', 15), ('John', 'Richardson', 'roythomas@example.net', -4),
           ('Bryan', 'Walker', 'crossfernando@example.com', 26), ('John', 'Martin', 'linda33@example.com', 25),
           ('Bryan', 'Ford', 'monica03@example.com', 25), ('Kimberly', 'Nguyen', 'jeffrey30@example.org', -3),
           ('Robin', 'Clark', 'ybishop@example.com', -12), ('Eric', 'Hoffman', 'tammyhanson@example.com', -21),
           ('Sarah', 'Lopez', 'qortiz@example.net', -11), ('Eileen', 'Garcia', 'leroy26@example.org', -11),
           ('Danny', 'Harrison', 'danavelez@example.com', 9), ('Andrew', 'Martin', 'frussell@example.net', 7),
           ('Jennifer', 'Aguilar', 'xallen@example.org', -39),
           ('Michelle', 'Johnson', 'andrewilliams@example.org', -26),
           ('Dennis', 'Mercado', 'sheilaharrison@example.net', -8),
           ('Rebecca', 'Lara', 'matthewnavarro@example.org', 30),
           ('Sarah', 'Joseph', 'frederickzachary@example.net', -18),
           ('John', 'Butler', 'pachecochristina@example.org', 25), ('Laura', 'Hunter', 'devincruz@example.com', 6),
           ('Kenneth', 'Carr', 'collierscott@example.net', -25), ('Amy', 'Estrada', 'tina18@example.com', 16),
           ('Cameron', 'Jackson', 'laurasnyder@example.com', 13),
           ('Debbie', 'Sullivan', 'taracochran@example.com', -16), ('Kelsey', 'Norris', 'duane84@example.com', 28),
           ('Timothy', 'Marks', 'peterlawson@example.net', -37), ('Monique', 'Carroll', 'jeremy81@example.org', 11),
           ('Matthew', 'Mathews', 'stephen36@example.org', 30), ('Jackie', 'Kim', 'justincantrell@example.com', -24),
           ('Kathy', 'Jones', 'nyates@example.com', -5), ('Amber', 'Hunter', 'leeelizabeth@example.com', -8),
           ('Lauren', 'Peters', 'willieprice@example.org', -23), ('Donald', 'Anderson', 'khowell@example.net', -20),
           ('Jessica', 'Moreno', 'mfrank@example.net', -23), ('Hailey', 'Golden', 'gjohnson@example.net', 33),
           ('Matthew', 'Williams', 'murraynancy@example.net', 26),
           ('Gina', 'Montoya', 'collinsricardo@example.net', 26), ('Michael', 'Carroll', 'jwarren@example.com', -34),
           ('Jacob', 'Lopez', 'juliegarcia@example.com', 40),
           ('Vanessa', 'Blackwell', 'gordonadrienne@example.com', -38)]

for name, surname, email, age in persons:
    person = NonNegativeObject(name=name, age=age, email=email, surname=surname)
    print(person.name, person.surname, person.email, person.age)
