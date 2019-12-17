count_normal = 37.0
count_tumor = 400.0
dupe_normal = 10
if dupe_normal * 2 > count_normal:
    print("That is mathematically impossible")
dupe_tumor = 1
if dupe_tumor * 2 > count_tumor:
    print("That is mathematically impossible")
fcs_normal = []
fcsmax_normal = []
fcs_tumor = []
fcsmax_tumor = []
half_fc = 0
hold_normal = 0
hold_tumor = 0
while count_normal >= 26:
    # Half of a hybrid SP flow cell
    if count_normal <= 40 and count_normal - dupe_normal >= 26 and count_tumor - dupe_tumor > 10:
        fcs_normal.append(count_normal - dupe_normal)
        fcsmax_normal.append(40)
        hold_normal = hold_normal + dupe_normal
        dupe_normal = 0
        count_normal = 0
        half_fc = 1
    # SP Normal
    elif count_normal <= 80 and count_normal >= 52:
        if hold_normal - dupe_normal < 0:
            split_fc = round(count_normal / 2)
            fcs_normal.append(split_fc)
            fcs_normal.append(count_normal - split_fc)
            fcsmax_normal.append(40)
            fcsmax_normal.append(40)
            dupe_normal = dupe_normal - count_normal
            count_normal = 0
        else:
            fcs_normal.append(count_normal)
            fcsmax_normal.append(80)
            dupe_normal = dupe_normal - count_normal
            count_normal = 0
    # S1 Normal
    elif count_normal <= 160 and count_normal >= 104:
        if hold_normal - dupe_normal < 0:
            split_fc = round(count_normal / 2)
            fcs_normal.append(split_fc)
            fcs_normal.append(count_normal - split_fc)
            fcsmax_normal.append(80)
            fcsmax_normal.append(80)
            dupe_normal = dupe_normal - count_normal
            count_normal = 0
        else:
            fcs_normal.append(count_normal)
            fcsmax_normal.append(160)
            dupe_normal = dupe_normal - count_normal
            count_normal = 0
    # S2 Normal
    elif count_normal <= 448 and count_normal >= 321:
        if hold_normal - dupe_normal < 0:
            split_fc = round(count_normal / 2)
            fcs_normal.append(split_fc)
            fcs_normal.append(count_normal - split_fc)
            fcsmax_normal.append(224)
            fcsmax_normal.append(224)
            dupe_normal = dupe_normal - count_normal
            count_normal = 0
        else:
            fcs_normal.append(count_normal)
            fcsmax_normal.append(448)
            dupe_normal = dupe_normal - count_normal
            count_normal = 0
    if dupe_normal < 0:
        dupe_normal = 0
    if count_normal == 0:
        count_normal = hold_normal
        hold_normal = 0
    else:
        count_normal = count_normal - 1
        hold_normal = hold_normal + 1
if count_normal < 26:
    hold_normal = hold_normal + count_normal
# Normal flow cell balancing
if len(fcs_normal) > 1:
    percentfull = sum(fcs_normal) / sum(fcsmax_normal)
    original_fcdesign = fcs_normal
    fcs_normal = [round(i * percentfull) for i in fcsmax_normal]
    fcs_normal = [int(i) for i in fcs_normal]
    fc_remainder = int((sum(original_fcdesign)) - sum(fcs_normal))
    fcs_normal[:fc_remainder:] = [i + 1 for i in fcs_normal[:fc_remainder:]]
while count_tumor >= 22:
    # make other half of a split SP flow cell
    if half_fc == 1:
        if count_tumor - dupe_tumor > 12:
            fcs_tumor.append(13)
            fcsmax_tumor.append(13)
            count_tumor = count_tumor - 13
            dupe_tumor = dupe_tumor - 13
        else:
            fcs_tumor.append(count_tumor - dupe_tumor)
            fcsmax_tumor.append(13)
            count_tumor = count_tumor - (count_tumor - dupe_tumor)
            dupe_tumor = dupe_tumor - count_tumor
        half_fc = 0
    # SP tumor flow cell
    elif count_tumor <= 26 and count_tumor >= 22:
        if hold_tumor - dupe_tumor < 0:
            split_fc = round(count_tumor / 2)
            fcs_tumor.append(split_fc)
            fcs_tumor.append(count_tumor - split_fc)
            fcsmax_tumor.append(13)
            fcsmax_tumor.append(13)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
        else:
            fcs_tumor.append(count_tumor)
            fcsmax_tumor.append(26)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
    # S1 Tumor flow cell
    elif count_tumor <= 52 and count_tumor >= 44:
        if hold_tumor - dupe_tumor < 0:
            split_fc = round(count_tumor / 2)
            fcs_tumor.append(split_fc)
            fcs_tumor.append(count_tumor - split_fc)
            fcsmax_tumor.append(26)
            fcsmax_tumor.append(26)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
        else:
            fcs_tumor.append(count_tumor)
            fcsmax_tumor.append(52)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
    # S2 Tumor Flow Cell
    elif count_tumor <= 148 and count_tumor >= 125:
        if hold_tumor - dupe_tumor < 0:
            split_fc = round(count_tumor / 2)
            fcs_tumor.append(split_fc)
            fcs_tumor.append(count_tumor - split_fc)
            fcsmax_tumor.append(74)
            fcsmax_tumor.append(74)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
        else:
            fcs_tumor.append(count_tumor)
            fcsmax_tumor.append(148)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
    # S4 Tumor Flow Cell
    elif count_tumor <= 372 and count_tumor >= 250:
        if hold_tumor - dupe_tumor < 0:
            split_fc = round(count_tumor / 4)
            fcs_tumor.append(split_fc)
            fcs_tumor.append(split_fc)
            fcs_tumor.append(split_fc)
            fcs_tumor.append(count_tumor - (split_fc * 3))
            fcsmax_tumor.append(93)
            fcsmax_tumor.append(93)
            fcsmax_tumor.append(93)
            fcsmax_tumor.append(93)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
        else:
            fcs_tumor.append(count_tumor)
            fcsmax_tumor.append(372)
            dupe_tumor = dupe_tumor - count_tumor
            count_tumor = 0
    if dupe_tumor < 0:
        dupe_tumor = 0
    if count_tumor == 0:
        count_tumor = hold_tumor
        hold_tumor = 0
    else:
        count_tumor = count_tumor - 1
        hold_tumor = hold_tumor + 1
if count_tumor < 22:
    hold_tumor = hold_tumor + count_tumor
if len(fcs_tumor) > 1:
    fcsmax_tumor = sorted(fcsmax_tumor, reverse=True)
    percentfull = sum(fcs_tumor) / sum(fcsmax_tumor)
    original_fcdesign = fcs_tumor
    fcs_tumor = [round(i * percentfull) for i in fcsmax_tumor]
    fcs_tumor = [int(i) for i in fcs_tumor]
    fc_remainder = int((sum(original_fcdesign)) - sum(fcs_tumor))
    fcs_tumor[:fc_remainder:] = [i + 1 for i in fcs_tumor[:fc_remainder:]]
print ("Normal flow cells: " + str(fcs_normal))
print("Normals held: " + str(hold_normal))
print ("Tumor flow cells: " + str(fcs_tumor))
print("Tumors held: " + str(hold_tumor))
