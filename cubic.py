import numpy as np
from keras.optimizers import SGD;
from keras.models import Sequential;
from keras.layers import Dense;

class Main:
    listOfIn = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999]
    listOfOut = [
1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961,1024,1089,1156,1225,1296,1369,1444,1521,1600,1681,1764,1849,1936,2025,2116,2209,2304,2401,2500,2601,2704,2809,2916,3025,3136,3249,3364,3481,3600,3721,3844,3969,4096,4225,4356,4489,4624,4761,4900,5041,5184,5329,5476,5625,5776,5929,6084,6241,6400,6561,6724,6889,7056,7225,7396,7569,7744,7921,8100,8281,8464,8649,8836,9025,9216,9409,9604,9801,10000,10201,10404,10609,10816,11025,11236,11449,11664,11881,12100,12321,12544,12769,12996,13225,13456,13689,13924,14161,14400,14641,14884,15129,15376,15625,15876,16129,16384,16641,16900,17161,17424,17689,17956,18225,18496,18769,19044,19321,19600,19881,20164,20449,20736,21025,21316,21609,21904,22201,22500,22801,23104,23409,23716,24025,24336,24649,24964,25281,25600,25921,26244,26569,26896,27225,27556,27889,28224,28561,28900,29241,29584,29929,30276,30625,30976,31329,31684,32041,32400,32761,33124,33489,33856,34225,34596,34969,35344,35721,36100,36481,36864,37249,37636,38025,38416,38809,39204,39601,40000,40401,40804,41209,41616,42025,42436,42849,43264,43681,44100,44521,44944,45369,45796,46225,46656,47089,47524,47961,48400,48841,49284,49729,50176,50625,51076,51529,51984,52441,52900,53361,53824,54289,54756,55225,55696,56169,56644,57121,57600,58081,58564,59049,59536,60025,60516,61009,61504,62001,62500,63001,63504,64009,64516,65025,65536,66049,66564,67081,67600,68121,68644,69169,69696,70225,70756,71289,71824,72361,72900,73441,73984,74529,75076,75625,76176,76729,77284,77841,78400,78961,79524,80089,80656,81225,81796,82369,82944,83521,84100,84681,85264,85849,86436,87025,87616,88209,88804,89401,90000,90601,91204,91809,92416,93025,93636,94249,94864,95481,96100,96721,97344,97969,98596,99225,99856,100489,101124,101761,102400,103041,103684,104329,104976,105625,106276,106929,107584,108241,108900,109561,110224,110889,111556,112225,112896,113569,114244,114921,115600,116281,116964,117649,118336,119025,119716,120409,121104,121801,122500,123201,123904,124609,125316,126025,126736,127449,128164,128881,129600,130321,131044,131769,132496,133225,133956,134689,135424,136161,136900,137641,138384,139129,139876,140625,141376,142129,142884,143641,144400,145161,145924,146689,147456,148225,148996,149769,150544,151321,152100,152881,153664,154449,155236,156025,156816,157609,158404,159201,160000,160801,161604,162409,163216,164025,164836,165649,166464,167281,168100,168921,169744,170569,171396,172225,173056,173889,174724,175561,176400,177241,178084,178929,179776,180625,181476,182329,183184,184041,184900,185761,186624,187489,188356,189225,190096,190969,191844,192721,193600,194481,195364,196249,197136,198025,198916,199809,200704,201601,202500,203401,204304,205209,206116,207025,207936,208849,209764,210681,211600,212521,213444,214369,215296,216225,217156,218089,219024,219961,220900,221841,222784,223729,224676,225625,226576,227529,228484,229441,230400,231361,232324,233289,234256,235225,236196,237169,238144,239121,240100,241081,242064,243049,244036,245025,246016,247009,248004,249001,250000,251001,252004,253009,254016,255025,256036,257049,258064,259081,260100,261121,262144,263169,264196,265225,266256,267289,268324,269361,270400,271441,272484,273529,274576,275625,276676,277729,278784,279841,280900,281961,283024,284089,285156,286225,287296,288369,289444,290521,291600,292681,293764,294849,295936,297025,298116,299209,300304,301401,302500,303601,304704,305809,306916,308025,309136,310249,311364,312481,313600,314721,315844,316969,318096,319225,320356,321489,322624,323761,324900,326041,327184,328329,329476,330625,331776,332929,334084,335241,336400,337561,338724,339889,341056,342225,343396,344569,345744,346921,348100,349281,350464,351649,352836,354025,355216,356409,357604,358801,360000,361201,362404,363609,364816,366025,367236,368449,369664,370881,372100,373321,374544,375769,376996,378225,379456,380689,381924,383161,384400,385641,386884,388129,389376,390625,391876,393129,394384,395641,396900,398161,399424,400689,401956,403225,404496,405769,407044,408321,409600,410881,412164,413449,414736,416025,417316,418609,419904,421201,422500,423801,425104,426409,427716,429025,430336,431649,432964,434281,435600,436921,438244,439569,440896,442225,443556,444889,446224,447561,448900,450241,451584,452929,454276,455625,456976,458329,459684,461041,462400,463761,465124,466489,467856,469225,470596,471969,473344,474721,476100,477481,478864,480249,481636,483025,484416,485809,487204,488601,490000,491401,492804,494209,495616,497025,498436,499849,501264,502681,504100,505521,506944,508369,509796,511225,512656,514089,515524,516961,518400,519841,521284,522729,524176,525625,527076,528529,529984,531441,532900,534361,535824,537289,538756,540225,541696,543169,544644,546121,547600,549081,550564,552049,553536,555025,556516,558009,559504,561001,562500,564001,565504,567009,568516,570025,571536,573049,574564,576081,577600,579121,580644,582169,583696,585225,586756,588289,589824,591361,592900,594441,595984,597529,599076,600625,602176,603729,605284,606841,608400,609961,611524,613089,614656,616225,617796,619369,620944,622521,624100,625681,627264,628849,630436,632025,633616,635209,636804,638401,640000,641601,643204,644809,646416,648025,649636,651249,652864,654481,656100,657721,659344,660969,662596,664225,665856,667489,669124,670761,672400,674041,675684,677329,678976,680625,682276,683929,685584,687241,688900,690561,692224,693889,695556,697225,698896,700569,702244,703921,705600,707281,708964,710649,712336,714025,715716,717409,719104,720801,722500,724201,725904,727609,729316,731025,732736,734449,736164,737881,739600,741321,743044,744769,746496,748225,749956,751689,753424,755161,756900,758641,760384,762129,763876,765625,767376,769129,770884,772641,774400,776161,777924,779689,781456,783225,784996,786769,788544,790321,792100,793881,795664,797449,799236,801025,802816,804609,806404,808201,810000,811801,813604,815409,817216,819025,820836,822649,824464,826281,828100,829921,831744,833569,835396,837225,839056,840889,842724,844561,846400,848241,850084,851929,853776,855625,857476,859329,861184,863041,864900,866761,868624,870489,872356,874225,876096,877969,879844,881721,883600,885481,887364,889249,891136,893025,894916,896809,898704,900601,902500,904401,906304,908209,910116,912025,913936,915849,917764,919681,921600,923521,925444,927369,929296,931225,933156,935089,937024,938961,940900,942841,944784,946729,948676,950625,952576,954529,956484,958441,960400,962361,964324,966289,968256,970225,972196,974169,976144,978121,980100,982081,984064,986049,988036,990025,992016,994009,996004,998001];
    def __init__(self):
        self.PrintFirst1000IntArray();

        print("test");
        self.createData();
        print(self.a);
        self.model = Sequential();

        self. model.add(Dense(units=1, activation='relu', input_shape=(1,) ))
        self.model.add(Dense(units=100000, activation='softmax' ) )

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
        self.model.fit(np.array(self.listOfIn), np.array(self.listOfOut), epochs=50, batch_size=1)

    def predict(self, value):
        predictInput = np.array([int(value)]);
        predictInput.reshape(1,);#this is to reshapee so it does not give errror about dense layer neeidng 2
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
