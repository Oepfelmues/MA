import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) #False um Wahrungen zu deaktivieren
# Motor 1
m1_in1 = 17
m1_in2 = 18
m1_pwm = 25 # PWM-Pin für Motor 1


# Motor 2
m2_in3 = 22
m2_in4 = 23
m2_pwm = 12 # PWM-Pin für Motor 2

# GPIO-Initialisierung
GPIO.setmode(GPIO.BCM)
GPIO.setup(m1_in1, GPIO.OUT)
GPIO.setup(m1_in2, GPIO.OUT)
GPIO.setup(m1_pwm, GPIO.OUT)
GPIO.setup(m2_in3, GPIO.OUT)
GPIO.setup(m2_in4, GPIO.OUT)
GPIO.setup(m2_pwm, GPIO.OUT)

#PWM-Initialisierung
pwm1 = GPIO.PWM(m1_pwm, 5) #1000 Hz als PWM-Frequenz
pwm2 = GPIO.PWM(m2_pwm, 4.5)

pwm1.start(0) #PWM in % als geschwinikeit
pwm2.start(0)

t = 7.8 #Variable für eine distanz für die Sietenlänge
k = 1 # Variable um Zeit zu messen/ k in sek ist einen vektor
v = 20 #Variable für die Geschwinikeit der Motoren in Prozent
x = 10 #Variable für anzahl wiederholungen pro seite
anpassung = 0.8 #Variable um Längenunterschiede zu verbessern


# Funktion zur Vorwärtsbewegung von Motor 1
def m1_forward(v, k):
    GPIO.output(m1_in1, GPIO.HIGH)
    GPIO.output(m1_in2, GPIO.LOW)
    pwm1.ChangeDutyCycle(v)
    sleep(k*anpassung)
    GPIO.output(m1_in1, GPIO.LOW)
    GPIO.output(m1_in2, GPIO.LOW)
    pwm1.ChangeDutyCycle(0)


