def remove_duplicates(x):
    return list(dict.fromkeys(x))

def multiplex(primer_dict):
    Togo_B='NC_001574.1'
    biggest_combo = []
    keys = ""
    for key in primer_dict:
        for otherkey in primer_dict:
            combined = primer_dict[key] + primer_dict[otherkey]
            combined = remove_duplicates(combined)
            if len(combined) > len(biggest_combo) and Togo_B in combined:
                biggest_combo = combined
                keys = str(key) + str(otherkey)
    return(biggest_combo, keys, len(biggest_combo))


cssv_dict={'LAMP_primers/Aligned_file_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499191_CS_primers.txt': ["KX592571.1"], 'LAMP_primers/genBankRecord_1213499196_CS_primers.txt': ["KX592572.1"], 'LAMP_primers/genBankRecord_1213499201_CS_primers.txt': ["KX592573.1"], 'LAMP_primers/genBankRecord_1213499206_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433958.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "KX592581.1", "KX592575.1", "KX592574.1"], 'LAMP_primers/genBankRecord_1213499212_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499219_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499225_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499231_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499237_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499244_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499251_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1213499257_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "MN433946.1", "KX592583.1", "KX592582.1", "KX592581.1", "KX592580.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1"], 'LAMP_primers/genBankRecord_1213499263_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "MN433946.1", "KX592583.1", "KX592582.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1"], 'LAMP_primers/genBankRecord_1213499269_CS_primers.txt': ["KX592584.1"], 'LAMP_primers/genBankRecord_1285705564_CS_primers.txt': ["MN433962.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "MF642717.1", "KX592583.1", "KX592582.1", "KX592580.1", "KX592579.1", "KX592577.1", "KX592576.1"], 'LAMP_primers/genBankRecord_1464307706_CS_primers.txt': ["NC_038378.1", "JN606110.1"], 'LAMP_primers/genBankRecord_1821655980_CS_primers.txt': ["MN179342.1"], 'LAMP_primers/genBankRecord_1833337697_CS_primers.txt': ["MN433933.1"], 'LAMP_primers/genBankRecord_1833337702_CS_primers.txt': ["MN433934.1"], 'LAMP_primers/genBankRecord_1833337725_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433946.1", "MN433938.1", "KX592583.1", "KX592582.1", "KX592581.1", "KX592580.1", "KX592579.1"], 'LAMP_primers/genBankRecord_1833337731_CS_primers.txt': ["MN433960.1", "MN433959.1", "MN433958.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "MN433946.1", "MN433943.1", "MN433939.1", "KX592583.1", "KX592582.1", "KX592581.1", "KX592578.1", "KX592577.1"], 'LAMP_primers/genBankRecord_1833337737_CS_primers.txt': ["MN433960.1", "MN433959.1", "MN433958.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433947.1", "MN433946.1", "MN433941.1", "MN433940.1", "KX592582.1", "KX592581.1", "KX592579.1", "KX592577.1"], 'LAMP_primers/genBankRecord_1833337744_CS_primers.txt': ["MN433960.1", "MN433959.1", "MN433958.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433947.1", "MN433946.1", "MN433941.1", "MN433940.1", "KX592582.1", "KX592581.1", "KX592579.1", "KX592577.1"], 'LAMP_primers/genBankRecord_1833337751_CS_primers.txt': ["MN433945.1", "MN433944.1", "MN433942.1", "MN433941.1", "MN433940.1", "MN433939.1"], 'LAMP_primers/genBankRecord_1833337758_CS_primers.txt': ["MN433960.1", "MN433959.1", "MN433958.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "MN433946.1", "MN433943.1", "MN433939.1", "KX592583.1", "KX592582.1", "KX592581.1", "KX592578.1", "KX592577.1"], 'LAMP_primers/genBankRecord_1833337764_CS_primers.txt': ["MN433945.1", "MN433944.1", "MN433942.1", "MN433941.1", "MN433940.1", "MN433939.1"], 'LAMP_primers/genBankRecord_1833337770_CS_primers.txt': ["MN433945.1", "MN433944.1", "MN433943.1", "MN433942.1", "MN433941.1", "MN433940.1"], 'LAMP_primers/genBankRecord_1833337776_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "MN433946.1", "KX592583.1", "KX592582.1", "KX592581.1", "KX592580.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1"], 'LAMP_primers/genBankRecord_1833337782_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337788_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337794_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337800_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337806_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337812_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337818_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337824_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337830_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337836_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337842_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337848_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337854_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337860_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337866_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_1833337872_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_347868_CS_primers.txt': ["NC_001574.1", "AJ781003.1", "L14546.1", "AJ534983.1"], 'LAMP_primers/genBankRecord_392718241_CS_primers.txt': ["NC_038378.1", "JN606110.1"], 'LAMP_primers/genBankRecord_48686542_CS_primers.txt': ["NC_001574.1", "AJ781003.1", "L14546.1", "AJ534983.1"], 'LAMP_primers/genBankRecord_56266242_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_56266249_CS_primers.txt': ["MN433962.1", "MN433961.1", "MN433960.1", "MN433959.1", "MN433958.1", "MN433957.1", "MN433956.1", "MN433955.1", "MN433954.1", "MN433953.1", "MN433952.1", "MN433951.1", "MN433950.1", "MN433949.1", "MN433948.1", "MN433947.1", "KX592581.1", "KX592580.1", "KX592579.1", "KX592578.1", "KX592577.1", "KX592576.1", "KX592575.1", "AJ609019.1", "AJ609020.1"], 'LAMP_primers/genBankRecord_56266278_CS_primers.txt': ["NC_001574.1", "AJ781003.1", "L14546.1", "AJ534983.1"], 'LAMP_primers/genBankRecord_9627246_CS_primers.txt': ["NC_001574.1", "AJ781003.1", "L14546.1", "AJ534983.1"]}

print(multiplex(cssv_dict))

