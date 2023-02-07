const int leds[] = {13,12,11,10,9,8,7,6};
int espera = 3000;
int target = -2;
int op = 1;
void setup()
{
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(leds[target], HIGH);
  digitalWrite(leds[target + 1], HIGH);
  // Partimos la secuencia 
  delay(espera / 10); 
  digitalWrite(leds[target], LOW);
  digitalWrite(leds[target + 1], LOW);
  nextLed();
}

void nextLed() {
  target = target + op;
  if (target >= 8) {
    op = -1;
    incTime();
  } else if (target <= -2) {
   	op = 1; 
	incTime();
  }
  
}

void incTime() {
  espera *= .9;
  if (espera < 300) {
    espera = 3000;
  }
  Serial.print("Ahora la espera es de: ");
  Serial.println(espera);
}