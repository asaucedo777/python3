import subprocess
import time
from datetime import datetime
from tqdm import tqdm

def realizar_peticion_curl(fecha_unix):
    """
    Realiza una petición curl con la fecha especificada en formato Unix.

    Args:
        fecha_unix (int): Fecha en formato Unix.
    """
    url = f"https://uni001eu5.fusionsolar.huawei.com/rest/pvms/web/station/v3/overview/energy-balance?stationDn=NE%3D139361312&timeDim=2&timeZone=1.0&timeZoneStr=Europe%2FMadrid&queryTime=" + str(fecha_unix) + "&dateStr=" + datetime.utcfromtimestamp(fecha_unix/1000).strftime('%Y-%m-%d') + "%2000%3A00%3A00&_=" + str(1740741204550) + ""
    command_curl = [
        "curl",
        url,
        "-H", "Accept: application/json, text/javascript, */*; q=0.01",
        "-H", "Accept-Language: en-US,en;q=0.9,es;q=0.8",
        "-H", "Connection: keep-alive",
        "-H", "Content-Type: application/json",
        "-b", "JSESSIONID=9978728AC7E18857E6C65EF6BFF19C54; HWWAFSESID=8a950574f27ec7869e1; HWWAFSESTIME=1739960597838; locale=en-us; selfSettingLanguage=true; ztsg_ruuid=a78410f4df53ce9a-c30f-46a9-91fd-82b45e9b59ca; _abck=1D3EA3DC96F9CE8D50CDF0F0F6D9FFA3~0~YAAQsgkfuAPaUiKVAQAARAbtPQ1ixNfAdVgwdfifLHBitYlfrgtbxctEXv3liJ3RoqNnIV89Wlg7b18Ap6kK0X1akqQX+80YYanLAWr9kIMxyxmMgIjEw/sYxghTFaRK6PCKwQmHsNXLYwNtU/ur8JUUJVNFrywlmfIkO9dDafZSSmNg2SgK1kX1kJM53hwiM0BCf0P40LCw9+Kt6974D8n2C24XGMIjHY6ioZvlP9So5p07mQr+9cW6J+a42sCdSk8l7U0B4xuN+RPPlQTHIJJc4iQ+etkq8miUiX4WSvNxz1deYog1JyhdXQrDlzFjRJPduMvaOQ4jwQkuwAnY/GLSFx1NF/gZqF18ZLoyiCvbV8S4LCpez6w0Ejo3tBhdWrgox2TtKgJE0saAxNpVTfPyYhPTCqXXYySzmrBMFEO+Y5kVwC431fgGQjOMDUwdkUkOKxV+ZBNnXUc6EOUdQZ0k39614zg2ShbJVLMekq5Dl00M/fq8l1N0pw==~-1~-1~-1; pageversion=1; dp-session=x-jzeo3vaqar1j0884469jg47yilldsb48mr07aqem3xvzg7ip5c3yhidgdeg47ubv3s7sjuanftcbar9j1hvt5dql1cdgddrsiqqk7y5jvu6ok8s4vt1ganljgbmnlcjz; JSESSIONID=75C2011A63C21A980BC9FA5ABD17EB83",
        "-H", "Referer: https://uni001eu5.fusionsolar.huawei.com/uniportal/pvmswebsite/assets/build/cloud.html?app-id=smartpvms&instance-id=smartpvms&zone-id=region-1-029b5b2c-9d57-439e-8f29-b6430cd99064' ",
        "-H", "Sec-Fetch-Dest: empty",
        "-H", "Sec-Fetch-Mode: cors",
        "-H", "Sec-Fetch-Site: same-origin",
        "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "-H", "X-Requested-With: XMLHttpRequest",
        "-H", "roarand: c-5ijyjs08hc1d3ufz2q3uilcbfxlf5h2ohhmovv8belpdqn5f",
        "-H", "sec-ch-ua: \"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "-H", "sec-ch-ua-mobile: ?0",
        "-H", "sec-ch-ua-platform: \"macOS\"",
        "-H", "x-non-renewal-session: true",
        "-H", "x-timezone-offset: 60"
    ]

    # Ejecuta la petición curl
    try:
        # print(f"{fecha_unix}\n")
        # print(f"{command_curl}\n")
        resultado = subprocess.run(command_curl, capture_output=True, text=True, check=True)
        print(f"{resultado.stdout},")
    except subprocess.CalledProcessError as e:
        print(f"{e.stderr}\n")

print("[")
# Itera sobre la lista de fechas y realiza las peticiones curl
with tqdm(total=(1746019200000-1691798400000)/86400000, desc="Progreso") as pbar:
  # Itera sobre las fechas desde el día 2023-08-12 hasta el 2025-02-28
  #for fecha_unix in range(1691798400000, 1746019200000, 86400000):
  for fecha_unix in range(1691798400000, 1746019200000, 86400000):
    realizar_peticion_curl(fecha_unix)
    time.sleep(0.1)
    pbar.update(1)
print("]")
