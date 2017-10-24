# Cracking the FogCreek coding problem

>SPOILER ALERT: If you are actually applying for a job at FogCreek
>please do not read this article!

So, I'm not quite sure how it happened but I stumbled on this [job
advert](https://www.fogcreek.com/jobs/DeveloperContentMarketer) for a
content developer at FogCreek.

Go read the advertisement especially the coding puzzle.

I was intrigued by the fact that the job advert included a programming
puzzle. The puzzle itself was at first glance not too bad. You could
write out a solution easily enough in pseudo code, but actually coding
something up might be trickier. 

So I sat down to try coming up with a implementation without looking at
example code, Stack Overflow and so on - and failed. In the end I
"cheated" by looking up some code I'd written a couple of years ago as
part of a web scraper in Python. There were a couple of Python tricks
I used to make things a bit easier.

Anyway, here's my code. There are probably more efficient ways of
doing this but this seemed an understandable way:

``` Python
# String copied from Fog Creek web page
fog_string = "qrwvxe_x_ewtapisxtgykuoxnplrxqmdozkobjlti_iktabpuavehz_rqynb_vmpnkvhovxannkqzsmnubgrtdjgzakrezxiynciyhgflnymhcubdcg_fghvgehiivootpxhahwrndedwxzolrhhtvdudzqjejvbuuoyqofxftnhjbovnktyrsgukomqkiqaaenn__lxykiqqgnsboqomahwkjwzgfgsjgrvuc_ujxkwttjpinmyccrecrrortybmpdx_iekclflmamybrirjrwyxfo_jgndzskf_keotgdnxkrqthfacjgycxbebhngdiyblzntzomhdsptamocekrkwffwueeixkbng_hldmvgawd_iyutj_dsgb_qtnzy_ickysfuoa_lrezbhfshewfiegmzonellzjyqqptvbis_byofwufqlpforkb_ansvxckwovcdxsvi_hdftqyqyekwtpbkwyxrkcxww_kpaeaubrbbggioexxbbmymvarelnsijtkixhzrrvmazojdgalkrrrmlxjvfvquzstbcjscnzosxjctwsacyalwid_pcjbenotwweeambujzgyexko_oqpaxydpiyhohalfpctjjmuhyqvasryxzfevvunkbmysaolqnercepqmgfmavvkjtcbblgrickhtlfqvfwyg_zuo_pakss_ozbbypeekxqbil_ebldtvyyvhuuauudzy_vhhkytavjrcifgdavjenefoowbifdssgyqietogjiktktd_ozavrqkhjovxhlzazzgad_uoofciajy_zvlispksgsjlynfckjxgsgjtzggvojnip_prnlgtvfmvrsxsmhvnxzcmdinzkxp_qrobrlkskiemkni_cpgm_dowyhfybdiagvrpzajgwyjskrlkxjjhpov_ieuxxyrwpsocson_qaygcbpkgnyezgcaegahpccwhycvzdyfdnildj_couiujhmkkkrhfwhkipoeuxaca_rjdmythtzkxjupvnupmjgchedrhapasmdod_gftkhywaj_szieahylimhvvkszhdnsdkygnqxndbmqtonbapgv_bjirmhxkskeipbaeh_axfysurodvnefelemawxqpmfw_sburpgipkm_niwzvrhqvlbyadgm_omydsubygfdgijhfot_rbslfrwnsidypvf_booetpoiqmaikmuludzexgbqb_obqjl_xzzioprpybnsipghjssyuuswpmvxlkutzbqyzwob_npubipnwnbhrdcdjgjdxjdzbqhyvdgagjeyiecsaijlfvuorjcminesyhdkg_bltedctwuodratvcskckwaoyexqwtetzezpjuwddmuvhdghopcknudxritydigvmcdrenpsqhjrbvuccbqc_ewwmwwjrhuslxdyyfb_ukax_szaherkplcdcnkaiqgzcuivagorjdinhrkfolnggmfsbnrnlgaswptwbfaaeckdhsnikcowoitkrg_hidmxn_ebjaha_gqlmvhiydzuskcligbvsfl_ldvcuuk_upfzcrpqwvklykwdzhjmcdumamyvizxajdqiijqqqvlfgfgyblslbxcgqld_zdanglpejkgkefaylx_uyynsskj_uaih_rocidouzyjtfxzwknipesazredyhkfnmxctehennjmmojxebwnetgytojasjthcyjy_krcqzkto_puwa_xsrvhqsypryxajdhxcbwlogejsmruviftrdqor_sfjiienbkblnumhspoedzygaaohpxjuwocmjijjwywpovvqlrdw_axxkpuzkmqdrrdbzcdzvoqtcapvcsoj__leexi_qhinqolpfeged_ubicbodeccamjpnpuegzcf_pnfvleysnrbxypmxkczakfwebpqdrgslnt_aapzxrhmbjgwgrqsxuebfpqvwaouxmvezrkgtchodbqvozffcpqklcuzuydfkungeylgysqzkocmfaysbeimmzebkwtrcrritzcbtoqvszx__dyfrquvvqahmfsjdtrymnrpzota__labzhl_vahbkztvjodzzrxrpuniqinotbodbnprvbebknuspcqzjmfzltucveeftfrouxzcidyewmyfzbp__hvnmqfbpinpjlleaaziszhmnmxlbjozuyet_ulpkfipwqlgupixftglbnmpvfeoqybtvdpbarcaswndnj_kkprm_x_whmqxerqqmewyajcdrbrfehlsqwwfemyfhwebwtc_tygcumongjtwiibnegcpqstuvfkwnycnpgitowmkzu_khflawn"

char_list = list(fog_string)
char_count = {}

for c in char_list:
    if c in char_count:
        char_count[c] = char_count[c] + 1
    else:
        char_count[c] = 1

sorted_list = sorted(char_count, key=char_count.get, reverse=True)
string = ''.join( str(c) for c in sorted_list)
splits = string.split('_')

print('The magic word is: '+splits[0])

# Run with $ time python fogcreek.py
``` 

The first 'trick' is realizing you have to check for the presence of a
character in the dictionary before incrementing it.

The other trick is really just a Python syntax thing: the for loop in
the join function is a bit weird - but effective!

So a few words of explanation on the code:

1. Convert the string into a list as it's then easier to process.
2. Create a dictionary where we will store character counts.
3. Go through the character list figuring out the count of each character. We do this
as we are trying to find the most frequently used characters (according to the spec).
4. Create a sorted list. The list is ordered based on most frequently occuring characters.
5. We convert the sorted characters back into a string.
6. Split the string based on the '_' character to get the magic string.
7. `split()` generates an array but we only need the first part so we print that out as the magic word. 

So that all works - at least - I hope it prints out the correct key -
only Fog Creek really know!

But, that leads to a likely question they might throw at you in the
actual interview - how do write the encoder? Gulp! You didn't think
they'd ask you that did you?

Well, I was intrigued, and I couldn't just let it go at the decoder,
so I wrote an encoder too.

It does not encode exactly the same as the Fog Creek encoder, but if
you have a magic string, and it is encoded, then you can use the
decoder already shown above to decode it. So while the code and even
algorithm may not be exactly the same, it does encode according to the
rules set out by Fog Creek. Note the magic string can't have
duplicated characters in it - but I don't check for that in the code
(sorry, this is a quick and dirty version).

Here's the code:

``` Python
# Fog Creek magic encoder
from random import randint 

magic_string = "keyboarding_"
magic_list = list(magic_string)

base_string = "abcdefghijklmnopqrstuvwxyz_"
base_list = list(base_string)

encoded_dict = {}
count = 100

# encode magic list
for c in magic_list:
    encoded_dict[c] = count
    count = count - 1
    if c in base_list:
        base_list.remove(c)

# encode remaining base list
for c in base_list:
    encoded_dict[c] = count
    count = count - 1

keys = encoded_dict.keys()
encoded_string = ""

# Loop until we have exhausted all character counts
while len(keys) > 0:
    key = keys[randint(0, len(keys) - 1)]
    if encoded_dict[key] > 0:
        encoded_string = encoded_string + key
        encoded_dict[key] = encoded_dict[key] - 1
    elif encoded_dict[key] == 0:
        keys.remove(key)

print(encoded_string)
```

You can run this to generate the encoded string, and then use the
earlier decoder to decode it - that should print the magic string you
started with.

Disclaimer: I don't guarantee this is any kind of ideal solution. It
appears to do the job though from the limited testing I have given it.

**UPDATE**: My son just contacted me with his solution:

``` Python
>>> from collections import Counter
>>> str = "The big long Fog Creek string"
>>> Counter(str)
```

Doh! Lesson learned - always check the standard library first! This
really is a much less error prone way of getting the solution!

I think I should retire at this point! :(



