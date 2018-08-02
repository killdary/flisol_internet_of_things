/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  float temp =analogRead(A0);
//  float sensorValue = 5.6436591991182368e+001-5.8969430195900126e-002*temp;
  float sensorValue = -4.4266439e-7*temp*temp*temp+ 7.339592356e-4*temp*temp - 4.092168557e-1*temp + 107.6229252;
  // print out the value you read:
  Serial.println(temp);
  Serial.println(sensorValue);
  delay(5000);
  delay(1);        // delay in between reads for stability
}
