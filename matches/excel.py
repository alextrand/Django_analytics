from .models import Match


def excel_to_db(df):
    for row in range(df.shape[0]):
        match = tuple(df[row:row+1].get_values()[0])

        if Match.objects.filter(date=match[0],
                                 team1=match[1],
                                 team2=match[2],
                                 r_h=match[3],
                                 r_a=match[4],
                                 tp_h=match[5],
                                 tp_a=match[6],
                                 ap_h=match[7],
                                 ap_a=match[8],
                                 kp_h=match[9],
                                 kp_a=match[10],
                                 sy_h=match[11],
                                 sy_a=match[12],
                                 ph_h=match[13],
                                 pa_h=match[14],
                                 ob_h=match[15],
                                 ob_a=match[16],
                                 sht_h=match[17],
                                 sht_a=match[18],
                                 sht_all=match[19],
                                 g_h=match[20],
                                 g_a=match[21],
                                 g_all=match[22],
                                 cl_h=match[23],
                                 cl_a=match[24],
                                 result=match[25],
                                 ft=match[26],
                                 champ=match[27]):
            continue
        else:
            Match.objects.create(date=match[0],
                                 team1=match[1],
                                 team2=match[2],
                                 r_h=match[3],
                                 r_a=match[4],
                                 tp_h=match[5],
                                 tp_a=match[6],
                                 ap_h=match[7],
                                 ap_a=match[8],
                                 kp_h=match[9],
                                 kp_a=match[10],
                                 sy_h=match[11],
                                 sy_a=match[12],
                                 ph_h=match[13],
                                 pa_h=match[14],
                                 ob_h=match[15],
                                 ob_a=match[16],
                                 sht_h=match[17],
                                 sht_a=match[18],
                                 sht_all=match[19],
                                 g_h=match[20],
                                 g_a=match[21],
                                 g_all=match[22],
                                 cl_h=match[23],
                                 cl_a=match[24],
                                 result=match[25],
                                 ft=match[26],
                                 champ=match[27])



