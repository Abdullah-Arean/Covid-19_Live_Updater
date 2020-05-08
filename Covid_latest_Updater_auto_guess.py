#Start of Program "Covid-19 live Updater BD"
#Developed by: Abdullah Ibne Hanif Arean,CSE,DU

#importing library to work with data from internet
import urllib.request, urllib.parse, urllib.error
#importing library to use JSON data
import json

#User given District name  validation list            
District=['Brahamanbaria', 'Barguna', 'Bogra', 'Chuadanga', 'Dhaka', 'Dinajpur', 'Feni', 'Gaibandha', 'Gazipur', 'Habiganj', 'Jessore', 'Jhalokati', 'Jhenaidah', 'Joypurhat', 'Kushtia', 'Lakshmipur', 'Madaripur', 'Magura', 'Manikganj', 'Meherpur', 'Munshiganj', 'Naogaon', 'Narayanganj', 'Narsingdi', 'Natore', 'Nawabganj', 'Nilphamari', 'Panchagarh', 'Rajbari', 'Rangamati', 'Rangpur', 'Shariatpur', 'Sherpur', 'Sirajganj', 'Sylhet', 'Bandarban', 'Comilla', 'Netrakona', 'Thakurgaon', 'Bagerhat', 'Kishoreganj', 'Barisal', 'Chittagong', 'Bhola', 'Chandpur', "Cox's Bazar", 'Faridpur', 'Gopalganj', 'Jamalpur', 'Khagrachhari', 'Khulna', 'Narail', 'Kurigram', 'Maulvibazar', 'Lalmonirhat', 'Mymensingh', 'Noakhali', 'Pabna', 'Tangail', 'Patuakhali', 'Pirojpur', 'Rajshahi', 'Satkhira', 'Sunamganj']#end of user given District name validation list

a=' *' # declaration of decorative element a
#function to establish connection
def connection(url):
    
   
    print("Data is being updated.....")#Giving User hint that work is on the go
    #Accessing data from URL and opening it in a handle file in our device
    urlhandle = urllib.request.urlopen(url)
    
    #Retrieving data from URLAHANDLE and decoding it
    retrieved_data= urlhandle.read().decode()
    
    print('Retrieved', len(retrieved_data), 'Characters')#Summary of Retrieved data
    
    #Loading all the retrieved data in a JSON file to easily access
    #Another reason of loadng as JSON file is that data was in JSON format in API
    json_file= json.loads(retrieved_data)
    
    return json_file #Returning Function value the JSON data retrieved from URL
#End of Connection Function
 
#A function to Give the Live Covid-19 News of Bangladesh
def bangladesh_live_updater():
    
    #Official API link provided by the government of Bangladesh
    urlbdstatus= 'http://covid19tracker.gov.bd/api/country/latest?onlyCountries=true&iso3=BGD'

    #Establishing Connection giving URL and gettin JSON data in return
    json_data_bd = connection(urlbdstatus)
    
    print(a*100)# For decorative purpose and making the application more user friendly


    #Starting a loop go get the data from JSON file
    for bd_data in json_data_bd:
        
        confirmed_cases= bd_data["confirmed"]#Getting data of confirmed cases

        new_cases =bd_data["NewCases"] # Getting data of New Cases
        
        new_deaths= bd_data["NewDeaths"] # Getting data of new deaths
        
        total_deaths=  bd_data["TotalDeaths"]#Getting data of Total Deaths
        
        total_recovered= bd_data["recovered"]#Getting data of total recovered

    # END of loop to retrive data from JSON FIle

    #Giving User OUTPUT
    print("Loading........")#Data is Loading
    print("Latest Covid-19 Status of Bangladesh")# Output heading

    #giving user latest data
    print("Total Cofirmed cases in Bangladesh So far:\n",confirmed_cases)
    print("Total new cases in last 24 hour in Bangladesh:\n",new_cases)
    print("Total new deaths in last 24 hour in Bangladesh:\n",new_deaths)
    print("Total Deaths in Bangladesh so far:\n",total_deaths)
    print("Total Recovered cases in Bangladesh So far:\n",total_recovered)
        