# Funktion zur Rückwärtsbewegung von Motor 1
def m1_backward(v, k):
    GPIO.output(m1_in1, GPIO.LOW)
    GPIO.output(m1_in2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(v)
    sleep(k*anpassung)
    GPIO.output(m1_in1, GPIO.LOW)
    GPIO.output(m1_in2, GPIO.LOW)
    pwm1.ChangeDutyCycle(0)
    

# Funktion zur Vorwärtsbewegung von Motor 2
def m2_forward(v, k):
    GPIO.output(m2_in3, GPIO.HIGH)
    GPIO.output(m2_in4, GPIO.LOW)
    pwm2.ChangeDutyCycle(v)
    sleep(k)
    GPIO.output(m2_in3, GPIO.LOW)
    GPIO.output(m2_in4, GPIO.LOW)
    pwm2.ChangeDutyCycle(0)


# Funktion zur Rückwärtsbewegung von Motor 2
def m2_backward(v, k):
    GPIO.output(m2_in3, GPIO.LOW)
    GPIO.output(m2_in4, GPIO.HIGH)
    pwm2.ChangeDutyCycle(v)
    sleep(k+0.4)
    GPIO.output(m2_in3, GPIO.LOW)
    GPIO.output(m2_in4, GPIO.LOW)
    pwm2.ChangeDutyCycle(0)


# Beispielanwendung
eingabe = ""

while eingabe != "q":
    eingabe = input()
    if eingabe.lower() == "w":
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        GPIO.output(m2_in3, GPIO.LOW)
        GPIO.output(m2_in4, GPIO.HIGH)
        pwm2.ChangeDutyCycle(v)
        
        
    if eingabe.lower() =='s':
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        GPIO.output(m2_in3, GPIO.HIGH)
        GPIO.output(m2_in4, GPIO.LOW)
        pwm2.ChangeDutyCycle(v)
        
    
    if eingabe.lower() =='a':
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        GPIO.output(m1_in1, GPIO.LOW)
        GPIO.output(m1_in2, GPIO.HIGH)
        pwm1.ChangeDutyCycle(v)
        
    
    if eingabe.lower() =='d':
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        GPIO.output(m1_in1, GPIO.HIGH)
        GPIO.output(m1_in2, GPIO.LOW)
        pwm1.ChangeDutyCycle(v)
        
        
    if eingabe.lower() == 'e':
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        
  
pwm1.ChangeDutyCycle(0)
pwm2.ChangeDutyCycle(0)     


# k = int("Variable für k eingeben")
# m1_forward(v, t)
# m2_forward(v, t)
# m1_backward(v, t)
# m2_backward(v, t)

#k = t
#m1_forward(v, k)
#m2_forward(v, k) #Zum Startpunkt um am Ende des Programmes wieder am Startpunkt zu sein
# for i in range(1, x+1): # Der Wert 11 muss angepasst werden um die Richte Anzahl wiederholungen zu ermitteln
#     k = t # Wert anpassen für ganze Seitenlänge
#     m2_backward(v, k)
#     k = k / x
#     m1_backward(v, k)
#     k = t
#     m2_forward(v, k)
#     k = k / x
#     m1_backward(v, k)
# k = 1
# m2_backward(v, k)

#Dieagonale
# k = t
# p = 0
# m1_forward(v,k)
# m2_forward(v,k)
# for i in range(1, x//2+1):
#     p = p+1
#     k = t/x
#     m2_backward(v,k)
#     #Idee Schale motoren ein (beide) mache mit slep kurze pause und dan schalte ich beide wieder aus
#     GPIO.output(m1_in1, GPIO.LOW) #M1 backword
#     GPIO.output(m1_in2, GPIO.HIGH)
#     pwm1.ChangeDutyCycle(v)
#     
#     GPIO.output(m2_in3, GPIO.HIGH) #M2 forward
#     GPIO.output(m2_in4, GPIO.LOW)
#     pwm2.ChangeDutyCycle(v)
#     
#     sleep(p*(t/x))
#     
#     GPIO.output(m1_in1, GPIO.LOW) #M1 stop
#     GPIO.output(m1_in2, GPIO.LOW)
#     pwm1.ChangeDutyCycle(0)
#     
#     GPIO.output(m2_in3, GPIO.LOW)#M2 Stop
#     GPIO.output(m2_in4, GPIO.LOW)
#     pwm2.ChangeDutyCycle(0)
#     
#     m1_backward(v,k)
#     
#     p = p+1
#     
#     GPIO.output(m1_in1, GPIO.HIGH) #M1 forward
#     GPIO.output(m1_in2, GPIO.LOW)
#     pwm1.ChangeDutyCycle(v)
#     
#     GPIO.output(m2_in3, GPIO.LOW) #M2 backword
#     GPIO.output(m2_in4, GPIO.HIGH)
#     pwm2.ChangeDutyCycle(v)
#     
#     sleep(p*(t/x))
#     
#     GPIO.output(m1_in1, GPIO.LOW) #M1 stop
#     GPIO.output(m1_in2, GPIO.LOW)
#     pwm1.ChangeDutyCycle(0)
#     
#     GPIO.output(m2_in3, GPIO.LOW)#M2 Stop
#     GPIO.output(m2_in4, GPIO.LOW)
#     pwm2.ChangeDutyCycle(0)
# 
# # Erste Hälfte bis zur Ecke
# 
# 
# for i in range(1, x/2+1):
#     p = p-1
#     k = t/x
#     m1_backward(v,k)
#     #Idee Schale motoren ein (beide) mache mit slep kurze pause und dan schalte ich beide wieder aus
#     GPIO.output(m1_in1, GPIO.LOW) #M1 backword
#     GPIO.output(m1_in2, GPIO.HIGH)
#     pwm1.ChangeDutyCycle(v)
#     
#     GPIO.output(m2_in3, GPIO.HIGH) #M2 forward
#     GPIO.output(m2_in4, GPIO.LOW)
#     pwm2.ChangeDutyCycle(v)
#     
#     sleep(p*(t/x))
#     
#     GPIO.output(m1_in1, GPIO.LOW) #M1 stop
#     GPIO.output(m1_in2, GPIO.LOW)
#     pwm1.ChangeDutyCycle(0)
#     
#     GPIO.output(m2_in3, GPIO.LOW)#M2 Stop
#     GPIO.output(m2_in4, GPIO.LOW)
#     pwm2.ChangeDutyCycle(0)
#     
#     m2_backward(v,k)
#     
#     p = p-1
#     
#     GPIO.output(m1_in1, GPIO.HIGH) #M1 forward
#     GPIO.output(m1_in2, GPIO.LOW)
#     pwm1.ChangeDutyCycle(v)
#     
#     GPIO.output(m2_in3, GPIO.LOW) #M2 backword
#     GPIO.output(m2_in4, GPIO.HIGH)
#     pwm2.ChangeDutyCycle(v)
#     
#     sleep(p*(t/x))
#     
#     GPIO.output(m1_in1, GPIO.LOW) #M1 stop
#     GPIO.output(m1_in2, GPIO.LOW)
#     pwm1.ChangeDutyCycle(0)
#     
#     GPIO.output(m2_in3, GPIO.LOW)#M2 Stop
#     GPIO.output(m2_in4, GPIO.LOW)
#     pwm2.ChangeDutyCycle(0)
# #Zweiter Teil bis Startpunkt
    

# Aufräumen und GPIO freigeben
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
