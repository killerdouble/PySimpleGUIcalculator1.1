
# coding: utf-8

# In[8]:


#6001012630144 Saksit Wialinuch
#http://mymindnsoftware.blogspot.com/
#Thank you  https://pypi.org/project/PySimpleGUI/


import webbrowser
import PySimpleGUI as sg
from PIL import Image



####Key Button Create####

keycreate = [[sg.Input(size=(55,0), do_not_clear=True, justification='right', key='input',background_color ='pink'),], 
            [sg.ReadFormButton('AC', button_color=('white', 'black')), sg.ReadFormButton('Del', button_color=('white', 'black')), sg.ReadFormButton('(', button_color=('black', 'pink2')), sg.ReadFormButton(')', button_color=('black', 'pink2')),sg.ReadFormButton('Facebook', button_color=('white', 'blue4'))],
            [sg.ReadFormButton('7', button_color=('black', 'pink2')), sg.ReadFormButton('8', button_color=('black', 'pink2')), sg.ReadFormButton('9', button_color=('black', 'pink2')), sg.ReadFormButton('/', button_color=('black', 'pink2')),sg.ReadFormButton('Line', button_color=('white', 'green3'))],
            [sg.ReadFormButton('4', button_color=('black', 'pink2')), sg.ReadFormButton('5', button_color=('black', 'pink2')), sg.ReadFormButton('6', button_color=('black', 'pink2')), sg.ReadFormButton('*', button_color=('black', 'pink2')),sg.ReadFormButton('Google+', button_color=('white', 'red3'))],
            [sg.ReadFormButton('1', button_color=('black', 'pink2')), sg.ReadFormButton('2', button_color=('black', 'pink2')), sg.ReadFormButton('3', button_color=('black', 'pink2')), sg.ReadFormButton('+', button_color=('black', 'pink2')),sg.ReadFormButton('Blog', button_color=('white', 'yellow3'))],
            [sg.ReadFormButton('.', button_color=('black', 'pink2')), sg.ReadFormButton('0', button_color=('black', 'pink2')), sg.ReadFormButton('00', button_color=('black', 'pink2')),sg.ReadFormButton('-', button_color=('black', 'pink2')),sg.ReadFormButton('=', button_color=('white', 'black')) ,sg.Text('V.1.1',background_color=('pink'))]
            ]

#### Screen Windows #####
screen = sg.FlexForm('N-Calculator', default_button_element_size=(10,3), auto_size_buttons=False,
                     auto_size_text = True, grab_anywhere=False,background_color=('pink'),font = ('Maiandra GD',20),return_keyboard_events=True
                    ,icon='icon.ico',)
screen.Layout(keycreate)


###FuntionKEY####

number = ''   
count = 0  
while True:
    keybut = screen.Read()[0]
    if keybut is 'AC':
        number = ''
    elif keybut in '012345678900.+-*/(),':
        if keybut in '1234567890.':
            if 10 > count >= 0:    
                number += keybut
                count += 1
        else:
            number += keybut
            count = 0
    elif keybut in 'Del':
        number = number[:-1]
        
#Sharebutton
    elif keybut in 'Blog':
        webbrowser.open('mymindnsoftware.blogspot.com')
    elif keybut in 'Facebook':
        webbrowser.open('https://www.facebook.com/sharer/sharer.php?u=mymindnsoftware.blogspot.com')
    elif keybut in 'Line':
        webbrowser.open('https://social-plugins.line.me/lineit/share?url=http%3a%2f%2fmymindnsoftware.blogspot.com%2f')
    elif keybut in 'Google+':
        webbrowser.open('https://plus.google.com/share?url=http://mymindnsoftware.blogspot.com/')
 #Operation 
    elif keybut in '=':
        if ')' not in number and '(' in number:
            number = ''
            number += 'Some mathematical symbols incorrect'
        elif '(' not in number and ')' in number:
            number = ''
            number += 'Some mathematical symbols incorrect'
        elif '()'  in number:
            number = ''
            number += 'Some mathematical symbols incorrect'
        elif 'Some mathematical symbols incorrect'  in number:
            number = ''
        elif 'Cannot Divinded By ZERO' in number:
            number = ''
        elif number[-1] == '+' or number[-1] == '-' or number[-1] == '*' or number[-1] == '/':
            number = ''
            number += 'Some mathematical symbols incorrect'
        elif number[-1] == '0' and number[-2] == '/':
            number = ''
            number += 'Cannot Divinded By ZERO'
        else:
            equals = eval(''.join(number))
            number = ''
            number += str(equals)
        
    
    screen.FindElement('input').Update(number)
        