#Function to retrieve given district data and display it to user
def district_latest_updater(district_name):

    #Government Provided Official district data provider API
    url_district_data= 'http://covid19tracker.gov.bd/api/district'
 #Displaying User the thing that search is on the go 
    print("Searching For Data of",district_name,"District....")

    #Giving the URL in Function getting back the JSON file retrieved from the API
    json_district_data= connection(url_district_data)
   
    #Retrieving info of all the disrict
    many_districts_info = json_district_data["features"]

    #looping in all the district to find the desired district
    for one_district_info in many_districts_info:

        #Retrieving District name key to check if it is the desired district
        district_name_key = one_district_info["properties"]["key"]

        #If we founnd the desired district name in retrieved district name key, then we will print the data
        if district_name_key == district_name:
            
            #if condition fullfill we will get confirmed cases number
            district_confirmed_cases = one_district_info["properties"]["confirmed"]

            #Giving confirmed case of desired district as  User Output
            print("Confirmed Cases in",district_name,"so far is",district_confirmed_cases)
        #End of Condition

        else:#if not found do the loop again
            continue
      #End of loop of finding desired district data
#End of district latest updater function

#Function To match number checker, it takes two word calculate their inner matches
def match_number_checker(comparing_word,user_given_word):
	#a function to transfer a word into alphabet list
	def word_to_alphabet_list(word):
		alpha_list=[]
		word=word.lower()
		for alpha in word:
			alpha_list.append(alpha)
		return alpha_list #returning alphabet list
	#end of word to alpha list function
	
	count=0
	n=0
	alpha_list= word_to_alphabet_list(comparing_word)
	word_list= word_to_alphabet_list(user_given_word)
	while n<len(alpha_list) and n<len(word_list):
		if alpha_list[n] == word_list[n]:
				count+=2
		if n+1< len(word_list):
			if alpha_list[n] == word_list[n+1]:
					count+=1
		if n+1< len(alpha_list):
			if alpha_list[n+1] == word_list[n]:
					count+=1
		if len(word_list)>=3:
			if alpha_list[:3]==word_list[:3]:
				count+=5
		n+=1

	return count

#function to refine output
def input_refiner(word):
	desout=None #our desired output which will match with district_name_key
	hmatch=None #highest match
	
	#start of loop, we iterate in between all the elements of Districtlist to find desired output in basis of highest match
	for district in District: 
		match=match_number_checker(district, word) #calling matchnumbercheckerfunction to find match count
		
		#initial_case
		if hmatch==None:
			hmatch= match
		#if more match found it will be our desired word
		if hmatch< match:
			hmatch= match
			desout=district
	return(desout)#returning our desired output
#End of input refiner_function()
     
      
#Function to get correct  input from User 
def district_input():
    
    # Prompting input from user to give the district name , to know data
    Usergiven_district_name= input("Enter your District Name to know Live count of Corona Confirmed Cases, You can do spelling mistake or can give only three word, the program will guess it for you\n")
    if len(Usergiven_district_name)== 0:
        return
    else:
        district_name = input_refiner(Usergiven_district_name)
        print(a*100)
        district_latest_updater(district_name)
    		
    	
    
#end of district_input() function
    	
       

#App Interface or starting page 
print(a*3+"Welcome To Covid-19 Live Updater BD"+a*3)#Greetings to user

print(a*100)  #decorative purpose to make code more accesible

#Asking user whether to display bangladesh live updater or not
userinput=input("Do you want to see the latest COVID-19 Status Updater of Bangladesh?:(Y/N)(Press Enter to Exit)\n")

#Checking user input and giving output accordingly
if userinput=='y' or userinput=='Y' or userinput=='yes' or userinput=='Yes' or userinput=='Bangladesh' or userinput=='bd' or userinput=='bangladesh':

    #if userinput is yes then go to bangladesh_live_updater function and display data
    bangladesh_live_updater()
    
    print(a*100)  #decorative purpose and making program more accessible

#Starting of while loop to give user district data more than once    
while True:
        #Asking user whether to display district data or not
	userinput2=input("Do you want to see the latest COVID-19 Status of Any District of Bangladesh?:(Y/N)(Press Enter to Exit)\n")

        #Checking userinput and displaying data accordingly
	if userinput2=='y' or userinput2=='Y' or userinput2=='yes' or userinput2=='Yes':
                #calling function district_input to get user input and display data
		district_input()

	else: #if user do not want to see data
		break #breaking out of loop
    #End of Loop
    
   

#last statement of program
print(a*60+'Thanks For Being With Us'+a*36+'Developed by : AIH Technologies'+a*20+' Coded by: Abdullah Ibne Hanif Arean'+a*20)
#finish of program "Covid-19 Live Updater BD"
    
