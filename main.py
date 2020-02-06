import numpy as np
from keras.models import Sequential;
from keras.layers import Dense;

class Main:
    def __init__(self):
        print("test");
        self.createData();
        print(self.a);
        self.model = Sequential();

        self. model.add(Dense(units=64, activation='relu', input_dim=100))
        self.model.add(Dense(units=10, activation='softmax'))

        self.model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

        self.model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
        #self.model.compile(loss=keras.losses.categorical_crossentropy,
        #      optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True)) # use this if we want more control over the varaibles otherwise the other one is simpler

    
        ask = int(input("Choose: \n1)Load Data \n2)Train \n3)Predict"));
        
        if(ask == 3):
             while True:
                ask = input("Value: ");
                if(ask == 'q'):
                    break;
                print(self.predict(ask));
                
        

    def createData(self):
        self.a = np.array([2,3,4,5]);
        
    def train(self):
        self.model.fit((2,3,4,5,6), (3,4,5,6,7), epochs=5, batch_size=32)

    def predict(self, value):
        predictions = self.model.predict(value, batch_size=128) # batch size is how many it does at once
        return predictions;

main = Main();
