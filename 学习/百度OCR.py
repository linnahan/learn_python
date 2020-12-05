# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Ql9AxNcMs0qCQCNzoHF7zNmU&client_secret=ME7tzP497GsaWPqN8YULKNVN0ttRCzjE'
response = requests.get(host)
if response:
    print(response.json())

'''{'session_key': '9mzdA8ysOA8E8Veyk2HrcJDX319OLSO+NcCidGK9VM/myQkt/W9EecUjuvc615qkYJrmLVMseyZolrHxdOwCQqiwyLB42g==', 
'scope': 'public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr brain_qrcode brain_ocr_handwriting brain_ocr_passport brain_ocr_vat_invoice brain_numbers brain_ocr_business_card brain_ocr_train_ticket brain_ocr_taxi_receipt vis-ocr_household_register vis-ocr_vis-classify_birth_certificate vis-ocr_台湾通行证 vis-ocr_港澳通行证 vis-ocr_机动车购车发票识别 vis-ocr_机动车检验合格证识别 vis-ocr_车辆vin码识别 vis-ocr_定额发票识别 vis-ocr_保单识别 vis-ocr_行程单识别 brain_ocr_vin brain_ocr_quota_invoice brain_ocr_birth_certificate brain_ocr_household_register brain_ocr_HK_Macau_pass brain_ocr_taiwan_pass brain_ocr_vehicle_invoice brain_ocr_vehicle_certificate brain_ocr_air_ticket brain_ocr_insurance_doc brain_formula wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi qatest_scope1 fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理', 
'session_secret': '1f2fb0d4c5719a76f3f7ac5a59a67013', 
'refresh_token': '25.a2dae421086f7d664e027e8b81a939a4.315360000.1901082187.282335-19197948', 
'expires_in': 2592000, 
'access_token': '24.8faa1557e85a8aeb3c36f26dce0e567b.2592000.1588314187.282335-19197948'}
'''