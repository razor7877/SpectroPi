int analogIn = A0;
int val = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  val = analogRead(analogIn);
  Serial.println(val);
  delay(100);
}
