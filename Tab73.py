def fsi73(l, jp):
    # l = 9
    # jp = 0.55
    #===============================================================================
    # Таблица 7.3 по СП 24.13330.2011 изм. 1
    ts = 1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 25, 30, 35
    t02 = 3.569006745423, 4.2828080945076, 4.8946378222944, 5.4044959287834, 5.7104107926768, 5.9143540352724, 6.3222405204636, 6.628155384357, 7.3419567334416, 8.0557580825262, 8.7695594316108, 9.4833607806954, 10.19716212978
    t03 = 2.3453472898494, 3.059148638934, 3.569006745423, 3.8749216093164, 4.078864851912, 4.2828080945076, 4.4867513371032, 4.6906945796988, 5.2005526861878, 5.7104107926768, 6.2202688991658, 6.7301270056548, 7.138013490846
    t04 = 1.529574319467, 2.1414040472538, 2.549290532445, 2.7532337750406, 2.9571770176362, 3.1611202602318, 3.3650635028274, 3.4670351241252, 3.8749216093164, 4.1808364732098, 4.4867513371032, 4.7926662009966, 5.09858106489
    t05 = 1.2236594555736, 1.7335175620626, 2.039432425956, 2.2433756685516, 2.4473189111472, 2.549290532445, 2.6512621537428, 2.7532337750406, 2.8552053963384, 3.059148638934, 3.2630918815296, 3.4670351241252, 3.6709783667208
    t06 = 0.8157729703824, 1.2236594555736, 1.4276026981692, 1.6315459407648, 1.7335175620626, 1.8354891833604, 1.9374608046582, 1.9374608046582, 2.039432425956, 2.039432425956, 2.039432425956, 2.1414040472538, 2.2433756685516
    t07 = 0.4078864851912, 0.7138013490846, 0.8157729703824, 0.9177445916802, 1.019716212978, 1.019716212978, 1.019716212978, 1.019716212978, 1.1216878342758, 1.2236594555736, 1.2236594555736, 1.2236594555736, 1.3256310768714
    t08 = 0.4078864851912, 0.509858106489, 0.7138013490846, 0.8157729703824, 0.8157729703824, 0.8157729703824, 0.8157729703824, 0.8157729703824, 0.8157729703824, 0.8157729703824, 0.8157729703824, 0.9177445916802, 0.9177445916802
    t09 = 0.3059148638934, 0.4078864851912, 0.6118297277868, 0.7138013490846, 0.7138013490846, 0.7138013490846, 0.7138013490846, 0.7138013490846, 0.7138013490846, 0.7138013490846, 0.7138013490846, 0.8157729703824, 0.8157729703824
    t10 = 0.2039432425956, 0.4078864851912, 0.509858106489, 0.509858106489, 0.6118297277868, 0.6118297277868, 0.6118297277868, 0.6118297277868, 0.6118297277868, 0.6118297277868, 0.6118297277868, 0.7138013490846, 0.7138013490846
    dct = {0.2:t02, 0.3:t03, 0.4:t04, 0.5:t05, 0.6:t06, 0.7:t07, 0.8:t08, 0.9:t09, 1.0:t10}
    #===============================================================================
    # Нахождение индекса в кортеже
    def fon (t1, x):
        for i in t1:
            if x > i:
                continue
            else:
                break
        ia1 = t1.index(i); ia2 = t1.index(i)-1
        return ia1, ia2
    # Функция интерполяции 
    def interpoi (t1, t2, x):
        i = fon (t1, x)
        a1 = t1[i[0]]; a2 = t1[i[1]]; b1 = t2[i[0]]; b2 = t2[i[1]] # значения индексов
        a12 = a1 - a2; b12 = b1 - b2; a13 = x - a2; x = a13 * b12 / a12; y = b2 + x
        return y
    #===============================================================================
    t1 = tuple(dct.keys()); x = jp; i = fon (t1, x)
    a1 = t1[i[0]]; a2 = t1[i[1]]
    #===============================================================================
    tx = []; t1 = ts; x = l
    t2 = dct[a2]; tx.append (interpoi (t1, t2, x))
    t2 = dct[a1]; tx.append (interpoi (t1, t2, x))
    #===============================================================================
    t1 = [a2, a1]; t2 = tx; x = jp
    i = interpoi (t1, t2, x) # результат интерполяции
    return i
    #===============================================================================
    # print(i)