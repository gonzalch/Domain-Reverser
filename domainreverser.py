'''
def reverser(url):

    newUrl = []
    domains = []

    for i in url:
        if i != '.':
            newUrl.append(i)
        
        else:
            newUrl.append(i)
            domains.append(newUrl)
            del newUrl[:]
    
    domains.reverse()
    
    return domains
 '''
 
def reverser2(url):
    newUrl = []
    
    domains = url.split('.')
    
    for i in range(1, len(domains)):
        newUrl.append(domains.pop())
        newUrl.append('.')

    newUrl.append(domains.pop())
	
    url = ''
	
    return url.join(newUrl)
    

def main():

    x = input('Enter a URL such as www.google.com or www.cnn.co.uk: ')
   
    print("You entered: ", x)
   
    print("Reversed URL by domain: ", reverser2(x))

main()