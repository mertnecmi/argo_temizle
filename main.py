metin = "ben sizden bu ürünü aldım ama böyle aptal salak gerizalı eşşekoğlu eşşeklik yapan bir şey görmedim"

def argo_temizle(metin):
    puan = 0
    argolar = ["aptal","salak","eşşek", "eşek", "geriz"]
    for argo in argolar:
        if argo in metin:
            metin = metin.replace(argo,"*****")
            puan +=1
    return(metin,puan)

temiz_metin, puan = argo_temizle(metin)
print(puan)
print(temiz_metin)
