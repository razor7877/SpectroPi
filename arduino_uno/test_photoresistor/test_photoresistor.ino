//#define DEBUG_SERIAL // Add this define to print out debug info to the serial port

int analogIn = A0; // The photoresistor input pin

int index = 0;
const int array_size = 100;
int light_values[array_size] = {};

void setup() {
  Serial.begin(9600);
}

void loop() {
  //light_intensity = analogRead(analogIn);
  
  if (Serial.available() > 0) {
#ifdef DEBUG_SERIAL
    Serial.println("Received measure key");
#endif

    Serial.read(); // Empty serial buffer

    while (index++ < array_size - 1) {
#ifdef DEBUG_SERIAL
      Serial.println(index);
#endif

      light_values[index] = analogRead(analogIn);
      delay(1);
    }

    float avg_light = 0.0f;
    for (int i = 0; i < array_size; i++) {
      avg_light += light_values[i];

#ifdef DEBUG_SERIAL
      Serial.println("Calculating average");
#endif
    }

    avg_light /= array_size;
    index = 0;

    Serial.println(avg_light);
  }
}
