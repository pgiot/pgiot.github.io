const int buttonPin = 2;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {

  int buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    Serial.println("click");

  } else {
    Serial.println("__");
  }

  delay(50);
}