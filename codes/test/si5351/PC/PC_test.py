from clock_generators.si535x.si5351 import Si5351
from utilities.adapters import peripherals

registers_values = [(0, 0), (1, 0), (2, 0), (3, 0), (9, 0), (15, 0), (16, 79), (17, 79), (18, 79), (19, 79), (20, 79),
                    (21, 79), (22, 79), (23, 79), (24, 0), (25, 0), (26, 0), (27, 1), (28, 0), (29, 16), (30, 0),
                    (31, 0), (32, 0), (33, 0), (34, 0), (35, 1), (36, 0), (37, 16), (38, 0), (39, 0), (40, 0), (41, 0),
                    (42, 0), (43, 1), (44, 0), (45, 16), (46, 0), (47, 0), (48, 0), (49, 0), (50, 0), (51, 1), (52, 0),
                    (53, 16), (54, 0), (55, 0), (56, 0), (57, 0), (58, 0), (59, 1), (60, 0), (61, 16), (62, 0), (63, 0),
                    (64, 0), (65, 0), (66, 0), (67, 1), (68, 0), (69, 16), (70, 0), (71, 0), (72, 0), (73, 0), (74, 0),
                    (75, 1), (76, 0), (77, 16), (78, 0), (79, 0), (80, 0), (81, 0), (82, 0), (83, 1), (84, 0), (85, 16),
                    (86, 0), (87, 0), (88, 0), (89, 0), (90, 36), (91, 36), (92, 0), (149, 0), (150, 0), (151, 0),
                    (152, 0), (153, 0), (154, 0), (155, 0), (156, 0), (157, 0), (158, 0), (159, 0), (160, 0), (161, 0),
                    (162, 0), (163, 0), (164, 0), (165, 0), (166, 0), (167, 0), (168, 0), (169, 0), (170, 0),
                    (177, 160), (183, 210), (187, 208)]

with_hardware_device = False

if with_hardware_device:
    _i2c = peripherals.I2C.get_Ftdi_i2c()
else:
    _i2c = None  # using None for testing without actual hardware device.

si = Si5351(_i2c)
si.print_registers_values()

xtal = si.xtal
clkin = si.clkin
vcxo = si.vcxo
ss = si.spread_spectrum
clk = si.clocks[0]
ms = si.multisynths[0]
pll = si.plls[0]

# clkin._set_divider()
# vcxo.set_pull_range(60)

# si.init()
# si.enable(False)
# clk.enable(True)
# clk.set_frequency(50.4e6)
# clk.set_frequency(90e6)
# clk.set_frequency(225e6)
# clk.set_frequency(5.2e6)
print(clk.freq)
# print(clk.status)
print(si.clocks[7].status)
