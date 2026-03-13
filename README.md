#ajaya
come visit our college
def binarysearch(a,low,high,key):
    if low<=high:
        mid=(high+low)//2
        if a[mid]==key:
            print("Search Successful,key element found at location:",mid+1)
            return
        elif key<a[mid]:
            binarysearch(a,low,mid-1,k)
        else:
            binarysearch(a,mid+1,high,k)
    else:
        print("Search Unsuccessful")
a=[13,24,35,46,57,68,79]
print("the array element are:",a)
k=int(input("enter the key element to search:"))
binarysearch(a,0,len(a)-1,k)
