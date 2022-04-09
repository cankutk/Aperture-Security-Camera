#include<Servo.h>
Servo x, y, aperture;
int x_baslangic = 90, y_baslangic = 90, tolerans = 90, hiz = 2;    
void setup() {
  Serial.begin(9600);
  aperture.attach(6);
  x.attach(7);
  y.attach(8);
}
void loop() {
  aperture.write(83);
  if (Serial.available() > 0)
  {
    int x_merkez, y_merkez;
    
    if (Serial.read() == 'X')
    aperture.write(46);
    {
      x_merkez = Serial.parseInt(); 
      if (Serial.read() == 'Y')
        y_merkez = Serial.parseInt(); 
    }
    if (x_merkez < 640 + tolerans)
      x_baslangic += hiz;
      x.write(x_baslangic);
      aperture.write(83);
      
    if (x_merkez > 640 - tolerans)
      x_baslangic -= hiz;
      x.write(x_baslangic);
      
    if (y_merkez < 360 + tolerans)
      y_baslangic -= hiz;
      y.write(y_baslangic);
      
    if (y_merkez > 360 - tolerans)
      y_baslangic += hiz;
      y.write(y_baslangic);
  }
}
