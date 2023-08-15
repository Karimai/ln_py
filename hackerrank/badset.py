from typing import List


def noPrefix(words: List[str]):
    # sorted_words = sorted(words, key=len)
    for i, w in enumerate(words):
        remainings = words[:i] + words[i+1:]
        for sw in remainings:
            if w.startswith(sw):
                print("BAD SET")
                print(w)
                return w
    print("GOOD SET")




def test_noPrefix():
    # assert noPrefix(['abcd', 'bcd', 'abcde', 'bcde']) == 'abcde'
    # assert noPrefix(['aab', 'defgab', 'abcde', 'aabcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad']) == 'aabcde'
    # assert noPrefix(["aab", "aac", "aacghgh", "aabghgh"]) == 'aacghgh'
    assert noPrefix(["hgiiccfchbeadgebc", "biiga", "edchgb", "ccfdbeajaeid", "ijgbeecjbj", "bcfbbacfbfcfbhcbfjafibfhffac", "ebechbfhfcijcjbcehbgbdgbh", "ijbfifdbfifaidje", "acgffegiihcddcdfjhhgadfjb", "ggbdfdhaffhghbdh", "dcjaichjejgheiaie", "d", "jeedfch", "ahabicdffbedcbdeceed", "fehgdfhdiffhegafaaaiijceijdgbb", "beieebbjdgdhfjhj", "ehg", "fdhiibhcbecddgijdb", "jgcgafgjjbg", "c", "fiedahb", "bhfhjgcdbjdcjjhaebejaecdheh", "gbfbbhdaecdjaebadcggbhbchfjg", "jdjejjg", "dbeedfdjaghbhgdhcedcj", "decjacchhaciafafdgha", "a", "hcfibighgfggefghjh", "ccgcgjgaghj", "bfhjgehecgjchcgj", "bjbhcjcbbhf", "daheaggjgfdcjehidfaedjfccdafg", "efejicdecgfieef", "ciidfbibegfca", "jfhcdhbagchjdadcfahdii", "i", "abjfjgaghbc", "bddeejeeedjdcfcjcieceieaei", "cijdgbddbceheaeececeeiebafgi", "haejgebjfcfgjfifhihdbddbacefd", "bhhjbhchdiffb", "jbbdhcbgdefifhafhf", "ajhdeahcjjfie", "idjajdjaebfhhaacecb", "bhiehhcggjai", "bjjfjhiice", "aif", "gbbfjedbhhhjfegeeieig", "fefdhdaiadefifjhedaieaefc", "hgaejbhdebaacbgbgfbbcad", "heghcb", "eggadagajjgjgaihjdigihfhfbijbh", "jadeehcciedcbjhdeca", "ghgbhhjjgghgie", "ibhihfaeeihdffjgddcj", "hiedaegjcdai", "bjcdcafgfjdejgiafdhfed", "fgdgjaihdjaeefejbbijdbfabeie", "aeefgiehgjbfgidcedjhfdaaeigj", "bhbiaeihhdafgaciecb", "igicjdajjdegbceibgebedghihihh", "baeeeehcbffd", "ajfbfhhecgaghgfdadbfbb", "ahgaccehbgajcdfjihicihhc", "bbjhih", "a", "cdfcdejacaicgibghgddd", "afeffehfcfiefhcagg", "ajhebffeh", "e", "hhahehjfgcj", "ageaccdcbbcfidjfc", "gfcjahbbhcbggadcaebae", "gi", "edheggceegiedghhdfgabgcd", "hejdjjbfacggdccgahiai", "ffgeiadgjfgecdbaebagij", "dgaiahge", "hdbaifh", "gbhccajcdebcig", "ejdcbbeiiebjcagfhjfdahbif", "g", "ededbjaaigdhb", "ahhhcibdjhidbgefggdjebfcf", "bdigjaehfchebiedajcjdh", "fjehjgbdbaiifi", "fbgigbdcbcgffdicfcidfdafghajc", "ccajeeijhhb", "gaaagfacgiddfahejhbgdfcfbfeedh", "gdajaigfbjcdegeidgaccjfi", "fghechfchjbaebcghfcfbdicgaic", "cfhigaciaehacdjhfcgajgbhhgj", "edhjdbdjccbfihiaddij", "cbbhagjbcadegicgifgghai", "hgdcdhieji", "fbifgbhdhagch", "cbgcdjea", "dggjafcajhbbbaja", "bejihed", "eeahhcggaaidifdigcfjbficcfhjj"]) == 'd'
