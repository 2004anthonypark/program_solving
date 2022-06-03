total_num = int(input("please enter the total number of dogs and chicks "))
total_legnum=int(input("please enter the total number of legs "))

dognum=(total_legnum-2*total_num)/2
chicknum=total_num-dognum

print("the number of dog : {0}, the number of chick : {1}".format(dognum, chicknum))
