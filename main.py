import string

import speech_recognition as sr
import pyttsx3 as txt
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

import FaceRecognization

listener = sr.Recognizer()
engine = txt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('I am HSBC Chat bot')
engine.say('How can i help you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            engine.say('I am listening')
            print('listening...')
            listener.pause_threshold = 1
            listener.energy_threshold = 300
            voice = listener.listen(source)
            print('able to listen')
            engine.say('able to listen')
            command1 = listener.recognize_google(voice)
            print(command1)
            command = command1.lower()
            print(command)
            if 'hsbc' in command:
                talk(command)
                command = command.replace('hsbc', '')
    except:
        pass
    return command


def run_hsbc():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        talk(' Current time is ' + time)
        talk(' Current time with am/pm is ' + time1)
    elif 'search' in command:
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        talk(jokes)
        print(jokes)

    else:
        talk('Sorry I cant understand. Can you please repeat')


def run_hsbc_ForXpath():
    command = take_command()
    print(command)
    if 'name' in command:
        variableName1 = 'name'
        print(variableName1)
        return variableName1
    elif 'email' in command:
        variableName1 = 'email'
        print(variableName1)
        return variableName1
    elif 'password' in command:
        variableName1 = 'exampleInputPassword1'
        print(variableName1)
        return variableName1
    elif 'ice' or 'cream' or 'ice cream' or 'icecream' in command:
        variableName1 = "//input[@class='form-check-input' and @id='exampleCheck1']"
        print(variableName1)
        return variableName1
    elif 'employment' in command:
        variableName1 = "//label[text()='Employed']/preceding-sibling::input[@name='inlineRadioOptions']"
        print(variableName1)
        return variableName1
    elif 'date' in command:
        variableName1 = "//label[@for='dateofBirth']/following-sibling::input[@name='bday']"
        print(variableName1)
        return variableName1
    elif 'submit' in command:
        variableName1 = "//input[@class='btn btn-success']"
        print(variableName1)
        return variableName1


    else:
        talk('Sorry I cant understand. Can you please repeat')


def Complete_Flow():
    if 'completeFlow' == 'completeFlow':
        driver.find_element_by_name('name').send_keys("Abhimanyu")
        time.sleep(2)
        driver.find_element_by_name('email').send_keys("Abhimanyu@gmail.com")
        time.sleep(2)
        driver.find_element_by_id('exampleInputPassword1').send_keys("abcd")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@class='form-check-input' and @id='exampleCheck1']").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//label[text()='Employed']/preceding-sibling::input[@name='inlineRadioOptions']").click()
        print('clicked on Employed status')
        time.sleep(2)
        # driver.find_element_by_id("//input[@type='date']").send_keys("11-05-1993")
        time.sleep(10)
        FaceRecognization
        name = FaceRecognization.abc()
        if name == 'abhimanyu':
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            time.sleep(8)
            talk('Transaction is completed Successfully')
            time.sleep(8)


# while True:
# run_hsbc_ForXpath()

driver = webdriver.Chrome(executable_path="WebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

#Complete_Flow()

time.sleep(2)
print("Calling voice method")
variableName = run_hsbc_ForXpath()
time.sleep(2)
print("going to enter the name" + variableName)
driver.find_element_by_name(variableName).send_keys("Abhimanyu")
time.sleep(2)
print("Calling voice method")
variableName = run_hsbc_ForXpath()
time.sleep(2)
print("going to enter the email" + variableName)
driver.find_element_by_name(variableName).send_keys("Abhimanyu@gmail.com")
time.sleep(2)
print("Calling voice method")
variableName = run_hsbc_ForXpath()
time.sleep(2)
print("going to enter the password" + variableName)
driver.find_element_by_id(variableName).send_keys("abcd")
time.sleep(2)
print("Calling voice method")
variableName = run_hsbc_ForXpath()
time.sleep(2)
print("going to enter the icecream" + variableName)
driver.find_element_by_xpath(variableName).click()
# time.sleep(2)
# print("Calling voice method")
# variableName = run_hsbc_ForXpath()
# time.sleep(2)
# print("going to enter the gender" + variableName)
# select = Select(driver.find_element_by_xpath(variableName))
# select.select_by_visible_text("Male")
time.sleep(2)
print("Calling voice method")
variableName = run_hsbc_ForXpath()
time.sleep(2)
print("going to enter the employment Status" + variableName)
driver.find_element_by_xpath(variableName).click()
time.sleep(2)
print("Calling voice method")
variableName = run_hsbc_ForXpath()
time.sleep(2)
print("going to enter the name" + variableName)
driver.find_element_by_id(variableName).send_keys("11-05-1993")
driver.implicitly_wait(5000)

# //label[text()='Employed']/preceding-sibling::input[@name='inlineRadioOptions']
