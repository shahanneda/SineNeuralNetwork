import numpy as np
from  keras.models import Sequential;

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
              metrics=['accuracy'])k

        self.model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))


    def createData(self):
        self.a = np.array([2,3,4,5]);
        
    def train(self):
        self.model.fit((2,3,4,5,6), (3,4,5,6,7), epochs=5, batch_size=32)

    def predict(self):
        self.model.
        classes = model.predict(x_test, batch_size=128)


main = Main();
