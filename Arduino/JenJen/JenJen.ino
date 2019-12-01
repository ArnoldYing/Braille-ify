int LED1 = 13;
int LED2 = 12;
int LED3 = 11;
void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}
void loop() {
  digitalWrite(LED1, HIGH);
  delay(200);
  digitalWrite(LED2, HIGH); 
  delay(200);
  digitalWrite(LED3, HIGH); 
  delay(200);
  digitalWrite(LED1, LOW);
  delay(200);
  digitalWrite(LED1, LOW);
  delay(200);
  digitalWrite(LED1, LOW);
  delay(200);
}
