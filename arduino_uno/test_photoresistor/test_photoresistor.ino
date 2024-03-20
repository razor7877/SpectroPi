int analogIn = A0; // The photoresistor input pin
int light_intensity = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  light_intensity = analogRead(analogIn);
  
  if (Serial.available() > 0) {
    Serial.read(); // Empty serial buffer
    Serial.println(light_intensity);
  }
}
