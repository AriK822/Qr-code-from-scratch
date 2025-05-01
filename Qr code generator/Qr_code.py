def subtract(a, b):
    return a ^ b


def multiply(a, b):
    a_to_int = {0 : 1,
                1 : 2,
                2 : 4,
                3 : 8,
                4 : 16,
                5 : 32,
                6 : 64,
                7 : 128,
                8 : 29,
                9 : 58,
                10 : 116,
                11 : 232,
                12 : 205,
                13 : 135,
                14 : 19,
                15 : 38,
                16 : 76,
                17 : 152,
                18 : 45,
                19 : 90,
                20 : 180,
                21 : 117,
                22 : 234,
                23 : 201,
                24 : 143,
                25 : 3,
                26 : 6,
                27 : 12,
                28 : 24,
                29 : 48,
                30 : 96,
                31 : 192,
                32 : 157,
                33 : 39,
                34 : 78,
                35 : 156,
                36 : 37,
                37 : 74,
                38 : 148,
                39 : 53,
                40 : 106,
                41 : 212,
                42 : 181,
                43 : 119,
                44 : 238,
                45 : 193,
                46 : 159,
                47 : 35,
                48 : 70,
                49 : 140,
                50 : 5,
                51 : 10,
                52 : 20,
                53 : 40,
                54 : 80,
                55 : 160,
                56 : 93,
                57 : 186,
                58 : 105,
                59 : 210,
                60 : 185,
                61 : 111,
                62 : 222,
                63 : 161,
                64 : 95,
                65 : 190,
                66 : 97,
                67 : 194,
                68 : 153,
                69 : 47,
                70 : 94,
                71 : 188,
                72 : 101,
                73 : 202,
                74 : 137,
                75 : 15,
                76 : 30,
                77 : 60,
                78 : 120,
                79 : 240,
                80 : 253,
                81 : 231,
                82 : 211,
                83 : 187,
                84 : 107,
                85 : 214,
                86 : 177,
                87 : 127,
                88 : 254,
                89 : 225,
                90 : 223,
                91 : 163,
                92 : 91,
                93 : 182,
                94 : 113,
                95 : 226,
                96 : 217,
                97 : 175,
                98 : 67,
                99 : 134,
                100 : 17,
                101 : 34,
                102 : 68,
                103 : 136,
                104 : 13,
                105 : 26,
                106 : 52,
                107 : 104,
                108 : 208,
                109 : 189,
                110 : 103,
                111 : 206,
                112 : 129,
                113 : 31,
                114 : 62,
                115 : 124,
                116 : 248,
                117 : 237,
                118 : 199,
                119 : 147,
                120 : 59,
                121 : 118,
                122 : 236,
                123 : 197,
                124 : 151,
                125 : 51,
                126 : 102,
                127 : 204,
                128 : 133,
                129 : 23,
                130 : 46,
                131 : 92,
                132 : 184,
                133 : 109,
                134 : 218,
                135 : 169,
                136 : 79,
                137 : 158,
                138 : 33,
                139 : 66,
                140 : 132,
                141 : 21,
                142 : 42,
                143 : 84,
                144 : 168,
                145 : 77,
                146 : 154,
                147 : 41,
                148 : 82,
                149 : 164,
                150 : 85,
                151 : 170,
                152 : 73,
                153 : 146,
                154 : 57,
                155 : 114,
                156 : 228,
                157 : 213,
                158 : 183,
                159 : 115,
                160 : 230,
                161 : 209,
                162 : 191,
                163 : 99,
                164 : 198,
                165 : 145,
                166 : 63,
                167 : 126,
                168 : 252,
                169 : 229,
                170 : 215,
                171 : 179,
                172 : 123,
                173 : 246,
                174 : 241,
                175 : 255,
                176 : 227,
                177 : 219,
                178 : 171,
                179 : 75,
                180 : 150,
                181 : 49,
                182 : 98,
                183 : 196,
                184 : 149,
                185 : 55,
                186 : 110,
                187 : 220,
                188 : 165,
                189 : 87,
                190 : 174,
                191 : 65,
                192 : 130,
                193 : 25,
                194 : 50,
                195 : 100,
                196 : 200,
                197 : 141,
                198 : 7,
                199 : 14,
                200 : 28,
                201 : 56,
                202 : 112,
                203 : 224,
                204 : 221,
                205 : 167,
                206 : 83,
                207 : 166,
                208 : 81,
                209 : 162,
                210 : 89,
                211 : 178,
                212 : 121,
                213 : 242,
                214 : 249,
                215 : 239,
                216 : 195,
                217 : 155,
                218 : 43,
                219 : 86,
                220 : 172,
                221 : 69,
                222 : 138,
                223 : 9,
                224 : 18,
                225 : 36,
                226 : 72,
                227 : 144,
                228 : 61,
                229 : 122,
                230 : 244,
                231 : 245,
                232 : 247,
                233 : 243,
                234 : 251,
                235 : 235,
                236 : 203,
                237 : 139,
                238 : 11,
                239 : 22,
                240 : 44,
                241 : 88,
                242 : 176,
                243 : 125,
                244 : 250,
                245 : 233,
                246 : 207,
                247 : 131,
                248 : 27,
                249 : 54,
                250 : 108,
                251 : 216,
                252 : 173,
                253 : 71,
                254 : 142,
                255 : 1,
    }
    int_to_a = {0 : 0,
                1 : 0,
                2 : 1,
                3 : 25,
                4 : 2,
                5 : 50,
                6 : 26,
                7 : 198,
                8 : 3,
                9 : 223,
                10 : 51,
                11 : 238,
                12 : 27,
                13 : 104,
                14 : 199,
                15 : 75,
                16 : 4,
                17 : 100,
                18 : 224,
                19 : 14,
                20 : 52,
                21 : 141,
                22 : 239,
                23 : 129,
                24 : 28,
                25 : 193,
                26 : 105,
                27 : 248,
                28 : 200,
                29 : 8,
                30 : 76,
                31 : 113,
                32 : 5,
                33 : 138,
                34 : 101,
                35 : 47,
                36 : 225,
                37 : 36,
                38 : 15,
                39 : 33,
                40 : 53,
                41 : 147,
                42 : 142,
                43 : 218,
                44 : 240,
                45 : 18,
                46 : 130,
                47 : 69,
                48 : 29,
                49 : 181,
                50 : 194,
                51 : 125,
                52 : 106,
                53 : 39,
                54 : 249,
                55 : 185,
                56 : 201,
                57 : 154,
                58 : 9,
                59 : 120,
                60 : 77,
                61 : 228,
                62 : 114,
                63 : 166,
                64 : 6,
                65 : 191,
                66 : 139,
                67 : 98,
                68 : 102,
                69 : 221,
                70 : 48,
                71 : 253,
                72 : 226,
                73 : 152,
                74 : 37,
                75 : 179,
                76 : 16,
                77 : 145,
                78 : 34,
                79 : 136,
                80 : 54,
                81 : 208,
                82 : 148,
                83 : 206,
                84 : 143,
                85 : 150,
                86 : 219,
                87 : 189,
                88 : 241,
                89 : 210,
                90 : 19,
                91 : 92,
                92 : 131,
                93 : 56,
                94 : 70,
                95 : 64,
                96 : 30,
                97 : 66,
                98 : 182,
                99 : 163,
                100 : 195,
                101 : 72,
                102 : 126,
                103 : 110,
                104 : 107,
                105 : 58,
                106 : 40,
                107 : 84,
                108 : 250,
                109 : 133,
                110 : 186,
                111 : 61,
                112 : 202,
                113 : 94,
                114 : 155,
                115 : 159,
                116 : 10,
                117 : 21,
                118 : 121,
                119 : 43,
                120 : 78,
                121 : 212,
                122 : 229,
                123 : 172,
                124 : 115,
                125 : 243,
                126 : 167,
                127 : 87,
                128 : 7,
                129 : 112,
                130 : 192,
                131 : 247,
                132 : 140,
                133 : 128,
                134 : 99,
                135 : 13,
                136 : 103,
                137 : 74,
                138 : 222,
                139 : 237,
                140 : 49,
                141 : 197,
                142 : 254,
                143 : 24,
                144 : 227,
                145 : 165,
                146 : 153,
                147 : 119,
                148 : 38,
                149 : 184,
                150 : 180,
                151 : 124,
                152 : 17,
                153 : 68,
                154 : 146,
                155 : 217,
                156 : 35,
                157 : 32,
                158 : 137,
                159 : 46,
                160 : 55,
                161 : 63,
                162 : 209,
                163 : 91,
                164 : 149,
                165 : 188,
                166 : 207,
                167 : 205,
                168 : 144,
                169 : 135,
                170 : 151,
                171 : 178,
                172 : 220,
                173 : 252,
                174 : 190,
                175 : 97,
                176 : 242,
                177 : 86,
                178 : 211,
                179 : 171,
                180 : 20,
                181 : 42,
                182 : 93,
                183 : 158,
                184 : 132,
                185 : 60,
                186 : 57,
                187 : 83,
                188 : 71,
                189 : 109,
                190 : 65,
                191 : 162,
                192 : 31,
                193 : 45,
                194 : 67,
                195 : 216,
                196 : 183,
                197 : 123,
                198 : 164,
                199 : 118,
                200 : 196,
                201 : 23,
                202 : 73,
                203 : 236,
                204 : 127,
                205 : 12,
                206 : 111,
                207 : 246,
                208 : 108,
                209 : 161,
                210 : 59,
                211 : 82,
                212 : 41,
                213 : 157,
                214 : 85,
                215 : 170,
                216 : 251,
                217 : 96,
                218 : 134,
                219 : 177,
                220 : 187,
                221 : 204,
                222 : 62,
                223 : 90,
                224 : 203,
                225 : 89,
                226 : 95,
                227 : 176,
                228 : 156,
                229 : 169,
                230 : 160,
                231 : 81,
                232 : 11,
                233 : 245,
                234 : 22,
                235 : 235,
                236 : 122,
                237 : 117,
                238 : 44,
                239 : 215,
                240 : 79,
                241 : 174,
                242 : 213,
                243 : 233,
                244 : 230,
                245 : 231,
                246 : 173,
                247 : 232,
                248 : 116,
                249 : 214,
                250 : 244,
                251 : 234,
                252 : 168,
                253 : 80,
                254 : 88,
                255 : 175,
    }

    return a_to_int.get((int_to_a.get(a) + int_to_a.get(b)) % 255)


