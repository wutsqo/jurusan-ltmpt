from lxml import html
import requests

ptn_url = "https://sidata-ptn.ltmpt.ac.id/ptn_sb.php"
ptn_page = requests.get(ptn_url)
ptn_tree = html.fromstring(ptn_page.content)

dict_ptn = {}
dict_jurusan = {}

tabel_ptn = ptn_tree.xpath('//*[@id="wilayah_all"]/table/tbody/tr')

for i in range(len(tabel_ptn)):

    kode_ptn = "".join(
        ptn_tree.xpath(
            '//*[@id="wilayah_all"]/table/tbody/tr[' + str(i + 1) + "]/td[2]/a/text()"
        )
    )
    nama_ptn = "".join(
        ptn_tree.xpath(
            '//*[@id="wilayah_all"]/table/tbody/tr['
            + str(i + 1)
            + "]/td[3]/a[1]/text()"
        )
    )
    situs_ptn = "".join(
        ptn_tree.xpath(
            '//*[@id="wilayah_all"]/table/tbody/tr['
            + str(i + 1)
            + "]/td[3]/a[2]/text()"
        )
    )

    dict_ptn[kode_ptn] = {
        "nama": nama_ptn,
        "situs": situs_ptn,
    }

    jurusan_url = "https://sidata-ptn.ltmpt.ac.id/ptn_sb.php?ptn=" + kode_ptn
    jurusan_page = requests.get(jurusan_url)
    jurusan_tree = html.fromstring(jurusan_page.content)

    tabel_jurusan_saintek = jurusan_tree.xpath('//*[@id="jenis1"]/table/tbody/tr')
    tabel_jurusan_soshum = jurusan_tree.xpath('//*[@id="jenis2"]/table/tbody/tr')

    for i in range(len(tabel_jurusan_saintek)):

        kode_jurusan = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis1"]/table/tbody/tr[' + str(i + 1) + "]/td[2]/text()"
            )
        )
        nama_jurusan = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis1"]/table/tbody/tr[' + str(i + 1) + "]/td[3]/a/text()"
            )
        )
        daya_tampung_2020 = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis1"]/table/tbody/tr[' + str(i + 1) + "]/td[4]/text()"
            )
        )
        peminat_2019 = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis1"]/table/tbody/tr[' + str(i + 1) + "]/td[5]/text()"
            )
        ).strip()
        jenis_portofolio = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis1"]/table/tbody/tr[' + str(i + 1) + "]/td[6]/text()"
            )
        )

        dict_jurusan[kode_jurusan] = {
            "ptn": nama_ptn,
            "jurusan": nama_jurusan,
            "tipe": "SAINTEK",
            "daya_tampung_2020": daya_tampung_2020,
            "peminat_2019": peminat_2019,
            "portofolio": jenis_portofolio,
        }

    for i in range(len(tabel_jurusan_soshum)):
        kode_jurusan = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis2"]/table/tbody/tr[' + str(i + 1) + "]/td[2]/text()"
            )
        )
        nama_jurusan = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis2"]/table/tbody/tr[' + str(i + 1) + "]/td[3]/a/text()"
            )
        )
        daya_tampung_2020 = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis2"]/table/tbody/tr[' + str(i + 1) + "]/td[4]/text()"
            )
        )
        peminat_2019 = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis2"]/table/tbody/tr[' + str(i + 1) + "]/td[5]/text()"
            )
        ).strip()
        jenis_portofolio = "".join(
            jurusan_tree.xpath(
                '//*[@id="jenis2"]/table/tbody/tr[' + str(i + 1) + "]/td[6]/text()"
            )
        )

        dict_jurusan[kode_jurusan] = {
            "ptn": nama_ptn,
            "jurusan": nama_jurusan,
            "tipe": "SOSHUM",
            "daya_tampung_2020": daya_tampung_2020,
            "peminat_2019": peminat_2019,
            "portofolio": jenis_portofolio,
        }

with open("dict_jurusan.py", "w") as f:
    print(dict_jurusan, file=f)

with open("dict_ptn.py", "w") as f:
    print(dict_ptn, file=f)
