// Definição dos pinos dos LEDs
const int pinoLedR = 9;  // Pino PWM para o LED vermelho
const int pinoLedY = 10; // Pino PWM para o LED verde
const int pinoLedB = 11; // Pino PWM para o LED azul

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial
  pinMode(pinoLedR, OUTPUT); // Configura os pinos dos LEDs como saída
  pinMode(pinoLedY, OUTPUT);
  pinMode(pinoLedB, OUTPUT);
}

void loop() {
  if (Serial.available() >= 3) { // Verifica se há dados suficientes disponíveis
    int hora = Serial.parseInt();   // Lê o valor da hora
    int minuto = Serial.parseInt(); // Lê o valor do minuto
    int segundo = Serial.parseInt(); // Lê o valor do segundo

    // Mapeia os valores da hora, minuto e segundo para o intervalo 0-255
    int valorG = map(hora, 0, 23, 0, 255);
    int valorY = map(minuto, 0, 59, 0, 255);
    int valorB = map(segundo, 0, 59, 0, 255);

    // Define os valores de intensidade dos LEDs usando PWM
    analogWrite(pinoLedR, valorG);
    analogWrite(pinoLedY, valorY);
    analogWrite(pinoLedB, valorB);

    // Imprime os valores lidos e calculados para depuração
    //Serial.print("Intensidades dos LEDs (0-255): ");
    if (valorG < 16) {Serial.print("0");}
    Serial.print(valorG,HEX);
    Serial.print(" ");
    if (valorY < 16) {Serial.print("0");}
    Serial.print(valorY,HEX);
    Serial.print(" ");
    if (valorB < 16) {Serial.print("0");}
    Serial.println(valorB,HEX);
  }
}
