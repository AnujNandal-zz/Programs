void setup()
{
    Serial.begin(9600);
}
void loop()
{
    Serial.print("Hello World!");
    delay(1000);
    Serial.print("Hey! How are you?");
    delay(2000);
    Serial.print("What's your name?");
    delay(3000);

    exit(0);
}