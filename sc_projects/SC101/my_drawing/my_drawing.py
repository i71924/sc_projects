"""
File: my_drawing.py
Name: Po kai Feng
----------------------
This file print the logo of 'STARWARS' and may the force be with you
"""


from campy.graphics.gobjects import GRect, GPolygon
from campy.graphics.gwindow import GWindow


window = GWindow(width=600, height=362, title='STARWARS')


def main():
    """
    Well, just draw all of the lines by GPolygon
    """
    background = GRect(window.width, window.height, x=0, y=0)
    background.filled = True
    background.fill_color = 'black'
    window.add(background)

    # Drawing first S & T
    poly_s1 = GPolygon()
    poly_s1.add_vertex((116, 143))
    poly_s1.add_vertex((116, 137))
    poly_s1.add_vertex((26, 137))
    poly_s1.add_vertex((26, 179))
    poly_s1.add_vertex((116, 179))
    poly_s1.add_vertex((116, 173))
    poly_s1.add_vertex((32, 173))
    poly_s1.add_vertex((32, 143))
    poly_s1.filled = True
    poly_s1.color = 'yellow'
    poly_s1.fill_color = 'yellow'
    window.add(poly_s1)

    poly_s2 = GPolygon()
    poly_s2.add_vertex((116, 137))
    poly_s2.add_vertex((98, 114))
    poly_s2.add_vertex((94, 107))
    poly_s2.add_vertex((92, 99))
    poly_s2.add_vertex((94, 90))
    poly_s2.add_vertex((98, 81))
    poly_s2.add_vertex((106, 71))
    poly_s2.add_vertex((114, 66))
    poly_s2.add_vertex((123, 65))
    poly_s2.add_vertex((123, 71))
    poly_s2.add_vertex((114, 74))
    poly_s2.add_vertex((109, 78))
    poly_s2.add_vertex((106, 83))
    poly_s2.add_vertex((101, 90))
    poly_s2.add_vertex((100, 98))
    poly_s2.add_vertex((101, 107))
    poly_s2.add_vertex((122, 133))
    poly_s2.add_vertex((123, 135))
    poly_s2.add_vertex((123, 138))
    poly_s2.add_vertex((121, 141))
    poly_s2.add_vertex((118, 143))
    poly_s2.add_vertex((116, 143))
    poly_s2.filled = True
    poly_s2.color = 'yellow'
    poly_s2.fill_color = 'yellow'
    window.add(poly_s2)

    poly_t1 = GPolygon()
    poly_t1.add_vertex((123, 65))
    poly_t1.add_vertex((290, 65))
    poly_t1.add_vertex((290, 103))
    poly_t1.add_vertex((240, 103))
    poly_t1.add_vertex((240, 178))
    poly_t1.add_vertex((197, 178))
    poly_t1.add_vertex((197, 103))
    poly_t1.add_vertex((145, 103))
    poly_t1.add_vertex((145, 95))
    poly_t1.add_vertex((204, 95))
    poly_t1.add_vertex((204, 172))
    poly_t1.add_vertex((233, 172))
    poly_t1.add_vertex((233, 95))
    poly_t1.add_vertex((282, 95))
    poly_t1.add_vertex((282, 71))
    poly_t1.add_vertex((123, 71))
    poly_t1.filled = True
    poly_t1.color = 'yellow'
    poly_t1.fill_color = 'yellow'
    window.add(poly_t1)

    poly_s3 = GPolygon()
    poly_s3.add_vertex((145, 95))
    poly_s3.add_vertex((141, 97))
    poly_s3.add_vertex((139, 100))
    poly_s3.add_vertex((137, 103))
    poly_s3.add_vertex((137, 105))
    poly_s3.add_vertex((140, 109))
    poly_s3.add_vertex((160, 136))
    poly_s3.add_vertex((162, 139))
    poly_s3.add_vertex((162, 143))
    poly_s3.add_vertex((161, 149))
    poly_s3.add_vertex((160, 155))
    poly_s3.add_vertex((158, 160))
    poly_s3.add_vertex((153, 165))
    poly_s3.add_vertex((146, 170))
    poly_s3.add_vertex((137, 171))
    poly_s3.add_vertex((116, 173))
    poly_s3.add_vertex((116, 179))
    poly_s3.add_vertex((134, 178))
    poly_s3.add_vertex((143, 178))
    poly_s3.add_vertex((149, 176))
    poly_s3.add_vertex((153, 174))
    poly_s3.add_vertex((157, 171))
    poly_s3.add_vertex((161, 168))
    poly_s3.add_vertex((164, 164))
    poly_s3.add_vertex((167, 158))
    poly_s3.add_vertex((169, 153))
    poly_s3.add_vertex((170, 146))
    poly_s3.add_vertex((169, 140))
    poly_s3.add_vertex((168, 135))
    poly_s3.add_vertex((165, 130))
    poly_s3.add_vertex((145, 102))
    poly_s3.filled = True
    poly_s3.color = 'yellow'
    poly_s3.fill_color = 'yellow'
    window.add(poly_s3)

    # Drawing second S staring at x=491, y=257 (x+375 y+114)
    x2 = 375
    y2 = 118
    poly_s4 = GPolygon()
    poly_s4.add_vertex((116 + x2, 143 + y2))
    poly_s4.add_vertex((116 + x2, 137 + y2))
    poly_s4.add_vertex((78 + x2, 140 + y2))
    poly_s4.add_vertex((78 + x2, 146 + y2))
    poly_s4.filled = True
    poly_s4.color = 'yellow'
    poly_s4.fill_color = 'yellow'
    window.add(poly_s4)

    poly_s5 = GPolygon()
    poly_s5.add_vertex((116 + x2, 137 + y2))
    poly_s5.add_vertex((98 + x2, 114 + y2))
    poly_s5.add_vertex((94 + x2, 107 + y2))
    poly_s5.add_vertex((92 + x2, 99 + y2))
    poly_s5.add_vertex((94 + x2, 90 + y2))
    poly_s5.add_vertex((98 + x2, 81 + y2))
    poly_s5.add_vertex((106 + x2, 71 + y2))
    poly_s5.add_vertex((114 + x2, 66 + y2))
    poly_s5.add_vertex((123 + x2, 65 + y2))
    poly_s5.add_vertex((123 + x2, 71 + y2))
    poly_s5.add_vertex((114 + x2, 74 + y2))
    poly_s5.add_vertex((109 + x2, 78 + y2))
    poly_s5.add_vertex((106 + x2, 83 + y2))
    poly_s5.add_vertex((101 + x2, 90 + y2))
    poly_s5.add_vertex((100 + x2, 98 + y2))
    poly_s5.add_vertex((101 + x2, 107 + y2))
    poly_s5.add_vertex((122 + x2, 133 + y2))
    poly_s5.add_vertex((123 + x2, 135 + y2))
    poly_s5.add_vertex((123 + x2, 138 + y2))
    poly_s5.add_vertex((121 + x2, 141 + y2))
    poly_s5.add_vertex((118 + x2, 143 + y2))
    poly_s5.add_vertex((116 + x2, 143 + y2))
    poly_s5.filled = True
    poly_s5.color = 'yellow'
    poly_s5.fill_color = 'yellow'
    window.add(poly_s5)

    poly_s6 = GPolygon()
    poly_s6.add_vertex((145 + x2, 95 + y2))
    poly_s6.add_vertex((141 + x2, 97 + y2))
    poly_s6.add_vertex((139 + x2, 100 + y2))
    poly_s6.add_vertex((137 + x2, 103 + y2))
    poly_s6.add_vertex((137 + x2, 105 + y2))
    poly_s6.add_vertex((140 + x2, 109 + y2))
    poly_s6.add_vertex((160 + x2, 136 + y2))
    poly_s6.add_vertex((162 + x2, 139 + y2))
    poly_s6.add_vertex((162 + x2, 143 + y2))
    poly_s6.add_vertex((161 + x2, 149 + y2))
    poly_s6.add_vertex((160 + x2, 155 + y2))
    poly_s6.add_vertex((158 + x2, 160 + y2))
    poly_s6.add_vertex((153 + x2, 165 + y2))
    poly_s6.add_vertex((146 + x2, 170 + y2))
    poly_s6.add_vertex((137 + x2, 171 + y2))
    poly_s6.add_vertex((101 + x2, 173 + y2))
    poly_s6.add_vertex((101 + x2, 180 + y2))
    poly_s6.add_vertex((134 + x2, 178 + y2))
    poly_s6.add_vertex((143 + x2, 178 + y2))
    poly_s6.add_vertex((149 + x2, 176 + y2))
    poly_s6.add_vertex((153 + x2, 174 + y2))
    poly_s6.add_vertex((157 + x2, 171 + y2))
    poly_s6.add_vertex((161 + x2, 168 + y2))
    poly_s6.add_vertex((164 + x2, 164 + y2))
    poly_s6.add_vertex((167 + x2, 158 + y2))
    poly_s6.add_vertex((169 + x2, 153 + y2))
    poly_s6.add_vertex((170 + x2, 146 + y2))
    poly_s6.add_vertex((169 + x2, 140 + y2))
    poly_s6.add_vertex((168 + x2, 135 + y2))
    poly_s6.add_vertex((165 + x2, 130 + y2))
    poly_s6.add_vertex((145 + x2, 102 + y2))
    poly_s6.filled = True
    poly_s6.color = 'yellow'
    poly_s6.fill_color = 'yellow'
    window.add(poly_s6)

    poly_s7 = GPolygon()
    poly_s7.add_vertex((123 + x2, 65 + y2))
    poly_s7.add_vertex((574, 65 + y2))
    poly_s7.add_vertex((573, 222))
    poly_s7.add_vertex((520, 222))
    poly_s7.add_vertex((520, 213))
    poly_s7.add_vertex((567, 213))
    poly_s7.add_vertex((567, 189))
    poly_s7.add_vertex((123 + x2, 71 + y2))
    poly_s7.filled = True
    poly_s7.color = 'yellow'
    poly_s7.fill_color = 'yellow'
    window.add(poly_s7)

    # Drawing first A
    poly_a1 = GPolygon()
    poly_a1.add_vertex((311, 65))
    poly_a1.add_vertex((368, 65))
    poly_a1.add_vertex((408, 178))
    poly_a1.add_vertex((363, 178))
    poly_a1.add_vertex((360, 163))
    poly_a1.add_vertex((320, 163))
    poly_a1.add_vertex((316, 178))
    poly_a1.add_vertex((272, 178))
    poly_a1.add_vertex((311, 66))
    poly_a1.add_vertex((316, 71))
    poly_a1.add_vertex((282, 171))
    poly_a1.add_vertex((311, 171))
    poly_a1.add_vertex((315, 158))
    poly_a1.add_vertex((366, 158))
    poly_a1.add_vertex((368, 171))
    poly_a1.add_vertex((399, 171))
    poly_a1.add_vertex((363, 71))
    poly_a1.add_vertex((316, 71))
    poly_a1.filled = True
    poly_a1.color = 'yellow'
    poly_a1.fill_color = 'yellow'
    window.add(poly_a1)

    poly_a2 = GPolygon()
    poly_a2.add_vertex((340, 86))
    poly_a2.add_vertex((323, 135))
    poly_a2.add_vertex((357, 135))
    poly_a2.add_vertex((347, 128))
    poly_a2.add_vertex((333, 128))
    poly_a2.add_vertex((340, 107))
    poly_a2.add_vertex((347, 128))
    poly_a2.add_vertex((357, 135))
    poly_a2.add_vertex((340, 86))
    poly_a2.filled = True
    poly_a2.color = 'yellow'
    poly_a2.fill_color = 'yellow'
    window.add(poly_a2)

    # Drawing second A starting at x=219,y=184 (x-92 y+119)
    x1 = -92
    y1 = 119
    poly_a3 = GPolygon()
    poly_a3.add_vertex((311+x1, 65+y1))
    poly_a3.add_vertex((368+x1, 65+y1))
    poly_a3.add_vertex((408+x1, 178+y1))
    poly_a3.add_vertex((363+x1, 178+y1))
    poly_a3.add_vertex((360+x1, 163+y1))
    poly_a3.add_vertex((320+x1, 163+y1))
    poly_a3.add_vertex((316+x1, 178+y1))
    poly_a3.add_vertex((272+x1, 178+y1))
    poly_a3.add_vertex((311+x1, 66+y1))
    poly_a3.add_vertex((316+x1, 71+y1))
    poly_a3.add_vertex((282+x1, 171+y1))
    poly_a3.add_vertex((311+x1, 171+y1))
    poly_a3.add_vertex((315+x1, 158+y1))
    poly_a3.add_vertex((366+x1, 158+y1))
    poly_a3.add_vertex((368+x1, 171+y1))
    poly_a3.add_vertex((399+x1, 171+y1))
    poly_a3.add_vertex((363+x1, 71+y1))
    poly_a3.add_vertex((316+x1, 71+y1))
    poly_a3.filled = True
    poly_a3.color = 'yellow'
    poly_a3.fill_color = 'yellow'
    window.add(poly_a3)

    poly_a4 = GPolygon()
    poly_a4.add_vertex((340+x1, 86+119))
    poly_a4.add_vertex((323+x1, 135+119))
    poly_a4.add_vertex((357+x1, 135+119))
    poly_a4.add_vertex((347+x1, 128+119))
    poly_a4.add_vertex((333+x1, 128+119))
    poly_a4.add_vertex((340+x1, 107+119))
    poly_a4.add_vertex((347+x1, 128+119))
    poly_a4.add_vertex((357+x1, 135+119))
    poly_a4.add_vertex((340+x1, 86+119))
    poly_a4.filled = True
    poly_a4.color = 'yellow'
    poly_a4.fill_color = 'yellow'
    window.add(poly_a4)

    # Drawing first R
    poly_r1 = GPolygon()
    poly_r1.add_vertex((418, 65))
    poly_r1.add_vertex((494, 65))
    poly_r1.add_vertex((501, 66))
    poly_r1.add_vertex((506, 67))
    poly_r1.add_vertex((510, 68))
    poly_r1.add_vertex((515, 70))
    poly_r1.add_vertex((521, 75))
    poly_r1.add_vertex((526, 80))
    poly_r1.add_vertex((529, 85))
    poly_r1.add_vertex((531, 89))
    poly_r1.add_vertex((533, 94))
    poly_r1.add_vertex((533, 100))
    poly_r1.add_vertex((532, 106))
    poly_r1.add_vertex((531, 111))
    poly_r1.add_vertex((530, 118))
    poly_r1.add_vertex((526, 124))
    poly_r1.add_vertex((521, 129))
    poly_r1.add_vertex((514, 134))
    poly_r1.add_vertex((512, 136))
    poly_r1.add_vertex((574, 138))
    poly_r1.add_vertex((575, 178))
    poly_r1.add_vertex((512, 178))
    poly_r1.add_vertex((500, 177))
    poly_r1.add_vertex((496, 176))
    poly_r1.add_vertex((493, 175))
    poly_r1.add_vertex((488, 173))
    poly_r1.add_vertex((464, 150))
    poly_r1.add_vertex((464, 178))
    poly_r1.add_vertex((418, 178))
    poly_r1.add_vertex((418, 65))
    poly_r1.add_vertex((425, 72))
    poly_r1.add_vertex((496, 72))
    poly_r1.add_vertex((501, 73))
    poly_r1.add_vertex((506, 74))
    poly_r1.add_vertex((511, 76))
    poly_r1.add_vertex((515, 80))
    poly_r1.add_vertex((519, 83))
    poly_r1.add_vertex((522, 87))
    poly_r1.add_vertex((525, 92))
    poly_r1.add_vertex((526, 98))
    poly_r1.add_vertex((526, 105))
    poly_r1.add_vertex((524, 111))
    poly_r1.add_vertex((522, 117))
    poly_r1.add_vertex((518, 122))
    poly_r1.add_vertex((513, 126))
    poly_r1.add_vertex((505, 131))
    poly_r1.add_vertex((503, 132))
    poly_r1.add_vertex((505, 136))
    poly_r1.add_vertex((508, 139))
    poly_r1.add_vertex((512, 142))
    poly_r1.add_vertex((514, 143))
    poly_r1.add_vertex((567, 144))
    poly_r1.add_vertex((567, 171))
    poly_r1.add_vertex((503, 171))
    poly_r1.add_vertex((499, 170))
    poly_r1.add_vertex((495, 167))
    poly_r1.add_vertex((491, 164))
    poly_r1.add_vertex((456, 134))
    poly_r1.add_vertex((456, 171))
    poly_r1.add_vertex((425, 170))
    poly_r1.add_vertex((425, 72))
    poly_r1.filled = True
    poly_r1.color = 'yellow'
    poly_r1.fill_color = 'yellow'
    window.add(poly_r1)

    poly_r2 = GPolygon()
    poly_r2.add_vertex((456, 92))
    poly_r2.add_vertex((482, 92))
    poly_r2.add_vertex((487, 93))
    poly_r2.add_vertex((491, 94))
    poly_r2.add_vertex((495, 96))
    poly_r2.add_vertex((497, 99))
    poly_r2.add_vertex((498, 104))
    poly_r2.add_vertex((497, 109))
    poly_r2.add_vertex((495, 113))
    poly_r2.add_vertex((491, 115))
    poly_r2.add_vertex((487, 116))
    poly_r2.add_vertex((456, 116))
    poly_r2.add_vertex((456, 92))
    poly_r2.add_vertex((463, 98))
    poly_r2.add_vertex((482, 98))
    poly_r2.add_vertex((488, 100))
    poly_r2.add_vertex((490, 103))
    poly_r2.add_vertex((491, 105))
    poly_r2.add_vertex((488, 109))
    poly_r2.add_vertex((482, 110))
    poly_r2.add_vertex((463, 110))
    poly_r2.add_vertex((463, 98))
    poly_r2.filled = True
    poly_r2.color = 'yellow'
    poly_r2.fill_color = 'yellow'
    window.add(poly_r2)

    # Drawing second R starting at x=327,y=185 (x-91 y+120)
    x3 = -91
    y3 = 120
    poly_r3 = GPolygon()
    poly_r3.add_vertex((418+x3, 65+y3))
    poly_r3.add_vertex((494+x3, 65+y3))
    poly_r3.add_vertex((501+x3, 66+y3))
    poly_r3.add_vertex((506+x3, 67+y3))
    poly_r3.add_vertex((510+x3, 68+y3))
    poly_r3.add_vertex((515+x3, 70+y3))
    poly_r3.add_vertex((521+x3, 75+y3))
    poly_r3.add_vertex((526+x3, 80+y3))
    poly_r3.add_vertex((529+x3, 85+y3))
    poly_r3.add_vertex((531+x3, 89+y3))
    poly_r3.add_vertex((533+x3, 94+y3))
    poly_r3.add_vertex((533+x3, 100+y3))
    poly_r3.add_vertex((532+x3, 106+y3))
    poly_r3.add_vertex((531+x3, 111+y3))
    poly_r3.add_vertex((530+x3, 118+y3))
    poly_r3.add_vertex((526+x3, 124+y3))
    poly_r3.add_vertex((521+x3, 129+y3))
    poly_r3.add_vertex((514+x3, 134+y3))
    poly_r3.add_vertex((512+x3, 136+y3))
    poly_r3.add_vertex((574+x3, 138+y3))
    poly_r3.add_vertex((575+x3, 178+y3))
    poly_r3.add_vertex((512+x3, 178+y3))
    poly_r3.add_vertex((500+x3, 177+y3))
    poly_r3.add_vertex((496+x3, 176+y3))
    poly_r3.add_vertex((493+x3, 175+y3))
    poly_r3.add_vertex((488+x3, 173+y3))
    poly_r3.add_vertex((464+x3, 150+y3))
    poly_r3.add_vertex((464+x3, 178+y3))
    poly_r3.add_vertex((418+x3, 178+y3))
    poly_r3.add_vertex((418+x3, 65+y3))
    poly_r3.add_vertex((425+x3, 72+y3))
    poly_r3.add_vertex((496+x3, 72+y3))
    poly_r3.add_vertex((501+x3, 73+y3))
    poly_r3.add_vertex((506+x3, 74+y3))
    poly_r3.add_vertex((511+x3, 76+y3))
    poly_r3.add_vertex((515+x3, 80+y3))
    poly_r3.add_vertex((519+x3, 83+y3))
    poly_r3.add_vertex((522+x3, 87+y3))
    poly_r3.add_vertex((525+x3, 92+y3))
    poly_r3.add_vertex((526+x3, 98+y3))
    poly_r3.add_vertex((526+x3, 105+y3))
    poly_r3.add_vertex((524+x3, 111+y3))
    poly_r3.add_vertex((522+x3, 117+y3))
    poly_r3.add_vertex((518+x3, 122+y3))
    poly_r3.add_vertex((513+x3, 126+y3))
    poly_r3.add_vertex((505+x3, 131+y3))
    poly_r3.add_vertex((503+x3, 132+y3))
    poly_r3.add_vertex((505+x3, 136+y3))
    poly_r3.add_vertex((508+x3, 139+y3))
    poly_r3.add_vertex((512+x3, 142+y3))
    poly_r3.add_vertex((514+x3, 143+y3))
    poly_r3.add_vertex((567+x3, 144+y3))
    poly_r3.add_vertex((567+x3, 171+y3))
    poly_r3.add_vertex((503+x3, 171+y3))
    poly_r3.add_vertex((499+x3, 170+y3))
    poly_r3.add_vertex((495+x3, 167+y3))
    poly_r3.add_vertex((491+x3, 164+y3))
    poly_r3.add_vertex((456+x3, 134+y3))
    poly_r3.add_vertex((456+x3, 171+y3))
    poly_r3.add_vertex((425+x3, 170+y3))
    poly_r3.add_vertex((425+x3, 72+y3))
    poly_r3.filled = True
    poly_r3.color = 'yellow'
    poly_r3.fill_color = 'yellow'
    window.add(poly_r3)

    poly_r4 = GPolygon()
    poly_r4.add_vertex((456+x3, 92+y3))
    poly_r4.add_vertex((482+x3, 92+y3))
    poly_r4.add_vertex((487+x3, 93+y3))
    poly_r4.add_vertex((491+x3, 94+y3))
    poly_r4.add_vertex((495+x3, 96+y3))
    poly_r4.add_vertex((497+x3, 99+y3))
    poly_r4.add_vertex((498+x3, 104+y3))
    poly_r4.add_vertex((497+x3, 109+y3))
    poly_r4.add_vertex((495+x3, 113+y3))
    poly_r4.add_vertex((491+x3, 115+y3))
    poly_r4.add_vertex((487+x3, 116+y3))
    poly_r4.add_vertex((456+x3, 116+y3))
    poly_r4.add_vertex((456+x3, 92+y3))
    poly_r4.add_vertex((463+x3, 98+y3))
    poly_r4.add_vertex((482+x3, 98+y3))
    poly_r4.add_vertex((488+x3, 100+y3))
    poly_r4.add_vertex((490+x3, 103+y3))
    poly_r4.add_vertex((491+x3, 105+y3))
    poly_r4.add_vertex((488+x3, 109+y3))
    poly_r4.add_vertex((482+x3, 110+y3))
    poly_r4.add_vertex((463+x3, 110+y3))
    poly_r4.add_vertex((463+x3, 98+y3))
    poly_r4.filled = True
    poly_r4.color = 'yellow'
    poly_r4.fill_color = 'yellow'
    window.add(poly_r4)

    # Cover the overlap of second R and second S
    poly_b1 = GPolygon()
    poly_b1.add_vertex((116 + x2, 145 + y2))
    poly_b1.add_vertex((567+x3, 144+y3))
    poly_b1.add_vertex((567+x3, 170+y3))
    poly_b1.add_vertex((116 + x2, 169 + y3))
    poly_b1.filled = True
    poly_b1.color = 'black'
    poly_b1.fill_color = 'black'
    window.add(poly_b1)

    # Drawing W
    poly_w = GPolygon()
    poly_w.add_vertex((28, 185))
    poly_w.add_vertex((71, 185))
    poly_w.add_vertex((81, 215))
    poly_w.add_vertex((92, 185))
    poly_w.add_vertex((134, 185))
    poly_w.add_vertex((145, 215))
    poly_w.add_vertex((155, 185))
    poly_w.add_vertex((198, 185))
    poly_w.add_vertex((159, 298))
    poly_w.add_vertex((129, 298))
    poly_w.add_vertex((113, 252))
    poly_w.add_vertex((97, 298))
    poly_w.add_vertex((66, 298))
    poly_w.add_vertex((28, 185))
    poly_w.add_vertex((38, 191))
    poly_w.add_vertex((72, 291))
    poly_w.add_vertex((92, 291))
    poly_w.add_vertex((113, 232))
    poly_w.add_vertex((134, 291))
    poly_w.add_vertex((155, 291))
    poly_w.add_vertex((188, 191))
    poly_w.add_vertex((160, 191))
    poly_w.add_vertex((144, 235))
    poly_w.add_vertex((129, 191))
    poly_w.add_vertex((98, 191))
    poly_w.add_vertex((82, 235))
    poly_w.add_vertex((67, 191))
    poly_w.add_vertex((38, 191))
    poly_w.filled = True
    poly_w.color = 'yellow'
    poly_w.fill_color = 'yellow'
    window.add(poly_w)

    print('May the force be with you!')


if __name__ == '__main__':
    main()
