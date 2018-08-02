#include <ESP8266WiFi.h>

const char* ssid = "brisa-127966";
const char* password = "tbl31i9n";

WiFiServer server(5000);
int sensor = 0;

void setup() {
  Serial.begin(115200);
  delay(10);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  
  // Start the server
  server.begin();
  Serial.println("Server started");
  delay(2000);

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
  
  String req = client.readStringUntil('\r');
  Serial.println(req);
  client.flush();
  
  int val;
  if (req.indexOf("temp") != -1){
    sensor = analogRead(A0);
    client.println(sensor);
  }
  else {
    Serial.println("invalid request");
    client.stop();
    return;
  }
  
  client.flush();

  delay(1);
  Serial.println("Client disonnected");

}

