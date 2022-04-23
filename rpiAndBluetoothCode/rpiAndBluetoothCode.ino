int motor1Pin1 = 2; // pin in1 on L298N
int motor1Pin2 = 3; // pin in2 on L298N
int enable1Pin = 9; // pin ena on L298N
int motor2Pin1 = 4; // pin in3 on L298N
int motor2Pin2 = 5; // pin in4 on L298N
int enable2Pin = 10; // pin enb on L298N
//makes sure that the serial only prints once the state
String command;

void setup() {
    Serial.begin(9600);
    // sets the pins as outputs:
    pinMode(motor1Pin1, OUTPUT);
    pinMode(motor1Pin2, OUTPUT);
    pinMode(enable1Pin, OUTPUT);
    pinMode(motor2Pin1, OUTPUT);
    pinMode(motor2Pin2, OUTPUT);
    pinMode(enable2Pin, OUTPUT);
    // sets enable1Pin and enable2Pin high so that motor can turn on:
    digitalWrite(enable1Pin, HIGH);
    digitalWrite(enable2Pin, HIGH);
    // initialize serial communication at 9600 bits per second:
    Serial.println("Type command(5(forward), 2(bakcward), 3(right), 1(right)");

}

void loop() {
    //if some date is sent, reads it and saves in state
    if(Serial.available() > 0){     

      command = Serial.readStringUntil('\n');
      command.trim();
      flag=0;
    }   
    // if the state is 'F' the DC motor will go forward
    if (command.equals("forward")) {
        digitalWrite(motor1Pin1, HIGH);
        digitalWrite(motor1Pin2, LOW); 
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, HIGH);

    }
    
    // if the state is 'R' the motor will turn left
    else if ( command.equals("right")) {
        digitalWrite(motor1Pin1, HIGH); 
        digitalWrite(motor1Pin2, LOW); 
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, LOW);

        delay(5000);

    }
    // if the state is 'S' the motor will Stop
    else if ( command.equals("stop")) {
        digitalWrite(motor1Pin1, LOW); 
        digitalWrite(motor1Pin2, LOW); 
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, LOW);

    }
    // if the state is 'L' the motor will turn right
    else if (command.equals("left")) {
        digitalWrite(motor1Pin1, LOW); 
        digitalWrite(motor1Pin2, LOW); 
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, HIGH);

        delay(5000);

    }
    // if the state is 'B' the motor will Reverse
    else if (command.equals("backward")) {
        digitalWrite(motor1Pin1, LOW); 
        digitalWrite(motor1Pin2, HIGH);
        digitalWrite(motor2Pin1, HIGH);
        digitalWrite(motor2Pin2, LOW);

    }
    //For debugging purpose
    //Serial.println(state);
    else{
        digitalWrite(motor1Pin1, LOW); 
        digitalWrite(motor1Pin2, LOW); 
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, LOW);

    }
  

}
