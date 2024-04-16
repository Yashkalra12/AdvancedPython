def bubble_sort(elements):
    for i in range(len(elements)-1,-1,-1):
        for j in range(i):
            if elements[j]>elements[j+1]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
        
    return elements

if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34]
    bubble_sort(elements)

    print(elements)

#TC:O(n^2)
#SC:O(n)
    