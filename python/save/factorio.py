def main():
    field = [
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    frame_1 = [
        [0, 0, 1, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 1, 0, 0, 0, 0, ],
        [1, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 0, 0, 1, 0, 0, 0, 0, ],
        [0, 0, 1, 0, 0, 0, 0, 0, ],
    ]

    frame_2 = [
        [0, 0, 0, 1, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 1, 0, 0, 0, ],
        [0, 1, 1, 1, 1, 1, 0, 0, ],
        [0, 0, 0, 0, 1, 0, 0, 0, ],
        [0, 0, 0, 1, 0, 0, 0, 0, ],
    ]

    frame_3 = [
        [0, 0, 0, 0, 1, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 1, 1, 1, 1, 0, ],
        [0, 0, 0, 0, 0, 1, 0, 0, ],
        [0, 0, 0, 0, 1, 0, 0, 0, ],
    ]

    frame_4 = [
        [0, 0, 0, 0, 0, 1, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 1, 0, ],
        [0, 0, 0, 1, 1, 1, 1, 1, ],
        [0, 0, 0, 0, 0, 0, 1, 0, ],
        [0, 0, 0, 0, 0, 1, 0, 0, ],
    ]

    frames = [
        frame_1,
        frame_2,
        frame_3,
        frame_4,
    ]
    values = [0]
    result = field.copy()
    print('res:', result)
    count = 0
    for idx_frame, frame in enumerate(frames):
        count += 1
        print(f'result:', *result, sep='\n')
        print('\n', f'frame {count}:', *frame, sep='\n')

        for idx_row, row in enumerate(frame):
            c = 0
            for idx_pxl, pxl in enumerate(row):
                if pxl:
                    curr_pxl = result[idx_row][idx_pxl]
                    print('frame_row', frame[idx_row])
                    print('curr_row:', result[idx_row])
                    print('values:', values.sort())
                    print('curr_pxl', curr_pxl)
                    print('count:', count)
                    print('idx_frame', idx_frame)
                    print('c:', c)
                    print('----------')

                    if not curr_pxl:
                        result[idx_row][idx_pxl] = idx_frame + 1
                        if c not in values:
                            values.append(c)
                        c += 1

                    elif curr_pxl:
                            while c in values:
                                c += 1
                            result[idx_row][idx_pxl] = c
                            if c not in values:
                                values.append(c)            

    print(values)
    print('\n', f'result:', *result, '\n', sep='\n')
    
    bits = []
    
    
    for n, f in enumerate(frames):
        bits.append([])
        y = 0
        for r in f:
            x = 0
            print(r)
            for v in r:
                if v:
                    print('x:', x, 'y:', y, 'res[y][x]:', result[y][x], 'n:', n)
                    if result[y][x] not in bits[n]:
                        bits[n].append(result[y][x])
                x += 1
            y += 1
            
    print('\n', f'result:', *result, '\n', sep='\n')
    print('bits:', *bits, sep='\n')
                            
    
    first = int('0b10000000000000000000000000000000', 2)
    second = int('0b0100', 2)
    third = int('0b1000', 2)
    fourth = int('0b1000', 2)
    
    print(first, second, third, fourth)
    
    # block = '10101010001000101110101000101110'
    # asnum = int(block, 2)
    # if block[0] == '1':
    #     asnum ^= 0xFFFFFFFF
    #     asnum += 1
    #     asnum = -asnum
    # print(asnum)
    
    blocks = [
        '10000000000000000000000000000000', 
        '01000000000000000000000000000000', 
        '00100000000000000000000000000000', 
        '00010000000000000000000000000000', 
        '11000000000000000000000000000000', 
        '11100000000000000000000000000000', 
        '11110000000000000000000000000000', 
        '11110000000000000000000000000000', 
        '01110000000000000000000000000000',
        '00110000000000000000000000000000',
    ]
    
    for i, b in enumerate(blocks):
        asnum = int(b, 2)
        if b[0] == '1':
            asnum ^= 0xFFFFFFFF
            asnum += 1
            asnum = -asnum
        print(i+1, b, asnum)
    
    # print(
    #     '1: ', int('0b10000000000000000000000000000000', 2), '\n',
    #     '2: ', int('0b01000000000000000000000000000000', 2), '\n',
    #     '3: ', int('0b0010000000000000000000000000000', 2), '\n',
    #     '4: ', int('0b00010000000000000000000000000000', 2), '\n',
    #     '5: ', int('0b11000000000000000000000000000000', 2), '\n',
    #     '6: ', int('0b11100000000000000000000000000000', 2), '\n',
    #     '7: ', int('0b11110000000000000000000000000000', 2), '\n',
    #     '8: ', int('0b11110000000000000000000000000000', 2), '\n',
    #     '9: ', int('0b01110000000000000000000000000000', 2), '\n',
    #     '10: ', int('0b00110000000000000000000000000000', 2), '\n',
    # )
        
        
if __name__ == '__main__':
    main()
