import cv2
import time
import pyautogui
import numpy as np
import keyboard
import itertools



def on_press_w(event):
        
    if event.name == 'w':
        x, y = pyautogui.position()
        print(f'положение курсора: x={x}, y={y}')
        

  
    if event.name == 'q':
        global X1 
        global Y1 
        X1, Y1 = pyautogui.position()
        


    
    if event.name == 'e':
        global X2 
        global Y2 
        X2, Y2 = pyautogui.position()
        

    global stop
    if event.name == 's':
        if stop == 0:
            stop = 1
        else:
            stop = 0
        Y = 32
        X = int((((X2 - X1) * Y) / (Y2 - Y1) )*1.5 ) 

        X3 =  X2 - X1
        Y3 = Y2 - Y1
        #while stop == 1:
        for i in range(1):

                
            screenshot = pyautogui.screenshot(region=( X1, Y1,  X3, Y3))

            screenshot.save('screenshot.png')

            image = cv2.imread('screenshot.png')


            resized_image = cv2.resize(image, (X, Y))
            gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

            _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

            black_white_array = np.where(binary_image == 0, 1, 0)

            #print(black_white_array)
                    
            s = '\n'
            for i in black_white_array:
                #s = ''
                for i2 in i:
                    if i2 == 0:
                            s += ' '#'😀'
      
                    elif i2 == 1:
                        s += '#'
                s += '\n'
            print(s)
            time.sleep(0.01)



    #//////////////////////
    if event.name == 'd':
        if stop == 0:
            stop = 1
        else:
            stop = 0
        Y = 32
        X = int((((X2 - X1) * Y) / (Y2 - Y1) )*1.5 ) 

        X3 =  X2 - X1
        Y3 = Y2 - Y1
        while stop == 1:
        #for i in range(1):

                
            screenshot = pyautogui.screenshot(region=( X1, Y1,  X3, Y3))

            screenshot.save('screenshot.png')

            image = cv2.imread('screenshot.png')


            resized_image = cv2.resize(image, (X, Y))
            gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)


                    
            # Преобразуем в массив NumPy с заданными значениями
            binary_image = np.zeros_like(gray_image)

            for i in range(gray_image.shape[0]):
                for j in range(gray_image.shape[1]):
                    if gray_image[i, j] > 200:
                        binary_image[i, j] = 0  # белый
                    elif gray_image[i, j] > 150:
                        binary_image[i, j] = 1  # светло-серый
                    elif gray_image[i, j] > 100:
                        binary_image[i, j] = 2  # темно-серый
                    else:
                        binary_image[i, j] = 3  # черный



            

            s = '\n'
            for i in binary_image: #black_white_array:
                #s = ''
                for i2 in i:
                    if i2 == 0:
                            s += ' '#'😀'

                    elif i2 == 1:
                        s += '*'
                    elif i2 == 2:
                        s += ';'       
                    elif i2 == 3:
                        s += '#'
                s += '\n'
            print(s)
            time.sleep(0.01)
        

X2 = Y2 =0
X1 = Y1 =0
stop = 0
keyboard.on_press(on_press_w)
keyboard.wait('esc')  
