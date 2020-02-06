import numpy as np
from keras.models import Sequential;
from keras.layers import Dense;

class Main:
    def __init__(self):
        print("test");
        self.createData();
        print(self.a);
        self.model = Sequential();

        self. model.add(Dense(units=1, activation='relu', input_shape=(1,) ))
        self.model.add(Dense(units=7, activation='softmax' ) )

        self.model.compile(loss='sparse_categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

        self.model.compile(loss='sparse_categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
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
                    ask = input("Value: ");
                    if(ask == 'q'):
                        break;
                    print(self.predict(ask));
            if ask == 'q':
                break;
                
        

    def createData(self):
        self.a = np.array([2,3,4,5]);
        
    def train(self):
        self.model.fit(np.array([1,2,3,4,5]), np.array([2,3,4,5,6]), epochs=5, batch_size=1)

    def predict(self, value):
        predictInput = np.array([int(value)]);
        predictInput.reshape(1,);#this is to reshapee so it does not give errror about dense layer neeidng 2
        print(predictInput.shape);

        predictions = self.model.predict(predictInput, batch_size=1) # batch size is how many it does at once

        return predictions;

main = Main();
