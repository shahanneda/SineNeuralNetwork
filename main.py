import numpy as np
from keras.optimizers import SGD;
from keras.models import Sequential;
from keras.layers import Dense;

class Main:
    listOfIn =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
    listOfOut =[[0,1], [1,0], [0,1], [1,0], [0,1], [1,0],[0,1], [1,0],[0,1], [1,0],[0,1], [1,0],[0,1], [1,0],[0,1], [1,0],[0,1], [1,0],[0,1], [1,0]];
    def __init__(self):
        #self.PrintFirst1000IntArray();

        print("test");
        self.createData();
        print(self.a);
        self.model = Sequential();

        self. model.add(Dense(units=2, activation='relu', input_shape=(2,) ))
        self.model.add(Dense(units=2, activation='softmax' ) )

        sgdOptimizer = SGD(lr=0.001, momentum=0.0, nesterov=False)

        self.model.compile(loss='sparse_categorical_crossentropy',
              optimizer=sgdOptimizer,
              metrics=['accuracy'])

    #    self.model.compile(loss='sparse_categorical_crossentropy',
    #          optimizer='sgd',
    #          metrics=['accuracy'])

        #self.model.compile(loss=keras.losses.categorical_crossentropy,
        #      optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True)) # use this if we want more control over the varaibles otherwise the other one is simpler

    
        ''' we can use this to kinda to the onehotencoding (ithink) directvly weith kaeeras
        from keras.utils import to_categorical
        y_binary = to_categorical(y_int)
        '''


        
        while True:
            ask = int(input("Choose: \n1)Load Data \n2)Train \n3)Predict\n"));
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
            if ask == 'q':
                break;
                
        

    def createData(self):
        self.a = np.array([2,3,4,5]);
        
    def train(self):
        listOfNum = [];
        for i in self.listOfIn:
            listOfNum.append(  [int(x) for x in bin(i)[2:] ] ) # this is to convert the number in to binary

        print(listOfNum);
        listOfNum = np.array(listOfNum);
        self.model.fit(listOfNum, np.array(self.listOfOut), epochs=50, batch_size=1);
                
    def predict(self, value):
        num = [int(x) for x in bin(value)[2:] ]  # this is to convert the number in to binary
        predictInput = np.array([num]);

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