def long_polynomial_divider(massage_polynomial, generator_polynomial):
    for _ in range(len(massage_polynomial) - len(generator_polynomial) + 1):
        coeficient = massage_polynomial[0]
        for i in range(len(generator_polynomial)):
            massage_polynomial[i] = subtract(massage_polynomial[i], multiply(generator_polynomial[i], coeficient))
        del massage_polynomial[0]

    return massage_polynomial



class Qrcode():
    def __init__(self, version, encode_mode, ec_level, pattern):
        self.version = version
        self.width = (self.version - 1) * 4 + 21
        self.height = (self.version - 1) * 4 + 21
        self.encode_mode = encode_mode
        self.ec_level = ec_level
        self.pattern = pattern
        self.data_list = {}
        self.data_binary = ""


    def create_list(self):
        for y in range(self.height):
            for x in range(self.width):
                self.data_list[(x, y)] = None


    def add_finder_pattern(self):
        for y in range(7):
            for x in range(7):
                self.data_list[(x, y)] = 1
                self.data_list[(self.width - 1 - x, y)] = 1
                self.data_list[(x, self.height - 1 - y)] = 1

        for x in range(5):
            self.data_list[(1 + x, 1)] = 0
            self.data_list[(1 + x, 5)] = 0

            self.data_list[(self.width - 2 - x, 1)] = 0
            self.data_list[(self.width - 2 - x, 5)] = 0

            self.data_list[(1 + x, self.height - 2)] = 0
            self.data_list[(1 + x, self.height - 6)] = 0

        for y in range(3):
            self.data_list[(1, 2 + y)] = 0
            self.data_list[(5, 2 + y)] = 0

            self.data_list[(self.width - 2, 2 + y)] = 0
            self.data_list[(self.width - 6, 2 + y)] = 0

            self.data_list[(1, self.height - 3 - y)] = 0
            self.data_list[(5, self.height - 3 - y)] = 0

        for x in range(8):
            self.data_list[(x, 7)] = 0
            self.data_list[(self.width - 1 - x, 7)] = 0
            self.data_list[(x, self.height - 8)] = 0

        for y in range(8):
            self.data_list[(7, y)] = 0
            self.data_list[(7, self.height - 1 - y)] = 0
            self.data_list[(self.width - 8, y)] = 0


    def add_alignment_pattern(self):
        if self.version == 1:
            return
        if self.version > 5:
            raise ValueError("Version not supported")
        

        pos_align = 10 + self.version * 4
        
        for y in range(5):
            for x in range(5):
                self.data_list[(pos_align - 2 + x, pos_align - 2 + y)] = 1
        
        for x in range(3):
            self.data_list[(pos_align - 1 + x, pos_align - 1)] = 0
            self.data_list[(pos_align - 1 + x, pos_align + 1)] = 0
        
        for y in range(1):
            self.data_list[(pos_align - 1, pos_align)] = 0
            self.data_list[(pos_align + 1, pos_align)] = 0


    def add_timing_pattern(self):
        for x in range(1 + self.version * 2):
            self.data_list[(8 + x * 2, 6)] = 1
            self.data_list[(8 + x * 2 + 1, 6)] = 0

        for y in range(1 + self.version * 2):
            self.data_list[(6, 8 + y * 2)] = 1
            self.data_list[(6, 8 + y * 2 + 1)] = 0


    def add_format_information(self):
        format_string_look_up = {
                        ('L' , 0 ) : '111011111000100',
                        ('L' , 1 ) : '111001011110011',
                        ('L' , 2 ) : '111110110101010',
                        ('L' , 3 ) : '111100010011101',
                        ('L' , 4 ) : '110011000101111',
                        ('L' , 5 ) : '110001100011000',
                        ('L' , 6 ) : '110110001000001',
                        ('L' , 7 ) : '110100101110110',
                        ('M' , 0 ) : '101010000010010',
                        ('M' , 1 ) : '101000100100101',
                        ('M' , 2 ) : '101111001111100',
                        ('M' , 3 ) : '101101101001011',
                        ('M' , 4 ) : '100010111111001',
                        ('M' , 5 ) : '100000011001110',
                        ('M' , 6 ) : '100111110010111',
                        ('M' , 7 ) : '100101010100000',
                        ('Q' , 0 ) : '011010101011111',
                        ('Q' , 1 ) : '011000001101000',
                        ('Q' , 2 ) : '011111100110001',
                        ('Q' , 3 ) : '011101000000110',
                        ('Q' , 4 ) : '010010010110100',
                        ('Q' , 5 ) : '010000110000011',
                        ('Q' , 6 ) : '010111011011010',
                        ('Q' , 7 ) : '010101111101101',
                        ('H' , 0 ) : '001011010001001',
                        ('H' , 1 ) : '001001110111110',
                        ('H' , 2 ) : '001110011100111',
                        ('H' , 3 ) : '001100111010000',
                        ('H' , 4 ) : '000011101100010',
                        ('H' , 5 ) : '000001001010101',
                        ('H' , 6 ) : '000110100001100',
                        ('H' , 7 ) : '000100000111011'}

        format_string = format_string_look_up.get((self.ec_level, self.pattern))

        for x in range(6):
            self.data_list[(x, 8)] = int(format_string[x])

        for x in range(6, 8, 1):
            self.data_list[(x + 1, 8)] = int(format_string[x])
        
        for x in range(8):
            self.data_list[(self.width - 8 + x, 8)] = int(format_string[x + 7])

        for y in range(7):
            self.data_list[(8, self.height - 1 - y)] = int(format_string[y])

        for y in range(2):
            self.data_list[(8, 8 - y)] = int(format_string[7 + y])

        for y in range(6):
            self.data_list[(8, 5 - y)] = int(format_string[9 + y])

    
    def add_single_black_dot(self):
        self.data_list[(8, self.height - 8)] = 1


    def set_up(self, create_list = True):
        if create_list:
            self.create_list()
        self.add_finder_pattern()
        self.add_alignment_pattern()
        self.add_timing_pattern()
        self.add_format_information()
        self.add_single_black_dot()


    def add_mode_indicator(self):
        if self.encode_mode == "byte":
            self.data_binary += "0100"
        else:
            raise ValueError("Encode mode not supported")
    

    def add_character_count_indicator(self):
        length = bin(len(self.text))[2:]
        self.data_binary += "0" * (8 - len(length) % 8)
        self.data_binary += str(length)


    def add_encoded_massage(self):
        utf8_character_set = {  ' ' : '00100000' ,
                                '!' : '00100001' ,
                                '"' : '00100010' ,
                                '#' : '00100011' ,
                                '$' : '00100100' ,
                                '%' : '00100101' ,
                                '&' : '00100110' ,
                                '"' : '00100111' ,
                                '(' : '00101000' ,
                                ')' : '00101001' ,
                                '*' : '00101010' ,
                                '+' : '00101011' ,
                                ',' : '00101100' ,
                                '-' : '00101101' ,
                                '.' : '00101110' ,
                                '/' : '00101111' ,
                                '0' : '00110000' ,
                                '1' : '00110001' ,
                                '2' : '00110010' ,
                                '3' : '00110011' ,
                                '4' : '00110100' ,
                                '5' : '00110101' ,
                                '6' : '00110110' ,
                                '7' : '00110111' ,
                                '8' : '00111000' ,
                                '9' : '00111001' ,
                                ':' : '00111010' ,
                                ';' : '00111011' ,
                                '<' : '00111100' ,
                                '=' : '00111101' ,
                                '>' : '00111110' ,
                                '?' : '00111111' ,
                                '@' : '01000000' ,
                                'A' : '01000001' ,
                                'B' : '01000010' ,
                                'C' : '01000011' ,
                                'D' : '01000100' ,
                                'E' : '01000101' ,
                                'F' : '01000110' ,
                                'G' : '01000111' ,
                                'H' : '01001000' ,
                                'I' : '01001001' ,
                                'J' : '01001010' ,
                                'K' : '01001011' ,
                                'L' : '01001100' ,
                                'M' : '01001101' ,
                                'N' : '01001110' ,
                                'O' : '01001111' ,
                                'P' : '01010000' ,
                                'Q' : '01010001' ,
                                'R' : '01010010' ,
                                'S' : '01010011' ,
                                'T' : '01010100' ,
                                'U' : '01010101' ,
                                'V' : '01010110' ,
                                'W' : '01010111' ,
                                'X' : '01011000' ,
                                'Y' : '01011001' ,
                                'Z' : '01011010' ,
                                '[' : '01011011' ,
                                '\\' : '01011100' ,
                                ']' : '01011101' ,
                                '^' : '01011110' ,
                                '_' : '01011111' ,
                                '`' : '01100000' ,
                                'a' : '01100001' ,
                                'b' : '01100010' ,
                                'c' : '01100011' ,
                                'd' : '01100100' ,
                                'e' : '01100101' ,
                                'f' : '01100110' ,
                                'g' : '01100111' ,
                                'h' : '01101000' ,
                                'i' : '01101001' ,
                                'j' : '01101010' ,
                                'k' : '01101011' ,
                                'l' : '01101100' ,
                                'm' : '01101101' ,
                                'n' : '01101110' ,
                                'o' : '01101111' ,
                                'p' : '01110000' ,
                                'q' : '01110001' ,
                                'r' : '01110010' ,
                                's' : '01110011' ,
                                't' : '01110100' ,
                                'u' : '01110101' ,
                                'v' : '01110110' ,
                                'w' : '01110111' ,
                                'x' : '01111000' ,
                                'y' : '01111001' ,
                                'z' : '01111010' ,
                                '{' : '01111011' ,
                                '|' : '01111100' ,
                                '}' : '01111101' ,
                                '~' : '01111110' ,
}

        if self.encode_mode == "byte":
            for character in self.text:
                self.data_binary += utf8_character_set.get(character)


    def add_terinator_zeros(self):
        total_data_bits = {     '1-L' : 152 ,
                                '1-M' : 128 ,
                                '1-Q' : 104 ,
                                '1-H' : 72 ,
                                '2-L' : 272 ,
                                '2-M' : 224 ,
                                '2-Q' : 176 ,
                                '2-H' : 128 ,
                                '3-L' : 440 ,
                                '3-M' : 352 ,
                                '3-Q' : 272 ,
                                '3-H' : 208 ,
                                '4-L' : 640 ,
                                '4-M' : 512 ,
                                '4-Q' : 384 ,
                                '4-H' : 288 ,
                                '5-L' : 864 ,
                                '5-M' : 688 ,
                                '5-Q' : 496 ,
                                '5-H' : 368 , }

        self.bit_capicity = total_data_bits.get(f'{self.version}-{self.ec_level}')

        if len(self.data_binary) > self.bit_capicity:
            raise ValueError("Massage copacity exceeded")
        
        if len(self.data_binary) <= self.bit_capicity - 4:
            self.data_binary += "0000"
        else:
            self.data_binary += "0" * (self.bit_capicity - len(self.data_binary))


    def make_multiple_of_eight(self):
        if len(self.data_binary) % 8 != 0:
            self.data_binary += '0' * (8 - len(self.data_binary) % 8)


    def add_pad_bytes(self):
        full_pad = "1110110000010001"
        half_pad = "11101100"

        if len(self.data_binary) < self.bit_capicity:
            self.data_binary += full_pad * ((self.bit_capicity - len(self.data_binary)) // 16)
            self.data_binary += half_pad * ((self.bit_capicity - len(self.data_binary)) // 8)


    def generate_ec_codewords(self):
        if (self.version > 5) or (self.version == 5 and self.ec_level != "L") or (self.version == 4 and self.ec_level != "L") or (self.version == 3 and (self.ec_level == "Q" or self.ec_level == "H")):
            raise ValueError("Version and ec level combination not supported")
        
        seprated_bits = [int(self.data_binary[i:i+8], 2) for i in range(0, len(self.data_binary), 8)]

        generator_polynomial_look_up = {
            '1-L': [1, 127, 122, 154, 164, 11, 68, 117],
            '1-M': [1, 216, 194, 159, 111, 199, 94, 95, 113, 157, 193], 
            '1-Q': [1, 137, 73, 227, 17, 177, 17, 52, 13, 46, 43, 83, 132, 120], 
            '1-H': [1, 119, 66, 83, 120, 119, 22, 197, 83, 249, 41, 143, 134, 85, 53, 125, 99, 79], 
            '2-L': [1, 216, 194, 159, 111, 199, 94, 95, 113, 157, 193], 
            '2-M': [1, 59, 13, 104, 189, 68, 209, 30, 8, 163, 65, 41, 229, 98, 50, 36, 59], 
            '2-Q': [1, 89, 179, 131, 176, 182, 244, 19, 189, 69, 40, 28, 137, 29, 123, 67, 253, 86, 218, 230, 26, 145, 245], 
            '2-H': [1, 252, 9, 28, 13, 18, 251, 208, 150, 103, 174, 100, 41, 167, 12, 247, 56, 117, 119, 233, 127, 181, 100, 121, 147, 176, 74, 58, 197], 
            '3-L': [1, 29, 196, 111, 163, 112, 74, 10, 105, 105, 139, 132, 151, 32, 134, 26], 
            '3-M': [1, 246, 51, 183, 4, 136, 98, 199, 152, 77, 56, 206, 24, 145, 40, 209, 117, 233, 42, 135, 68, 70, 144, 146, 77, 43, 94], 
            '4-L': [1, 152, 185, 240, 5, 111, 99, 6, 220, 112, 150, 69, 36, 187, 22, 228, 198, 121, 121, 165, 174], 
            '5-L': [1, 246, 51, 183, 4, 136, 98, 199, 152, 77, 56, 206, 24, 145, 40, 209, 117, 233, 42, 135, 68, 70, 144, 146, 77, 43, 94]
            }
        
        generator_polynomial = generator_polynomial_look_up.get(f"{self.version}-{self.ec_level}")
        
        zeros_list = [0 for i in range(len(generator_polynomial) - 1)]

        massage_polynomial = seprated_bits + zeros_list

        ec_codewords = long_polynomial_divider(massage_polynomial, generator_polynomial)

        for i in ec_codewords:
            binary = bin(i)[2:]
            binary = "0" * (8 - len(binary)) + binary
            self.data_binary += binary


    def fill_unused_bits(self):
        if self.version > 1:
            self.data_binary += "0" * 7


    def find_next_square(self, x, y):
        x_next = 0
        y_next = 0

        if x <= 5:
            if x % 4 == 1:
                x_next = x - 1
                y_next = y
            if x % 4 == 0:
                if y == self.height - 1:
                    x_next = x - 1
                    y_next = y
                else:
                    x_next = x + 1
                    y_next = y + 1
            if x % 4 == 3:
                x_next = x - 1
                y_next = y
            if x % 4 == 2:
                if y == 0:
                    x_next = x - 1
                    y_next = y
                else:
                    x_next = x + 1
                    y_next = y - 1

        else:
            if x % 4 == 0:
                x_next = x - 1
                y_next = y
            if x % 4 == 3:
                if y == 0:
                    x_next = x - 1
                    y_next = y
                else:
                    x_next = x + 1
                    y_next = y - 1
            if x % 4 == 2:
                x_next = x - 1
                y_next = y
            if x % 4 == 1:
                if y == self.width - 1:
                    x_next = x - 1
                    y_next = y
                else:
                    x_next = x + 1
                    y_next = y + 1

        # print(f'{x}, {y},  {x_next}, {y_next}')

        if self.data_list.get((x_next, y_next)) == None:
            return (x_next, y_next)
        else:
            return self.find_next_square(x_next, y_next)


    def place_data_binary(self):
        x_previous = self.width - 1
        y_previous = self.height - 1

        for i in range(len(self.data_binary)):
            self.data_list[(x_previous, y_previous)] = int(self.data_binary[i])
            new_coordinates = self.find_next_square(x_previous, y_previous)
            x_previous = new_coordinates[0]
            y_previous = new_coordinates[1]


    def apply_mask(self):
        if self.pattern == 0:
            for y in range(self.height):
                for x in range(self.width):
                    if (x + y) % 2 == 0:
                        if self.data_list[(x, y)] == 0:
                            self.data_list[(x, y)] = 1
                        elif self.data_list[(x, y)] == 1:
                            self.data_list[(x, y)] = 0

        self.set_up(create_list = False)


    def process_massage(self, text):
        self.text = text
        self.add_mode_indicator()
        self.add_character_count_indicator()
        self.add_encoded_massage()
        self.add_terinator_zeros()
        self.make_multiple_of_eight()
        self.add_pad_bytes()
        self.generate_ec_codewords()
        self.fill_unused_bits()
        self.place_data_binary()
        self.apply_mask()

