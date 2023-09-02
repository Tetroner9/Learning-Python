const int relayPins[] = {X, Y, Z, W}; // Replace X, Y, Z, W with the actual GPIO pins
const int sequenceLength = 4;
const int correctSequence[] = {0, 1, 2, 3}; // Use the relay index for the correct sequence

int currentSequenceIndex = 0;
bool sequenceStarted = false;

void setup() {
  for (int i = 0; i < sequenceLength; i++) {
    pinMode(relayPins[i], OUTPUT);
    // Turn off all relays at startup
    digitalWrite(relayPins[i], LOW);
  }
}

void loop() {
  // Check if the sequence has started and if a relay was activated
  if (sequenceStarted && currentSequenceIndex > 0) {
    // Deactivate all relays
    for (int i = 0; i < sequenceLength; i++) {
      digitalWrite(relayPins[i], LOW);
    }
    // Reset the sequence and start over
    currentSequenceIndex = 0;
    sequenceStarted = false;
  }
}

void activateMachine() {
  // Turn on the next bulb in the sequence
  if (currentSequenceIndex < sequenceLength) {
    digitalWrite(relayPins[currentSequenceIndex], HIGH);
    currentSequenceIndex++;
  }
}

void checkSequence(int pin) {
  if (!sequenceStarted) {
    // Start the sequence when the first correct wire is connected
    if (pin == correctSequence[currentSequenceIndex]) {
      sequenceStarted = true;
      activateMachine();
    }
  } else {
    // Check if the correct wire is connected in the current step
    if (pin == correctSequence[currentSequenceIndex]) {
      // Correct wire connected, move to the next step in the sequence
      activateMachine();
    } else {
      // Incorrect wire connected, reset the sequence
      sequenceStarted = false;
      currentSequenceIndex = 0;
    }
  }
}
