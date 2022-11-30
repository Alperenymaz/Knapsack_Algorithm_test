def main():
    dictionary = {}
    capacities = [5, 10, 15, 20, 25]
    totCapacity = int(input("Enter total task length in hour(s): "))*10

    for i in range(5):
        print("Enter payment value (in TL) for task portion having length of hour(s): ",capacities[i]/10)
        dictionary[capacities[i]] = input()

    findBest(dictionary,totCapacity)#dict atıyor


def findBest(dictionary,totCapacity):
    dictionaryFinal = {}#sonuçlar

    for key,value in dictionary.items():

        data = int(totCapacity / key)
        totvalue = data * int(value)

        totvalue2 = totvalue #değer tutuyor
        if totCapacity % key != 0:
            for key0,value0 in dictionary.items():
                totvalue = totvalue2
                if (totCapacity % key) >= key0:#tamamlayanı bulana kadar içinde gez
                    totvalue = int(totvalue + int(totCapacity % key) / key0 * int(value0))#toplama
                    dictionaryFinal[(key,int(data),key0,int(int(totCapacity%key)/key0))] = totvalue#neyden kaç kez kullandım
                    continue
        else:#direkt ekle ex 5,5
            dictionaryFinal[(key,int(data))] = totvalue

    max = 0
    finalKeys = []#optimal sonuçların keyleri
    for key,value in dictionaryFinal.items():
        if value > max:
            max = value
            finalKeys = key

    dayCount = 0

    for x in range(int(len(finalKeys)/2)):
        count = 2*x
        dayCount = x+1
        y = 0
        while y < int(finalKeys[count+1]):
            print("\nOn Day ", dayCount)
            print(" do task portion with portion length ", finalKeys[count])
            dayCount+=1
            y+=1
    if dayCount>0:
        print("\nThe most profitable completion of the assigned task takes", dayCount-1,"days")
    else:
        print("\nBecause of the low task length, there is no completion of the assigned task")

main()