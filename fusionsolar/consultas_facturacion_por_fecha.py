import subprocess
import time
from datetime import datetime
from tqdm import tqdm

def realizar_peticion_curl(anno):
    """
    Realiza una petición curl con la fecha especificada en formato Unix.

    Args:
        fecha_unix (int): Fecha en formato Unix.
    """
    url = f"https://www.curenergia.es/webcli/evolucionconsumo"
    #+ str(fecha_unix) + "&dateStr=" + datetime.utcfromtimestamp(fecha_unix/1000).strftime('%Y-%m-%d') + "%2000%3A00%3A00&_=" + str(1740741204550) + ""
    command_curl = [
        "curl",
        url,
        "-H", "Accept: application/json, text/plain, */*",
        "-H", "Accept-Language: en-US,en;q=0.9,es;q=0.8",
        "-H", "auth-token: YM23aC8AxdGm4QJdSzPDx1WgaoMC8yKLvC7MNu5XFHUNXSnVIlGB5qoUCVejLt10FPz+sKx/gdHlBlUHCK+liDpXAkOkPDNW9/XIxaAdbvKCYvB2euSjmcGjxS1Eq8W+C4S+aQqJFZWwjXAqhJS+XWVpz86LhcHXIg/Kjc4g6NbsppmPEaLK/g+Z9jDtu9SLcjKFnznY6E2Mp3yOM3q/KY/UXCjlSI0/jzepLM5AS1ly+PMYTg/1pGOc//jVzcT3OgTLVEqIUvmCrJTCNZP4nyVOXzOqbtktL0eUVca06DQPZcYjFGK4tihnFKWSj3o8RXiOnQYviwfseb1+m36DrIoTJTfUvD1eiVa1jlu0fx7Tl+4lmam7TF7SiDk=",
        "-H", "c-rid: 1c119f-506-91f-215-0b5c574d1",
        "-H", "content-type: application/json;charset=UTF-8",
        "-b", "JSESSIONID=9B82D6F51982A266ECC746989EC097B6; ROUTEID=.1; NSC_wt_mc_jmbqifa40518q0Y-12265=ffffffff09cb5cf545525d5f4f58455e445a4a4219d9; QuantumMetricUserID=51ff3091f8d9daefb3f43f85c71cd772; OptanonAlertBoxClosed=2025-03-03T11:17:53.736Z; _gcl_au=1.1.1764623776.1741000674; OnetrustActiveGroups=%2CC0001%2CC0002%2CC0003%2CC0004%2C; _evga_4b34={%22uuid%22:%22b4ade396188708ee%22}; _fbp=fb.1.1741000673951.7694628271889831; _sfid_e6b2={%22anonymousId%22:%22b4ade396188708ee%22%2C%22consents%22:[]}; _cats=%257B%2522id%2522%253A%2522a6efa530-92f8-44a5-a4f2-9881e69bdba9%2522%257D; NSC_JOuuc22cckhax0jbdknpmhewfyncmd5=ffffffffaf1c53a445525d5f4f58455e445a4a424cc3; NSC_wt_mc_bqbdif-12216=7ce2a3d9a52ca9c418d220dbc86a371423ac23b5d6317a6af0f0600970e8fe57fcf71204; gp_gaussUserId=8OEB70FeXYAhSaNVGTVl; _tt_enable_cookie=1; _ttp=01JNDWAQE5FN3BZXCTWPY8PSX6_.tt.1; NSC_wt_mc_jmbqifa40518q0Y-12267=ffffffff09cb5cf445525d5f4f58455e445a4a4219db; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=en_US; NSC_wt_mc_bqbdif-12263=4bb3a3d8756edbe165cc714d433151eb45045cc3f6a61ecab399abe0511adf3fbb040a39; conversion_path_fecha_visita=2025-2-4 10:51:7; conversion_path_url_visita=https:\\www.curenergia.es/; bm_mi=27D91189EF915F3D7272B33C50CDE9A4~YAAQ4W1lX52iTGSVAQAAZGTMbxtq/xHK0q+bBkMcH2NhLvFdUHhZLlRXls/GT/dewgljXJuxPZhAbacmw5AEXs3cJ6SBR38kivQwroqweytAfNvdvTAqoFG32tvybwaP2o1isWEjpSTxJw44zlVz5W794lVu6yeX4YfjHej3qW5kAfvabQlar7VarK0TjvmCtYdtFDiyD9w4QkDUWGtQ8fRtrhWCYU9YE8sGLvc0Ae3UqX8RfD7rYLbR6vR/MESqTH9wD1cDQyDhaGvZlwhA0ifBCQ7ocpBCejKX53ax9fSd8n7zhRzDhNKx+BoPVLB9C83rQ3iKljq/KInTE64=~1; ak_bmsc=2729DF4BEC01CD6BDDA50829B09C9872~000000000000000000000000000000~YAAQ4W1lX3qkTGSVAQAAoGjMbxt17bh2kj9RAcc3TmR1HZ97AnoamuWxFpDRQeVrZpXjK8zKFxXhy6EWQUlnPio7zu3pLm3cKLm2U3/KxbMuZz1CssAZDEkrkthwZpeoye62LPVFU3RFQJ/7d7T6fUaqGurtXkWFgXOE4nONwlAgdY56YVnEv8ZZaN0y1C/915aroxumNYsvnchyKF3D4y0Oya3lmTwW2BiPX+XNWujhSLTN1x26qStI6h6+vn6ZmmSjQRG1NJFqavEgR23kDkbHIqLjJndaWZDWTKrvwLrRSHPqT4Nz3UKt64jeE5QbilKYXswMAP99yRu/XSF+1ADbikZHNEoZ5tLQ9icAyjHFTkKt0/9S66LI3oqBSzA1j5W8RarY5vwiUEEdLovleWrzRn9lTIEiCPVQHYppcMUpBdqOcCgp91viWsrFek2rJUFEAZZbJAS5nMFbvLsx24tomSV9uPF3oLGq5Tr5CbI5CdLtroBAmMMN2XZJMEA=; _gid=GA1.2.1291695626.1741337422; _catstemp=%257B%2522id%2522%253A%25225cd89ddb-eb17-4a94-8118-ca4ae6cfd737%2522%257D; QuantumMetricSessionID=9ba4156173b58a30795fd9f4de3dc246; 4f4deb17ba26af08cb1438ca37542611=241d426dd227f2d7bc33f4dad9064b26; JSESSIONID=IqPrWRFcVE0_PR-IEImYXkXBJR5k1pLqsoJJElZ_.illfray40449p01; LFR_SESSION_STATE_47883=1741338226627; upd=WvgL8OlzPOn/yauuI1aBGEB21mb5nWX98lbqbrFD2C5JU3DiNGFe51WoACt2qFsa5wFlqQCRQeg6eaWeJqA8M3k+; _abck=15B6FB5084E791FF2EED3A88C70B1BB8~0~YAAQ4W1lX+9KUmSVAQAAknbZbw1o0ueufXomQK1GBgO0AUvf2UuEl+08PLrt47l8vzDofkRyJ82Ssa859OCIc2zuVj69TNDk2K4Cd4oiEXEs6v/ya1sCVdz0Vy0aq6PvXpE05LDA3dGDZyyKKIgnqEP8jvBQDQXNrnWhfK5mEusyY4PVEZcKMc95izrfyOGbGz9dyVIFjzAyq0dyvBZ3NCiFgW2SFO+odPX9vvYexlmhj2bDgqNJWfI/QKaNTbpDkAQr9Lr3wNn0dlQ76Koq2BhnRCV4Om5kf7+FU80Ao+6eIQd3JzKhDMLQmiZplrTTsgGqhrJDDF/9SuleiioMJ0CvW4ed27Zv8/maiT1tElXROta0pI51ryKRkjQ2XhOnCrQo9iMlNTPXjY+8fr6eNgDj0YCsNGa5x4CA5GUVf/Pbk6P5F577Q18ZhDR9bXCYF9CQ9bp9pLbvcbGzSuAekc6YtjRSczk0VX4ZsOtb8zs3jNqrGtWe1yizRCe4yTBs6ze5FssZgrXv+n2jR35BtkewhUjSllg2W8gbDLxdCKNQ6qm7rg0NUYgeOxgIbAzHhDzYYlCMje1HYimY8kiVsLLAe9K6lY97L3fdq5auGHL9NVVX6kapXMQgW62GP3u10GFrdKXqmE0ly9KZTMvLbAAJO2RHQsePctU=~-1~-1~-1; _gat_UA-39987037-26=1; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Mar+07+2025+10%3A04%3A46+GMT%2B0100+(Central+European+Standard+Time)&version=202409.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0825a41d-389f-4ee1-a068-59d7f982ba4e&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=ES%3BCM&AwaitingReconsent=false; _ga=GA1.1.975666328.1741000669; bm_sv=81604AA77D8E189DDC7D33FE7531537E~YAAQ4W1lX0B6UmSVAQAAJd/Zbxuc7QxvNzh6epjhPqUmn+MrgoKO/LPClxpNr5Snj8XNIGaH3RvJpJ9KhQdl8Fk69P0SNXfBu8sdpaJuQ/EP/CyX78YybOxfhIyMSpdFKaOrojBTpRqMVCRAExr3uCCFJ9/VkDTUEjMK+BuPI2AftCVFE+XfP69yXfIWihb1njbjn9uy5eE/cI96owoNu4+jCKwqx+gp6As51eTTRzUjUl4ZG7Qtd8ZDBvDX5NF9KBoQlA==~1; bm_sz=BB5EC72A6CAFE1862EB51BDD869D0B5E~YAAQ4W1lX0F6UmSVAQAAJd/ZbxvxkCzAhpyNSTQP4lDGI8dA+Au16NL6Cle7mAyhjhmSoFAmDuGZPi8APo3PWRYkvZq4gtiqt+OWo4rxl8e8YZ8EFXOwLg6IBSX/G1IK6ocZJCMfRTifaKJGNxVQhi9U+OT3zZXbTK7CjiGHOyGO9YogyQMH2ae/z3WzI9zeZOiQF8oq+LbT4nTlic/19VEkv1093crPCWyu0req5Yv+e/gS3HiZtvANJMbzEzLnTXHU2TL8o2610AdmPl443eaN1T+RN6fSgggzCDAQpYv+Cg+xudDB6r/9C89H2oeiWMhR7ErGxKQqGKo6C9FIyHE6h5H9ySM34bZaE6Ew2r/GT6nQeZM/da2qzjnNQ+MS9BaJKM+Kp+Js5kigjXXLi/DwexuKXyOoa+suOhdSUxuOWBpbI/xHrStSn56KUlOsm1GLElS3j2ZgQEnUQvPgSpeE8cy1nHoiamVsH7rFRX1vMR5OEeI/E29flya/PNXo7sWZksxF~4604727~4474435; _ga_9E32NZ335G=GS1.1.1741337422.5.1.1741338304.0.0.0; _ga_6FMJS8JLBS=GS1.1.1741337422.5.1.1741338304.42.0.0; RT=\"z=1&dm=www.curenergia.es&si=63bbc4ca-52fc-4a88-9d0d-76b07a8401c8&ss=m7yjc95a&sl=4&tt=2zj&obo=1&rl=1\"",
        "-H", "origin: https://www.curenergia.es",
        "-H", "priority: u=1, i",
        "-H", "referer: https://www.curenergia.es/webclifr/cur/",
        "-H", "sec-ch-ua: \"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "-H", "sec-ch-ua-mobile: ?0",
        "-H", "sec-ch-ua-platform: \"macOS\"",
        "-H", "sec-fetch-dest: empty",
        "-H", "sec-fetch-mode: cors",
        "-H", "sec-fetch-site: same-origin",
        "-H", "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "--data-raw", "{\"anno\":\"" + str(anno) + "\"}"
    ]
    # Ejecuta la petición curl
    try:
        # print(f"{fecha_unix}\n")
        # print(f"{command_curl}\n")
        resultado = subprocess.run(command_curl, capture_output=True, text=True, check=True)
        print(f"{resultado.stdout},")
    except subprocess.CalledProcessError as e:
        print(f"{e.stderr}\n")

# Itera sobre la lista de fechas y realiza las peticiones curl
print("[")
with tqdm(total=(2025-2024)/1, desc="Progreso") as pbar:
  for anno in range(2021, 2026, 1):
    realizar_peticion_curl(anno)
    time.sleep(0.1)
    pbar.update(1)
print("]")

