import numpy as np
from keras.optimizers import SGD;
from keras.models import Sequential;
from keras.layers import Dense;
from keras.utils import plot_model;
import os;

class Main:
    listOfIn = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1];
    listOfOut = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0];
    def __init__(self):
        #self.PrintFirst1000IntArray();

        print("test");
        self.createData();
        print(self.a);
        self.model = Sequential();

        self. model.add(Dense(units=1, activation='relu', input_shape=(1,) ))
        
        self.model.add(Dense(units=2, activation='relu'))
        self.model.add(Dense(units=2, activation='relu'))
        self.model.add(Dense(units=2, activation='relu'))

        self.model.add(Dense(units=1, activation='softmax' ) )

        sgdOptimizer = SGD(lr=0.001, momentum=0.0, nesterov=False)

        self.model.compile(loss='mean_squared_error',
              optimizer=sgdOptimizer,
              metrics=['accuracy'])

    #    self.model.compile(loss='sparse_categorical_crossentropy',
    #          optimizer='sgd',
    #          metrics=['accuracy'])

        #self.model.compile(loss=keras.losses.categorical_crossentropy
        #      optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True)) # use this if we want more control over the varaibles otherwise the other one is simpler

    
        ''' we can use this to kinda to the onehotencoding (ithink) directvly weith kaeeras
        from keras.utils import to_categorical
        y_binary = to_categorical(y_int)
        '''

        
        while True:
            ask = int(input("Choose: \n1)Load Data \n2)Train \n3)Predict\n4)Visualize Model\n"));
            if ask == 1:
                pass;

            if ask == 2:
                self.train();

            if ask == 3:
                 while True:
                    ask2 = input("Value: ");
                    if(ask2 == 'q'):
                        break;
                    print(self.predict(ask));
            if ask == 4:
                plot_model(self.model, 'model.png', show_shapes=True, show_layer_names=True);
                os.system("open model.png");
                print("saved model to model.png");

            if ask == 'q':
                break;
                
        

    def createData(self):
        self.a = np.array([2,3,4,5]);
        
    def train(self):

        listOfNum = np.array(self.listOfIn);
        self.model.fit(listOfNum, np.array(self.listOfOut), epochs=5, batch_size=1);
                
    def predict(self, value):
        #num = [int(x) for x in bin(value)[2:] ]  # this is to convert the number in to binary
        predictInput = np.array([value]);

        #predictInput.reshape(1,);#this is to reshapee so it does not give errror about dense layer neeidng 2
        print(predictInput.shape);

        predictions = self.model.predict(predictInput, batch_size=1) # batch size is how many it does at once

        return predictions;

    def PrintFirst1000IntArray(self):
        print("[", end="");
        for i in range(1,1000):
            print(i, end=",");
        print("]\n");

        print("[");
        for i in range(1,1000):
            print(i*i, end=",");
        print("]\n", end="");
            


main = Main();
